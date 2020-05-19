
import pickle
from listoperations import *
from chatbot import *
from spell import correction

with open('stopwords.pkl', 'rb') as f:
	stop_words = pickle.load(f)


def mapping(msg):
	global stop_words
	init_msg=msg
	msg=msg.split(" ")
	qry=[]
	for word in msg:
		if(word not in stop_words):
			qry.append(correction(word))

	print("\n\n\n")
	print(qry)
	print("\n\n\n")

	############################################################
	#					Best Time To visit
	#					Best Places to visit
	############################################################
	l1=["best","correct","good","right","important"]
	l2=["visit","tour"]
	l3=["weather","time","season"]
	l4=["places","place","interests","sightseeing","sight","site","sites"]
	# if(intersection(l1,qry)):
	# if(intersection(l2,qry))	:
	if(intersection(l3,qry)):	
		f=subtract(qry,l1)
		f=subtract(f,l2)
		f=subtract(f,l3)
		s=""
		for word in f:
			s=s+word+" "
		print("Best Time To Visit")
		return best_time_to_visit(s)

	elif(intersection(l4,qry)):	
		f=subtract(qry,l1)
		f=subtract(f,l2)
		f=subtract(f,l4)
		s=""
		for word in f:
			s=s+word+" "
		print("Places To Visit")
		return places_to_visit(s)

	############################################################
	#					Current Temperature
	############################################################

	l1=["weather","temperature","temp","climate"]
	if(intersection(l1,qry)):
		f=subtract(qry,l1)
		s=""
		for word in f:
			s=s+word+" "
		return current_temperature(s)


	############################################################
	#					Places to eat
	############################################################
	l1=["eateries","eatery","eat","restaurant","restaurants","dhaba","food","snacks","tea","coffee","drink","drinks"]
	if(intersection(l1,qry)):
		f=subtract(qry,l1)
		s=""
		for word in f:
			s=s+word+" "
		return restaurants_near_me(s)

	############################################################
	#					Hotels
	############################################################
	l1=["hotel","hotels","guesthouse","lodge","stay"]
	if(intersection(l1,qry)):
		l1.extend(["place","places"])
		f=subtract(qry,l1)
		s=""
		for word in f:
			s=s+word+" "
		if("star" in s or "stars" in s):
			s=s.replace("stars","")
			s=s.replace("star","")
			if("2" in s or "two" in s):
				return hotels_near_me(s,2)
			if("3" in s or "three" in s):
				return hotels_near_me(s,3)
			if("4" in s or "four" in s):
				return hotels_near_me(s,4)
			if("5" in s or "five" in s):
				return hotels_near_me(s,5)

		return hotels_near_me(s,4)

	############################################################
	#					Nearest Railway Station
	############################################################
	l1=["rail","railway","station","train","stations"]
	if(intersection(l1,qry)):
		f=subtract(qry,l1)
		s=""
		for word in f:
			s=s+word+" "

		return nearest_railway_station(s)

	############################################################
	#					Nearest Airport
	############################################################
	l1=["airport","airway"]
	if(intersection(l1,qry)):
		f=subtract(qry,l1)
		s=""
		for word in f:
			s=s+word+" "

		return nearest_airport(s)

	############################################################
	#					Booking Flights
	############################################################
	l1=["flight","plane","airway","tickets","air","book","from"]
	if(intersection(l1,qry)):
		f=subtract(qry,l1)
		return book_air_tickets(f[0],f[1])
	

	return tell_me_about(init_msg)
