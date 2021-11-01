from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.marathonbet.ru/su/live/26418'
page = requests.get(url)
HEADERS = { 'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 ' }
soup = BeautifulSoup(page.text, "html.parser")

#req = requests.get(url)
all_matches = soup.find_all('div', {'class': 'category-container'})
a = []
for match in all_matches:

    #print(match)
    #print(5467457567567567567)
    headers = match.find_all('div',class_='category-label-block')[0] #Все заголовки
    header_1 = headers.find_all('span', class_ = 'nowrap')[0]  #Первый заголовок
    header_2 = headers.find_all('span', class_='nowrap')[1] #Второй заголовок (Добавить третий, не везде есть)
    a.append ({ 'headers': header_1.get_text()+ ' ' + header_2.get_text()})
    print(header_1.get_text()+ ' ' + header_2.get_text())
    first_command = match.find_all('a',class_ = 'member-link')[0] #Первая команда
    a.append({'first_command':(first_command.get_text()) })
    print(first_command.get_text())
    second_command = match.find_all('a', class_='member-link')[1] #Вторая команда
    a.append( {'second_command': second_command.get_text()} )
    print(second_command.get_text())
    try:
        match_time = match.find_all('div',class_='green bold nobr')[0] #Время матча
        a.append( {'match_time': match_time.get_text()})
        print(match_time.get_text())
    except Exception:
        a.append({'match_time': 'error'})
        print('error')
    score = match.find_all('div',class_='cl-left red')[0] #Счёт
    score.span.decompose()  # Убираем вложеные теги
    a.append({ 'score' : score.get_text() })
    print(score.get_text())
    print(a)
    print('END match')



df = pd.DataFrame(a)
print(df)

