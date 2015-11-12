import lxml.html
from lxml import html
import requests
import sys
import datetime
m_cas_id = 1
m_gen_id = 1
m_pro_id = 1
m_dir_id = 1
m_lan_id = 1
m_cou_id = 1
m_loc_id = 1
#cas_id = 1
gen_id = 1
#pro_id = 1
#dir_id = 1
lan_id = 1
cou_id = 1
loc_id = 1
codelist=[]   #list of codes
movielist=[] #list of dictionaries
def getDetail(url):
	hxs = lxml.html.document_fromstring(requests.get("http://www.imdb.com"+url).content)
	detail = {}
	yr = hxs.xpath('//*[@id="name-born-info"]/time/a[2]/text()')
	md = hxs.xpath('//*[@id="name-born-info"]/time/a[1]/text()')
	if yr == []:
		dt= '0000-00-00'
	else:
		dt = md[0] + " "+yr[0]
		dt=datetime.datetime.strptime(dt, '%B %d %Y').strftime('%Y-%m-%d')
	detail['dob'] = dt
	name = hxs.xpath('//*[@id="overview-top"]/div[1]/div/h1/span[1]/text()')
	if name == []:
		name = hxs.xpath('//*[@id="overview-top"]/h1/span[1]/text()')
	detail['name'] = name[0]
	g = hxs.xpath('//*[@id="name-job-categories"]/a[1]/span/text()')
	g[0] = g[0][1:]
	
	if g[0]=='Actor':
		g[0] = 'M'
	elif g[0]=='Actress':
		g[0]='F'
	else:
		g[0]='-'
	detail['gender'] = g[0]
	detail['pid'] = url[6:15]
	return detail

def getMovie(id): 
	hxs = lxml.html.document_fromstring(requests.get("http://www.imdb.com" + id).content)
	movie_title = hxs.xpath('//*[@id="overview-top"]/h1/span[1]/text()')[0].strip()

	return movie_title

def getCode(url):
	page = requests.get(url)
	tree = html.fromstring(page.text)
	#returns a list
	code = tree.xpath('//*[@id="main"]/table/tr[*]/td[3]/a/@href')
	return code


if __name__ == "__main__":
	urls="http://www.imdb.com/search/title?languages=hi|1&title_type=feature&num_votes=50,&sort=user_rating,desc"
	codelist = getCode(urls)
	n = len(codelist)
	for i in range(n):
		movie_name = getMovie(codelist[i])
		print i+1,". Crawled movie name : "+movie_name
