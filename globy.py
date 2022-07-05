import requests, json, string, random, os, logging, asyncio, time, datetime
from urllib.parse import urlparse
from urllib.parse import parse_qs
from colorama import Fore, init
from termcolor import colored, cprint
from urllib import request
import discord, json, requests, os, httpx, base64, time, subprocess
from threading import Thread
from hcapbypass import bypass
import gratient
from fresh_useragent import UserAgent

emails = [
 'gmail.com', 'seksownyczlowiek.fun', 'yahoo.com', 'discordsupport.space', 'velipsemail.fun', 'asshole.fun', 'voicerecorder.fun']
#MEDAL_USER_AGENT = 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36 Environment/production'
MEDAL_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Safari/537.36'
randomStr = ''.join(random.choices((string.ascii_lowercase), k=8))
email = randomStr + 'seks.fun'
userName = 'Globy ' + randomStr
password = randomStr
tokens = open('tokens.txt').read().splitlines()
DISCORD_TOKEN = random.choice(tokens)
os.system('title Globy Gen')
width = os.get_terminal_size().columns
now = datetime.datetime.utcnow()
printSpaces = ''
s = requests.session()
proxy = set()
with open('proxies.txt', 'r') as (f):
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy.add(line1.strip())

proxies = {'http': 'http://' + random.choice(list(proxy))}
fresh_useragent = UserAgent() 
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def generate():
    tokens = open('tokens.txt').read().splitlines()
    DISCORD_TOKEN = random.choice(tokens)
    if ':' in DISCORD_TOKEN:
        token_chosen = None
        tokensplit = DISCORD_TOKEN.split(':')
        for thing in tokensplit:
            if '@' not in thing:
                if '.' in thing:
                    if len(thing) > 30:
                        DISCORD_TOKEN = thing
                    if DISCORD_TOKEN == None:
                        print_error('Error finding token', Fore.RED)
                else:
                    print_info('Creating Nitro Link...')

    else:
        print_info('Creating Nitro Link...')
    emails = [
     'generejtomomento.bruh', 'bruhmomento.fun', 'backroomswiki.com', 'pornhub.com', 'globy.fun', 'gmail.com', 'seksownyczlowiek.fun', 'yahoo.com', 'discordsupport.space', 'velipses.fun', 'asshole.fun', 'voicerecorder.fun']
    MEDAL_USER_AGENT = 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production'
    randomStr = ''.join(random.choices((string.ascii_lowercase), k=8))
    email = randomStr + '@' + random.choice(emails)
    userName = 'Globy ' + randomStr
    password = randomStr
    print_info(f"Creating account... ({email})")
    register = requests.post('https://medal.tv/api/users', json={'email':email,  'userName':userName,  'password':password}, headers={'Accept':'application/json',  'Content-Type':'application/json',  'User-Agent':MEDAL_USER_AGENT,  'Medal-User-Agent':MEDAL_USER_AGENT}, proxies=proxies)
    if not register.ok:
        print_error(register.text)
        print_info('Retrying...')
        time.sleep(0.01)
        generate()
    authenticate = requests.post('https://medal.tv/api/authentication', json={'email':email,
     'password':password},
      headers={'Accept':'application/json',
     'Content-Type':'application/json',  'User-Agent':MEDAL_USER_AGENT,  'Medal-User-Agent':MEDAL_USER_AGENT},
      proxies=proxies)
    if not authenticate.ok:
        print_error(authenticate.text)
        print_info('Retrying...')
        time.sleep(0.01)
        generate()
    authResp = json.loads(authenticate.text)
    token = authResp['userId'] + ',' + authResp['key']
    discordOauth = requests.post('https://medal.tv/social-api/connections', json={'provider': 'discord'}, headers={'Accept':'application/json',  'Content-Type':'application/json',  'User-Agent':MEDAL_USER_AGENT,  'Medal-User-Agent':MEDAL_USER_AGENT,  'X-Authentication':token}, proxies=proxies)
    if not discordOauth.ok:
        print_error(discordOauth.text)
        print_info('Retrying...')
        time.sleep(0.01)
        generate()
    doOauth = requests.post((json.loads(discordOauth.text)['loginUrl']), headers={'Authorization':DISCORD_TOKEN,  'Content-Type':'application/json'}, json={'permissions':'0',  'authorize':'true'}, proxies=proxies)
    if not doOauth.ok:
        print_error(doOauth.text)
        print_info('Retrying...')
        time.sleep(0.01)
        generate()
    medalLink = json.loads(doOauth.text)['location']
    oauthDone = requests.get(medalLink)
    oauthResponse = parse_qs(urlparse(oauthDone.url).query)
    if oauthResponse['status'][0] == 'error':
        print_error(oauthResponse['message'][0])
        print_info('Retrying...')
        time.sleep(0.01)
        generate()
    nitroLink = requests.get('https://medal.tv/api/social/discord/nitroCode', headers={'Accept':'application/json',  'Content-Type':'application/json',  'User-Agent':MEDAL_USER_AGENT,  'Medal-User-Agent':MEDAL_USER_AGENT,  'X-Authentication':token}, proxies=proxies)
    nitro = json.loads(nitroLink.text)
    print_detect(nitro)
    try:
        print_important(nitro['url'])
        codes = open('nitro-codes.txt', 'a')
        codes.write('\n' + nitro['url'])
        codes.close()
    except Exception:
        print_error('Cant get your nitro link, retrying')
    else:
        print('')
        print_info('Waiting for Globy...')
        print('')
        randomStr = ''.join(random.choices((string.ascii_lowercase), k=8))
        email = randomStr + '@' + random.choice(emails)
        userName = 'Globy ' + randomStr
        password = randomStr + '!1'
        generate()
        deleteRes = requests.delete(('https://medal.tv/api/users/' + authResp['userId'] + '/connections/discord'), headers={'Accept':'application/json',  'Content-Type':'application/json',  'User-Agent':MEDAL_USER_AGENT,  'Medal-User-Agent':MEDAL_USER_AGENT,  'X-Authentication':token}, proxies=proxies)
        if not deleteRes.ok:
            print_error(deleteRes.text)
            print_info('Retrying...')
            time.sleep(0.01)
            generate()


