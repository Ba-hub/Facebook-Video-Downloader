#!/usr/bin/env python3
# Made By : Ghosthub

import re
import sys
import argparse
import requests

ERASE_LINE = '\e[2K'

def main():
    parser = argparse.ArgumentParser(description="Download videos from facebook from your terminal")

    parser.add_argument('url', action="store")
    parser.add_argument('resolution', action="store", nargs="?")

    args = parser.parse_args()

    print("Fetching source code...", end="\r", flush=True)
    request = requests.get(args.url)
    print(ERASE_LINE, end="\r", flush=True)

    print("\033[92m✔\033[0m Fetched source code")
    
    file_name = str(re.findall(r"videos\/(.+?)\"", request.text)[-1].replace("/", "")) + f"_{'sd' if args.resolution == 'sd' else 'hd'}.mp4"

    print("Downloading video...", end="\r", flush=True)

    try:
        request = requests.get(re.findall(f"{'sd_src' if args.resolution == 'sd' else 'hd_src'}:\"(.+?)\"", request.text)[0])
    except IndexError:
        print(ERASE_LINE, end="\r", flush=True)
        print("\e[91m✘\e[0m Video could not be downloaded")
        sys.exit()

    # Write the content to the file
    with open(file_name, "wb") as f:
        f.write(request.content)

    print(ERASE_LINE, end="\r", flush=True)

    print(f"\033[92m✔\033[0m Video downloaded: {file_name}")

if __name__ == "__main__":
    main()
