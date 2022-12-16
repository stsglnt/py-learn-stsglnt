import asyncio
import requests
from bs4 import BeautifulSoup



async def scrape_url(url, sleep_time):
    response = requests.get(url)
    await asyncio.sleep(sleep_time)
    print(f"Scrapping, {url}")
    soup = BeautifulSoup(response.content, features='lxml')
    return True

async def main():
    task1 = asyncio.create_task(scrape_url("https://www.google.com/", 10))
    task2 = asyncio.create_task(scrape_url("https://www.youtube.com/", 3))
    task3 = asyncio.create_task(scrape_url("https://twitter.com/", 4))
    task4 = asyncio.create_task(scrape_url("https://translate.google.com/", 2))
    task5 = asyncio.create_task(scrape_url("https://duckduckgo.com/", 7))
    value1 = await task1
    value2 = await task2
    value3 = await task3
    value4 = await task4
    value5 = await task5

if __name__ == '__main__':
    asyncio.run(main())
