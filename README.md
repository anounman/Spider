# Spider

Spider is a simple Python 3 web crawler that recursively collects all internal links from a given website. It is useful for quickly enumerating pages within a domain for auditing or bug‑hunting.

## Features

- Recursively crawls a target URL and follows internal links within the same domain.
- Uses Python's `requests` library and regular expressions to extract links.
- Normalizes relative and absolute URLs using `urllib.parse.urljoin`.
- Avoids revisiting the same link using a global list of discovered URLs.
- Command‑line interface with `-u`/`--url` option to specify the starting URL.

## Requirements

- Python 3
- `requests` library

## Installation

    git clone https://github.com/anounman/Spider.git
    cd Spider
    pip install requests

## Usage

Run the script with the target URL:

    python3 spider.py -u "http://example.com"

The script will:

1. Send an HTTP GET request to the provided URL.
2. Extract all `href` links from the page.
3. Normalize each link to an absolute URL.
4. Recursively crawl each internal link (within the same domain).
5. Print each discovered URL to the console.

Be cautious when crawling large or complex websites, as the script will continue recursively until all reachable internal links are visited.

## Disclaimer

This tool is for educational and authorized testing purposes only. Always obtain permission before crawling or scraping a website. Excessive requests may impact website performance, so use responsibly.
