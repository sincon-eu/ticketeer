import socket
from dataclasses import dataclass

import requests
import urllib3
from requests import get
from requests.exceptions import ConnectionError
from contextlib import closing
from bs4 import BeautifulSoup
import html5lib


@dataclass
class Gig:
    title: str
    href: str
    processed: bool = False


def get_gigs(html_content) -> list:
    gigs = []
    soup = BeautifulSoup(html_content, 'html5lib')
    list_of_gigs = soup.find("div", {"class": "table_info tbl_repertoire"}, recursive=True).find_all("div", {"class": "title"}, recursive=True)

    for event_soup in list_of_gigs:
        event = event_soup.find('a')
        gigs.append( Gig(title=event.attrs['title'].split('Kup bilet - ')[1], href=event.attrs['href']))
    return gigs


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
    [print(gig.title) for gig in get_gigs(raw_html_content)]
