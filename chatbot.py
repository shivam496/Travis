from googlesearch import search
import requests
import bs4
import webbrowser
from bs4 import BeautifulSoup

def fetch_data(url):
	headers = {'User-Agent': 'Mozilla/5.0'}
	res=requests.get(url,headers=headers)
	return BeautifulSoup(res.content, 'html5lib')

def google(query):
	result_link=[]
	for j in search(query, num=1, stop=1): 
		result_link.append(j)

	url=result_link[0];
	return url

def tell_me_about(location):
	query="holidify "+location
	url=google(query)
	soup = fetch_data(url)
	text=soup.find('div',attrs={'class':'readMoreText'})
	print(text.text)
	return text.text

def places_to_visit(location):
	query="holidify places to visit "+location
	url=google(query)
	if "sightseeing-and-things-to-do.html" not in url:
		url=url+"sightseeing-and-things-to-do.html"
	soup = fetch_data(url)
	places=soup.findAll('h3',attrs={'class':'card-heading'})
	result=""
	for place in places:
		print(place.text)
		result=result+place.text+"<br>"	
	return result

def best_time_to_visit(location):
	query="holidify best time to visit "+location
	url=google(query)
	if "best-time-to-visit.html" not in url:
		url=url+"best-time-to-visit.html"
	soup = fetch_data(url)
	summary=soup.findAll('p')
	print(summary[1].text)
	return summary[1].text
	
def current_temperature(location):
	query="timeanddate.com weather "+location
	url=google(query)
	soup=fetch_data(url)
	summary=soup.find('div',attrs={'class':'h2'})
	desc=summary.next_element.next_element
	print(summary.text)
	print(desc.text)
	result=summary.text+"<br><br>"+desc.text
	return result

def how_to_reach(location):
	query="holidify how to reach "+location
	url=google(query)
	if "how-to-reach.html" not in url:
		url=url+"how-to-reach.html"
	soup=fetch_data(url)
	summary=soup.findAll('p')
	print(summary[1].text)
	return summary[1].text

def restaurants_near_me(location):
	query="zomato restaurant near "+location
	url=google(query)
	# print(url)
	soup=fetch_data(url)
	stores=soup.findAll('a',attrs={'data-result-type':'ResCard_Name'})

	result=""
	for store in stores:
		print(store.text)
		result=result+store.text+"<br>"
	return result
		
def hotels_near_me(location,stars):
	query="makemytrip "+str(stars)+" star hotels near "+location
	url=google(query)
	soup=fetch_data(url)
	hotels=soup.findAll('p',attrs={'id':'hlistpg_hotel_name'})

	result=""
	for hotel in hotels:
		print(hotel.text)
		result=result+hotel.text+"<br>"

	return result

def book_air_tickets(src,dest):
	query="paytm flight from "+src+" to "+dest
	url=google(query)
	webbrowser.open_new_tab(url)
	return "Opened Link in New Tab"

def book_rail_tickets(src,dest):
	pass

def book_bus_tickets(src,dest):
	pass

def nearest_railway_station(location):
	query="train spy nearest railway station to "+location
	url=google(query)
	soup=fetch_data(url)
	# print(url)
	result=""
	t=1
	tables = soup.findAll('table', attrs={'id':'trains'})
	for table in tables:	
		

		data = []
		table_body = table.find('tbody')

		rows = table_body.find_all('tr')
		for row in rows:
		    cols = row.find_all('td')
		    cols = [ele.text.strip() for ele in cols]
		    data.append([ele for ele in cols if ele]) 	

		c=4
		if t==1:
			print("Minor Stations")
			result+="Minor Stations<br>"
			t=t+1
		else:
			print("\n\nMajor Stations")
			result+="<br><br>Major Stations<br>"
		print("\nStation\t\tDistance")
		result+="<br>Station\t\tDistance<br>"
		for row in data:
			if(c==0):
				break
			if(c==4):
				c=c-1
				continue
			print(row[0]+"\t"+row[2])
			result+=row[0]+"\t"+row[2]+"<br>"
			c=c-1
	return result

def nearest_airport(location):
	query="globefeed nearest airport to "+location
	url=google(query)
	soup=fetch_data(url)
	result=""
	table = soup.find('table')
	data = []
	table_body = table.find('tbody')

	rows = table_body.find_all('tr')
	for row in rows:
	    cols = row.find_all('td')
	    cols = [ele.text.strip() for ele in cols]
	    data.append([ele for ele in cols if ele]) 	
	row=data[1:]
	try:
		for data in row:
			print(data[0]+"\n"+data[1]+"\t"+data[2]+"\t"+data[3]+"\n")
			result+=data[0]+"<br>"+data[1]+"\t"+data[2]+"\t"+data[3]+"<br>"+"<br>"
	except:
		pass

	return result

# tell_me_about('mansa devi mandir')
# places_to_visit('haridwar')
# best_time_to_visit('haridwar')
# current_temperature('hyderabad')
# how_to_reach('haridwar')
# restaurants_near_me("near harki pauri")
# hotels_near_me("near harki pauri",3)
# nearest_railway_station("near qutub minar")
# nearest_airport("moradabad")
#book airticket
#book rail ticket
#book bus ticket