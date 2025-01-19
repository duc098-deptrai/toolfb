
from api import hustmedia,facebook
from pystyle import Colors,Colorate,Write
from pyfiglet import figlet_format
import requests,os,time,random
if 'nt' in os.name:
    os.system('cls')
else:
    os.system('clear')
do = '\033[31m'
xanhla ='\033[32m' 
xanhduong ='\033[34m'
vang ='\033[33m'
tim ='\033[35m'
xanhCyan ='\033[36m'
trang ='\033[37m'
text = 'TOOL FACEBOOK'
Write.Print(figlet_format(text),Colors.red_to_purple,interval=0.001)
Write.Print('--------------------------NHD TOOLS--------------------------\n',Colors.blue_to_black,interval=0.0001)
textapikey = Colorate.Horizontal(Colors.red_to_yellow,'nhập apikey của bạn : ')
listfile = os.listdir()
luachoninput = Colorate.Horizontal(Colors.blue_to_purple,'Do you want to use apikey again (y/n) ?: ')  
if 'apikey.txt' in listfile :
    luachon = input(luachoninput)
    if luachon == 'y':
        pass
    elif luachon == 'n':
        while True:
                    nhapApikey1 = input(textapikey)
                    try:
                        sodu = hustmedia(nhapApikey1).danngnhap('facebook')
                        writesodu = 'số dư:'+str(sodu)+'\n'
                        ten = hustmedia(nhapApikey1).get_usernameHutsmedia()
                        writeTen = 'username:'+ten+'\n'
                        Write.Print('════════════════════════════\n',Colors.blue_to_black,interval=0.0001)
                        Write.Print(writeTen,Colors.red_to_purple,interval=0.0001)
                        Write.Print(writesodu,Colors.green_to_red,interval=0.0001)
                        Write.Print('════════════════════════════\n',Colors.blue_to_black,interval=0.0001)
                        with open('apikey.txt','w') as file:
                            file.write(nhapApikey1)
                        break
                    except:
                        print(f'{do}apikey không đúng')  
                        continue

elif 'apikey.txt' not in listfile:
            while True:
                nhapApikey1 = input(textapikey)
                try:
                    sodu = hustmedia(nhapApikey1).danngnhap('facebook')
                    writesodu = 'số dư:'+str(sodu)+'\n'
                    ten = hustmedia(nhapApikey1).get_usernameHutsmedia()
                    writeTen = 'username:'+ten+'\n'
                    Write.Print('════════════════════════════\n',Colors.blue_to_black,interval=0.0001)
                    Write.Print(writeTen,Colors.red_to_purple,interval=0.0001)
                    Write.Print(writesodu,Colors.green_to_red,interval=0.0001)
                    Write.Print('════════════════════════════\n',Colors.blue_to_black,interval=0.0001)
                    with open('apikey.txt','w') as file:
                        file.write(nhapApikey1)                    
                    break
                except:
                    print(f'{do}apikey không đúng')  
                    continue
fileCookie = "listcookie.txt"
i = 1
with open('apikey.txt','r') as file:
    apikey = file.read()
if 'listcookie.txt' in listfile:
    textinput = Colorate.Horizontal(Colors.green_to_blue,'Do you want to use cookie fb again (y/n) ?: ')
    luachon = input(textinput)
    if luachon == 'n':
        with open(fileCookie, "w") as file:
            listcookie = file.write('')
        while True:
            cookie = input(f'{trang}[{i}] {tim}nhập cookie của bạn (out để thoạt nhập cookie) : ')
            if cookie == 'out':
                break
            try:
                check = facebook(cookie).get_uername_id()
                username = check[0]
                if username in hustmedia(apikey).get_list_nick('facebook'): 
                    print(vang,'═══════════════════════════════════════════════\r')
                    print(xanhCyan,username,f'{trang}</>',xanhCyan,check[1])
                    print(vang,'═══════════════════════════════════════════════')
                    i += 1
                else:
                    print(f'{do}nick facebook chưa thêm vào hệ thống')
                    i += 1
                    continue
            except IndexError:
                print(f'{do}cookie không đúng')
                i += 1
                continue
    elif luachon == 'y':
        pass
