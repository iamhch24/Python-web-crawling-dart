import requests
import datetime
import telepot

AUTH_KEY = 'a1085e73b6f15fed673b1a8c363789120bef84f0'

#30일 전 : 오늘을 기점으로 30일을 뺀 날짜 today()-30 => timedelta
today = datetime.date.today()
bng_de = today - datetime.timedelta(days=30)

args = {
    'bgn_de': bng_de.strftime('%Y%m%d'),
    'end_de': today.strftime('%Y%m%d'),
    'page_no': '5',
    'sort':'date'
}

args_str = ''
for k, v in args.items():
    args_str += '&%s=%s' %(k,v)

url = 'https://opendart.fss.or.kr/api/list.json?crtfc_key=%s%s' %(AUTH_KEY, args_str)
print(url+"\n")
# quit()

bot = telepot.Bot('1474600206:AAHdSqIOulOWNgP5584x6DIknVOmeRz69bU')

res = requests.get(url)
data = res.json()
# print(data)

if data['status'] != '000':
    bot.sendMessage('1272860274','공시정보 조회 실패'+data['message'])
else:
    msg = ''
    data_list = data['list']

    for d in data_list:
        for k, v in d.items():
            msg += '%s, ' % v
        msg += '\n'            
#텔레그램 메신저로 알림을 받는다        
    bot.sendMessage('1272860274','공시정보 조회 성공\n'+msg)

