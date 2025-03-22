import requests
from datetime import datetime
import base64,os,time

now = datetime.now()
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
xanhla ='\033[32m'
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
def tao_link_key(key,loai) :
    link = f'http://nguyenhuynhduccti.free.nf/?key={key}'
    linkyeumnoney = f'https://yeumoney.com/QL_api.php?token=8e6274c1d9190de74866757c32193fc00fc78f254878a80c3fe7e62fcbbe9d88&format=json&url={link}' 
    link4m = f'https://link4m.co/api-shorten/v2?api=67af5eeb2c9032706c7fc52d&url={link}'
    link_can = 0
    if loai == 1:
        link_can = link4m
    elif loai == 2 :
        link_can = linkyeumnoney
    data = requests.post(link_can).json()
    print(f'{do}lỗi get link {trang}') if data['status'] != "success" else print(f"{vang} Vượt link {trang}[ {luc}{data['shortenedUrl']}{trang} ] {vang}để lấy key")
def taoKey():
    now = datetime.now()
    year = int(now.year)
    month = int(now.month)
    day = int(now.day)
    acscii_day = day + 64 if day <= 27 else day + 69
    ki_tu = chr(acscii_day)
    acscii_month = month + 64 
    ki_tu2 = chr(acscii_month) 
    text_key =ki_tu +str((year + month + day)*2009)+ki_tu2+ "nguyenduc" 
    encoded_bytes = base64.b64encode(text_key.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    key1 = encoded_str
    key = key1[:-6]
    return key

def r():
    List_file = os.listdir()
    key_hom_nay = taoKey()
    def check():
        key_today = taoKey()
        lua_chon = 1 
        tao_link_key(key_today,lua_chon)
        nhap_key = input(f"{xanhla}[{xduong}nhdtool{xanhla}]{luc} Nhập key hoặc link đã vượt (nhập doi để đổi link) :{hong} ")
        while True:
            if nhap_key == "doi":
                lua_chon = 1
                tao_link_key(key_today,lua_chon)
                nhap_key = input(f"{xanhla}[{xduong}nhdtool{xanhla}]{luc} Nhập key hoặc link đã vượt (nhập doi để đổi link) : {hong} ")
                if lua_chon == 2 : lua_chon = 1
                if nhap_key == "doi":
                    lua_chon += 1
            else:
                # get key 
                if "key=" in nhap_key:
                    key = nhap_key.split('key=')[0]
                else:
                    key = nhap_key
                # check 
                if key == key_hom_nay:
                    with open("keynhdtool.txt","w") as file:
                        file.write(key)
                    print(f"{xnhac} Key đúng vào tool !!!",end="\r")
                    time.sleep(3)
                    break
                else:
                    print(f"{do}key sai vui lòng nhập lại key")
                    nhap_key = input(f"{xanhla}[{xduong}nhdtool{xanhla}]{luc} Nhập key hoặc link đã vượt (nhập doi để đổi link) :{hong} ")
                    continue
    if 'keynhdtool.txt' not in List_file:
        check()
    else:
        with open("keynhdtool.txt",'r') as dkey:
            key = dkey.read()
            if key == key_hom_nay:
                print(f"{xnhac}key đúng vào tool !!!",end="\r")
                time.sleep(3)
                pass
            else:
                check()

r()