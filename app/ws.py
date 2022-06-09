###  Made BY xrevix [ ! xrevix#5241 ]
###  https://github.com/xrevix

from pystyle import *
from colorama import Fore
from app.plugin.Proxy import proxy, getTempDir
import requests,time
from threading import Thread

proxy_list = []
with open(getTempDir()+"\\WebTool_Proxies.txt", "w", encoding="utf-8", errors='ignore'): pass
temp = getTempDir()
with open(getTempDir()+"\\WebTool_Proxies.txt", 'r') as proxy_file:
            for proxy in proxy_file:
                proxy_list.append(proxy.split('\n')[0])
        
proxy_list = list(set(proxy_list))

def Spammer(web, proxy, msg):
        while True:
            try:
                response = requests.post(web, headers= {'content-type': 'application/json'}, proxies= {'http': proxy, 'https': proxy}, json= {"content": msg })
                    
                if response.status_code == 204 or response.status_code == 200:
                    print(f'''{Fore.GREEN}                        [+] Message sent{Fore.RESET}''')

                elif response.status_code == 429: 
                    timeout = int(str(response.json()['retry_after'])[2:])
                    print(f'''{Fore.YELLOW}                        [-] Ratelimited sleep For {timeout}s{Fore.RESET}''')
                    time.sleep(timeout)

                elif response.status_code == 404:
                   input(f'''{Fore.RED}                        [-] Webhook Link Not Valid!{Fore.RESET}''')
                   return

                else:
                    input(f"""{Fore.RED}                        [-] Unknown Error: {response.status_code}{Fore.RESET}""")
                    return

            except:
                return    

def WebhookSpammer(web, msg):
        thread_list = []

        for proxy in proxy_list:
                thread_list.append(Thread(target= Spammer, args= (web, proxy, msg)))
        
        for thread in thread_list:
            thread.start()
        
        for thread in thread_list:
            thread.join()
        
