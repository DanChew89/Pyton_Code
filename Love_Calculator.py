# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

Combine_Name = name1 + name2

true_score_first = Combine_Name.lower().count("t")
true_score_first += Combine_Name.lower().count("r")
true_score_first += Combine_Name.lower().count("u")
true_score_first += Combine_Name.lower().count("e")

true_score_Second = Combine_Name.lower().count("l")
true_score_Second += Combine_Name.lower().count("o")
true_score_Second += Combine_Name.lower().count("v")
true_score_Second += Combine_Name.lower().count("e")


Love_Score = int(str(true_score_first) + str(true_score_Second))

if Love_Score < 10 or Love_Score > 90:
  print(f"Your score is {Love_Score}, you go together like coke and mentos")
elif Love_Score >= 40 and Love_Score <= 50:
  print(f"Your score is {Love_Score}, you are alright together")
else:
   print(f"Your score is {Love_Score}")