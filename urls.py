#!usr/bin/python3

import webbrowser
from googlesearch import google
urls=open('urlfile.txt','w')
data= input('Search for a topic:')

#x = number of urls
x=search(web,stop=10)

for i in x:
	urls.write(i + "\n")
webbrowser.open("https://www.google.co.in/search?q="+data)
