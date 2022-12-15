import requests
import time
from bs4 import BeautifulSoup
from threading import Thread

res = list()

def scrape_google():
    main_url = "https://www.google.com/"
    response = requests.get(main_url)
    print("Scrapping")
    time.sleep(2)
    soup = BeautifulSoup(response.content, features='lxml')
    res.append(soup.select(".lnXdpd"))


if __name__ == '__main__':
    thread = Thread(target=scrape_google)
    thread2 = Thread(target=scrape_google)
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()

print(res)