else:
        while True:
            cookie = input(f'{trang}[{i}] {tim}nhập cookie của bạn (out để thoát nhập cookie) : ')
            if cookie == 'out':
                break
            try:
                check = facebook(cookie).get_uername_id()
                username = check[0]
                if username in hustmedia(apikey).get_list_nick('facebook'):
                    print(vang,'═══════════════════════════════════════════════\r')
                    print(xanhCyan,username,f'{trang}</>',xanhCyan,check[1])
                    print(vang,'═══════════════════════════════════════════════')
                    i += 1
                else:
                    print(f'{do}nick facebook chưa thêm vào hệ thống')
                    i += 1  
                    continue 
            except IndexError:
                print(f'{do}cookie không đúng')
                i += 1
                continue
            else:
                i += 1
                nhapcookie = username+ ':' + cookie + '\n'
                with open(fileCookie, "a", encoding="utf-8") as file:
                    file.write(nhapcookie)
if  'setting.txt' in listfile:
    luachon = input(f'{do}[{xanhCyan}nhdtools{do}]{xanhla} Do you want use setting again(y/n): ')
    if luachon == 'y':
        with open('setting.txt','r') as file:
            lines = file.readlines()
        for i in lines:
            if 'maxfl' in i:
                maxfl = i.split('maxfl=')[1].split(',')[0]
            elif 'minfl' in i:
                minfl = i.split('minfl=')[1].split(',')[0]
            elif 'maxreact' in i:
                maxreact = i.split('maxreact=')[1].split(',')[0]
            elif 'minreact' in i:
                minreact = i.split('minreact=')[1].split(',')[0]
            elif 'maxcommet' in i:
                maxcommet = i.split('maxcommet=')[1].split(',')[0]
            elif 'mincommet' in i:
                mincommet = i.split('mincommet=')[1].split(',')[0]
            elif 'max_job_change_nick' in i:
                max_job_change_nick = i.split('max_job_change_nick=')[1].split(',')[0]  
    elif luachon == 'n':
        minfollow = int(input(Colorate.Horizontal(Colors.red_to_green,'min follow : ')))
        maxfollow = int(input(Colorate.Horizontal(Colors.red_to_green,'max follow : ')))
        minreact = int(input(Colorate.Horizontal(Colors.red_to_green,'min react : ')))
        maxreact = int(input(Colorate.Horizontal(Colors.red_to_green,'max react : ')))
        mincommet = int(input(Colorate.Horizontal(Colors.red_to_green,'min commet : ')))
        maxcommet = int(input(Colorate.Horizontal(Colors.red_to_green,'max commet : ')))
        max_job_change_nick1 = int(input(Colorate.Horizontal(Colors.red_to_green,'sau bao nhiêu job thì đổi nick : ')))
        file = open('setting.txt','w')
        vietminfl = file.write(f'maxfl={maxfollow}\n')
        vietmaxfl = file.write(f'minfl={minfollow}\n')
        vietminre = file.write(f'maxreact={maxreact}\n')
        vietmaxre = file.write(f'minreact={minreact}\n')
        vietmincom = file.write(f'maxcommet={maxcommet}\n')
        vietmaxcom = file.write(f'mincommet={mincommet}\n')
        write_max_job_change_nick = file.write(f'max_job_change_nick={max_job_change_nick1}\n')
        with open('setting.txt','r') as file:
            lines = file.readlines()
        for i in lines:
            if 'maxfl' in i:
                maxfl = i.split('maxfl=')[1].split(',')[0]
            elif 'minfl' in i:
                minfl = i.split('minfl=')[1].split(',')[0]
            elif 'maxreact' in i:
                maxreact = i.split('maxreact=')[1].split(',')[0]
            elif 'minreact' in i:
                minreact = i.split('minreact=')[1].split(',')[0]
            elif 'maxcommet' in i:
                maxcommet = i.split('maxcommet=')[1].split(',')[0]
            elif 'mincommet' in i:
                mincommet = i.split('mincommet=')[1].split(',')[0]   
            elif 'max_job_change_nick' in i:
                max_job_change_nick = i.split('max_job_change_nick=')[1].split(',')[0] 
