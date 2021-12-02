f = open("dag1djup.txt", "r")

lista = []
for x in f:
  lista.append(int(x))
  
djupare = 0
for i in range(len(lista)):
    if (lista[i-1] < lista[i]):
      djupare += 1
          
print(djupare)