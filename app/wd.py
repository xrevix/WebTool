###  Made BY xrevix [ ! xrevix#5241 ]
###  https://github.com/xrevix

from pystyle import *
import requests
  
def WebhookDeleter(web):
    r = requests.delete(web)
    if r.status_code == 200 or 204:
          input(Colorate.Vertical(Colors.purple_to_blue, """                        [+] Webhook Successfully Deleted"""))
          return

    if r.status_code == 404:
          input(Colorate.Vertical(Colors.red_to_blue, f'''                        [-] Webhook Link Not Valid!''', 1 ))
          return
    else:
        input(Colorate.Vertical(Colors.red_to_blue, f'''                        [-] Error: {r.status_code}''', 1))
        return

