"""Download the UCI "Default of Credit Card Clients" dataset into data/raw/.

The script is safe to run repeatedly: if the dataset file already exists and its
checksum matches, nothing is downloaded. It only uses the standard library, so it
can run before the project requirements are installed.
"""

import argparse
import hashlib
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

DATASET_URL = "https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip"
ARCHIVE_MEMBER = "default of credit card clients.xls"
TARGET_NAME = "default_of_credit_card_clients.xls"
EXPECTED_SHA256 = "30c6be3abd8dcfd3e6096c828bad8c2f011238620f5369220bd60cfc82700933"

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(url, destination):
    request = urllib.request.Request(url, headers={"User-Agent": "credit-card-default-prediction"})
    with urllib.request.urlopen(request, timeout=60) as response, open(destination, "wb") as out:
        shutil.copyfileobj(response, out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=DATASET_URL, help="source of the ZIP archive")
    args = parser.parse_args()

    target = RAW_DIR / TARGET_NAME

    if target.exists():
        if sha256_of(target) == EXPECTED_SHA256:
            print(f"Dataset already present: {target}")
            return 0
        print(f"Error: {target} exists but its checksum does not match.", file=sys.stderr)
        print("Delete the file and run this script again.", file=sys.stderr)
        return 1

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        archive = Path(tmp) / "dataset.zip"
        print(f"Downloading {args.url}")
        try:
            download(args.url, archive)
        except (urllib.error.URLError, OSError) as error:
            print(f"Error: download failed: {error}", file=sys.stderr)
            return 1

        try:
            with zipfile.ZipFile(archive) as zf:
                if ARCHIVE_MEMBER not in zf.namelist():
                    print(f"Error: '{ARCHIVE_MEMBER}' not found in the archive.", file=sys.stderr)
                    print(f"Archive contents: {zf.namelist()}", file=sys.stderr)
                    return 1
                extracted = Path(zf.extract(ARCHIVE_MEMBER, tmp))
        except zipfile.BadZipFile:
            print("Error: the downloaded file is not a valid ZIP archive.", file=sys.stderr)
            return 1

        if sha256_of(extracted) != EXPECTED_SHA256:
            print("Error: the extracted file has an unexpected checksum; it was not installed.", file=sys.stderr)
            return 1

        shutil.move(str(extracted), str(target))

    print(f"Dataset saved to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
