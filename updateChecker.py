#!/usr/bin/python2

from subprocess import Popen,PIPE



class updateChecker:
	def __init__(self):
		self.packageList = Popen(['sudo','pacman','-Qu'],stdout = PIPE).communicate()[0].split('\n')
		self.genPackageDict()
		self.down = self.inst = 0
		self.getTotalSize()
		self.printPackages()

	def genPackageDict(self):
		self.packageDict = {}
		self.totalSize = 0;
		for package in self.packageList:
			if package:
				info = Popen(['pacman','-Si',package.split()[0]],stdout = PIPE)
				sizes = Popen(['grep','Size'],stdin=info.stdout,stdout=PIPE).communicate()[0]
				self.packageDict[package] = [sizes.split()[3],sizes.split()[8]]

	def getTotalSize(self):
		for package in self.packageDict:
			self.down += float(self.packageDict[package][0])
			self.inst += float(self.packageDict[package][1])

	def printPackages(self):
		print "Package Name"
		print "==============================="
		for package in self.packageDict:
			print package
		print "================================"
		print "Total Download Size :",
		if self.down > 1024:
			print round(self.down/1024,2),"MB"	
		else:
			print round(self.down,2),"KB"
		print "Total Install Size :",
		if self.inst > 1024:
			print round(self.inst/1024,2),"MB"	
		else:
			print round(self.inst,2),"KB"


check = updateChecker()

		
