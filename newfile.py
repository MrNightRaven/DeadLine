from linepy import *
from akad import *
from akad import TalkService
from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Process, Pool
import time, random, sys, json, codecs, ast, threading, glob, re, string, os, requests, subprocess, six, atexit, datetime, multiprocessing, pytz
from datetime import datetime
import locale
from urllib import parse as urlparse
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import six; from six.moves import cPickle as pickle
import os, random, psutil, time, threading
import numpy as np
from threading import Thread

mike = LINE("TOKEN KAMU")#kosongin aja kalau pengen login qr
mike.log("Auth Token: " + str(mike.authToken))

oepoll = OEPoll(mike)
simike = mike.getProfile().mid

pergrup = ["disini diisi gid/groupid. dikosongin juga gapapa"] #ini dipake buat yg mau botnya aktif cuman pergrup bukan global/menyeluruh



#Udah ya langsung aja ya simple kok ;)#
#Yang mo ngejudge hargai hasil usaha orang

while True:
	try:
		ops = oepoll.singleTrace(count=50)
		if ops is not None:
			for op in ops:
				if op.type == 25:
					if op.param1 in pergrup:
						msg = op.message()
						pesanku = msg.text
						msg_id = msg.id
						buatsiska = msg.to
						darimike = msg._from
						try:
							if msg.contentType == 0:
								if "help" == pesanku.lower():
									siskacantik = "Selfbot Version\n"
									siskacantik += "Speed"
									mike.sendMessage(buatsiska, siskacantik)
							if "speed" == pesanku.lower():
								aa = time.time()
								mike.sendMessage(buatsiska,"wait mike")
								ab = time.time() - aa
								mike.sendMessage(buatsiska, "%s " % (ab))
							if "restart" == pesanku.lower():
								mike.sendMessage(buatsiska, "Restart Program")
								python = sys.executable
								os.execl(python, python, *sys.argv)
								
								
						except Exception as error:
							trev.sendMessage(buatsiska, error)
			if op.type == 25:
				msg = op.message
				pesanku = msg.text
				msg_id = msg.id
				buatsiska = msg.to
				darimike = msg._from
				try:
					if msg.contentType == 0:
						if "bot:on" == pesanku.lower():
							if msg.to in pergrup:
								siskacantik = mike.getGroup(msg.to)
								aa = "STATUS: \n Already Trev"
								mike.sendMessage(buatsiska, aa)
							else:
								siskacantik = mike.getGroup(msg.to)
								pergrup.append(msg.to)
								simike = "\nAbout:\n BOT MODE AKTIF HANYA DI GROUP {}".format(siskacantik)
								mike.sendMessage(buatsiska,simike)
						if "bot:off" == pesanku.lower():
							if msg.to in pergrup:
								siskaa = mike.getGroup(msg.to)
								pergrup.remove(msg.to)
								mikey = "BOT AKAN DI NON AKTIFKAN DI GROUP {}".format(siskaa)
								mike.sendMessage(buatsiska, mikey)
							else:
								siskaa = mike.getGroup(msg.to)
								cantik = "Already Remove or not registerd"
								mike.sendMessage(buatsiska, cantik)
								
							
				except Exception as error:
					print(error)
			oepoll.setRevision(op.revision)
						
	except Exception as error:
		print(error)
		
#Thanks ;) 