import requests
from bs4 import BeautifulSoup

NFL_URL = "http://www.footballlocks.com/nfl_point_spreads.shtml"


def main():
    global Spread, Underdog, Favorite
    response = requests.get(NFL_URL)
    soup = BeautifulSoup(response.text, features='lxml')
    rows = soup.find_all('tr', class_= 'font4')
    for n, row in enumerate(rows):
        if n > 15:
            break
        row.find_all("td")
        Favorite = cells[0].find('span', title_='Favorite').text.strip()
        Spread = Spread.find('span', title_='Spread').text.strip()
        Underdog = Underdog.find('span', title_='Underdog').text.strip()

        print([cells.get_text(strip=True) for cell in row.find_all('td')])


if __name__ == "__main__":
    main()
