
import blocksmith 
import random
import time
import sys
from colorama import Fore, Style
import requests
import hashlib
import binascii
import random


# функция для записи переменной в файл
#def write_to_file(variable):
    #with open("Decimal.txt", "a") as f:
        #f.write(str(variable) + "\n")
S = 0
F = 40000000000054675619
#start_time = time.time()
with open("n.txt", "a") as f:
    while True:
        #start = time.time()
        #список слов для генерации seed фразы
        # открытие файла с seed фразой
        with open('seed.txt', 'r') as file:
            seed_phrase = file.read().strip()

# разделение seed фразы на слова
            words = seed_phrase.split()
            #wordse = seed_phrase.split()

# выбор случайных 12 слов из списка
             
            random_words = random.sample(words, 12)
            #pop = ("of")
            #randomsd = random.sample(wordse, 1)
            #random_wordss = (str(random_words) + str(pop) + str(randomsd))
# объединение слов в строку через пробел
            new_seed_phrase = " ".join(random_words)
# хеширование новой seed фразы с помощью SHA-256
            new_seed_hash = hashlib.sha256(new_seed_phrase.encode('utf-8')).digest()

# преобразование хеша в hex
            seed = new_seed_hash.hex()

            

            

        print("Seed phrase:", new_seed_phrase)
        print("Hex seed:", seed)
        U = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'

        AD = blocksmith.BitcoinWallet.generate_compressed_address(seed)
        S += 1
        address = AD

        url = f"https://blockchain.info/balance?active={address}"

        response = requests.get(url)
  
        data = response.json()
        balance = data[address]['final_balance']
        balances = data[address]['total_received']
        print("----------------------------------------------------------")
        print(f"The balance of {address}")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print(f"{balance} satoshi.")
        print(f"{balances} oldsatoshi.")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        if balance > 0:
            print(Fore.RED + "Money Нашел")
            f.write(AD + "\n")
            f.write(str(seed) + "\n")
        if balances > 0:
            print(Fore.RED + "txd Нашел")
            f.write(AD + "\n")
            f.write(str(seed) + "\n")
            break
        print(Fore.RED + "AD: " + AD)
        
        print(Fore.GREEN + "DEC: " + str(seed))
        
        print(Fore.YELLOW + "HEX: " + seed)
        
        print(Fore.MAGENTA + "Просканировано: " + str(S) + " Адресов")
        
        

                
                
        if AD == U:
            print(Fore.RED + "ВНИМАНИЕ НАЙДЕН PRIVATE KEY")
            f.write(AD + "\n")
            f.write(str(F) + "\n")
            break
 # записываем переменную в файл каждые 5 минут
       # if time.time() - start_time >= 300:
               # write_to_file(F)
              #  start_time = time.time()
               # print(Fore.BLUE + "Запись Decimal произведена")
         #       print(Fore.BLUE + "Запись Decimal произведена")
              #  print(Fore.BLUE + "Запись Decimal произведена")
              #  print(Fore.BLUE + "Запись Decimal произведена")
             #   print(Fore.BLUE + "Запись Decimal произведена")
        
                
        