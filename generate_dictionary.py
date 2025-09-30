#!/usr/bin/env python3

import argparse
import json
import zipfile
import csv
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', '--output',
        dest='output_file',
        default='rtk.zip',
        help='Specify the output file name. Defaults to "rtk.zip".'
    )
    args = parser.parse_args()
    output_filename = args.output_file

    with zipfile.ZipFile(output_filename, mode="w") as rtk_zip:
        with rtk_zip.open("index.json", mode="w") as index_json_f:
            index_json_f.write(json.dumps(generate_index()).encode("utf-8"))
        with rtk_zip.open("tag_bank_1.json", mode="w") as tag_bank_f:
            tag_bank_f.write(json.dumps(generate_tags()).encode("utf-8"))
        with rtk_zip.open("kanji_bank_1.json", mode="w") as kanji_bank_f:
            kanji_bank_f.write(json.dumps(generate_kanji_bank()).encode("utf-8"))
    print(f"Wrote '{output_filename}'")

def generate_index():
    with open(Path(__file__).parent / "version-number") as v_f:
        revision = v_f.read().strip()
    obj = {
        "title": "Remembering the Kanji",
        "revision": revision,
        "format": 3,
        "sequenced": False,
        "description": "Kanji keywords from Remembering the Kanji",
        "author": "James W. Heisig",
        "url": "https://github.com/cartolad/rtk-kanji-bank/releases/latest/download/rtk.zip",
        "attribution": "tbc"
    }
    return obj

def generate_tags():
    obj = [
        ["rtk", "source", 0, "Keyword from Remembering the Kanji", 0]
    ]
    return obj

def generate_kanji_bank():
    obj = []
    rtk_csv_path = Path(__file__).parent / "rtk.csv"
    with open(rtk_csv_path) as rtk_csv_f:
        reader = csv.DictReader(rtk_csv_f)
        for row in reader:
            obj.append(
                [row["character"], "", "", "rtk", [row["keyword"]], {}],
            )
    return obj


if __name__ == "__main__":
    main()
