#!/usr/bin/env python3
import requests
import re
import sys
import urllib.parse as urlparse
import optparse
target_link = []
def links(url):
    responce = requests.get(url)
    return re.findall('(?:href=")(.*?)"' ,responce.content.decode(errors="ignore"))
def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Target url for getting subdomain")
    (options, arguments) = parser.parse_args()
    if not options.url:
        print("[-]Please enetr a url or use '-h' or '--h' for info")
        sys.exit()
    return options
def crawl(url):
    href_links = links(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]
        if url in link and link not in target_link:
            target_link.append(link)
            print("[+]Find a link -->>"  + link)
            crawl(link)
options= get_argument()
crawl(options.url)