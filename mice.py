# -*- coding: utf-8 -*-
from linepy import *
from akad import *
from akad import TalkService

trev = LINE("Esq17c1lzRHiSrlABJ91.rJuz0N0TgYkI9BTxFRkoSq.8Uzqdyp5AnZ2PTu2H9az0eNFjM/CNZNWAGA79uGKG3Q=")
trev.log("Ini Auth Token mu: {}".format(str(channel.getChannelResult())))

trev2 = LINE("EsbQTNzvBuXikwktGXn6.Vp/dMx+zq4GmBnGUgwhKjG.SS45xqgULbABLPmvNI5adi1YeBGIjexXJ4eOo50pkVY=")
trev2.log("In Auth Token TREVOR2: {}".format(str(channel.getChannelResult())))

trev3 = LINE("EsYNNhCq8v1xMcjgTLU4.FJRwpnblCqckSZFvFol3na.IAurqd2e/OdyW6RZmNitLs1/JNWly79ZiAIeZfAwz9c=")
trev3.log("In Auth Token TREVOR3: {}".format(str(channel.getChannelResult())))
trev4 = LINE("EsDLzrwj9BKbvmQzin2f./0YOwEcSseri8u3XXZhipW.s+Vgpx7JiaseqwLQXP3f5xrPLGSWotl0t7Q9u1O6Q70=")
trev4.log("In Auth Token TREVOR4: {}".format(str(channel.getChannelResult())))
oepoll = OEPoll(trev)
cl = trev
ca = trev2
cs = trev3
cz = trev4
KAC=[cl,ca,cs,cz]
A3V=[ca,cs,cz]
KAV=[ca,cs]
mid = cl.getProfile().mid
Amid = ca.getProfile().mid
Bmid = cs.getProfile().mid
Cmid = cz.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid]
admin=["uecc0e521c7c6f1a7c9e09bc2bb019523"]
settingTamu = []
settingQr=[]
settingProtect=[]
settingCancel=[]

