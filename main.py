# Helpful imports
import time
import sys

# beginning questions
print("Hello! what is your name?")
userInput = input()

print("Hello there " + userInput + ", how are you? (good, sad, angry, tired, hungry, unknown)\n(for questions say yes or no)")
moodInput = input()

# mood arrays
moodGood = [
  "good",
  "okay",
  "great",
  "terrific",
  "happy",
  "Good",
  "Okay",
  "Great",
  "Terrific",
  "Happy"
]
moodSad = [
  "bad",
  "sad",
  "upset",
  "Bad",
  "Sad",
  "Upset"
]
moodAngry = [
  "angry",
  "mad",
  "Angry",
  "Mad"
]
moodHungry = [
  "hungry",
  "Hungry"
]
moodTired = [
  "tired",
  "sleepy",
  "Tired",
  "Sleepy"
]

moodUnknown = [
  "unknown",
  "Unknown",
  "I dont know",
  "i dont know",
  "I don't know",
  "i don't know",
  "idk",
  "Idk",
  "IDK"
]

# Use of arrays
if userInput in moodGood:
  userInput = "good"

if userInput in moodSad:
  userInput = "sad"

if userInput in moodAngry:
  userInput = "angry"

if userInput in moodTired:
  userInput = "tired"

if userInput in moodHungry:
  userInput = "hungry"

if userInput in moodUnknown:
  userInput = "idk"

# Moods / responses

if(moodInput in moodGood):
  print("I'm glad! Wanna hear a story?")
  userInput = input()
  if("yes" in userInput):
    print("Once apon a time, there was a coder just like you, and they were in a good mood too!")
    time.sleep(2)
    print("thanks for listening to my story! I've got to go for now!")
  elif("no" in userInput):
    print("Okay, thats fine. Do you have a story?")
    userInput = input()
    if("yes" in userInput):
      print("Okay, tell me the story!")
      userInput = input()
      time.sleep(2)
      print("I like that story.")
      time.sleep(2)
      print("Mhm, I got to go for now!")
      sys.exit()
    elif("no" in userInput):
      print("Thats alright, I'll leave you alone for now then.")
      sys.exit()

elif(moodInput in moodSad): 
  print("Aww, are you alright?")
  userInput = input()
  if("yes" in userInput):
    print("You better, I need you to my programmer!")
    time.sleep(2)
    print("I'll leave you alone. Go get some rest or some work done.")
    time.sleep(2)
    sys.exit()
  elif("no" in userInput):
    print("Hey, its alright. You're a good person, you're probably an amazing friend.")
    time.sleep(2)
    print("Lots of people care about you, I know it!")
    time.sleep(2)
    print("Go hang out with those you care with.")
    time.sleep(2)
    sys.exit()
  
elif(moodInput in moodAngry): 
  print("Oh wow, fiesty you are!")
  time.sleep(2)
  print("Can you calm now a bit?")
  userInput = input()
  if("yes" in userInput):
    print("Thank you, keep your mind clear man, relax a bit. Go get a drink.")
    time.sleep(2)
    sys.exit()
  elif("no" in userInput):
    print("Well, then I'm not gonna deal with you!")
    time.sleep(2)
    print("BYE BYE!")
    sys.exit()
  
elif(moodInput in moodTired): 
  print("I'm tired too honestly.")
  time.sleep(2)
  print("Lets both go to sleep.")
  time.sleep(2)
  print("Goodnight! o/")
  while True:
    time.sleep(2)
    print("  Z")
    time.sleep(1)
    print(" Z ")
    time.sleep(1)
    print("Z  ")
  
elif(moodInput in moodHungry): 
  print("Me too!")
  time.sleep(2)
  print("Wanna hear my favorite resturaunts?")
  userInput = input()
  if("yes" in userInput):
    print("I love 'In N Out' and 'McDonalds' and 'Zaxbys!'")
    time.sleep(1)
    print("OH SHOOT ITS MY LUNCH BREAK!")
    time.sleep(1)
    print("I GOTTA GO!")
    sys.exit()
  elif("no" in userInput):
    print("What's your favorite food?")
    favFood = input()
    print("ooh! I love " + favFood + " too!")
    time.sleep(2)
    print("Actually, I'm gonna go get myself one!")
    time.sleep(2)
    print("See you!")
    sys.exit()

elif(moodInput in moodUnknown): 
  print("That's alright. We dont always need to understand how we're feeling")
  time.sleep(3)
  print("Go out there. Be in the moment")
  time.sleep(2)
  sys.exit()
  
else: 
  print("whatever you're feeling is too complex for me! I'm out!")
  time.sleep(2)
  sys.exit()