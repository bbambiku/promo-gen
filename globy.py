import requests
import json
import string
import random
import os
import time
import datetime
import platform
import sys
import gratient
from urllib.parse import urlparse, parse_qs
from colorama import init, Fore
from threading import Thread
from termcolor import cprint
from pyfiglet import figlet_format


init(strip=not sys.stdout.isatty())

EMAIL = [
    'generejtomomento.bruh', 'bruhmomento.fun', 'backroomswiki.com', 'pornhub.com', 'globy.fun', 'gmail.com', 'seksownyczlowiek.fun', 'yahoo.com', 'discordsupport.space', 'velipses.fun', 'asshole.fun', 'voicerecorder.fun']
MEDAL_USER_AGENT = 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production'

ENDPOINTS = {
    'register': 'https://medal.tv/api/users',
    'login': 'https://medal.tv/api/authentication',
    'connection': 'https://medal.tv/social-api/connections',
    'nitroCode': 'https://medal.tv/api/social/discord/nitroCode',
    'connectionDelete': 'https://medal.tv/api/users/userId/connections/discord'
}


proxy = set()
with open('proxies.txt', 'r') as (f):
    proxyFile = f.readlines()
    for line in proxyFile:
        proxy.add(line.strip())


def generate_promos():

    TOKENS = open('tokens.txt').read().splitlines()
    DISCORD_TOKEN = random.choice(TOKENS)
    RANDOM_PROXY = random.choice(list(proxy))

    os.system('clear' if platform.system() == 'Linux' else 'cls')

    if ':' in DISCORD_TOKEN:
        SPLITTED = DISCORD_TOKEN.split(":")

        for infos in SPLITTED:
            if "@" not in infos:
                if '.' in infos:
                    if len(infos) > 30:
                        DISCORD_TOKEN = infos
                    if DISCORD_TOKEN == None:
                        print_message(
                            'error', 'Error finding token in tokens.txt', Fore.RED)
                else:
                    print_message(
                        'started', 'Creating Nitro Links!', Fore.GREEN)
    else:
        print_message('started', 'Creating Nitro Links!', Fore.GREEN)

    randomString = ''.join(random.choices((string.ascii_lowercase), k=8))

    data = {
        'email': randomString + "@" + random.choice(EMAIL),
        'userName': 'Globy ' + randomString,
        'password': randomString
    }

    print_message(
        'account', f'Registering Account with ({data["email"]}) in Medal.tv', Fore.GREEN)

    requests.session()

    register = requests.post(
        ENDPOINTS['register'], json=data, headers={'Accept': 'application/json',  'Content-Type': 'application/json',  'User-Agent': MEDAL_USER_AGENT,  'Medal-User-Agent': MEDAL_USER_AGENT}, proxies={'http': RANDOM_PROXY})

    if not register.ok:
        print_message(
            'error', f'Registering account on Medal.tv with (${data["email"]})', Fore.RED)
        print_message('info', 'Retrying....', Fore.WHITE)
        time.sleep(0.01)
        generate_promos()

    del data['userName']
    auth = requests.post(ENDPOINTS['login'], json=data, headers={
        'Accept': 'application/json',  'Content-Type': 'application/json',  'User-Agent': MEDAL_USER_AGENT,  'Medal-User-Agent': MEDAL_USER_AGENT}, proxies={'http': RANDOM_PROXY})

    if not auth.ok:
        print_message(
            'error', f'Authenticating account on Medal.tv with (${data["email"]})', Fore.RED)
        print_message('info', 'Retrying....', Fore.WHITE)
        time.sleep(0.01)
        generate_promos()

    authRes = json.loads(auth.text)
    token = authRes['userId'] + ',' + authRes['key']

    discordAuth = requests.post(ENDPOINTS['connection'], json={
        'provider': 'discord'
    }, headers={'Accept': 'application/json',  'Content-Type': 'application/json',  'User-Agent': MEDAL_USER_AGENT,  'Medal-User-Agent': MEDAL_USER_AGENT,  'X-Authentication': token}, proxies={'http': RANDOM_PROXY})

    if not discordAuth.ok:
        print_message('error', 'Connecting with Discord', Fore.RED)
        print_message('info', 'Retrying....', Fore.WHITE)
        time.sleep(0.01)
        generate_promos()

    doAuth = requests.post((json.loads(discordAuth.text)['loginUrl']), headers={
        'Authorization': DISCORD_TOKEN,
        'Content-Type': 'application/json'
    }, json={
        'permissions': '0', 'authorize': 'true'
    }, proxies={'http': RANDOM_PROXY})

    if not doAuth.ok:
        print_message('error', 'Authenticating with Discord', Fore.RED)
        print_message('info', 'Retrying....', Fore.WHITE)
        time.sleep(0.01)
        generate_promos()

    oauthDone = requests.get(json.loads(doAuth.text)['location'])
    oauthRes = parse_qs(urlparse(oauthDone.url).query)
    if oauthRes['status'][0] == 'error':
        print_message('error', 'Authenticating with Discord', Fore.RED)
        print_message('info', 'Retrying....', Fore.WHITE)
        time.sleep(0.01)
        generate_promos()

    nitroLink = requests.get(ENDPOINTS['nitroCode'], headers={'Accept': 'application/json',  'Content-Type': 'application/json',
                             'User-Agent': MEDAL_USER_AGENT, 'Medal-User-Agent': MEDAL_USER_AGENT,  'X-Authentication': token}, proxies={'http': RANDOM_PROXY})
    nitro = json.loads(nitroLink.text)

    try:
        print_message('nitro', nitro['url'], Fore.GREEN)
        file = open('nitro-codes.txt', 'a')
        file.write('\n' + nitro['url'])
        file.close()

    except Exception:
        print_message(
            'error', 'Couldn\'t get your nitro links, retrying', Fore.RED)

    else:
        data = {
            'email': randomString + "@" + random.choice(EMAIL),
            'userName': 'Globy ' + randomString,
            'password': randomString
        }
        generate_promos()

        deleteRes = requests.delete(ENDPOINTS['connectionDelete'].replace('userId', authRes['userId']), headers={
                                    'Accept': 'application/json',  'Content-Type': 'application/json',  'User-Agent': MEDAL_USER_AGENT,  'Medal-User-Agent': MEDAL_USER_AGENT,  'X-Authentication': token}, proxies={'http': RANDOM_PROXY})

        print_message('info', 'Deleted Connection With Discord', Fore.GREEN)


def getCurrentTime():
    return datetime.datetime.utcnow().strftime('%H:%M:%S')


def print_message(action, message, color):
    print(
        f"{Fore.BLUE}[{getCurrentTime()}] {color}[{action.upper()}] {color}{message}")


# generate_promos()


def main_screen():
    os.system('clear' if platform.system() == 'Linux' else 'cls')

    cprint(figlet_format('Globy', font='puffy'),
           'green', attrs=['bold'])
    cprint('Made by bambiku#7777 | Version: 1.0', 'white')

    print(' ')

    print(gratient.blue('1 - Discord Promotion Generator'))
    print(gratient.blue('2 - Credits'))

    option = input(f"{Fore.GREEN}Option: ")

    if option == '1':
        threads = int(input(f'{Fore.GREEN}Threads: '))

        for i in range(threads):
            t = Thread(target=generate_promos)
            t.start()

    else:
        if option == '2':
            print(f"\n{Fore.LIGHTWHITE_EX}Made by bambiku#777")
            exit(0)


main_screen()
