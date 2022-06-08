###  Made BY xrevix [ ! xrevix#5241 ]
###  https://github.com/xrevix

from pystyle import *
from time import sleep
from colorama import Fore
import os,requests,time
#
from app.wd import WebhookDeleter
from app.wi import WebhookInfo
from app.ws import WebhookSpammer
from app.plugin.Proxy import proxy_scrape, getTempDir
#


        
def clear():
    if os.name in ('nt', 'dos'): 
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass

def validateWebhook(hook, mode):
    try:
        responce = requests.get(hook)
        if responce.status_code == "200" or responce.status_code == "204":
            try:
                if mode == 1:
                    print(f"{Fore.GREEN}                        [+] Valid webhook! ({name})")
                    return
            except:
                    input(f"{Fore.RED}                        [-] Invalid Webhook.{responce.status_code}{Fore.RESET}")
                    sleep(0.3)
                    WebTool()  
        if responce.status_code == 404:
            input(f"{Fore.RED}                        [-] Invalid Webhook.{Fore.RESET}")
            sleep(0.3)
            WebTool()  
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        input(f"{Fore.RED}                        [-] Invalid Webhook.{Fore.RESET}")
        sleep(0.3)
        WebTool()
  
    try:
        name = responce.json()["name"]
    except:
        name = ""

    if mode == 1:
        print(f"{Fore.GREEN}                        [+] Valid webhook! ({name})")
        return
    else:
        input(f"{Fore.GREEN}                        [+] Valid webhook! ({name})")
        return
     
Banner = """



                             ██╗    ██╗███████╗██████╗ ████████╗ ██████╗  ██████╗ ██╗
                             ██║    ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║
                             ██║ █╗ ██║█████╗  ██████╔╝   ██║   ██║   ██║██║   ██║██║
                             ██║███╗██║██╔══╝  ██╔══██╗   ██║   ██║   ██║██║   ██║██║
                             ╚███╔███╔╝███████╗██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗
                              ╚══╝╚══╝ ╚══════╝╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                Made By ! xrevix#5241
                                              https://github.com/xrevix


                        [1] Webhook Verifyer                              [4] Webhook Deleter
                        [2] Webhook Info                                  [5] [Coming Soon]
                        [3] Webhook Spammer                               [6] Exit

"""

def WebTool():
    os.system("title WebTool - Made By ! xrevix#5241" if os.name == 'nt' else '' )
    clear()
    print(Colorate.Vertical(Colors.blue_to_purple, Banner, 1))
    input = Write.Input(f"""                        [>] Choice: """, Colors.blue_to_purple, interval=0.005)
    while True:

            if input == '1': 
                web = Write.Input(f"""                        [?] Webhook Link: """, Colors.blue_to_purple, interval=0.005)
                validateWebhook(web, 2)
                WebTool()

            if input == "2":
                web = Write.Input(f"""                        [?] Webhook Link: """, Colors.blue_to_purple, interval=0.005)
                validateWebhook(web, 1)
                WebhookInfo(web)                
                clear()
                WebTool()

            if input == '3': 
                web = Write.Input(f"""                        [?] Webhook Link: """, Colors.blue_to_purple, interval=0.005)
                validateWebhook(web, 1)
                msg = Write.Input(f"""                        [?] Message: """, Colors.blue_to_purple, interval=0.005)
                WebhookSpammer(web, msg)

            if input == '4': 
                web = Write.Input(f"""                        [?] Webhook Link: """, Colors.blue_to_purple, interval=0.005)
                validateWebhook(web, 1)
                delete = Write.Input(f"""                        [?] Are You Sure You Want To Delete Webhook? y/n """, Colors.blue_to_purple, interval=0.005)
                if delete == "y" or delete == "yes" or delete == "Yes" or delete == "Y":
                    WebhookDeleter(web)
                    WebTool()
                else:
                    time.sleep(0.2)
                    WebTool()

            if input == '5':
                Write.Input(f"""                        [?] Coming Soon.. """, Colors.blue_to_purple, interval=0.005)
                WebTool()

            if input == '6':
                exit = Write.Input(f"""                        [?] Are You Sure You Want To Exit? y/n """, Colors.blue_to_purple, interval=0.005)
                if exit == "y" or exit == "yes" or exit == "Yes" or exit == "Y":
                  os._exit(0)
                else:
                    time.sleep(0.2)
                    WebTool()

            
            if input == "":
                WebTool()
         
            else:
                WebTool()

with open(getTempDir()+"\\WebTool_Proxies.txt", 'w'): pass
proxy_scrape()
WebTool()