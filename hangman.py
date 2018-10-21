import msvcrt as m
def wait():
    m.getch()

keyword=input("tell me a secret! ")
hangman=[]
x= len(keyword)
for i in range(x):
    hangman.append("_")

print (keyword,)
print (hangman,)

word=False
lives=6
while lives!=0 and word==False:
    
    guess=input("guess a letter!")
    if len(guess)!=1:
        print ("you can only quess one letter!")
        guess=input("guess a letter!")
    counter=0
    for i in range(len(keyword)):
        if guess == keyword[i]:
            hangman[i]=guess
            counter=1

    if counter==0:
        lives=lives-1
        if lives==5:
            print ("you have 5 lives")
            print (" | ")
            print (" O ")           
        elif lives==4:
            print ("you have 4 lives")
            print (" | ")
            print (" O ")
            print (" | ")
        elif lives==3:
            print ("you have 3 lives")
            print (" | ")
            print (" O ")
            print ("/| ")
        elif lives==2:
            print ("you have 2 lives")
            print (" | ")
            print (" O ")
            print ("/|\\")
        elif lives==1:
            print ("you have 6 lives")
            print (" | ")
            print (" O ")
            print ("/|\\")
            print ("/  ")
        else:
            print ("you got hanged!")
            print (" | ")
            print (" O ")
            print ("/|\\")
            print ("/ \\")
            wait()
    else:
        print ("Wow you got one!")
        print (hangman,)

    test=0
    for i in range(len(hangman)):
        if hangman[i]!="_":
            test=test+1
    if test==len(hangman):
        word=True
        print ("you found it!")
        wait()
    
