name = input("What is your name?  ")
print("Welcome to who wants to be millionaire", name)

# -------------------------First Question-------------------------------
question = "Question 1: What was the first spacecraft to reach the moon?"
choices = ["a. Apolo 13", "b. Apolo 11", "c. Apolo 1", "d. Apolo 4"]
answer = "b"

def ask_question(question): #definig the function the argument is question variable
	global ans #globalizing the variable so can be called outside of the function
	print(question)
	for index in range(len(choices)):
		print(choices[index])
	ans = input("Please select an answer (a, b, c or d): ")

points = 0

def check_answer(ans):
	global points
	if ans == answer:
		points += 100
		print("You are correct! Your total points are:", points)
	else:    
		print("Incorrect, good luck the netx time!,your total points: 0")
		exit()#The game  ended.
# ---call functions---
ask_question(question) 
check_answer(ans) 

# -------------------------Second Question-----------------------------------
question = "Question 2: What was the physicist who proposed the string theory?"
choices = ["a. Albert Einstein", "b. stephen hawking", "c. Isaac newton", "d. Joel Scherk and John Henry Schwarz"]
answer = "d"

def ask_question(question): 
	global ans
	print(question)
	for index in range(len(choices)):
		print(choices[index])
	ans = input("Please select an answer (a, b, c or d): ")

points = 0

def check_answer(ans):
	global points
	if ans == answer:
		points += 200
		print("You are correct! Your total points are:", points)
	else:
		print("Incorrect, good luck the netx time!,your total points: 100")
		exit()
 
ask_question(question)
check_answer(ans)

# --------------------------third question------------------------------
question = "Question 3: What is the function of the gallbladder?"
choices = ["a. produces bile", "b. stores bile", "c. produces insuline", "d. produces kidney stones"]
answer = "b"

def ask_question(question):
	global ans 
	print(question)
	for index in range(len(choices)):
		print(choices[index])
	ans = input("Please select an answer (a, b, c or d): ")

points = 0

def check_answer(ans):
	global points
	if ans == answer:
		points += 300
		print("You are correct! Your total points are:", points)
	else:
		print("Incorrect, good luck the next time!, your total points: 200")
		exit()

ask_question(question)
check_answer(ans)

# ---------------------------------forth question---------------------------------
question = "Question 4: Where in the world did the battle of Ticonderoga take place?"
choices = ["a. North America", "b. South india", "c. Philipines", "d. Mexico"]
answer = "a"

def ask_question(question):
	global ans 
	print(question)
	for index in range(len(choices)):
		print(choices[index])
	ans = input("Please select an answer (a, b, c or d): ")

points = 0

def check_answer(ans):
	global points
	if ans == answer:
		points += 400
		print("You are correct! Your total points are:", points)
	else:
	    print("Incorrect, good luck the next time!, your total points: 300")
        # exit() #exit not working for some reason

ask_question(question) 
check_answer(ans)

# ---------------------------fifth question--------------------------------
question = "Question 5: In the Disney movie; Tambor, Bambi's friend, is he?"
choices = ["a. Bunny", "b. Cat", "c. Elephant", "d. Tiger"]
answer = "a"

def ask_question(question): 
	global ans 
	print (question)
	for index in range(len(choices)):
		print (choices[index])
	ans = input("Please select an answer (a, b, c or d): ")

points = 0

def check_answer(ans):
	global points
	if ans == answer:
		points += 500
		print ("You are correct! Your total points are:", points)
	else:
		print ("Incorrect, good luck the next time!, your total points: 400")
		exit()
	
ask_question(question) 
check_answer(ans)

# ------------------------And the last question-------------------------------
question = "Last Question: Which company created spiderman?"
choices = ["a. DC comics", "b. Marvel", "c. Disney", "d. Fox"]
answer = "b"

def ask_question(question):
	global ans 
	print (question)
	for index in range(len(choices)):
		print (choices[index])
	ans = input("Please select an answer (a, b, c or d): ")

points = 0

def check_answer(ans):
	global points
	if ans == answer:
		points += 1000
		print("Congratulations you win!, Your final points are:", points)
        # print('!!!!' * 5) # again not working don't know why
	else:
            print("incorrect, good luck the next time!, your total points: 500")
            exit()

ask_question(question)
check_answer(ans)
# ----------------------------------game ending here--------------------------------- 

