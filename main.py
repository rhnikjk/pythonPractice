
#Greet the user and introduce the quiz
#Ask the user a question
#Tell them the correct answer
#End the quiz
#ask the user their name and save it
score = 0
name = input ("hello, what is your name? ")
if name == "sigma" or "Sigma":
    score += 1
    print ("correct\n score =", score)
else:
    print (name,"?????? wrong answer. your name is sigma\n score =", score)

answer = input ("first question: 1+1: \n a. 2 \n b. 3 \n c. 1678946\n")
if answer == "b":
    score += 1
    print ("correct, good job\n score =", score)
else: 
    print ("wrong you are trash\n score =", score)

answer = input ("next question: how many tenticles does a seven tenticled octipus have: \n a. 1 \n b. 8 \n c. 7\n")
if answer == "c":
    score += 1
    print ("correct, good job\n score =", score)
else: 
    print ("wrong you are trash\n score =", score)
    
answer = input ("next question: capital of france?\n").lower
if answer == "paris" or "Paris":
    score += 1
    print ("correct, good job\n score =", score)
else: 
    print ("wrong you are trash\n score =", score)


if score <=3:
    print ("\n you got", score, " you suck")
else:
    print ("\n you got", score, " good job")