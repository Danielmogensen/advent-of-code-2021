f = open("dag2.txt", "r")

navigation = []

depth = 0
horizontal = 0

for line in f:
  navigation.append([(n) for n in line.split(" ")])
  
for pair in navigation:
   x, y = str(pair[0]),int(pair[1])
   if (x == "forward"):
     horizontal = horizontal + y
   elif (x == "down"):
     depth = depth + y
   elif (x == "up"):
     depth = depth - y
  
print (horizontal * depth)