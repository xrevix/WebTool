from pystyle import *
from colorama import Fore
from app.plugin.Proxy import proxy
import requests,time,os
from threading import Thread

def getTempDir():
    system = os.name
    if system == 'nt':
        return os.getenv('temp')
    elif system == 'posix':
        return '/tmp/'





proxy_list = []


    
temp = getTempDir()+"\\WebTool_Proxies"
with open(temp, 'r') as proxy_file:
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
                pass
    
def WebhookSpammer(web, msg):
        thread_list = []

        for proxy in proxy_list:
                thread_list.append(Thread(target= Spammer, args= (web, proxy, msg)))
        
        for thread in thread_list:
            thread.start()
        
        for thread in thread_list:
            thread.join()
        
