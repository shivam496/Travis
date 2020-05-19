import pickle


f=open("stop_words.txt")
li=f.readlines()

for i in range(0,len(li)):
	li[i]=li[i].rstrip('\n')

print(li)

with open('stopwords.pkl', 'wb') as f:
	pickle.dump(li, f)