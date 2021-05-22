logo ='''
 ######   ##     ##  ######   ######  ########  ######      ######      ###    ##     ## ######## 
##    ##  ##     ## ##    ## ##    ## ##       ##    ##    ##    ##    ## ##   ###   ### ##       
##        ##     ## ##       ##       ##       ##          ##         ##   ##  #### #### ##       
##   #### ##     ##  ######   ######  ######    ######     ##   #### ##     ## ## ### ## ######   
##    ##  ##     ##       ##       ## ##             ##    ##    ##  ######### ##     ## ##       
##    ##  ##     ## ##    ## ##    ## ##       ##    ##    ##    ##  ##     ## ##     ## ##       
 ######    #######   ######   ######  ########  ######      ######   ##     ## ##     ## ######## 





'''
import random
print(logo)
print("computer guess a number in 1 to 100 . guess the number")
def guess():
  make_guess = int(input("make a guess"))
  
  if make_guess == GUESS:
  
    print("you choose  coorrect !!! you win")
    return False
  elif make_guess < GUESS:
    print("too small ")
    return True
  elif make_guess > GUESS:
    print("too big")
    return True
  else:
    print("you choose wrong option")

def leval(attamp):
  
  game_over = True
  while game_over == True and attamp != 0:
    print(f"you have {attamp} to choose ")
    attamp-=1
    game_over = guess()
  if attamp ==0:
    print("you loose all atamps !! you loose it :(")
        
        

GUESS = random.choice(range(0,101))
# print(GUESS)
level = input("choose difficulty 'hard ' or 'easy' ")
if level == "hard":
  attamp = 5
  leval(attamp)
elif level =="easy":
  attamp = 10
  leval(attamp)
else:
  print("you choose wrong option")
