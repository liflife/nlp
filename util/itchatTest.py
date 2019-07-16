import itchat
import time
# 登录
itchat.login()
send_userid='灵蕴-旭'
itcaht_user_name = itchat.search_friends(name=send_userid)[0]['UserName']
# 发送消息
itchat.send(u'who are you?',toUserName=itcaht_user_name)
time.sleep(3)
itchat.send(u'lingyun hahaha',toUserName=itcaht_user_name)
time.sleep(3)
itchat.send(u'how old are you?',toUserName=itcaht_user_name)
time.sleep(3)
itchat.send(u'Can you guess what', toUserName=itcaht_user_name)
time.sleep(3)
itchat.send(u'do you love me?',  toUserName=itcaht_user_name)
time.sleep(3)
itchat.send(u'yes',  toUserName=itcaht_user_name)
time.sleep(3)
itchat.auto_login(hotReload=True)
