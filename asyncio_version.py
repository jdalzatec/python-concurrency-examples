from typing import List
import asyncio
import aiohttp
from codetiming import Timer


async def download_site(url: str, session: aiohttp.ClientSession) -> None:
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites: List[str]) -> None:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice"] * 80

    with Timer(text="Elapsed time: {:.2f} seconds"):
        asyncio.run(download_all_sites(sites))
