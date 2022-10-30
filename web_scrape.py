'''
you receive the data from the web-site here
'''
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'}
main_url = 'https://www.emlakjet.com/satilik-konut/istanbul/'
links = []
last_index=0
page = 0
while(page < 10):
    if page == 0:
        req = requests.get(main_url, headers=headers)
    else:
        req = requests.get(main_url + str(page), headers=headers)

    soup = BeautifulSoup(req.content, 'html.parser')
    things = soup.find_all('div', class_='_3qUI9q')
    for i in things:
        link = []
        last_index = last_index + 1
        link.append(last_index)
        img = i.find('img')
        link.append(img.get('alt'))
        a = i.find('a')
        url_first = "https://www.emlakjet.com"
        link.append(url_first + a.get('href'))
        links.append(link)
        page = last_index // 30
for i in links:
    req_det = requests.get(i[2], headers=headers)
    soup_det = BeautifulSoup(req_det.content, 'html.parser')
    loc = soup_det.find('div', class_='_3VQ1JB').find('p').text
    i.append(loc)
    features = soup_det.find_all('div', class_='_35T4WV')
    index1 = 0
    for j in features:
        index1 = index1 + 1
        detail = j.findAll('div', class_='_1bVOdb')
        print(detail[1].text, index1)
        if index1 == 5: i.append(detail[1].text)
        if index1 == 9: i.append(detail[1].text)
        if index1 == 20: i.append(detail[1].text)
        if index1 == 22: i.append(detail[1].text)

print(links)


'''
[index, title ,semt ,m2 ,floor , oda, yaş]
'''