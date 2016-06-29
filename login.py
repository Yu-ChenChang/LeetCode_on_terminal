import urllib, urllib2, cookielib, re
import ssl 
import sys
import getpass

class leetcode_on_terminal:
	def __init__(self):
		reload(sys)
		sys.setdefaultencoding('utf-8') 
		ssl._create_default_https_context = ssl._create_unverified_context
		self.leeURL = 'https://leetcode.com/'

	def getUserInfo(self):
		self.NAME = raw_input('Username: ')
		self.PWD = getpass.getpass('Password:')

	def login(self):
		loginURL = self.leeURL+'accounts/login/'
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		opener.addheaders = [
			('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko')
		]
		ptn = re.compile(".*name='csrfmiddlewaretoken' value='(.*)'.*")
		login_page_data = opener.open(loginURL).read()
		csrfmiddlewaretoken = ptn.search(login_page_data).group(1)
		data = urllib.urlencode({"csrfmiddlewaretoken":csrfmiddlewaretoken, "login":self.NAME, "password":self.PWD})
		opener.addheaders.append(('Referer', 'https://leetcode.com/accounts/login/'))
		opener.open(loginURL, data)
		if opener == None:
			print 'Failed to login.'
			exit(-1)
		return opener


def mainpage():
	x = leetcode_on_terminal()
	x.getUserInfo()
	x.login()

mainpage()
