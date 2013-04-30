import elementtree.ElementTree as ET
from database import Redis
import re


'''
NOTE: unicode.

sys.setdefaultencoding('iso-8859-1')

'''


class Crawler:
	def __init__(self, file, output):
		self.file = file
		self.output = output
		self.context = iter(ET.iterparse(file))
		self.database = Redis()
		self.par_re = re.compile(ur'\[\[([\w, \(\)"]+)\]\]') #For parsing for article links
		self.redirect_re = re.compile(ur'#REDIRECT',re.UNICODE)
		
		
		
		'''
		Regular Expression (above): matches [[word]] where 'word' can have any alphanumeric characters, along with the characters ",()
		'''
		
	def parse_article(self, text):
		if text is not None:
			return self.par_re.findall(text) 
		else:
			return []
		

	def is_redirect(self, text):
		if text is not None:
			return self.redirect_re.findall(text)	 
		
	def crawl(self):
		event, root = self.context.next()
		self.output.write("Started")
			
		for event, elem in self.context:
			if elem.tag == '{http://www.mediawiki.org/xml/export-0.4/}page':
				title = elem.find('{http://www.mediawiki.org/xml/export-0.4/}title').text
				#self.output.write("%s\n" % title)
				'''
				if self.is_redirect(elem.find('./{http://www.mediawiki.org/xml/export-0.4/}revision/{http://www.mediawiki.org/xml/export-0.4/}text').text):
					self.database.add_set("redirects",title)
				'''
				
				
				if not self.database.is_member_set("redirects",title):
					self.database.add_set("articles",title)
				links = self.parse_article(elem.find('./{http://www.mediawiki.org/xml/export-0.4/}revision/{http://www.mediawiki.org/xml/export-0.4/}text').text)
				
				for link in links:
					if not self.database.is_member_set("redirects",link):
						self.database.add_set(title,link)
				
				elem.clear()
				