helpmsg = """
*url:on/off
*linkprotect:on/off
*cancelprotect:on/off
*kickprotect:on/off
*inviteprotect:on/off
*trevmasuk
*trevbye
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
def mice(op):
	try:
		if op.type == 13:
			if op.param3 in mid:
				if op.param2 in Amid:
					G = ca.getGroup(op.param1)
					G.preventJoinByTicket = False
					ca.updateGroup(G)
					Ticket = ca.reissueGroupTicket(op.param1)
					cl.acceptGroupInvitationByTicket(op.param1,Ticket)
					G.preventJoinByTicket = True
					ca.updateGroup(G)
					Ticket = ca.reissueGroupTicket(op.param1)
			if op.param3 in Amid:
				if op.param2 in Bmid:
					X = cs.getGroup(op.param1)
					X.preventJoinByTicket = False
					cs.updateGroup(X)
					Ti = cs.reissueGroupTicket(op.param1)
					ca.acceptGroupInvitationByTicket(op.param1,Ti)
					X.preventJoinByTicket = True
					cs.updateGroup(X)
					Ti = cs.reissueGroupTicket(op.param1)
			if op.param3 in Bmid:
				if op.param2 in Cmid:
					X = cz.getGroup(op.param1)
					X.preventJoinByTicket = False
					cz.updateGroup(X)
					Ti = cz.reissueGroupTicket(op.param1)
					cs.acceptGroupInvitationByTicket(op.param1,Ti)
					X.preventJoinByTicket = True
					cz.updateGroup(X)
					Ti = cz.reissueGroupTicket(op.param1)
					
			if op.param3 in Cmid:
				if op.param2 in mid:
					X = cl.getGroup(op.param1)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					Ti = cl.reissueGroupTicket(op.param1)
					cz.acceptGroupInvitationByTicket(op.param1,Ti)
					X.preventJoinByTicket = True
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
							G.preventJoinByTicket = False
							ca.updateGroup(G)
							Ti = ca.reissueGroupTicket(op.param1)
							cl.acceptGroupInvitationByTicket(op.param1,Ti)
							cs.acceptGroupInvitationByTicket(op.param1,Ti)
							cz.acceptGroupInvitationByTicket(op.param1,Ti)
							X = ca.getGroup(op.param1)
							X.preventJoinByTicket = True
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
						X.preventJoinByTicket = False
						cs.updateGroup(X)
						Ti = cs.reissueGroupTicket(op.param1)
						cl.acceptGroupInvitationByTicket(op.param1,Ti)
						ca.acceptGroupInvitationByTicket(op.param1,Ti)
						cz.acceptGroupInvitationByTicket(op.param1,Ti)
						G = cs.getGroup(op.param1)
						G.preventJoinByTicket = True
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
							X.preventJoinByTicket = False
							cz.updateGroup(X)
							Ti = cz.reissueGroupTicket(op.param1)
							cl.acceptGroupInvitationByTicket(op.param1,Ti)
							ca.acceptGroupInvitationByTicket(op.param1,Ti)
							cs.acceptGroupInvitationByTicket(op.param1,Ti)
							G = cz.getGroup(op.param1)
							G.preventJoinByTicket = True
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
							X.preventJoinByTicket = False
							ca.updateGroup(X)
							Ti = ca.reissueGroupTicket(op.param1)
							cl.acceptGroupInvitationByTicket(op.param1,Ti)
							cs.acceptGroupInvitationByTicket(op.param1,Ti)
							cz.acceptGroupInvitationByTicket(op.param1,Ti)
							G = cz.getGroup(op.param1)
							G.preventJoinByTicket = True
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
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					invsend = 0
					Ti = cl.reissueGroupTicket(op.param1)
					ca.acceptGroupInvitationByTicket(op.param1,Ti)
					cs.acceptGroupInvitationByTicket(op.param1,Ti)
					cz.acceptGroupInvitationByTicket(op.param1,Ti)
					G = cz.getGroup(op.param1)
					G.preventJoinByTicket = True
					cz.updateGroup(G)
					cz.reissueGroupTicket(op.param1)
					
		if op.type == 11:
			if op.param2 not in Bots:
				if op.param2 not in admin:
					if op.param1 in settingQr:
						blacklist.append(op.param2)
						G = cl.getGroup(op.param1)
						G.preventJoinByTicket = True
						random.choice(A3V).kickoutFromGroup(op.param1,[op.param2])
						random.choice(A3V).updateGroup(G)
		if op.type == 26:
			msg = op.message
			pesanku = msg.text
			msg_id = msg.id
			receiver = msg.to
			darimike = msg._from
			try:
				if "linkprotect:on" == pesan.lower():
					if msg._from in admin:
						if msg.to in settingQr:
							siska = cl.getGroup(msg.to,"「􏿿 Protect Link 」\n Protect Link Already Activated in Group {}".format(siska.name))
						else:
							settingQr.append(msg.to)
							siska = cl.getGroup(msg.to)
							cl.getGroup(msg.to,"「􏿿 Protect Link 」\n Protect Link Has Been Activated in Group {}".format(siska.name))
							cl.sendMessage(msg.to,"")
				if "linkprotect:off" == pesan.lower():
					if msg._from in admin:
						if msg.to in settingQr:
							siska = cl.getGroup(msg.to)
							settingQr.remove(msg.to)
							cl.sendMessage(msg.to,"「􏿿 Protect Link 」\n Protect Link Has Been Non-Activated in Group {}".format(siska.name))
						else:
							cl.sendMessage(msg.to,"「􏿿 Protect Link 」\n Protect Link Already Non-Active")
					if "cancelprotect:on" == pesan.lower():
						if msg._from in admin:
							if msg.to in settingCancel:
								cl.sendMessage(msg.to,"「􏿿 Protect Cancel 」\n Protect Cancel Already Active")
							else:
								settingCancel.append(msg.to)
								cl.sendMessage(msg.to,"「􏿿 Protect Cancel 」\n Protect Cancel Has Been Activated")
					if "cancelprotect:off" == pesan.lower():
						if msg._from in admin:
							if msg.to in settingCancel:
								settingCancel.remove(msg.to)
								cl.sendMessage(msg.to,"「􏿿 Protect Cancel 」\n Protect Cancel Has Been Non-Activated")
							else:
								cl.sendMessage(msg.to,"「􏿿 Protect Cancel 」\n Protect Cancel Already Non-Active")
					if "kickprotect:on" == pesan.lower():
						if msg._from in admin:
							if msg.to in settingProtect:
								cl.sendMessage(msg.to,"「􏿿 Protect Kick 」\n Protect Kick Already Active")
							else:
								settingProtect.append(msg.to)
								cl.sendMessage(msg.to,"「􏿿 Protect Kick 」\n Protect Kick Has Been Activated")
					if "kickprotect:off" == pesan.lower():
						if msg._from in admin:
							if msg.to in settingProtect:
								settingProtect.remove(msg.to)
								cl.sendMessage(msg.to,"「􏿿 Protect Kick 」\n Protect Has Been Non-Activated")
							else:
								cl.sendMessage(msg.to,"「􏿿 Protect Kick 」\n Protect Kick Already Non-Active")
								
					if "inviteprotect:on" == pesan.lower():
						if msg._from in admin:
							if msg.to in settingTamu:
								cl.sendMessage(msg.to,"「􏿿 Protect Invite 」\n Protect Invite Already Active")
							else:
								settingTamu.append(msg.to)
								cl.sendMessage(msg.to,"「􏿿 Protect Invite 」\n Protect Invite Has Been Activated")
								
					if "inviteprotect:off" == pesan.lower():
						if msg._from in admin:
							if msg.to in settingTamu:
								settingGuest.remove(msg.to)
								cl.sendMessage(msg.to,"「􏿿 Protect Invite 」\n Protect Invite Has Been Non-Activated")
							else:
								cl.sendMessage(msg.to,"「􏿿 Protect Invite 」\n Protect Invite Already Non-Active")
					if "url:off" == pesan.lower():
						if msg._from in admin:
							aa = cl.getGroup(msg.to)
							aa.preventedJoinByTicket = True
							cl.updateGroup(aa)
							cl.sendMessage(msg.to,"「􏿿 Link Group 」\n⚔ Status: Blocked QR in Group {}".format(aa.name))
						else:
							cl.sendMessage(msg.to,"You're Not Admin")
					if "url:on" == pesan.lower():
						if msg._from in admin:
							X = cl.getGroup(msg.to)
							X.preventedJoinByTicket = True
							cl.updateGroup(X)
							cl.sendMessage(msg.to,"「􏿿 Link Group 」\n⚔ Status: Allowed QR in Group {}".format(X.name))
						else:
							cl.sendMessage(msg.to,"You're Not Admin")
					if "help" == pesan.lower():
						cl.sendMesage(msg.to,helpmsg)
					if "trevmasuk" == pesan.lower():
						if msg._from in admin:
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
							G.preventJoinByTicket = True
							cz.updateGroup(G)
							ca.sendMessage(msg.to,"Halo ! "+ str(ginfo.name))
							cs.sendMessage(msg.to,"Halo ! "+ str(ginfo.name))
							cz.sendMessage(msg.to,"Halo ! "+ str(ginfo.name))
							print("kicker ok")
							G.preventJoinByTicket(G)
							cz.updateGroup(G)
					if "trevbye" == pesan.lower():
						if msg._from in admin:
							ginfo = cl.getGroup(msg.to)
							try:
								cl.sendMessage(msg.to,"Bye ! "+ str(ginfo.name))
								ca.sendMessage(msg.to,"Bye ! "+ str(ginfo.name))
								cs.sendMessage(msg.to,"Bye ! "+ str(ginfo.name))
								cz.sendMessage(msg.to,"Bye ! "+ str(ginfo.name))
								cl.leaveGroup(msg.to)
								ca.leaveGroup(msg.to)
								cs.leaveGroup(msg.to)
								cz.leaveGroup(msg.to)
							except:
								pass
			except Exception as error:
				print(error)
	except Exception as error:
		print(error)

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