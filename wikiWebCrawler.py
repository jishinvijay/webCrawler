import requests
from bs4 import BeautifulSoup
import time
import urllib


#Get the first link
def get_first_link(input_url):
	"""
	This function accepts a string as the input url
	Looks up and returns the first url that comes up
	"""
	response = requests.get(input_url)
	#print("input url : {}".format(input_url))
	page_link = response.text

	soup = BeautifulSoup(page_link,"html.parser")
	content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

	article_link = None


	for element in content_div.find_all("p", recursive=False):
		if element.find("a", recursive=False):
			article_link = element.find("a", recursive=False).get('href')
			#print (article_link)
			break
	
	if article_link:
		return urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
	else:
		return article_link	


def exit_criteria(link_history,target_url):
	"""
	This function accepts a list of URLs and a target URL string.
	This function looks up the first html anchor tag, and returns the anchor url.
	The function returns None if no anrchor tag is found.
	"""
	if link_history[-1] == target_url :
		"""
		Target URL reached
		"""
		print('Target URL reached!!!')
		return False
	if len(link_history) > 25:
		"""
		Crawling URL List more than 25
		"""
		print('Crawling URL List more than 25!!!')
		return False
	if link_history[-1] in link_history[:-1]:
		"""
		Loop detected
		"""
		print('Loop detected at URL : ''{}'''.format(link_history[-1]))
		return False
	else:
		print('{} : {}'.format(len(link_history),link_history[-1]))
		return True

start_url = 'https://en.wikipedia.org/wiki/Special:Random'
target_url = 'https://en.wikipedia.org/wiki/Philosophy'

link_history=[]

#store the first link in history
link_history.append(start_url)

next_url=None

while exit_criteria(link_history,target_url):
	next_url=get_first_link(link_history[-1])

	if next_url:
		link_history.append(next_url)
	else:
		print('No more URLs found!!')
		break

	time.sleep(2)

#print('URL History ::')
#for url in link_history:
#	print(url)


