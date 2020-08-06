from bs4 import BeautifulSoup

import requests

import json

urls=['https://www.imdb.com/list/ls002939221/','https://www.imdb.com/list/ls002939221/?sort=list_order,asc&st_dt=&mode=detail&page=2','https://www.imdb.com/list/ls002939221/?sort=list_order,asc&st_dt=&mode=detail&page=3','https://www.imdb.com/list/ls002939221/?sort=list_order,asc&st_dt=&mode=detail&page=4','https://www.imdb.com/list/ls002939221/?sort=list_order,asc&st_dt=&mode=detail&page=5','https://www.imdb.com/list/ls002939221/?sort=list_order,asc&st_dt=&mode=detail&page=6','https://www.imdb.com/list/ls002939221/?sort=list_order,asc&st_dt=&mode=detail&page=7','https://www.imdb.com/list/ls002939221/?st_dt=&mode=detail&page=8&sort=list_order,asc']
a=[]
for url in urls: 
	source = requests.get(url).text
	soup = BeautifulSoup(source,'lxml')
	for content in soup.find_all('div',class_='lister-item-content'):
		d={}
		head=content.find('h3',class_='lister-item-header')
		i=head.find('span',class_='lister-item-index').text
		name=head.a.text
		year=head.find('span',class_='lister-item-year').text
		q=content.find('p',class_='text-muted')
		genre=q.find('span',class_='genre').text[1::]
		try:
			time=q.find('span',class_='runtime').text
		except AttributeError:
			time=None 		
		rating=content.find('span',class_='ipl-rating-star__rating').text
		des=content.find('p',class_="").text[5::]
		d={"index":i,"name":name,"year":year,"genre":genre,"runtime":time,"rating":rating,"description":des}
		a.append(d)
print(a)
with open('imdbdata.json', 'w') as outfile:
	json.dump(a, outfile)

