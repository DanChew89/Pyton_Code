import random

rock = 0
paper = 1
scissors = 2

ran = 0
#print(ran)

my_score= 0
opponant= 0
answer = 0
count = 0
played_games=0

#print(answer)
#print(type(answer))
#print(type(0))

def results():
    
    if (answer == ran):
      print("Draw")
      return 0
    else:
      if (answer == 0):
        if(ran == 1):
          print("Paper beats rock. Opponant win ")
          return 1        
        else:
          print("Rock beats Scissors. I win ")
          return 2
        #opponant += int(1)
      if (answer == 1 ):
        if(ran == 0):
          print("Paper beats rock. I win")
          return 2
        else:
          print("Scissors beats Paper . Opponant win  ")
          return 1
      if (answer == 2 ):
        if(ran == 0):
          print("Rock beats Scissors. Opponant win")
          return 1
        else:
          print("Scissors beats Paper. I win  ")
          return 2



play_game = int(input("How many games would you like to play? "))
while(played_games < play_game ):
  ran = random.randint(0,2)
  answer = int(input("what do you choose?\n0 for rock,\n1 for Paper\n2 for scissors\n5 Exit "))
  if(answer == 5 ):
    print("Thanks for playing you chose to exit game")
    played_games = 5
  elif(answer < 0 or answer > 2):
    print("Invalid enterty\nPlease choose number \n0 for rock \n1 for Paper \n2 for scissors \n5 to exit ")
  else:
    if(results() == 2):
      my_score =+1
    elif(results() == 1):
      opponant =+1
      
  played_games +=1
  #print("\n")
  #print ("Number I have picked " + str(answer))
  #print("This is the random number " + str(ran))
  #print("\n")
  #print("My score " + str(my_score))
  #print("Opponants Score "+str(opponant))
  #print("\n")
  #print("How many games I have played " + str(played_games))
  #print("How many hames is set to play " + str(play_game))
  count=1

print("\nThanks for playing.\nScore\nMy score "+ str(my_score)+ "\nYour score " + str(opponant))

#print(answer)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

