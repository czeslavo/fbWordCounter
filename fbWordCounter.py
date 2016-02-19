# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from bs4 import *
import re

class FbWordCounter:
	yourName = ""
	friendsName = ""
	words = []
	stats = {}
	soup = BeautifulSoup()
	namesChanged = True

	def __init__(self, fileName):
		file = open(fileName, 'r')
		self.rawData = file.read()

		
	def parse(self):
		self.soup = BeautifulSoup(self.rawData, 'html.parser', parse_only=SoupStrainer(class_="thread"))


	def countWords(self):
		if self.namesChanged == True:
			self.refreshThreads()
			self.namesChanged = False
		self.stats.clear()
		for thread in self.yourThreads:
			metas = thread.find_all(class_="meta")
			ps = thread.find_all("p")
			for i in range(0, len(metas)):
				date = self.parseDate(metas[i].string)
				for word in self.words:
					if not isinstance(ps[i].string, type(None)):
						match = re.findall(word, u''+ps[i].string, flags=re.IGNORECASE)
						if date in self.stats:
							self.stats[date] += len(match)
						else:
							self.stats[date] = len(match)


	def refreshThreads(self):
		self.yourThreads = self.soup.find_all(self.onlyYourThreads)

	def parseDate(self, dateStr):
		month = {
			"January": "01",
			"February": "02",
			"March": "03",
			"April": "04",
			"May": "05",
			"June": "06",
			"July": "07",
			"August": "08",
			"September": "09",
			"October": "10",
			"November": "11",
			"December": "12"
		}
		myMonth = month[re.search(r", ([A-Z][a-z]+)", dateStr).group(1)]
		day = re.search(r"[0-9]+", dateStr).group(0)
		year = re.search(r", ([0-9]+)", dateStr).group(1)
		return (day, myMonth, year)

	def yourNames(self):
		if self.friendsName > self.yourName:
			return u''+self.yourName + ", " + self.friendsName
		else:
			return u''+self.friendsName + ", " + self.yourName 

	def onlyYourThreads(self, thread):
		names = ""
		visited = False
		for string in thread.strings:
			if visited == True:
				break
			visited = True
			names = u''+string

		if names == self.yourNames():
			return True
		else:
			return False

	def setYourName(self, name):
		self.yourName = name

	def setFriendsName(self, name):
		self.friendsName = name

	def setWords(self, *words):
		self.words = list(words)

	def getStatsByMonth(self):
		months = {}
		for day, number in self.stats.items():
			month = (day[2], day[1])
			if month in months:
				months[month] += number
			else:
				months[month] = number

		statsByMonth = ""
		for month in sorted(months):
			output = month[1] + "." + month[0] + "\t " + str(months[month]) + "\n"
			statsByMonth += output
		return statsByMonth



