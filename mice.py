# -*- coding: utf-8 -*-
#author :Mike!
#sesuaikan dengan lib kamu :)

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit

from threading import Thread


cl = LINE()
cl.log("Ini Auth Token mu:"+str(cl.authToken))

ca = LINE()
ca.log("In Auth Token TREVOR2:"+str(ca.authToken))

cs = LINE()
cs.log("In Auth Token TREVOR3:" + str(cs.authToken))

cz = LINE()
cz.log("In Auth Token TREVOR4: "+str(cz.authToken))

oepoll = OEPoll(cl)
capoll = OEPoll(ca)
cspoll = OEPoll(cs)
czpoll = OEPoll(cz)

KAC=[cl,ca,cs,cz]
A3V=[ca,cs,cz]
KAV=[ca,cs]
mid = cl.getProfile().mid
Amid = ca.getProfile().mid
Bmid = cs.getProfile().mid
Cmid = cz.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid]
admin=["uecc0e521c7c6f1a7c9e09bc2bb019523"]
settingTamu = [] #protect pergrup tidak global
settingQr=[] #protect pergrup 
settingProtect=[] #pergrup
settingCancel=[] #pergrup

helpmsg = """
*url:on/off
*linkprotect:on/off
*cancelprotect:on/off
*kickprotect:on/off
*inviteprotect:on/off
*trevmasuk
*trevbye
*system
"""
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print("[Command] Tag All")
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print(error)
def command(pesan):
    cmd = pesan.lower()
    return cmd
    
