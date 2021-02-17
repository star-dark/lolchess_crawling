import requests
from bs4 import BeautifulSoup
leaderboards_URL = ("https://lolchess.gg/leaderboards")
leaderboards = requests.get(leaderboards_URL)
lolchess_soup = BeautifulSoup(leaderboards.text, "html.parser")
nick_name = ""
def find_ranking():

def paging():

def 