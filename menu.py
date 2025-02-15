
xanhduong ='\033[34m'
from datetime import datetime
import random
from time import sleep
try:
    import requests,json,numpy
    from pystyle import Colors,Write
    import os,pystyle
    import base64
except:
    import os
    os.system('python -m pip install requests')
    os.system('python -m pip install pystyle')
    os.system('python -m pip install pyfiglet')
    os.system('python -m pip install json')
    os.system('python -m pip install numpy')
    import requests
    from pystyle import Colors,Write
    import base64
if 'nt' in os.name:
    os.system('cls')
else:
    os.system('clear')
do = '\033[31m'
xanhla ='\033[32m' 
vang ='\033[33m'
tim ='\033[35m'
xanhCyan ='\033[36m'
trang ='\033[37m'

a = 'NHDUC'
link = 'yt:https://www.youtube.com/@M%C3%A8ochill-s8o'
Write.Print('    _   ____  ______  __  ________\n',Colors.purple_to_blue,interval=0.0001)
Write.Print('   / | / / / / / __ \/ / / / ____/',Colors.purple_to_blue,interval=0.0001)
Write.Print('   ╔═════════════════════════════════════════════╗\n',Colors.yellow,interval=0.0001)
Write.Print('  /  |/ / /_/ / / / / / / / /',Colors.purple_to_blue,interval=0.0001)
Write.Print('        ║',Colors.yellow,interval=0.001)
Write.Print(link,Colors.blue_to_red,interval=0.001)
Write.Print('║\n',Colors.yellow,interval=0.001)
Write.Print(' / /|  / __  / /_/ / /_/ / /___',Colors.purple_to_blue,interval=0.0001)
Write.Print('      ║',Colors.yellow,interval=0.001)
Write.Print('     made by : ',Colors.red_to_purple,interval=0.001)
Write.Print('Nguyễn Huỳnh Đức              ',Colors.white_to_blue,interval=0.001)
Write.Print('║\n',Colors.yellow,interval=0.001)
Write.Print('/_/ |_/_/ /_/_____/\____/\____/',Colors.purple_to_blue,interval=0.0001)
Write.Print('      ╚═════════════════════════════════════════════╝\n',Colors.yellow,interval=0.001)
Write.Print('TOOL HUST MEDIA    \n',Colors.pink,interval=0.001)
print(f'{do}[{trang}×_×{do}]{xanhduong}==>{xanhla} nhập{tim} [{xanhCyan}1{tim}] {xanhla}auto facebook')
print(f'{do}[{trang}×_×{do}]{xanhduong}==>{xanhla} nhập{tim} [{xanhCyan}2{tim}] {xanhla}auto instagram{trang}')
print(f'{trang}---------------------------------')
luachon = input(f'{xanhla}[{xanhCyan}nhdtool{xanhla}]{xanhla}==>{tim} nhập lựa chọn của bạn : ')
if luachon == '1':
    import runfb
elif luachon == '2':
    from run import hustmedia_instagram as run
    run.run()

else:
    print('sai dữ liệu vui lòng vào lại tool')
