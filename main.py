
#Greet the user and introduce the quizN
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
ANSWERS = [1,2,0,2,1,2,2,0,0,0]
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
        while(questionAttempts > 0):
            answer = input(QUESTIONFORMAT.format(QUESTIONS[i], OPTIONS[i][0], OPTIONS[i][1], OPTIONS[i][2])).lower()
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                score += 10 - skillLevel
                print("correct\n score = ", score)
                print(random.choice(GOODCOMMENTS))
                break
            else:
                print("wrong")
                print(random.choice(BADCOMMENT))
            questionAttempts -=1

    #End the quiz
    if score <=100:
        print ("\n {}, you got {} you suck".format(name, score))
    else:
        print ("\n {}, you got {} good job".format(name, score))
    play = input("do you want to play again?\n yes/no\n").lower()
print("hope you play again soon")