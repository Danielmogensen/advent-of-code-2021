f = open("dag2.txt", "r")

navigation = []

aim = 0
depth = 0
horizontal = 0

for line in f:
  navigation.append([(n) for n in line.split(" ")])
  
for pair in navigation:
   x, y = str(pair[0]),int(pair[1])
   if (x == "down"):
     aim = aim + y
   elif (x == "up"):
     aim = aim - y
   elif (x == "forward"):
    horizontal = horizontal + y
    depth = depth + (aim * y)


print (horizontal * depth)