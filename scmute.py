# -*- coding: utf-8 -*-
#author trevor
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

trev = LINE()
trev.log("Auth Token: " + str(trev.authToken))

oepoll = OEPoll(trev)
inti = trev.profile.mid
intii = trev.getProfile().mid


def example(op):
	try:
		msg = op.message()
		pesan = msg.text
		msg_id = msg.id
		receiver = msg.to
		sender = msg._from
		if "mute:on" == pesan.lower():
			aa = trev.getGroup(msg.to)
			if aa.notificationDisable == False:
				trev.sendMessage(msg.to,"Already Mute :)")
			else:
				aa.notificationDisabled = False
				trev.updateGroup(aa)
				trev.sendMessage(msg.to,"Berhasil menyalakan notif")
			if "mute:off" == pesan.lower():
				aa = trev.getGroup(msg.to)
				if aa.notificationDisable == True:
					trev.sendMessage(msg.to,"Already mute notif trev")
				else:
					aa.notificationDisabled = True
					trev.updateGroup(aa)
					trev.sendMessage(msg.to,"Berhasil menonaktifkan notif group")
					
	except Exception as e:
		print(e)
while True:
	try:
		ops = oepoll.singleTrace(count=50)
		if ops is not None:
			for op in ops:
				example(op)
				oepoll.setRevision(op.revision)
	except Exception as e:
		print(e)