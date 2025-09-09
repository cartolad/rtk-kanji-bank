#!/usr/bin/env python

import argparse
import json
import zipfile

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
    obj = {
        "title": "Remembering the Kanji",
        "revision": "0.1",
        "format": 3,
        "sequenced": False,
        "description": "Kanji keywords from Remembering the Kanji",
        "author": "tbc",
        "url": "tbc",
        "attribution": "tbc"
    }
    return obj

def generate_tags():
    obj = [
        ["rtk", "source", 0, "Keyword from Remembering the Kanji", 0]
    ]
    return obj

def generate_kanji_bank():
    obj = [
        ["今", "", "", "rtk", ["now"], {}],
        ["高", "", "", "rtk", ["tall"], {}],
    ]
    return obj


if __name__ == "__main__":
    main()
