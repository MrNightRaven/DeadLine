
# -*- coding: utf-8 -*-
#Thanks Author Trevor :]
#Mute for notification your group
#jadi fungsinya kaya lu matiin notif group lu biar line lu ga bising hahaha :)
from linepy import *
from akad import *
from akad import ttypes
from akad import TalkService
from datetime import datetime
from multiprocessing import Process, Pool
import time, random, sys, json, codecs, ast, threading, glob, re, string, os, requests, subprocess, six, atexit, datetime, multiprocessing, pytz



trev = LINE()#kosongin aja kalau pengen login qr
trev.log("Auth Token: " + str(trev.authToken))

oepoll = OEPoll(trev)
inti = trev.profile.mid
intii = trev.getProfile().mid

def example(op):
    try:
        if op.type == 25:
            msg = op.message
            pesan = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if "mute:on" == pesan.lower():
                aa = trev.getGroup(msg.to)
                if aa.notificationDisabled == False:
                    trev.sendMessage(msg.to,"Already Mute :)")
                else:
                    aa.notificationDisabled = False
                    trev.updateGroup(aa)
                    trev.sendMessage(msg.to,"Berhasil menyalakan notif")
            if "mute:off" == pesan.lower():
                aa = trev.getGroup(msg.to)
                if aa.notificationDisabled == True:
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
        
        
