from bs4 import BeautifulSoup
import requests


url = 'https://www.marathonbet.ru/su/live/26418'
page = requests.get(url)
HEADERS = { 'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 ' }
soup = BeautifulSoup(page.text, "html.parser")

#req = requests.get(url)
all_matches = soup.find_all('div', {'class': 'category-container'})

for match in all_matches:
    #print(match)
    #print(5467457567567567567)
    #--print(match.find_all('table',attrs={'class': 'coupon-row-item coupone-labels'})[0]) #Шапка блока
    #headers = match.find_all('div',class_='category-label-block')[0] #Все заголовки
    #header_1 = headers.find_all('span', class_ = 'nowrap')[0]  #Первый заголовок
    #header_2 = headers.find_all('span', class_='nowrap')[1] #Второй заголовок (Добавить третий, не везде есть)
    #first_command = match.find_all('a',class_ = 'member-link')[0] #Первая команда
    #second_command = match.find_all('a', class_='member-link')[1] #Вторая команда
    match_time = match.find_all('table',attrs={'class': 'coupon-row-item'})[0]
    print(match_time)
    print(4444444444444444)

    # for one in one_matches:
    #     print(one.find('a',class_ = 'member-link'))

# <a class="member-link" href="/su/live/12503189">
# <span data-member-link="true">Шимшон Кафр Касим</span>