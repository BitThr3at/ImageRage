# import urllib
import requests as req
from bs4 import BeautifulSoup

num = 0
keyword = input("Enter the Keyword: ")
resp = req.get("https://www.vectorstock.com/royalty-free-vectors/" + keyword + "-vectors")
page = str(BeautifulSoup(resp.content))

def getURL(page):

    start_link = page.find('content="https://cdn')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    resp = page[start_quote + 1: end_quote]
    return resp, end_quote

while True:
    resp, n = getURL(page)
    page = page[n:]
    if resp:
        print("Wait..........." + " Saved")
        num = num + 1
        r = req.get(resp)
        with open("image_" + str(num) + ".jpg","wb") as f:
            f.write(r.content)
    else:
        break
