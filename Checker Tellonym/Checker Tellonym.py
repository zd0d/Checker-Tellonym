#by king berlin | @680068
import requests
import os

count = 0

banner = ('''
[!] Follow Me In Instagram : @680068
  _______ ______ _      _         _____ _    _ ______ _____ _  ________ _____  
 |__   __|  ____| |    | |       / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
    | |  | |__  | |    | |      | |    | |__| | |__ | |    | ' /| |__  | |__) |
    | |  |  __| | |    | |      | |    |  __  |  __|| |    |  < |  __| |  _  / 
    | |  | |____| |____| |____  | |____| |  | | |____ |____| . \| |____| | \ \ 
    |_|  |______|______|______|  \_____|_|  |_|______\_____|_|\_\______|_|  \_\
                                                                               
                          Coded by | @680068        
''')
print(banner)



file0 = input("[~] Enter File Name :")

input("\n[~] Press, Enter To Start")

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__cfduid=d9a45d5a0d1610e2a1abf30dac99aa7681613198934; _ga=GA1.2.1551905763.1613198948; _gid=GA1.2.767379040.1613198948; __cf_bm=ee7ac75044152eb1d2ad2f130402990e23eb0cda-1613232593-1800-AQ08xpweTVOHARq3LOG08YITD6T71cgZNqq41jhl8gtsnAg3eEVY5jwwMSOZloDO+EAv3V2SX2xaOSJKBnM5cBEPYNza54sWGauQeMsRKPnrnKMf2jKcta+uoo5ZWQV9ag==; _gat=1; __rtgt_sid=kl3x176qgjlsv2',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',#berlin
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    }

file = open(file0, "r")

while True:
  che = file.readline().split('\n')[0]
  url = f'https://tellonym.me/{che}'
  req = requests.get(url, headers=headers)
  if (che == ""):
      print(" ")
      input("Press, Enter To Close Program .. ")
      exit(0)
  if req.status_code == 404:
      count += 1
      print("{}: {}".format(count, che.strip()) + " | Available")
      with open('Available @680068.txt', 'a') as x:
             x.write(che + '\n')
  else:
      count +=1
      print("{}: {}".format(count, che.strip()) + " | Not Available")
