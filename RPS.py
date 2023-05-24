import random
rock = '''
       ____
______/  __)       
        ___)
______ ____)
     \____ )
    
'''
    
paper = '''
       ___________
______/  _________)       
        ___________)
______ ___________)
     \__________)

'''
scissor = '''
       ___________
______/  _________)       
          _________)
______   ____)
     \______)
'''

game_image = [rock,paper,scissor]
user_choice=int(input("enter your choice: type 0 for rock,type 1 fo paper,type 2 for scissor"))
if user_choice>=3 and user_choice<0:
    print("Invalid number, you lose")
else:
    print(game_image[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choose:",computer_choice)
    print(game_image[computer_choice])
    if computer_choice==user_choice:
        print("It's a draw")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif computer_choice==2 and user_choice==0:
        print("you win")
    elif computer_choice>user_choice:
        print("you lose")
    elif computer_choice<user_choice:
        print("you win")
        
