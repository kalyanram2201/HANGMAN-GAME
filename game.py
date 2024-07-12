import random
from hangman_stages import *
from word import *
print(logo)
print("..WelCome To HangMan Game..")
gameover=False
while not gameover:
    lives=6
    level=input("Choose a level to play..EASY or HARD: ").lower()
    choose=random.choice(words)
    for i in range(len(words)):
        if words[i]==choose:
            print(clues[i].upper())
    #print(choose)
    display=[]
    
    for i in range(len(choose)):
        display+='_'
    print(display)
    game=False
    while not game:
        guess=input("Guess a letter: ").lower()
        for i in range(len(choose)):
            letter=choose[i]
            if guess==letter and guess:
                display[i]=guess
        print(display)
        if guess not in choose:
            if level=='easy':
                lives-=1
            elif level=='hard':
                lives-=2
            print(stages[lives]) 
            if lives==0:
                game=True
                print("YOU LOST..")
                opt=input("If you want to continue game..Enter YES or NO..: ").lower()
                if opt=='yes':
                    gameover=False
                    game=True
                elif opt=='no':
                    gameover=True
                    game=True
                   # print("Thank You...")
        if '_' not in display:
            game=True
            print("YOU WON...")
            opt=input("If you want to continue game..Enter YES or NO..: ").lower()
            if opt=='yes':
                gameover=False
        
            elif opt=='no':
                gameover=True
print("Thank You...")       
        