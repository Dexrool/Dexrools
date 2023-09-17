import blocksmith 
import random
import time
import sys
with open("n.txt", "a") as f:
    
    def convert_to_hex(line):
        decimal_value = str(line.strip())
        hex_value = blocksmith.BitcoinWallet.generate_compressed_address(decimal_value)
        return line.strip() + ' ' + hex_value
    with open('number.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            converted_line = convert_to_hex(line)
            file.write(converted_line + '\n')
            