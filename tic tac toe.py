def board(xstate,zstate):
    #one=('X' if xstate[0] else('O' if zstate[0] else 1))
    if xstate[0]==1:
        one='X'
    elif zstate[0]==1:
        one='O'
    else:
        one=1
    
    if xstate[1]==1:
        two='X'
    elif zstate[1]==1:
        two='O'
    else:
        two=2
    
    if xstate[2]==1:
        three='X'
    elif zstate[2]==1:
        three='O'
    else:
        three=3
    
    if xstate[3]==1:
        four='X'
    elif zstate[3]==1:
        four='O'
    else:
        four=4

    if xstate[4]==1:
        five='X'
    elif zstate[4]==1:
        five='O'
    else:
        five=5

    if xstate[5]==1:
        six='X'
    elif zstate[5]==1:
        six='O'
    else:
        six=6
    
    if xstate[6]==1:
        seven='X'
    elif zstate[6]==1:
        seven='O'
    else:
        seven=7
    
    if xstate[7]==1:
        eight='X'
    elif zstate[7]==1:
        eight='O'
    else:
        eight=8
    
    if xstate[8]==1:
        nine='X'
    elif zstate[8]==1:
        nine='O'
    else:
        nine=9
    print(f"{one} | {two} | {three}")
    print(f"--|---|---")
    print(f'{four} | {five} | {six}')
    print(f'--|---|---')
    print(f'{seven} | {eight} | {nine}')

def checkwin(xstate,zstate):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win:
        if (xstate[i[0]]+xstate[i[1]]+xstate[i[2]]==3):
            return 1
        elif (zstate[i[0]]+zstate[i[1]]+zstate[i[2]]==3):
            return 0
        
    return -1
print('WECLOME TO TIC TAC TOE')
print("Follow the Instructon properly")
xstate=[0,0,0,0,0,0,0,0,0]
zstate=[0,0,0,0,0,0,0,0,0]
turn=2 #1=X's turn: 0=O's turn
board(xstate,zstate)
p=1
while p<=9:
    #board(xstate,zstate)
    if (turn%2)==0:
        print("X's turn")
        value=int(input('Choose a Number from remaining : '))
        if value>9 or value<1:
            print ("enter a proper value")
        elif zstate[value-1]!=0:
            print('Wrong input.... Type again')
            
            
        elif xstate[value-1]==0:
            xstate[value-1]=1
            board(xstate,zstate)
            turn+=1
            p+=1
    else:
        print("O's turn")
        value=int(input('Choose a Number from remaining: '))
        if value>9 or value<1: 
            print ("enter a proper value")
        elif xstate[value-1]!=0:
            print('Wrong input.... Type again')
            
            
        elif zstate[value-1]==0:
            zstate[value-1]=1
            board(xstate,zstate)
            turn+=1
            p+=1 
    
    
    
    k=checkwin(xstate,zstate)
    if k==1:
        print("X Wins!")
        break
    elif k==0:
        print("O Win!")
        break
    if p==10:  
        print("Match Tied!!! NO ONE LOOSE...")   
