import blocksmith 
import random
import time
import sys
from colorama import Fore, Style
import requests


# функция для записи переменной в файл
#def write_to_file(variable):
    #with open("Decimal.txt", "a") as f:
        #f.write(str(variable) + "\n")
S = 0
S1 = 0

prefix = input("Введите префикс:")
M = len(prefix)
V = 34 - M
H = str(prefix[:V])
#F = 40000000000142716216
#start_time = time.time()
with open("n.txt", "a") as f:
    while True:
        #start = time.time()
        F = random.randint(36893488147419103232,73786976294838206463)
        U = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
        T = '00000000000000000000000000000000000000000000000' + format(F, '016x')
        AD = blocksmith.BitcoinWallet.generate_compressed_address(T)
        S += 1
        address = AD

        url = f"https://blockchain.info/balance?active={address}"

        response = requests.get(url)
  
        data = response.json()
        balance = data[address]['final_balance']
        print("----------------------------------------------------------")
        print(f"The balance of {address}")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        print(f"{balance} satoshi.")
        print("----------------------------------------------------------")
        print("----------------------------------------------------------")
        if balance > 0:
            print(Fore.RED + "Money Нашел")
            break
        print(Fore.RED + "AD: " + AD)
        
        print(Fore.GREEN + "DEC: " + str(F))
        
        print(Fore.YELLOW + "HEX: " + T)
        
        print(Fore.MAGENTA + "Просканировано: " + str(S) + " Адресов")
        
        
        if H in AD:
            S1 += 1
            
            with open("prefix.txt", "a") as f:
                f.write("prefix: " + str(H) + " addres: " + str(AD) + " decimal: " + str(F) + "\n")
                
                
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
        print("Префикс",str(H),"найдено таких",S1,"шт.")                
                
        