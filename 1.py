import blocksmith 
import random
import time
import sys
from colorama import Fore, Style
F = 40000000000054803039
while F != 73786976294838206463:
    F += 1
    U = '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so'
        
    T = '00000000000000000000000000000000000000000000000' + format(F, '016x')
    AD = blocksmith.BitcoinWallet.generate_compressed_address(T)
    S += 1
    print(Fore.RED + "AD: " + AD)
        
    print(Fore.GREEN + "DEC: " + str(F))
        
        
    print(Fore.YELLOW + "HEX: " + T)
        
    print(Fore.MAGENTA + "scan: " + str(S) + " adress")
        
        
        
    if H in AD:
        S1 += 1
            
        
        print("prefix: " + " addres: " + str(AD) + " decimal: " + str(F) + "\n")
                
                
        if AD == U:
            print(Fore.RED + ("PRIVATE KEY")
            print(AD + "\n")
            print(str(F) + "\n")