else:
        minfollow = int(input(Colorate.Horizontal(Colors.red_to_green,'min follow : ')))
        maxfollow = int(input(Colorate.Horizontal(Colors.red_to_green,'max follow : ')))
        minreact = int(input(Colorate.Horizontal(Colors.red_to_green,'min react : ')))
        maxreact = int(input(Colorate.Horizontal(Colors.red_to_green,'max react : ')))
        mincommet = int(input(Colorate.Horizontal(Colors.red_to_green,'min commet : ')))
        maxcommet = int(input(Colorate.Horizontal(Colors.red_to_green,'max commet : ')))
        max_job_change_nick1 = int(input(Colorate.Horizontal(Colors.red_to_green,'sau bao nhiêu job thì đổi nick : ')))
        file = open('setting.txt','w')
        vietminfl = file.write(f'maxfl={maxfollow}\n')
        vietmaxfl = file.write(f'minfl={minfollow}\n')
        vietminre = file.write(f'maxreact={maxreact}\n')
        vietmaxre = file.write(f'minreact={minreact}\n')
        vietmincom = file.write(f'maxcommet={maxcommet}\n')
        vietmaxcom = file.write(f'mincommet={mincommet}\n')
        write_max_job_change_nick = file.write(f'max_job_change_nick={max_job_change_nick1}\n')
        with open('setting.txt','r') as file:
            lines = file.readlines()
        for i in lines:
            if 'maxfl' in i:
                maxfl = i.split('maxfl=')[1].split(',')[0]
            elif 'minfl' in i:
                minfl = i.split('minfl=')[1].split(',')[0]
            elif 'maxreact' in i:
                maxreact = i.split('maxreact=')[1].split(',')[0]
            elif 'minreact' in i:
                minreact = i.split('minreact=')[1].split(',')[0]
            elif 'maxcommet' in i:
                maxcommet = i.split('maxcommet=')[1].split(',')[0]
            elif 'mincommet' in i:
                mincommet = i.split('mincommet=')[1].split(',')[0]  
            elif 'max_job_change_nick' in i:
                max_job_change_nick = i.split('max_job_change_nick=')[1].split(',')[0]
print(f'{do}[{xanhCyan}1{do}]{xanhla} follow chéo')
print(f'{do}[{xanhCyan}2{do}]{xanhla} thả react pro') 
print(f'{do}[{xanhCyan}3{do}]{xanhla} thả react base')
print(f'{do}[{xanhCyan}4{do}]{xanhla} comment',f'{do}<đang bảo trì>{trang}')
luachon = input(Colorate.Horizontal(Colors.blue_to_cyan,'>> chọn chế độ (có thể chọn nhiều chế độ vd : 123) : '))
# get số dư 
def run_follow_cheo(cookie):
    get_coin = hustmedia(apikey).danngnhap('facebook')
    if get_coin == 'failure':
        print(f'{do}Đăng nhập thất bại')
        quit()
    else :
        coin = int(get_coin)
    print(f'{xanhCyan}xu của bạn :',coin)
    hust = hustmedia(apikey)
    getJob = hust.getJob('subcheo','facebook')['message']
    print(f'đã thấy {len(getJob)} job follow chéo')
    for job in getJob:
        
        try:
            idpost = job["idpost"]
            link = job['link']    
            delay = random.randint(int(minfl),int(maxfl))
            for s in range(delay):
                print(f'{xanhCyan}đang follow {s}', end='\r')
                time.sleep(1)
            for lan in range(3):
                try:
                    follow = facebook(cookie).follow(idpost)["data"]["actor_subscribe"]["subscribee"]["following_status"]["title"]["text"]                
                except:
                    print(f'limt follow')
                    break
                if 'Đang theo dõi' in follow:
                        break 
            for cho in range(5):
                print(f'8==> {xanhCyan}Đang nhận xu {cho} ',end='\r')
                time.sleep(1)
            for lan_bam_nhan in range(6):
                for m in range(4):
                    time.sleep(1)
                receive_coin = hust.receive_money(idpost,'subcheo','facebook')
                if 'error' in receive_coin:
                    if  lan_bam_nhan == 4:
                            print(f'{trang}[{do}fail{trang}] {do}nhận tiền lỗi                  ')
                            break
                    print(f'{xanhduong} Bấm nhận lần {lan_bam_nhan}                               ',end='\r')
                    time.sleep(0.5)
                    continue
                elif "mess" in receive_coin:
                    try:
                        coin_da_nhan = int(str(receive_coin['mess']).split('cộng')[1].split('điểm')[0])
                    except IndexError:
                        continue
                    print(f'{trang}[{xanhla}success{trang}]{tim}{idpost}{trang}|{xanhCyan}xu : {coin+coin_da_nhan }')
                    coin = coin + coin_da_nhan
                    break
                #{"mess":"Thành công, bạn được cộng 3600 điểm","sodu":3600}
        except TypeError:
            continue
   
