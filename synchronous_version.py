from codetiming import Timer
from typing import List
import requests
import time


def download_site(url: str, session: requests.Session) -> None:
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites: List[str]) -> None:
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice"] * 80

    with Timer(text="Total elapsed time {:.2f} seconds"):
        download_all_sites(sites)