def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
def mice(op):
	try:
		if op.type == 13:
			if op.param3 in mid:
				if op.param2 in Amid:
					G = ca.getGroup(op.param1)
					G.preventedJoinByTicket = False
					ca.updateGroup(G)
					Ticket = ca.reissueGroupTicket(op.param1)
					cl.acceptGroupInvitationByTicket(op.param1,Ticket)
					G.preventedJoinByTicket = True
					ca.updateGroup(G)
					Ticket = ca.reissueGroupTicket(op.param1)
			if op.param3 in Amid:
				if op.param2 in Bmid:
					X = cs.getGroup(op.param1)
					X.preventedJoinByTicket = False
					cs.updateGroup(X)
					Ti = cs.reissueGroupTicket(op.param1)
					ca.acceptGroupInvitationByTicket(op.param1,Ti)
					X.preventedJoinByTicket = True
					cs.updateGroup(X)
					Ti = cs.reissueGroupTicket(op.param1)
			if op.param3 in Bmid:
				if op.param2 in Cmid:
					X = cz.getGroup(op.param1)
					X.preventedJoinByTicket = False
					cz.updateGroup(X)
					Ti = cz.reissueGroupTicket(op.param1)
					cs.acceptGroupInvitationByTicket(op.param1,Ti)
					X.preventedJoinByTicket = True
					cz.updateGroup(X)
					Ti = cz.reissueGroupTicket(op.param1)
					
			if op.param3 in Cmid:
				if op.param2 in mid:
					X = cl.getGroup(op.param1)
					X.preventedJoinByTicket = False
					cl.updateGroup(X)
					Ti = cl.reissueGroupTicket(op.param1)
					cz.acceptGroupInvitationByTicket(op.param1,Ti)
					X.preventedJoinByTicket = True
					cl.updateGroup(X)
					Ti = cl.reissueGroupTicket(op.param1)
		if op.type == 19:
			if mid in op.param3:
				if op.param2 not in Bots and admin:
					pass
				try:
					ca.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						random.choice(A3V).kickoutFromGroup(op.param1,[op.param2])
						random.choice(A3V).inviteIntoGroup(op.param1,[op.param3])
					except:
						print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
						if op.param2 in blacklist:
							pass
						else:
							blacklist.append(op.param2)
							G = ca.getGroup(op.param1)
							G.preventedJoinByTicket = False
							ca.updateGroup(G)
							Ti = ca.reissueGroupTicket(op.param1)
							cl.acceptGroupInvitationByTicket(op.param1,Ti)
							cs.acceptGroupInvitationByTicket(op.param1,Ti)
							cz.acceptGroupInvitationByTicket(op.param1,Ti)
							X = ca.getGroup(op.param1)
							X.preventedJoinByTicket = True
							ca.updateGroup(X)
							Ti = ca.reissueGroupTicket(op.param1)
							if op.param2 in blacklist:
								pass
							else:
								blacklist.append(op.param2)
								
			if Amid in op.param3:
				if op.param2 not in Bots and admin:
					pass
				try:
					cs.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						random.choice(A3V).kickoutFromGroup(op.param1,[op.param2])
						random.choice(A3V).inviteIntoGroup(op.param1,[op.param3])
					except:
						print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
						print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
					if op.param2 in blacklist:
						pass
					else:
						blacklist.append(op.param2)
						X = cs.getGroup(op.param1)
						X.preventedJoinByTicket = False
						cs.updateGroup(X)
						Ti = cs.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ti)
						ca.acceptGroupInvitationByTicket(op.param1,Ti)
						cz.acceptGroupInvitationByTicket(op.param1,Ti)
						G = cs.getGroup(op.param1)
						G.preventedJoinByTicket = True
						cs.updateGroup(G)
						Ticket = cs.reissueGroupTicket(op.param1)
						if op.param2 in blacklist:
							pass
						else:
							blacklist.append(op.param2)
			if Bmid in op.param3:
				if op.param2 not in Bots and admin:
					pass
				try:
					cz.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						random.choice(A3V).kickoutFromGroup(op.param1,[op.param2])
						random.choice(A3V).inviteIntoGroup(op.param1,[op.param3])
					except:
						print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
						if op.param2 in blacklist:
							pass
						else:
							blacklist.append(op.param2)
							X = cz.getGroup(op.param1)
							X.preventedJoinByTicket = False
							cz.updateGroup(X)
							Ti = cz.reissueGroupTicket(op.param1)
							cl.acceptGroupInvitationByTicket(op.param1,Ti)
							ca.acceptGroupInvitationByTicket(op.param1,Ti)
							cs.acceptGroupInvitationByTicket(op.param1,Ti)
							G = cz.getGroup(op.param1)
							G.preventedJoinByTicket = True
							cz.updateGroup(G)
							Ticket = cz.reissueGroupTicket(op.param1)
							if op.param2 in blacklist:
								pass
							else:
								blacklist.append(op.param2)
								
			if Cmid in op.param3:
				if op.param2 not in Bots and admin:
					pass
				try:
					cl.kickoutFromGroup(op.param1,[op.param2])
				except:
					try:
						random.choice(A3V).kickoutFromGroup(op.param1,[op.param2])
						random.choice(A3V).inviteIntoGroup(op.param1,[op.param3])
					except:
						print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
						if op.param2 in blacklist:
							pass
						else:
							blacklist.append(op.param2)
							X = ca.getGroup(op.param1)
							X.preventedJoinByTicket = False
							ca.updateGroup(X)
							Ti = ca.reissueGroupTicket(op.param1)
							cl.acceptGroupInvitationByTicket(op.param1,Ti)
							cs.acceptGroupInvitationByTicket(op.param1,Ti)
							cz.acceptGroupInvitationByTicket(op.param1,Ti)
							G = cz.getGroup(op.param1)
							G.preventedJoinByTicket = True
							cz.updateGroup(G)
							Ticket = cz.reissueGroupTicket(op.param1)
							if op.param2 in blacklist:
								pass
							else:
								blacklist.append(op.param2)
								
		if op.type == 13:
			if op.param2 not in Bots:
				if op.param2 not in admin:
					if op.param3 not in admin:
						if op.param1 in settingTamu:
							blacklist.append(op.param2)
							group = cl.getGroup(op.param1)
							random.choice(A3V).cancelGroupInvitation(op.param1,[op.param3])
							random.choice(A3V).kickoutFromGroup(op.param1,[op.param2])
						
		if op.type == 19:
			if op.param2 not in Bots:
				if op.param2 not in admin:
					if op.param3 in admin:
						if op.param1 in settingProtect:
							try:
								mybot=[cl,ca,cs,cz]
								asw = random.choice(mybot)
								blacklist.append(op.param2)
								asw.kickoutFromGroup(op.param1,[op.param2])
								inviteIntoGroup(op.param1,[op.param3])
							except Exception as error:
								print(error)
					
		if op.type == 32:
			if op.param2 not in Bots:
				if op.param2 not in admin:
					if op.param3 not in admin:
						if op.param1 in settingCancel:
							blacklist.append(op.param2)
							group = cl.getGroup(op.param1)
							random.choice(A3V).cancelGroupInvitation(op.param1, [op.param3])
							random.choice(A3V).kickoutFromGroup(op.param1,[op.param2])
						
		if op.type == 13:
			if op.param3 in mid:
				if op.param2 in admin:
					G = cl.getGroup(op.param1)
					cl.acceptGroupInvitation(op.param1)
					G.preventedJoinByTicket = False
					cl.updateGroup(G)
					invsend = 0
					Ti = cl.reissueGroupTicket(op.param1)
					ca.acceptGroupInvitationByTicket(op.param1,Ti)
					cs.acceptGroupInvitationByTicket(op.param1,Ti)
					cz.acceptGroupInvitationByTicket(op.param1,Ti)
					G = cz.getGroup(op.param1)
					G.preventedJoinByTicket = True
					cz.updateGroup(G)
					cz.reissueGroupTicket(op.param1)
					
		if op.type == 11:
			if op.param2 not in Bots:
				if op.param2 not in admin:
					if op.param1 in settingQr:
						blacklist.append(op.param2)
						G = cl.getGroup(op.param1)
						G.preventedJoinByTicket = True
						random.choice(A3V).kickoutFromGroup(op.param1,[op.param2])
						random.choice(A3V).updateGroup(G)
		if op.type == 26:
			msg = op.message
			pesan = msg.text
			msg_id = msg.id
			receiver = msg.to
			sender = msg._from
			if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
				if msg.toType == 0:
					if sender != cl.profile.mid:
						to = sender
					else:
						to = receiver
				elif msg.toType == 1:
					to = receiver
				elif msg.toType == 2:
					to = receiver
				if msg.contentType == 0:
					if pesan is None:
						return
					else:
						cmd = command(pesan)
						if cmd == "help":cl.sendMessage(to, "Trevor\n"+helpmsg)
						if "linkprotect:on" == pesan.lower():
							if sender in admin:
								if msg.to in settingQr:
									septa = cl.getGroup(msg.to)
									cl.sendMessage(to,"「􏿿 Protect Link 」\n Protect Link Already Active in Group {}".format(str(septa.name)))
								else:
									septa = cl.getGroup(msg.to)
									settingQr.append(msg.to)
									cl.sendMessage(to,"「􏿿 Protect Link 」\n Protect Link Has Been Activated in Group {}".format(str(septa.name)))
						if "linkprotect:off" == pesan.lower():
							if sender in admin:
								if msg.to in settingQr:
									septa = cl.getGroup(msg.to)
									settingQr.remove(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Link 」\n Protect Link Has Been Non-Activated in Group [{}]".format(str(septa.name)))
								else:
									septa = cl.getGroup(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Link 」\n Protect Link Already Non-Active in Group [{}]".format(str(septa.name)))
						if "cancelprotect:on" == pesan.lower():
							if sender in admin:
								if msg.to in settingCancel:
									septa = cl.getGroup(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Cancel 」\n Protect Cancel Already Active in Group [{}]".format(septa.name))
								else:
									septa = cl.getGroup(msg.to)
									settingCancel.append(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Cancel 」\n Protect Cancel Has Been Activated in Group [{}]".format(septa.name))
						if "cancelprotect:off" == pesan.lower():
							if sender in admin:
								if msg.to in settingCancel:
									septa = cl.getGroup(msg.to)
									settingCancel.remove(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Cancel 」\n Protect Cancel Has Been Non-Activated in Group [{}]".format(septa.name))
								else:
									septa = cl.getGroup(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Cancel 」\n Protect Cancel Already Non-Active in Group [{}]".format(septa.name))
						if "kickprotect:on" == pesan.lower():
							if sender in admin:
								if msg.to in settingProtect:
									septa = cl.getGroup(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Kick 」\n Protect Kick Already Active in Group [{}]".format(septa.name))
								else:
									settingProtect.append(msg.to)
									septa = cl.getGroup(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Kick 」\n Protect Kick Has Been Activated in Group [{}]".format(septa.name))
						if "kickprotect:off" == pesan.lower():
							if sender in admin:
								if msg.to in settingProtect:
									septa = cl.getGroup(msg.to)
									settingProtect.remove(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Kick 」\n Protect Has Been Non-Activated in Group [{}]".format(septa.name))
								else:
									septa = cl.getGroup(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Kick 」\n Protect Kick Already Non-Active in Group [{}]".format(septa.name))
						if "inviteprotect:on" == pesan.lower():
							if sender in admin:
								if msg.to in settingTamu:
									septa = cl.getGroup(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Invite」\n Protect Invite Already Active in Group [{}]".format(septa.name))
								else:
									settingTamu.append(msg.to)
									septa = cl.getGroup(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Invite 」\n Protect Invite Has Been Activated in Group [{}]".format(septa.name))
						if "inviteprotect:off" == pesan.lower():
							if sender in admin:
								if msg.to in settingTamu:
									septa = cl.getGroup(msg.to)
									settingTamu.remove(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Invite 」\n Protect Invite Has Been Non-Activated in Group [{}]".format(septa.name))
								else:
									septa = cl.getGroup(msg.to)
									cl.sendMessage(msg.to,"「􏿿 Protect Invite 」\n Protect Invite Already Non-Active in Group [{}]".format(septa.name))
							
						if "url:on" == pesan.lower():
							if sender in admin:
								aa = cl.getGroup(msg.to)
								aa.preventedJoinByTicket = False
								cl.updateGroup(aa)
							cl.sendMessage(msg.to,"「􏿿 Link Group 」\n⚔ Status: Allowed QR in Group {}".format(aa.name))
								
						if "url:off" == pesan.lower():
							if sender in admin:
								X = cl.getGroup(msg.to)
								X.preventedJoinByTicket = True
								cl.updateGroup(X)
								cl.sendMessage(msg.to,"「􏿿 Link Group 」\n⚔ Status: Blocked QR in Group {}".format(X.name))
								
						
						if "trevmasuk" == pesan.lower():
							if sender in admin:
								G = cl.getGroup(msg.to)
								ginfo = cl.getGroup(msg.to)
								G.preventedJoinByTicket = False
								cl.updateGroup(G)
								invsend = 0
								Ticket = cl.reissueGroupTicket(msg.to)
								ca.acceptGroupInvitationByTicket(msg.to,Ticket)
								cs.acceptGroupInvitationByTicket(msg.to,Ticket)
								cz.acceptGroupInvitationByTicket(msg.to,Ticket)
								G = cz.getGroup(msg.to)
								G.preventedJoinByTicket = True
								cz.updateGroup(G)
						if "trevbye" == pesan.lower():
							if sender in admin:
								ginfo = cl.getGroup(msg.to)
								try:
									cl.sendMessage(msg.to,"Bye ! "+ str(ginfo.name))
									cl.leaveGroup(msg.to)
									ca.leaveGroup(msg.to)
									cs.leaveGroup(msg.to)
									cz.leaveGroup(msg.to)
								except:
									pass
									
						if "system" == pesan.lower():
							 mike = "SYSTEM BOT\n"
							 if msg.to in settingTamu: mike +="⌬ [ON] Protect Invite \n"
							 else: mike +="⌬ [OFF] Protect Invite \n"
							 if msg.to in settingQr: mike +="⌬ [ON] Protect Link \n"
							 else: mike +="⌬ [OFF] Protect Link \n"
							 if msg.to in settingProtect : mike+="⌬ [ON] Protection \n"
							 else:mike+="⌬ [OFF] Protection \n"
							 if msg.to in settingCancel : mike+="⌬ [ON] Protect Cancel \n"
							 else:mike+="⌬ [OFF] Protect Cancel \n"
							 cl.sendMessage(msg.to,mike)

							
							
	except Exception as error:
		logError(error)
		traceback.print_tb(error.__traceback__)

def thread():
	while True:
		try:
			ops = oepoll.singleTrace(count=50)
			if ops is not None:
				for op in ops:
					mice(op)
					oepoll.setRevision(op.revision)
		except Exception as e:
			print(e)
			
Thread(target=thread()).start()
print("Started")
