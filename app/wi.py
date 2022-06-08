###  Made BY xrevix [ ! xrevix#5241 ]
###  https://github.com/xrevix

from pystyle import *
from colorama import Fore
import requests,json

def WebhookInfo(web):
       try:
              r = requests.get(web)
              if r.status_code == 200 or 204:
                     Write.Print(f"""                        [+] Webhook Name: {r.json()["name"]}                        
                        [+] Webhook ID: {r.json()["id"]}
                        [+] Guild ID: {r.json()["guild_id"]}
                        [+] Channel ID: {r.json()["channel_id"]}
                        [+] Token: {r.json()["token"]}""", Colors.blue_to_purple, interval=0.005)
                     try:
                            av = r.json()["avatar"]
                            if av == "null":
                                   Write.Print(f"""
                        [+] Avatar: None""", Colors.blue_to_purple, interval=0.005)
                            else:
                                   Write.Input(f"""
                        [+] Avatar: https://cdn.discordapp.com/avatars/{r.json()["id"]}/{r.json()["avatar"]}""", Colors.blue_to_purple, interval=0.005)
                                   return
                     except:
                            pass
              
              else:
                     input(Colorate.Vertical(Colors.red_to_blue, f'''                        [-] Error: {r.status_code}''', 1))
                     return
       except ( json.decoder.JSONDecodeError ):
                     input(f'''{Fore.RED}                        [-] No Info Find{Fore.RED}''')
