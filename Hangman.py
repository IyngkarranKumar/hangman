import os
import csv
import time

#a = os.path.join('C:\\','Users', 'Admin','Desktop','images','Megatron.txt')   #Here is the general parameters for importing a file

#print( stages[0],'\n', stages[1],'\n',stages[2])

#Hangman

def clear():             #Does not seem to be a nice way to clear screen
    print(100*'\n')
    return

word = input('Player 1, please enter a word: ')
time.sleep(1)
clear()
solve = word[::-1]
L2 = []

#clear()

def hangman(word):
    
    stages = [' __________        ','|         |        ','|         0        ','|        /|\       ','|         |        ','|        / \       ','|                 ']
    L = ['__ ']*len(word)
    x0 = ''.join(L)
    time.sleep(1)
    print(x0)
    j=1
    n=0
    for j in range(1,100):
        wrong = 1
        ans = input('Player 2, choose a letter: ')
        for i in range(0,len(word)):
            if ans==word[i]:
                L[i]=ans
                time.sleep(1)
                wrong = 0
        x1 = ''.join(L)
        print(x1)
        
        
            
        if wrong == 1:
            time.sleep(1)
            n+=1
            if n ==7:
                print("Sorry, that's the game! You lost you stinking retard")
                break
                
            for i in range(n):
                print(stages[i])
            print('\n','\n')
            
            print('That letter does not appear in the word. Try again.')
            wrong = 0

        
            
                
        j+=1
                      #So wouldn't get caught in loop
        if x1 ==word:
            print('Well done, you won the game!')
            break
        
    return
hangman(word)
