import requests,time,random,os
from colorama import init,Fore
init()
width = os.get_terminal_size().columns

def check():
    proxies = open("proxy.txt", "r", encoding="utf8").read().strip( ).splitlines()
    promo = open('promo.txt','r')
    for ligne in promo:
        proxy = [{"https": "http://"+proxy} for proxy in proxies]
        ligne = ligne.strip().split('/')
        code = ligne[3]
        r = requests.get(f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true',proxies=random.choice(proxy),timeout=10)
        if r.status_code == 200:
            print(Fore.WHITE + '[+]',Fore.GREEN + f'https://promos.discord.gg/{code}')
            with open('code.txt','a',encoding='utf-8') as hit:
                hit.writelines(f'https://promos.discord.gg/{code}\n')
        elif r.status_code == 429:
            print(Fore.WHITE + '[+]',Fore.RED + f'Rate limited.')
            print(Fore.WHITE + '[+]',Fore.RED + f'Sleeping.....')
            time.sleep(10)
        elif r.status_code == 404:
            print(Fore.WHITE + '[+]',Fore.RED + f'Unknown Gift Code')

def banner():
    os.system('cls')
    print(f'''
██████╗ ██████╗  ██████╗ ███╗   ███╗ ██████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔═══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║██╔████╔██║██║   ██║██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██║   ██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ '''.replace('█', f'{Fore.LIGHTMAGENTA_EX}█{Fore.LIGHTBLUE_EX}'))
    print(f'{Fore.LIGHTBLUE_EX}Dev By DK16#0001'.center(width))
    check()

banner()