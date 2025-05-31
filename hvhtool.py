import os, sys
from time import strftime
from datetime import datetime, timedelta, date
import requests
from pystyle import *
import pyfiglet

# Định nghĩa màu sắc (7 màu cầu vồng)
RED = "\033[1;31m"     # Đỏ
ORANGE = "\033[1;33m"  # Cam (dùng vàng làm cam)
YELLOW = "\033[1;93m"  # Vàng sáng
GREEN = "\033[1;32m"   # Lục
CYAN = "\033[1;36m"    # Lam (cyan)
INDIGO = "\033[1;34m"  # Chàm (dùng xanh dương đậm)
PURPLE = "\033[1;35m"  # Tím
WHITE = "\033[1;37m"
END = '\033[0m'

# Chuỗi màu cầu vồng
RAINBOW_COLORS = [RED, ORANGE, YELLOW, GREEN, CYAN, INDIGO, PURPLE]

# Ký hiệu đẹp
thanh_xau = WHITE + RED + "[" + YELLOW + "⟨⟩" + RED + "] " + WHITE + "➩ "
thanh_dep = WHITE + RED + "[" + GREEN + "✓" + RED + "] " + WHITE + "➩ "

# Tạo banner mới với 7 màu cầu vồng
def create_rainbow_banner():
    text = "HvH Tool"
    font = "big"  # Font to, thẳng, dễ nhìn
    banner = pyfiglet.figlet_format(text, font=font)
    banner_lines = banner.split('\n')
    colored_banner = ""
    
    # Áp dụng màu cầu vồng cho từng dòng
    for i, line in enumerate(banner_lines):
        if line.strip():  # Chỉ tô màu các dòng không rỗng
            color = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
            colored_banner += f"{color}{line}{END}\n"
        else:
            colored_banner += "\n"
    
    # Thêm thông tin tác giả bên dưới
    colored_banner += f"{WHITE}= = = = = = = = = = = = = = = = = = = = = = = = = = = = = {END}\n"
    colored_banner += f"{CYAN}┌────────────────────── Bé Tập Code TOOL ──────────────────────┐{END}\n"
    colored_banner += f"{CYAN}║   {WHITE}TOOL BY{CYAN}            :  Bé Tập Code                          {CYAN}║{END}\n"
    colored_banner += f"{CYAN}║   {WHITE}YOUTUBER{CYAN}           :  HVHTOOL                         {CYAN}     ║{END}\n"
    colored_banner += f"{CYAN}║   {WHITE}YOTUBE_LINK{CYAN}        :  https://www.youtube.com/@HVHTOOL{CYAN}     ║{END}\n"
    colored_banner += f"{CYAN}└──────────────────────────────────────────────────────────────┘{END}\n"
    colored_banner += f"{WHITE}= = = = = = = = = = = = = = = = = = = = = = = = = = = = = {END}\n"
    
    return colored_banner

banner = create_rainbow_banner()

os.system('cls')
print(banner)

