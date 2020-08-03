from typing import List
import requests
import multiprocessing
from codetiming import Timer


session = None


def set_global_session() -> None:
    global session
    if not session:
        session = requests.Session()


def download_site(url: str) -> None:
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites: List[str]) -> None:
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice"] * 80

    with Timer(text="Elapsed time {:.2f}"):
        download_all_sites(sites)
