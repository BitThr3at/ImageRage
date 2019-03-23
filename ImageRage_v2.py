# import urllib
import requests as req
from bs4 import BeautifulSoup
import os
import argparse

num = 0
pn = 0
parser = argparse.ArgumentParser()
parser.add_argument("keyword")
args = parser.parse_args()
keyword =args.keyword               #input("Enter the Keyword: ")
os.makedirs(keyword)
os.chdir(keyword)

while (pn <= 30):
    pn = pn +1
    resp = req.get("https://www.vectorstock.com/royalty-free-vectors/" + keyword + "-vectors-page_" + str(pn))
    page = str(BeautifulSoup(resp.content, 'html.parser'))


    def getURL(page):

        start_link = page.find('vectorstock.com/i/1000x1000') #page.find('href="https://cdn')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link - 14)
        end_quote = page.find('"', start_quote + 1)
        resp = page[start_quote + 1: end_quote]
        return resp, end_quote


    while True:
        resp, n = getURL(page)
        page = page[n:]
        if resp:
            print(resp, "   ->Saved")
            num = num + 1
            r = req.get(resp)
            with open("image_" + str(num) + ".jpg", "wb") as f:
                f.write(r.content)
        else:
            break