# Setup thư viện
setup = input(f'{YELLOW}[Nhập 1 để Setup tất cả thư viện | nếu set setup 1 tool vẫn lỗi thư viện thì chọn 2 | 2 lỗi thì cài lại python bản mới nhất ==> ai setup rồi thì ENTER để vào tool]:{END}')
if setup == '1':
    os.system("pip install requests")
    os.system("pip install pyfiglet")
    os.system("pip3 install requests selenium webdriver-manager")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system("pip install tabulate")
    os.system("pip install bs4")
    os.system("pip install pystyle")
    os.system("pip install curl_cffi")
    os.system("pip install random2")
    os.system("pip install selenium")
    os.system("pip install DateTime")
    os.system("pip install threaded")
    os.system("pip install thread")
    os.system("pip install urllib3")
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()
elif setup == '2':
    os.system("pip3 install requests")
    os.system("pip3 install pyfiglet")
    os.system("pip3 pip3 install requests selenium webdriver-manager")
    os.system("pip3 install art")
    os.system("pip3 install colorama")
    os.system("pip3 install tabulate")
    os.system("pip3 install bs4")
    os.system("pip3 install pystyle")
    os.system("pip3 install curl_cffi")
    os.system("pip3 install random2")
    os.system("pip3 install selenium")
    os.system("pip3 install DateTime")
    os.system("pip3 install threaded")
    os.system("pip3 install thread")
    os.system("pip3 install urllib3")
    os.system("pip3 install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()
else:
    pass

# Kiểm tra import
try:
    from time import strftime
    from datetime import datetime, timedelta, date
    import re, requests, os, sys
    from time import sleep
except ImportError:
    os.system("pip install requests")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system("pip install tabulate")
    os.system("pip install bs4")
    os.system("pip install pystyle")
    os.system("pip install curl_cffi")
    os.system("pip install random2")
    os.system("pip install selenium")

# Thời gian hiện tại
time = datetime.now().strftime("%H:%M:%S")
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")

# Hiển thị menu
os.system('cls')
print(banner)
print(f'{GREEN}Chạy tiến trình{END}')

print(f"{RED}────────────────────────────────────────────────────────────{END}")
print(f"{WHITE}╔═════════════════════╗{END}")
print(f"{WHITE}║  {ORANGE}GOLIKE PC|IOS  {WHITE}   ║{END}")
print(f"{WHITE}╚═════════════════════╝{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 1 {RED}] {GREEN}Tool GOLIKE AutoLinkedin{RED}[{YELLOW}PC|CODESPACES{RED}]{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 2 {RED}] {GREEN}Tool GOLIKE INSTAGRAM {RED}[{YELLOW}PC|CODESPACES{RED}]{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 3 {RED}] {GREEN}Tool GOLIKE INSTAGRAM RANDOM User_Agent {RED}[{YELLOW}PC|CODESPACES{RED}]{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 4 {RED}] {GREEN}Tool GOLIKE X {RED}[{YELLOW}PC|CODESPACES{RED}]{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 17 {RED}] {GREEN}Tool GOLIKE Thead {RED}[{YELLOW}PC|CODESPACES{RED}]{END}")
print(f"{RED}────────────────────────────────────────────────────────────{END}")
print(f"{WHITE}╔═══════════════════════╗{END}")
print(f"{WHITE}║  {ORANGE}GOLIKE MOBILE+VPN  {WHITE} ║{END}")
print(f"{WHITE}╚═══════════════════════╝{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 5 {RED}] {GREEN}Tool GOLIKE AutoLinkedin {RED}[{YELLOW}termux{RED}] {RED}(bảo trì) {END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 6 {RED}] {GREEN}Tool GOLIKE INSTAGRAM {RED}[{YELLOW}termux{RED}] {RED}(bảo trì){END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 7 {RED}] {GREEN}Tool GOLIKE INSTAGRAM RANDOM User_Agent {RED}[{YELLOW}termux{RED}] {RED}(bảo trì){END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 8 {RED}] {GREEN}Tool GOLIKE TIKTOK {RED}[{YELLOW}termux{RED}] {RED}(bảo trì){END}")
print(f"{RED}────────────────────────────────────────────────────────────{END}")
print(f"{WHITE}╔═══════════════════════╗{END}")
print(f"{WHITE}║  {ORANGE}TOOL TTC  {WHITE}         ║{END}")
print(f"{WHITE}╚═══════════════════════╝{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 9 {RED}] {GREEN}Tool TTC INSTAGRAM {RED}[{YELLOW}PC|CODESPACES|termux{RED}]{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 10 {RED}] {GREEN}Tool TTC INSTAGRAM RANDOM User_Agent {RED}[{YELLOW}PC|CODESPACES|termux{RED}]{END}")
print(f"{RED}────────────────────────────────────────────────────────────{END}")
print(f"{WHITE}╔═════════════════════╗{END}")
print(f"{WHITE}║  {ORANGE}Tool FACEBOOK      {WHITE}║{END}")
print(f"{WHITE}╚═════════════════════╝{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 11{RED}] {GREEN}Tool BUFF LIKE PAGE{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 12{RED}] {GREEN}Tool Share Ảo Cookie{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 13{RED}] {GREEN}Tool BUFF LIKE COMMENT{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 14{RED}] {GREEN}Tool BUFF FOLLOW PAGE {END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 15{RED}] {GREEN}Tool GET THÔNG TIN BÀI VIẾT {END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 16 {RED}] {GREEN}Tool Tool REGPAGE PRO5 {END}")
print(f"{RED}────────────────────────────────────────────────────────────{END}")
print(f"{WHITE}╔═════════════════════╗{END}")
print(f"{WHITE}║{ORANGE}Tool REG TIKTOK CHROME{WHITE}║{END}")
print(f"{WHITE}╚═════════════════════╝{END}")
print(f"{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {RED}[{YELLOW}✨ 18 {RED}] {GREEN}Tool Tool REG TIKTOK CHROME (TỰ THÊM CHROME DRIVER){END}")
print(f"{RED}────────────────────────────────────────────────────────────{END}")
# Nhập lựa chọn
chon = int(input(f'{RED}[{WHITE}Bé Tập Code{RED}] {WHITE}=> {GREEN}Nhập Số {WHITE}: {YELLOW}'))

# Xử lý lựa chọn
if chon == 1:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/AutoLinkedin/AutoLinkedin_PC.py').text) 
elif chon == 2:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/IG/IG_PC/AutoIG1_PC.py').text)
elif chon == 3:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/IG/IG_PC/AutoIG1_PC_User_Agent.py').text) 
elif chon == 4:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/X/AUTO-X_PC.py').text) 
elif chon == 5: 
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/AutoLinkedin/AutoLinkedin_mobile.py').text) 
elif chon == 6:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/IG/IG_MOBILE/AutoIG1_mobile.py').text)
elif chon == 7:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/IG/IG_MOBILE/AutoIG1_mobile_user-agent.py').text)
elif chon == 8:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/TIKTOK/TIKTOK.py').text)
elif chon == 9:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TTC/TTC%20INSTAGRAM/TTCIG.py').text)
elif chon == 10:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TTC/TTC%20INSTAGRAM/TTCIG_user-agent.py').text)
elif chon == 11:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/LIKE%20PAGE%20PRO5%20VIP.py').text)
elif chon == 12:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/Tool%20Share%20%E1%BA%A2o%20Cookie%20%5BPRO5%5D.py').text)
elif chon == 13:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/LIKE_PAGE_BINHLUAN.py').text)
elif chon == 14:
    exec(requests.get('https://raw.githubusercontent.com/shopaccrandom/TOOLGOPHVHsdfgbvusjygfuierfhsfvbskugahzusebtfgaiusetbgvasitdcziubv5465argedrsardhtdudtyregzsergsrfyu/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/%5B21%5D%20Tool%20Reg%20Page%20Pro5.py').text)
elif chon == 15:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/GET_NOIDUNGFB.py').text)
elif chon == 16:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL%20TI%E1%BB%86N%20%C3%8DCH%20FACEBOOK/%5B21%5D%20Tool%20Reg%20Page%20Pro5.py').text)
elif chon == 17:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/TOOL-GOLIKE/THRADS/AutoTheads.py').text)
elif chon == 18:
    exec(requests.get('https://raw.githubusercontent.com/HOANGHUY785/HVHTOOL/refs/heads/main/TOOL_G%E1%BB%98P_HVHTOOOL/regtik/logintik.py').text)
elif chon == 0:
    exit()
else:
    exit()
