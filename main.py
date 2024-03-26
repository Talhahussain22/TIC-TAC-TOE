def create_board(row):
    for i in range(3):
        print("\t\t",end="")
        print(" | ".join(row[i]))


def create_user():
    user1=input("Enter the char for user1 (X or O):").upper()
    user2=input("Enter the char for user2 (X or O):").upper()
    return user1,user2


def is_board_full():
    for i in range(3):
        for j in range(3):
            if row[i][j]=="_":
                return 0
    return 1

def winner(i,char):
    winning_combinations=[[[0,0],[1,0],[2,0]],[[0,0],[0,1],[0,2]],[[0,0],[1,1],[2,2]],[[2,0],[2,2],[2,2]],[[1,0],[1,1],[1,2]],[[0,2],[1,2],[2,2]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,0]]]
    symbol=char[i]
    for j in winning_combinations:
        for k in j:
            if row[k[0]][k[1]]!="_"+symbol:
                break
        else:
            return i

def match_box(l):
    while True:
        for i in range(2):
            while True:
                box=int(input(f"Enter a box number(1-9) user{i+1}:"))
                match box:
                    case 1:
                        
                        if  row[0][0]=='_':
                            row[0][0]+=l[i]
                            break
                        else:
                            print("Already filled!")    
                    case 2:
                        if  row[0][1]=='_':
                            row[0][1]+=l[i]
                            break
                        else:
                            print("Already filled!")
                    case 3:
                        if  row[0][2]=='_':
                            row[0][2]+=l[i]
                            break
                        else:
                            print("Already filled!")
                    case 4:
                        if  row[1][0]=='_': 
                            row[1][0]+=l[i]
                            break
                        else:
                            print("Already filled!")
                    case 5:
                        if  row[1][1]=='_': 
                            row[1][1]+=l[i]
                            break
                        else:
                            print("Already filled!")
                    case 6:
                        if  row[1][2]=='_': 
                            row[1][2]+=l[i]
                            break
                        else:
                            print("Already filled!")
                    case 7:
                        if  row[2][0]=='_':
                            row[2][0]+=l[i]
                            break
                        else:
                            print("Already filled!")
                    case 8:
                        if  row[2][1]=='_':
                            row[2][1]+=l[i]
                            break
                        else:
                            print("Already filled!")
                    case 9:
                        if  row[2][2]=='_':
                            row[2][2]+=l[i]
                            break
                        else:
                            print("Already filled!")
            create_board(row)
            
            win=winner(i,char)
            if win==i:
                print(f"User{i+1} has won the game!")
                quit()
            check=is_board_full()
            if check==1:
                print("Game TIE!")
                return 0

print("_______________________________________")
print()
print("\tWELCOME TO TIC TOC TIE!")
print("_______________________________________")
print()
input("Press any key to continue!")
print()
row=[["_" for _ in range(3)] for _ in range(3)]     
char=create_user()
match_box(char)


