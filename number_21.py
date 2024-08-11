import random
import sys

def compute(lists):  
    if len(lists)==0:
        p=0
    else:
        p=int(lists[-1])   
               
    no_digit=random.choice([1,2,3,4])
    
    list=[]
    for i in range(no_digit):
        app=int(p+i+1)
        list.append(app)    
    
    return list  
    

def play():
    print("Do you want to play First or second (1 or 2)")
    choices=False
    while not choices:
        try:
            ch=int(input())
        except:
            print("Enter an integer")    
        if ch>2 or ch<1:
            print("Enter 1 or 2") 
        else:
            choices=True      
         
    
    lose=False
    game_list=[]
    comp_list=[]
    while not lose:
        if ch ==1:
            print("\nYour turn\n")
            try:
                num_count=int(input("How many numbers do you want to enter?"))
            except:
                print("Enter an integer")
                continue    
            if num_count>4:
                print("You can't enter more than 4 numbers")
                continue
            print("Enter the ",num_count," numbers")

            for i in range(num_count):
                try :
                    n=int(input())
                    if len(game_list)!=0:
                        if n!=game_list[-1]+1:
                            print("Enter consecutive numbers")
                            continue
                    elif n!=1:
                        print("Start from one")
                        continue
                except:
                    continue
                            
                game_list.append(n)
                
            print("Game count:")
            print(game_list)
            
            if len(game_list)>=21:
                print("The computer wins")
                lose=True
                continue
                
            print("\nComputer's turn\n")
                
            comp_list=compute(game_list)
            
            for j in comp_list:
                game_list.append(j)
                
            print("Game count:")
            print(game_list)
            
            if len(game_list)>=21:
                print("You win")
                lose=True
                continue
        elif ch ==2:
            print("\nComputer's turn\n")
             
            comp_list=compute(game_list)
            
            for j in comp_list:
                game_list.append(j)
                
            print("Game count:")
            print(game_list)
            
            if len(game_list)>=21:
                print("You win")
                lose=True
                continue
                
            print("\nYour turn\n")
            try:
                num_count=int(input("How many numbers do you want to enter?"))
            except:
                print("Enter an integer")
                continue    
            if num_count>4:
                print("You can't enter more than 4 numbers")
                continue
                
            print("Enter the ",num_count," numbers")
            
            for i in range(num_count):
                try :
                    n=int(input())
                    if len(game_list)!=0:
                        if n!=game_list[-1]+1:
                            print("Enter consecutive numbers")
                            continue
                    elif n!=1:
                        print("Start from one")
                        continue
                except:
                    continue
            
            print(game_list)
            if len(game_list)>=21:
                print("The computer wins")
                lose=True
                continue
            
        
if __name__=="__main__":        
    play()        