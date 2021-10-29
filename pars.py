from bs4 import BeautifulSoup
import requests


url = 'https://www.marathonbet.ru/su/live/26418'
page = requests.get(url)
HEADERS = { 'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 ' }
soup = BeautifulSoup(page.text, "html.parser")

#req = requests.get(url)
all_matches = soup.find_all('div', {'class': 'foot-market'})

for match in all_matches:
    #print(soup.find('table',attrs={'class': 'coupon-row-item coupone-labels'})) Шапка блока
    first_command = match.find_all('a',class_ = 'member-link')[0]
    second_command = match.find_all('a', class_='member-link')[1]
    print(first_command.get_text() + '-' + second_command.get_text())
    print(second_command.get_text())
    # for one in one_matches:
    #     print(one.find('a',class_ = 'member-link'))

# <a class="member-link" href="/su/live/12503189">
# <span data-member-link="true">Шимшон Кафр Касим</span>