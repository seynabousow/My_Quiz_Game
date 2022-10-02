print("Welcome to quiz games!")

playing = input("Are you ready to play? ")

if playing.lower() != "yes":
  quit()

print("Okay! Let's Play :)")
score = 0

answer = input("What does TCP stand for? ")
if answer.lower() == "transmission control protocol":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

answer = input("What does DNS do? ")
if answer.lower() == "translates ip address to human readable domain name":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

answer = input("What does TCP/IP stand for? ")
if answer.lower() == "transmission control protocol/internet protocol":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

answer = input(
  "OSPF is an interior gateway protocol which is used in your own? ")
if answer.lower() == "network":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

answer = input("EIGRP was developed by who? ")
if answer.lower() == "cisco":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print('Correct!')
  score += 1
else:
  print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 7) * 100) + "%.")
