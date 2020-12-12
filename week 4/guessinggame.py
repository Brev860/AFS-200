import random




def game():  
    
    guesses = 0    
    a = random.randint(1,5)
    while True:
        answer = int(input('Guess a number between 1 and 5. Enter 0 to exit: '))
        guesses += 1

        if a > answer and answer > 0:
            print('Your guess was too low. Try again')
            
           
        elif a < answer:
            print('Your guess was too high')
            
            

        elif a == answer:
            print('You are correct')
            
            

        elif answer == 0:
            break
    print(guesses)

 
game()



    


