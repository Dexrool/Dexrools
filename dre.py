import blocksmith
F = 40000000000075719660
line_number = 0
while F != 73786976294838206463:
        
        line_number += 1
          # Номер строки, которую вы хотите извлечь

        file_path = 'number.txt'  # Путь к файлу, из которого вы хотите извлечь строку

        with open(file_path, 'r') as file:
            lines = file.readlines()

            if line_number <= len(lines):
                line = lines[line_number - 1].strip()
                print(f"{line}")
            else:
                print("Invalid line number.")
            hex_value = blocksmith.BitcoinWallet.generate_compressed_address(line)
        with open(file_path, 'r') as file:
            lines = file.readlines()

# Проверяем, что указанный номер строки не превышает число строк в файле
        if line_number <= len(lines):
            lines[line_number - 1] = line + ' ' + hex_value + '\n'

            with open(file_path, 'w') as file:
                file.writelines(lines)
        else:
            print("Invalid line number.")