b=1
guesses = []
ANSWERS = ["Russia","Canada","China","USA","Brazil","Australia","India","Argentina","Kazakhstan","Algeria","Congo","Greenland","Saudi Arabia","Mexico","Indonesia","Sudan","Libya","Iran","Mongolia","Peru","Chad","Niger","Angola","Mali","South Africa","Colombia","Ethiopia","Bolivia","Mauritania","Egypt","Tanzania","Nigeria","Venezuela","Pakistan","Namibia","Mozambique","Turkey","Chile","Zambia","Myanmar","Afghanistan","Somalia","Central African Republic","South Sudan","Ukraine","Madagascar","Botswana","Kenya","France","Yemen"]
#-----------------------FUNCTIONS----------------------------------------
def intro():
    print("hello welcome to the quiz")
    name = input ("hello, what is your name? ")
    if name == "sigma" or name == "Sigma":
        print ("correct")
    else:
        print (name,"?????? wrong answer. your name is sigma")
        name = "sigma"
b=0
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

#--------------------------MAIN CODE-----------------------------------
intro()
lives = getlives()
score = 0

while lives > 0:
    for i in range(len(ANSWERS)):
        i=b
        x=i+1
        answer = input("name one of the 50 biggest contrys\n")
        if inlist(answer,ANSWERS) and inlist(answer,guesses):
            print("correct")
            b += 1
        else:
            print("worng")
            b = 0