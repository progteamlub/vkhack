import vk_api, time,colorama
from colorama import Fore, Back, Style
from vk_api import VkUpload
colorama.init()

priva = [
"""
▓▓▓▓▓▓▀▀░░░░░░▀▀▓▓▓▓▓▓ 
▓▓▓▀░░░░░▄██▄░░░░░▀▓▓▓ 
▓▓░░░░░▄▄██▀░░░░░░░░▓▓ 
▓░░░░░▄██▀░░░▄█▄░░░░░▓ 
▌░░░░░▀██▄▄▄█████▄░░░▐ 
░░▄▄▄░░░▀████▀░▀▀██▄░░ 
░░▀██▄░▄▄████▄░░░▀▀▀░░ 
▌░░░▀█████▀▀▀██▄░░░░░▐ 
▓░░░░░▀█▀░░░▄██▀░░░░░▓ 
▓▓░░░░░░░░▄██▀░░░░░░▓▓ 
▓▓▓▄░░░░░▀█▀▀░░░░░▄▓▓▓
"""
]

opicanya = [
"""
×ProgTeam ¤ Termux SU×
Накрутка фотографий в ВК
    ВЫБЕРИ ЦИФРУ:
01. Инструкция VK-PhoHack.
02. Включить VK-PhoHack.
1. Инструкция VK-BanHack. ×В разработке до 05.10.20×
2. Запустить Vk-BanHack. ×В разработке до 05.10.20×
"""
]
print(Fore.GREEN + priva[0])
print(Fore.RED + opicanya[0])
vibor = input('-->')
if vibor == "02":
	login1 = input('Введите логин от страницы:')
	password1 = input('Введите пароль от страницы:')
	album = input('Введите ID альбома:')
if vibor == "01":
	print('''
	Для начало создай альбом
	Потом включи программу
	За тем введи все данные
	P.S Вас перенесет в меню через 15 минут''')
	time.sleep(15)
	print(Fore.GREEN + priva[0])
	print(Fore.RED + opicanya[0])
if vibor == "1":
    print('Просто введи токен и всё\nP.S Тебя перенесет в главное меню через 15 секунд')
    time.sleep(15)
if vibor == "2":
	os.system('ban.py')
vk_session = vk_api.VkApi(login=login1, password=password1, app_id='2685278')
vk_session.auth(token_only=True)
vks = vk_session
upload = VkUpload(vk_session)

while True: 
	upload.photo(photos="photo.jpg",album_id=album)
