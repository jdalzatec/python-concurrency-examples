from typing import List
import concurrent.futures
import requests
import threading
from codetiming import Timer

thread_local = threading.local()


def get_session() -> requests.Session:
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url: str) -> None:
    session = get_session()
    with session.get(url) as response:
        pass
        # print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites: List[str], max_workers: int) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice"] * 80

    for max_workers in range(1, 21):
        print(max_workers)
        for _ in range(50):
            with Timer(text="Elapsed time: {:.2f} seconds"):
                download_all_sites(sites, max_workers)
