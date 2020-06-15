import vk_api
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.RED + "Скрипт для накрутки ПОСТОВ ")
print("Создатель: vk.com/chmotie \n Группа https://vk.com/scripts_xxx")
print("По вопросам писать в ЛС группы.")
print("Что бы продолжить пиши 1")
nav = input("--> ")
if nav == "1":
   token = input("Введите токен: ")
   owner = input("Введите ID страницы: ")
   post = input("Введите текст поста: ")
   kolvo = input("Введите кол-во постов: ")
   ky = 0

   vk_session = vk_api.VkApi(token=token)
   vk = vk_session.get_api()
while int(ky) < int(kolvo):
   try:
      print("Скрипт работает")
      vk.wall.post(owner_id=owner,message=post)
      time.sleep(5)
   except vk_api.exceptions.Captcha as captcha:
          continue
