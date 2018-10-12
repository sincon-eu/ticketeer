import socket

import requests
import urllib3
from requests import get
from requests.exceptions import ConnectionError
from contextlib import closing
from bs4 import BeautifulSoup

"""
based on
https://realpython.com/python-web-scraping-practical-introduction/
"""


def get_gigs(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')
    # for all direct children
    table_contents = soup.find("div", {"class": "table_info tbl_repertoire"}).findAll("a", recursive=True)
    # asa = table_contents.findAll("a", recursive=False)
    # titles = soup.find("div", {"class": "table_info tbl_repertoire"}.findAll("a", recursive=False))
    f = 1


def get_content(url: str) -> object:
    try:
        with closing(get(url, stream=True)) as resp:
            if resp.status_code == 200 and resp.content:
                return resp.content
    except ConnectionError:
        print(f'Unable to connect to {url}')


if __name__ == '__main__':

    url = "https://tickets.klubzak.com.pl/"
    raw_html_content = get_content(url)
    get_gigs(raw_html_content)
