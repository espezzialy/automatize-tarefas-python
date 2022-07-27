print('Digite uma frase:')

message = str(input())

count = {} 

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char]+1

for k,v in count.items():
    if k == ' ':
        print('Espaço aparece '+ str(v) +' vezes.') 
    else:
        print('Letra: ' + k + ' aparece '+ str(v) + ' vezes.')


