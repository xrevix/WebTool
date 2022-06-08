###  Made BY xrevix [ ! xrevix#5241 ]
###  https://github.com/xrevix

from pystyle import *
import requests
  
def WebhookDeleter(web):
    r = requests.delete(web)
    if r.status_code == 200 or 204:
          Write.Input(f"""                        [+] Webhook Successfully Deleted""", Colors.blue_to_purple, interval=0.005)
          return

    if r.status_code == 404:
          Write.Input(f"""                        [-] Webhook Link Not Valid!""", Colors.blue_to_purple, interval=0.005)
          return
    else:
        Write.Input(f"""                        [-] Error: {r.status_code}""", Colors.blue_to_purple, interval=0.005)
        return

