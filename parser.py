# # command option i | check html elements
# import requests
# from bs4 import BeautifulSoup
# response = requests.get('https://tw.yahoo.com')

# if response.status_code ==200:
#     print('Connected Successfully!')
#     webText= response.text
#     # print(webText)
#     bsoup=BeautifulSoup(webText, 'html.parser')
#     # print(bsoup.title)
#     a_tags = bsoup.find_all('a', class_='Fz(16px) LineClamp(1,20px) Fw(700) Td(n) Td(u):h C(#324fe1) V(h) active_V(v)')
#     # print(a_tags)
#     for i in a_tags:
#       print('新聞標題：', i.string)
#       print('新聞連結：', i.get('href'))

# else:
#     print('Not connected')


import requests
from bs4 import BeautifulSoup

url = 'https://tw.yahoo.com'
response = requests.get(url)

if response.status_code == 200:
    print('連線成功！')
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)

    # 找尋新聞標題的元素，這裡以 CSS class 來搜尋
    news_titles = soup.find_all('a')
    print(news_titles)

    # 輸出新聞標題及連結
    for title in news_titles:
        news_title = title.text.strip()
        news_link = title['href']
        print('新聞標題：', news_title)
        print('新聞連結：', news_link)
else:
    print('無法連線至網頁')
