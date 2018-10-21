triliza_positions=["0 0","0 1","0 2"],["1 0","1 1","1 2"],["2 0","2 1","2 2"]
triliza=["_","_","_"],["_","_","_"],["_","_","_"]

for i in range ( len(triliza)):
    print (triliza[i])

for i in range ( len(triliza_positions)):
    print (triliza_positions[i])

inputs=0
player=1
while inputs<9:
    print ("Give me the posistion of your choice, divided by space, player",player)
    x,y=input().split()
    try:
        x=int(x)
        y=int(y)
    except ValueError:
        print ("Whut???")
        continue
    if x<0 or y<0 or x>2 or y>2:
        print ("You should check the position array better mate!")
        continue
    
    if player==1:
        if triliza[x][y] == "_":
            triliza[x][y] = "X"
        else:
            print ("you can NOT play there!")
            continue
    else:
        if triliza[x][y] == "_":
            triliza[x][y] = "O"
        else:
            print ("you can NOT play there!")
            continue
    for i in range ( len(triliza)):
        print (triliza[i])
    if triliza[0][0]!="_" and triliza[0][0]==triliza[0][1] and triliza[0][0]==triliza[0][2] \
                   or triliza[0][0]!="_" and triliza[0][0]==triliza[1][1] and triliza[0][0]==triliza[2][2] \
                   or triliza[1][0]!="_" and triliza[1][0]==triliza[1][1] and triliza[1][0]==triliza[1][2] \
                   or triliza[2][0]!="_" and triliza[2][0]==triliza[2][1] and triliza[2][0]==triliza[2][2] \
                   or triliza[2][0]!="_" and triliza[2][0]==triliza[1][1] and triliza[2][0]==triliza[0][2] \
                   or triliza[0][0]!="_" and triliza[0][0]==triliza[1][0] and triliza[0][0]==triliza[2][0] \
                   or triliza[0][1]!="_" and triliza[0][1]==triliza[1][1] and triliza[0][1]==triliza[2][1] \
                   or triliza[0][2]!="_" and triliza[0][2]==triliza[1][2] and triliza[0][2]==triliza[2][2] :
        print ("Wow! player ",player,"won!!")
        break
    if player == 1:
        player=2
    else:
        player=1
    inputs+=1
    if inputs==9:
        print("Hehe, no one won!")
        