def getCurrentTime():
    return datetime.datetime.utcnow().strftime('%H:%M:%S')
def print_important(message):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.RED}[IMPORTANT] {Fore.GREEN}{message}".center(width))
def print_info(message):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[INFORMATION] {Fore.GREEN}{message}".center(width))
def print_cmd(command):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[COMMAND] {Fore.GREEN}{command}".center(width))
def print_sharecmd(author, command):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[SHARE COMMAND] {Fore.GREEN}({author}) {command}".center(width))
def print_error(error):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.RED}[ERROR] {Fore.GREEN}{error}".center(width))
def print_detect(message):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[DEBUG] {Fore.RED}{message}".center(width))
def print_sniper(message):
    print(f"{printSpaces}{Fore.BLUE}[{getCurrentTime()}] {Fore.WHITE}[SNIPER] {Fore.GREEN}{message}".center(width))
def print_sniper_info(firstmessage, secondmessage):
    spaces = ''

def genandjoin(link):
    s = requests.session()
    proxy = set()
    with open('proxies.txt', 'r') as (f):
        file_lines1 = f.readlines()
        for line1 in file_lines1:
            proxy.add(line1.strip())

    proxies = {
        "all://": "http://" + random.choice(list(proxy)),
    }
    username = "Globy | " + random_char(10)
    email =  random_char(9) + "@" + random_char(4) + ".com"
    password = random_char(11)

    header1 = {
        "Host": "discord.com",
        "Connection": "keep-alive",
        "User-Agent": fresh_useragent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-us,en;q=0.9",
    }

    getcookie = httpx.get("https://discord.com/register").headers['set-cookie']
    sep = getcookie.split(";")
    sx = sep[0]
    sx2 = sx.split("=")
    dfc = sx2[1]
    split = sep[6]
    split2 = split.split(",")
    split3 = split2[1]
    split4 = split3.split("=")
    sdc = split4[1]

    header2 = {
        "Host": "discord.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        "X-Context-Properties": "eyJsb2NhdGlvbiI6IlJlZ2lzdGVyIn0=",
        "Accept-Language": "en-US",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": fresh_useragent,
        "Authorization": "undefined",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://discord.com/register",
        "Accept-Encoding": "gzip, deflate, br"
    }

    fingerprintres = httpx.get("https://discord.com/api/v9/experiments", timeout=10)

    while True:
        if fingerprintres.text != "":
            fingerprint = fingerprintres.json()['fingerprint']
            break
        else:
            return True

    sitekey = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"

    while True:
        captchakey = bypass(sitekey, "discord.com", proxy="")
        if captchakey == "False":
            continue
        else:
            break

    print_info("Captcha Solved (prob.)")

    header3 = {

        "Host": "discord.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        "X-Fingerprint": fingerprint,
        "Accept-Language": "en-US",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": fresh_useragent,
        "Content-Type": "application/json",
        "Authorization": "undefined",
        "Accept": "*/*",
        "Origin": "https://discord.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://discord.com/register",
        "X-Debug-Options": "bugReporterEnabled",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": f"__dcfduid={dfc}; __sdcfduid={sdc}"

    }

    payload = {"fingerprint": fingerprint,
                "email": email,
                "username": username,
                "password": password,
                "invite": link,
                "consent": "true",
                "date_of_birth": "1991-04-06",
                "gift_code_sku_id": "",
                "captcha_key": captchakey,
                }

    req = httpx.post("https://discord.com/api/v9/auth/register", headers=header3, proxies=proxies, json=payload, timeout=10)

    token = req.json()['token']

    print_info("Registered: " + token)

    def join(token, link):
        header = {"authorization": token}
        r = requests.post("https://discord.com/api/v8/invites/{}".format(link), proxies=proxies, headers=header1)

    codes = open('generated_tokens.txt', 'a')
    codes.write('\n' + token)
    codes.close()
    print_important("Saved token to generated_tokens.txt. " + "(" + token + ")")

