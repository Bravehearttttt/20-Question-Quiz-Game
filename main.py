print("Welcome to 10 Question random Quiz")

playing = input(
    "Do you want to play 10 Question Quiz?.Type Yes Or No to continue").lower()

if playing != "yes":
    quit()

print("Lets Play")
score = 0

answer = input("What does CPU stand for?").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1

else:
    print("Incorrect")
answer = input("What is RAM?").lower()
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What does USB stand for?").lower()
if answer == "universal serial bus":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What does GPU stand for?").lower()
if answer == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What does BIOS stand for?").lower()
if answer == "basic input/output system":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What does LAN stand for?").lower()
if answer == "local area network":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("Who is considered the 'father of the computer'?").lower()
if answer == "charles babbage":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What is the most common operating system?").lower()
if answer == "windows":
    print("Correct")
    score += 1
else:
    print("Incorrect")
answer = input("What does HTTP stand for?").lower()
if answer == "hypertext transfer protocol":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f"You have got  {score} Questions correct")

print(f"Your total Score is {(score/9)*100}%")
