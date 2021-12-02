f = open("dag1djup.txt", "r")

lista = []
for x in f:
  lista.append(int(x))
  
djupare = 0
for i in range(len(lista)-3):
        if ((lista[i]+lista[i+1]+lista[i+2]) < (lista[i+1]+lista[i+2]+lista[i+3])):
          djupare += 1
          
print(djupare)