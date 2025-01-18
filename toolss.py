import requests
import os , time,sys
listfile = os.listdir()

url = "https://raw.githubusercontent.com/duc098-deptrai/toolfb/refs/heads/main/apiencode.py"  # Đường dẫn đến file
output_file = "api.py"
response = requests.get(url, stream=True)  # Dùng stream để tải file lớn
with open(output_file, "wb") as file:
    for chunk in response.iter_content(chunk_size=8192):  # Tải từng phần nhỏ
        file.write(chunk)
url = "https://raw.githubusercontent.com/duc098-deptrai/toolfb/refs/heads/main/runfb_encode.py"  # Đường dẫn đến file
output_file = "runfb.py"

response = requests.get(url, stream=True)  # Dùng stream để tải file lớn
with open(output_file, "wb") as file:
    for chunk in response.iter_content(chunk_size=8192):  # Tải từng phần nhỏ
        file.write(chunk)

def loading_bar():
    total = 100  # Tổng số phần trăm của thanh tiến trình
    bar_length = 50  # Độ dài của thanh tiến trình

    for i in range(total + 1):
        percent = (i / total) * 100
        bar = '█' * int((i / total) * bar_length)  # Tạo phần đã đầy
        spaces = ' ' * (bar_length - len(bar))  # Tạo phần còn lại
        sys.stdout.write(f'\rLoading... [{bar}{spaces}] {percent:.2f}%')  # In thanh tiến trình
        sys.stdout.flush()
        time.sleep(0.1)  # Đợi một chút để thanh tiến trình đầy từ từ
        sys.stdout.write('\nDone!')
    print('đang tải tài nguyên')
    loading_bar()
menu = requests.get('https://raw.githubusercontent.com/duc098-deptrai/toolfb/refs/heads/main/menu.py').text
exec(menu)