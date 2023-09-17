with open("n.txt", "a") as f:
    
    def convert_to_hex(line):
        decimal_value = int(line.strip())
        hex_value = '00000000000000000000000000000000000000000000000' + format(decimal_value, '016x')
        return hex_value
    with open('number.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            converted_line = convert_to_hex(line)
            file.write(converted_line + '\n')
            