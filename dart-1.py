import requests

AUTH_KEY = 'a1085e73b6f15fed673b1a8c363789120bef84f0'

args = {
    'bgn_de':'20201001',
    'end_de':'20201101',
    'copr_cls':'K',
    'sort':'date'
}

args_str = ''
for k, v in args.items():
    args_str += '&%s=%s' %(k,v)

url = 'https://opendart.fss.or.kr/api/list.json?crtfc_key=%s%s' %(AUTH_KEY, args_str)
print(url+"\n")
res = requests.get(url)
data = res.json()
# print(data)

if data['status'] != '000':
    print(datap['message'])
else:
    data_list = data['list']
    for d in data_list:
        print(d['corp_name'])
        


