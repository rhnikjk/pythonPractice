guesses = []
ANSWERS = ["Russia","Canada","China","USA","Brazil","Australia","India","Argentina","Kazakhstan","Algeria","Congo","Greenland","Saudi Arabia","Mexico","Indonesia","Sudan","Libya","Iran","Mongolia","Peru","Chad","Niger","Angola","Mali","South Africa","Colombia","Ethiopia","Bolivia","Mauritania","Egypt","Tanzania","Nigeria","Venezuela","Pakistan","Namibia","Mozambique","Turkey","Chile","Zambia","Myanmar","Afghanistan","Somalia","Central African Republic","South Sudan","Ukraine","Madagascar","Botswana","Kenya","France","Yemen"]
def intro():
    print("hello welcome to the quiz")
    name = input ("hello, what is your name? ")
    if name == "sigma" or name == "Sigma":
        print ("correct")
    else:
        print (name,"?????? wrong answer. your name is sigma")
        name = "sigma"

def getlives():
    try:
        lives = int(input("how many lives do you want\n"))  
        if lives >= 0:
            return lives
    except:
        print("thats not a number")

def inlist(answer,list):
    if answer in list:
        return True
    else:
        return False


intro()
lives = getlives()
score = 0

for i in range(len(ANSWERS)):
    while lives > 0:
        x=i+1
        print("name the top ",x)
        answer = input("biggest contry")
        if answer == ANSWERS[i]:
            print("correct")
            break
        else:
            print("worng")
            lives=-1