#{"mess":"Thành công, bạn được cộng 700 điểm"}
def run_like_cheo(cookie,che_do):
    get_coin = hustmedia(apikey).danngnhap('facebook')
    if get_coin == 'failure':
        print(f'{do}Đăng nhập thất bại')
        quit()
    else :
        coin = int(get_coin)
    print(f'{xanhduong}xu của bạn :',coin)
    hust = hustmedia(apikey)
    if che_do == 'vip':
        getJob = hust.getJob('camxucvipcheo','facebook')['message']
        the_loai = 'camxucvipcheo'
        print(f'đã thấy {len(getJob)} cảm xúc chéo vip')
    elif che_do == 'basic':
        getJob = hust.getJob('camxuccheo','facebook')['message']
        the_loai = 'camxuccheo'
        print(f'đã thấy {len(getJob)} cảm xúc chéo')
    for job in getJob:
        delay_like = random.randint(int(minreact),int(maxreact))
        link = job['link']
        loaicx = job['loaicx']
        idpost = job['idpost'] # để nhận tiền 
        for delay in range(delay_like):
            text = Colorate.Horizontal(Colors.cyan_to_green,f'đang like {delay}')
            print(text,end='\r')
            time.sleep(1)
        try:
            like = facebook(cookie).like(link,loaicx)
        except:
            print(f'{do}link bị die{trang}                                     ')
        for cho in range(4):
            print(f'{xanhCyan}đang nhận tiền',end='\r')   
        receive = hust.receive_money(idpost,the_loai,'facebook')
        if 'error' in str(receive) :
            for lan_bam_nhan in range(4):
                print(f'{do}Bấm nhận lại lần thứ {lan_bam_nhan}',end='\r')
                time.sleep(1)
                for i in range(4):
                    time.sleep(1)
                receive2 = hust.receive_money(idpost,the_loai,'facebook')
                if 'error' in  str(receive2):
                    if lan_bam_nhan == 3:
                        print(link)
                        print(f'{trang}[{do}fail{trang}] {do}nhận tiền lỗi')
                    else:
                        continue
                elif  "mess" in str(receive2):
                    try:
                        coin_vua_nhan1 = int(str(receive2['mess']).split('cộng ')[1].split('điểm')[0])
                    except:
                        print('like nick này rồi                           ')
                        getJob = hust.getJob(the_loai,'facebook')['message']
                        break
                    print(f'{trang}[{xanhla}success{trang}]{tim}{link}{trang}|{xanhCyan}xu : {coin+coin_vua_nhan1 }')
                    coin = coin + coin_vua_nhan1    
                    #{"mess":"Thành công, bạn được cộng 700 điểm"}
        elif "Thành công" in str(receive):
            try:
                coin_vua_nhan2 = int(str(receive['mess']).split('cộng ')[1].split('điểm')[0])
                tet = Colorate.Horizontal(Colors.yellow_to_green,link)
                print(f'{trang}[{xanhla}success{trang}]{tet}{trang}|{xanhCyan}xu:{coin+coin_vua_nhan2 }')
                coin = coin + coin_vua_nhan2
            except:
                continue
#{"mess":"Thành công, bạn được cộng 700 điểm"}

index_cookie = 0
mission = []
for job_lam in luachon:
    if '1' in job_lam:
        mission.append('follow chéo')
    elif '2' in job_lam:  
        mission.append('thả react pro')
    elif '3'in job_lam:
        mission.append('thả react base')
    with open('listcookie.txt','r',encoding='utf-8') as file:
        arr_cookie = file.readlines()
index_cookie = 0
while True:
    cookie = str(arr_cookie[index_cookie]).split(':')[1].split('\n')[0]
    ten = str(arr_cookie[index_cookie]).split(':')[0]
    for job_lam in mission:
        if job_lam == "follow chéo":
                run_follow_cheo(cookie)
                continue
        elif job_lam == 'thả react pro':
                run_like_cheo(cookie,'vip')
                continue
        elif job_lam == 'thả react base':
                run_like_cheo(cookie,'basic')
                continue
    if cookie == (len(arr_cookie) - 1):
            index_cookie = 0
            continue
    index_cookie += 1
    cookiee = str(arr_cookie[index_cookie]).split(':')[1].split('\n')[0]
    id = facebook(cookiee).get_uername_id()[1]
    hustmedia(apikey).nickConfiguration(ten,'facebook',id)
    for din in range(4):
        print('đang cấu hình nick')
        time.sleep(1)




# [1] follow chéo
# [2] thả react pro
# [3] thả react base