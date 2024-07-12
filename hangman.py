import random
from word import *
from hangman_stages import *
print("..WelCome To HangMan Game..")
level=input("choose level..Easy or Hard: ").lower()
Lives=6
choose=random.choice(words)
for i in range(len(words)):
    if words[i]==choose:
        print(clues[i])
        
print(choose)
display=[]
for i in range(len(choose)):
    display+='_'
print(display)
gameover=False
while not gameover:
    user_let=input("Guess a letter: ").lower()
    for i in range(len(choose)):
        if user_let==choose[i]:
            display[i]=user_let
    print(display)
    if user_let not in choose:
        if level=="easy":
            Lives-=1
        else:
            Lives-=2
        if Lives==0:
            print("YOU LOST..!")
            opt=input("You want to continue game: YES or NO: ").lower()
            if opt=='yes':
                gameover=False
            elif opt=='no':
                gameover=True
    
    if '_' not in display:
        print("YOU WON..!")
        opt=input("You want to continue game: YES or NO: ").lower()
        if opt=='yes':
            gameover=False
        elif opt=='no':
            gameover=True
    
    print(stages[Lives-1])
        
    
            
            
            