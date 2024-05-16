
#Greet the user and introduce the quiz
import random
QUESTIONFORMAT = "{}\na. {}\nb. {}\nc. {}\n"
GOODCOMMENTS = ["nice", "good job", "wow, so good", "great", "sigma as flip"]
BADCOMMENT = ["wow, I didnt know you were that stupid", "you suck", "bad.", "you should comsider getting an education"]
QUESTIONS = ["first question: what is 1+1", "second question: how many tenticles does a seven armed octipus have",
             "next question, top speed of p47", "next question, when was sigmund freud born", "next question, what is the average walking speed", 
             "next question, who is the richest person in the world", "next question, 10+10", "what year did covid 19 start", "when did ww1 start", 
             "last question, how many teeth does a human have"]
OPTIONS = [["2", "3", "1"], ["8", "1", "7"], ["426mph", "478mph", "443mph"], ["1894", "1942", "1856"], ["5.2kph", "4.8kph", "4.5kph"], 
           ["Jeff Bezos", "Elon Musk", "Bernard Arnault"], ["22", "21", "20"], ["2019", "2020", "2021"], ["1914", "1915", "1916"], ["32", "34", "36"]]
SHORT_OPTIONS = ["a", "b", "c"]
ANSWERS = [2,3,1,3,2,3,3,1,1,1]
play = "yes"




#Greet the user and introduce the quiz
print("hello welcome to the quiz")
while(play == "yes" or play == "y"):
    while(True):
        skillLevel = 0
        try:
            attempts = int(input("how many tries per question do you want?\n"))
            skillLevel = attempts-1
            if(skillLevel > 9):
                print("you wanted more than 10 tries?! have some confidence in yourself")
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
            score += 10 - skillLevel
            print ("correct\n score =", score)
            break
        else:
            print (name,"?????? wrong answer. your name is sigma\n score =", score)
            questionAttempts -= 1
            name = "sigma"
    #Ask the user a question
    for i in range(len(QUESTIONS)):
        questionAttempts = attempts
        while questionAttempts > 0:
            answer = input(QUESTIONFORMAT.format(QUESTIONS[i], OPTIONS[1][0],
                                                 OPTIONS[i][1], OPTIONS[i][2])).lower()
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                score += 10 - skillLevel
                print("correct\n score = ", score)
                print(random.choice(GOODCOMMENTS))
                break
            elif answer == "":
                print("not sure?")
            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("wrong")
                print(random.choice(BADCOMMENT))
            else:
                print("that isnt an option")
            questionAttempts -=1





    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("first question: what is 1+1", "2", "3", "1"))
        if answer == "b" or answer == "3":
            score += 10 - skillLevel
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
            score += 10 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1
    
    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("next question, top speed of p47", "426mph", "478mph", "443mph"))
        if answer == "a" or answer == "426" or answer == "426mph":
            score += 10 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1

    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("next question, when was sigmund freud born", "1894", "1942", "1856"))
        if answer == "c" or answer == "1856":
            score += 10 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1

    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("next question, what is the average walking speed", "5.2kph", "4.8kph", "4.5kph"))
        if answer == "b" or answer == "4.8kph" or answer == "4.8":
            score += 10 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1

    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("next question, who is the richest person in the world", "Jeff Bezos", "Elon Musk", "Bernard Arnault")).lower()
        if answer == "c" or answer == "Bernard Arnault":
            score += 10 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1

    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("next question, 10+10", "22", "21", "20"))
        if answer == "c" or answer == "20":
            score += 10 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1

    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("what year did covid 19 start", "2019", "2020", "2021"))
        if answer == "a" or answer == "2019":
            score += 10 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1

    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("when did ww1 start", "1914", "1915", "1916"))
        if answer == "a" or answer == "1914":
            score += 10 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1

    questionAttempts = attempts
    while(questionAttempts > 0):   
        answer = input ("next question: capital of France?\n").lower()
        if answer == "paris":
            score += 10 - skillLevel
            print ("correct, good job \n score = {}".format(score))
            break
        else: 
            print ("wrong, you are trash \n score = {}".format(score))
            questionAttempts -= 1

    questionAttempts = attempts
    while(questionAttempts > 0):
        answer = input (QUESTIONFORMAT.format("last question, how many teeth does a human have", "32", "34", "36"))
        if answer == "a" or answer == "32":
            score += 10 - skillLevel
            print ("correct, good job\n score =", score)
            break
        else: 
            print ("wrong you are trash\n score =", score)
            questionAttempts -= 1
    #End the quiz
    if score <=100:
        print ("\n {}, you got {} you suck".format(name, score))
    else:
        print ("\n {}, you got {} good job".format(name, score))
    play = input("do you want to play again?\n yes/no\n").lower()
print("hope you play again soon")