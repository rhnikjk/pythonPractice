
#Greet the user and introduce the quiz
play = "yes"
QUESTIONFORMAT = "{}\na. {}\nb. {}\nc. {}\n"
#Greet the user and introduce the quiz
print("hello welcome to the quiz")
while(play == "yes" or play == "y"):
    while(True):
        skillLevel = 0
        try:
            attempts = int(input("how many tres per question do you want?\n"))
            skillLevel = attempts * 0.1 - 0.1
            if(skillLevel >= 1):
                print("you wanted more than 10 tries?!  have some confidence in yourself")
            else:
                break
        except:
            print("thats not a number")
        

        

    score = 0
    #ask the user their name and save it
    questionAttempts = attempts
    while(questionAttempts > 0):
        name = input ("hello, what is your name? ")
        if name == "sigma" or name == "Sigma":
            score += 1 - skillLevel
            print ("correct\n score =", score)
            break
        else:
            print (name,"?????? wrong answer. your name is sigma\n score =", score)
            questionAttempts -= 1
            name = "sigma"
    #Ask the user a question
    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("first question: what is 1+1", "2", "3", "1"))
        if answer == "b" or answer == "3":
            score += 1 - skillLevel
            #Tell them the correct answer
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1

    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("second question: howmany tenticles does a seven armed octipus have", "8", "1", "7"))
        if answer == "c" or answer == "7":
            score += 1 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1
    
    questionAttempts = attempts
    while(questionAttempts > 0):   
        answer = input ("next question: capital of France?\n").lower()
        if answer == "paris":
            score += 1 - skillLevel
            print ("correct, good job \n score = {}".format(score))
            break
        else: 
            print ("wrong, you are trash \n score = {}".format(score))
            questionAttempts -= 1
    #End the quiz
    if score <=3:
        print ("\n {}, you got {} you suck".format(name, score))
    else:
        print ("\n {}, you got {} good job".format(name, score))
    play = input("do you want to play again?\n yes/no\n").lower()