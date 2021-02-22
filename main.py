import requests
from bs4 import BeautifulSoup
menu = ""
lolchessgg_URL = ("https://lolchess.gg/{menu}")
lolchess = requests.get(lolchessgg_URL)
lolchess_soup = BeautifulSoup(leaderboards.text, "html.parser")
nick_name = ""
def meta_deck():
  menu = "meta"
  if lolchess_soup.select("#wrapper > div.container-full > div.guide-meta.mt-4 > div.guide-meta__group.tier-S > div.guide-meta__group__content > div:nth-child(1) > div > div.guide-meta__deck__column.name.mr-3 > span").get_text == "HOT"
    HOT_deck = lolchess_soup.select("#wrapper > div.container-full > div.guide-meta.mt-4 > div.guide-meta__group.tier-S > div.guide-meta__group__content > div:nth-child(1) > div > div.guide-meta__deck__column.name.mr-3").get_text().strip()
def find_ranking():

def paging():

def 