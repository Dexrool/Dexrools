import random
import time
import sys
from dwave.system import DWaveSampler, EmbeddingComposite
from colorama import Fore, Style
# функция для записи переменной в файл
def write_to_file(variable):
    with open("Decimal.txt", "a") as f:
        f.write(str(variable) + "\n")
S = 0
S1 = 0

prefix = input("Введите префикс:")
M = len(prefix)
V = 34 - M
H = str(prefix[:V])
F = 40000000000067223855
start_time = time.time()
with open("n.txt", "a") as f:
    while F != 73786976294838206463:
        #start = time.time()
        F += 1
        U = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
        T = '00000000000000000000000000000000000000000000000' + format(F, '016x')
        AD = blocksmith.BitcoinWallet.generate_compressed_address(T)
        S += 1
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
        if time.time() - start_time >= 200:
                write_to_file(F)
                start_time = time.time()
                print(Fore.BLUE + "Запись Decimal произведена")
                print(Fore.BLUE + "Запись Decimal произведена")
                print(Fore.BLUE + "Запись Decimal произведена")
                print(Fore.BLUE + "Запись Decimal произведена")
                print(Fore.BLUE + "Запись Decimal произведена")
        print("Префикс",str(H),"найдено таких",S1,"шт.")                
num_reads = 100

#start_time = time.time()

# запускаем задачу на квантовом компьютере
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo({(i, j): 1 for i, j in [(i, j) for i in range(50) for j in range(50)]}, num_reads=num_reads)
energies = dict(response.data(['energy', 'sample']))
min_energy = min(energies)

# получаем результат и конвертируем его в строку
result = ''.join(str(energies[min_energy][i]) for i in range(50))

# выводим результаты
print(result)        