def main_screen():
    os.system('cls')
    print('')
    print(f"{Fore.BLUE} $$$$$$\\  $$\\           $$\\                     ".center(width))
    print(f"{Fore.CYAN}$$  __$$\\ $$ |          $$ |                     ".center(width))
    print(f"{Fore.GREEN}$$ /  \\__|$$ | $$$$$$\\  $$$$$$$\\  $$\\   $$\\      ".center(width))
    print(f"{Fore.LIGHTBLUE_EX}$$ |$$$$\\ $$ |$$  __$$\\ $$  __$$\\ $$ |  $$ |     ".center(width))
    print(f"{Fore.LIGHTCYAN_EX}$$ |\\_$$ |$$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |     ".center(width))
    print(f"{Fore.LIGHTGREEN_EX}$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |     ".center(width))
    print(f"{Fore.LIGHTWHITE_EX} \\$$$$$$  |$$ |\\$$$$$$  |$$$$$$$  |\\$$$$$$$ |      ".center(width))
    print(f"{Fore.LIGHTGREEN_EX}  \\______/ \\__| \\______/ \\_______/  \\____$$ |      ".center(width))
    print(f"{Fore.LIGHTCYAN_EX}                                   $$\\   $$ |      ".center(width))
    print(f"{Fore.LIGHTBLUE_EX}                                   \\$$$$$$  |     ".center(width))
    print(f"{Fore.LIGHTWHITE_EX}                                    \\______/       ".center(width))
    print('')
    print(f"{Fore.LIGHTWHITE_EX}Ver 0.4".center(width))
    print('')

target_url = 'https://licensekeys.essazwamiwidzowie.repl.co/keys.txt'
for line in request.urlopen(target_url):
    something = line.decode('utf-8')
else:
    os.system('cls')
    print('')
    print(f"{Fore.BLUE} $$$$$$\\  $$\\           $$\\                     ".center(width))
    print(f"{Fore.CYAN}$$  __$$\\ $$ |          $$ |                     ".center(width))
    print(f"{Fore.GREEN}$$ /  \\__|$$ | $$$$$$\\  $$$$$$$\\  $$\\   $$\\      ".center(width))
    print(f"{Fore.LIGHTBLUE_EX}$$ |$$$$\\ $$ |$$  __$$\\ $$  __$$\\ $$ |  $$ |     ".center(width))
    print(f"{Fore.LIGHTCYAN_EX}$$ |\\_$$ |$$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |     ".center(width))
    print(f"{Fore.LIGHTGREEN_EX}$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |     ".center(width))
    print(f"{Fore.LIGHTWHITE_EX} \\$$$$$$  |$$ |\\$$$$$$  |$$$$$$$  |\\$$$$$$$ |      ".center(width))
    print(f"{Fore.LIGHTGREEN_EX}  \\______/ \\__| \\______/ \\_______/  \\____$$ |      ".center(width))
    print(f"{Fore.LIGHTCYAN_EX}                                   $$\\   $$ |      ".center(width))
    print(f"{Fore.LIGHTBLUE_EX}                                   \\$$$$$$  |     ".center(width))
    print(f"{Fore.LIGHTWHITE_EX}                                    \\______/       ".center(width))
    print('')
    print(f"{Fore.LIGHTWHITE_EX}Made by bambiku#7777, version: {Fore.LIGHTBLUE_EX}0.4".center(width))
    print('')
    print(gratient.blue("Loading...".center(width)))
    print('')
    time.sleep(3)
    os.system("cls")

    main_screen()
    print(gratient.blue("1 Discord Promotion Gen".center(width)))
    print(gratient.blue("2 Member Botter (tukan gen)".center(width)))
    print(gratient.blue("3 Credits".center(width)))
    option1 = input(f"{Fore.GREEN}\n".center(width))
    if option1 == '1':
        main_screen()
        threads = int(input(gratient.blue("Threads: ".center(width))))
        main_screen()
        for i in range(threads):
            t = Thread(target=generate)
            t.start()
    else:
        if option1 == '2':
            main_screen()
            print(gratient.blue("Threads: \n".center(width)))
            threads = int(input(f"{Fore.GREEN}\n".center(width)))
            main_screen()
            print(gratient.blue("Server Link: \n".center(width)))
            link2 = input(f"{Fore.GREEN}\n".center(width))
            main_screen()
            for i in range(threads):
                t = Thread(target=genandjoin, kwargs={'link': link2})
                t.start()
        else:
            if option1 == '3':
                print(f"{Fore.GREEN} Made by {Fore.LIGHTWHITE_EX}bambiku#777")
                time.sleep(5)
                exit(0)
            else:
                print(gratient.blue("Invalid Option.".center(width)))
                time.sleep(5)
                exit(0)
