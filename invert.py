string = "Leonardo Monteiro Medeiros"

# Método 01
string_inv = string[::-1]

print(string_inv)

# Método 02
string_inv = ""

for i in range(len(string)-1, -1, -1):
    string_inv += string[i]

print(string_inv)
