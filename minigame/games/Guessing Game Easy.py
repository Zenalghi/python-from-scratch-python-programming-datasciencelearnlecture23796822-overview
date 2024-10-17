sec_num=8
guess_cnt=0
guess_limit=3
out_of_guess=False
print("Welcome to the Guessing Game Easy Mode!")
while guess_cnt<guess_limit:
    try:
        guess=int(input('Guess 1 - 9: '))
        guess_cnt+=1
        if guess==sec_num:
            print('You win!')
            break
        else:
            print('Wrong! Try Again!')
    except ValueError:
        print('Invalid input')
        
print("="*50,"\n")
