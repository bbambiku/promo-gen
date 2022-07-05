import requests, json, string, random, os, logging, asyncio, time, datetime
from urllib.parse import urlparse
from urllib.parse import parse_qs
from colorama import Fore, init
from termcolor import colored, cprint
from urllib import request
import discord, json, requests, os, httpx, base64, time, subprocess
init()
emails = [
 'gmail.com', 'seksownyczlowiek.fun', 'yahoo.com', 'discordsupport.space', 'velipsemail.fun', 'asshole.fun', 'voicerecorder.fun']
MEDAL_USER_AGENT = 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production'
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
    print(f"{Fore.LIGHTGREEN_EX}  \\______/ \\__| \\______/    \\_______/  \\____$$ |      ".center(width))
    print(f"{Fore.LIGHTCYAN_EX}                                   $$\\   $$ |      ".center(width))
    print(f"{Fore.LIGHTBLUE_EX}                                   \\$$$$$$  |     ".center(width))
    print(f"{Fore.LIGHTWHITE_EX}                                    \\______/       ".center(width))
    print(''")
    print(f"{Fore.LIGHTWHITE_EX}Made by bambiku#7777, version: {Fore.LIGHTBLUE_EX} 0.3".center(width))
    print('')
    os.system("cls")

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
    print(f"{Fore.LIGHTWHITE_EX}Ver 0.3".center(width))
    print('')
    print(f"{Fore.BLUE}1 Discord Promotion Gen".center(width))
    print(f"{Fore.BLUE}2 Boost Discord Server".center(width))
    print(f"{Fore.BLUE}3 Credits".center(width))
    option1 = input(f"{Fore.GREEN}\n".center(width))
    if option1 == '1':
        generate()
    else:
        if option1 == '2':
            print(f"{Fore.GREEN} Coming Soon!")
            time.sleep(5)
            exit(0)
        else:
            if option1 == '3':
                print(f"{Fore.GREEN} Made by {Fore.LIGHTWHITE_EX}bambiku#777")
                time.sleep(5)
                exit(0)
            else:
                print(f"{Fore.GREEN} Invalid Option.")
                time.sleep(5)
                exit(0)
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
