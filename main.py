from bs import soupify
from getItems import getItems
import csv

f = csv.writer(open('results.csv', 'w', newline=''))
f.writerow(['buyer', 'price'])


mainPage = 'http://econpy.pythonanywhere.com/ex/001.html'
initSoup = soupify(mainPage)
pages = initSoup.find_all('a')
urls = [mainPage]
for page in pages:
    urls.append(page['href'])

for url in urls:
    pageSoup = soupify(url)
    pageItems = getItems(pageSoup)
    for i in range(len(pageItems[0])):
        f.writerow([pageItems[0][i],pageItems[1][i]])



