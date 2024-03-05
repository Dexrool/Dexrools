import blocksmith 
import random
import time
import sys
from colorama import Fore, Style
import requests
def write_to_file(variable):
    with open("Decimal_save.txt", "a") as f:
        f.write(str(variable) + "\n")
S = 0
S1 = 0
F = 40000000000171652404
prefix = input("Введите префикс:")
M = len(prefix)
V = 34 - M
H = str(prefix[:V])
start_time = time.time()
with open("Found.txt", "a") as f:
    while True:
        F += 1
        U = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
        T = '00000000000000000000000000000000000000000000000' + format(F, '016x')
        AD = blocksmith.BitcoinWallet.generate_compressed_address(T)
        S += 1
        address = AD
        print("\033c", end="")
        print( "AD: " + AD)
        
        print("DEC: " + str(F))
        
        print("HEX: " + T)
        
        print("Просканировано: " + str(S) + " Адресов")
        if H in AD:
            S1 += 1
            
            with open("prefix.txt", "a") as f:
                f.write("prefix: " + str(H) + " addres: " + str(AD) + " decimal: " + str(F) + "\n")
                f.write(str(AD) + "\n")
                
                
        if AD == U:
            print("ВНИМАНИЕ НАЙДЕН PRIVATE KEY")
            f.write(AD + "\n")
            f.write(str(F) + "\n")
            break
 # записываем переменную в файл каждые 5 минут
        if time.time() - start_time >= 100:
            with open("Decimal.txt", "a") as f:
                write_to_file(F)
                start_time = time.time()
            print("Запись Decimal произведена")
         #       print(Fore.BLUE + "Запись Decimal произведена")
              #  print(Fore.BLUE + "Запись Decimal произведена")
              #  print(Fore.BLUE + "Запись Decimal произведена")
             #   print(Fore.BLUE + "Запись Decimal произведена")
        print("Префикс",str(H),"найдено таких",S1,"шт.")                
                
        