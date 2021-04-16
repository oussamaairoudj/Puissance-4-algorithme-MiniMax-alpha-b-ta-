import sys,pygame,math,time
import numpy as np

run = True
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
col,row = 7,6
radius = int(78/2)
tour = 1
player_one=0
player_two=0
count=0

def creeGrille(grille):
    for i in range(row):
        for j in range(col):
            pygame.draw.rect(screen,BLUE,(j*80,i*80+80,80,80))
            if grille[i][j] == 0:
                pygame.draw.circle(screen,BLACK,(int(j*80+80/2),int(i*80+80+80/2)),radius)
            elif grille[i][j] == 1 or grille[i][j] == 3:
                pygame.draw.circle(screen,RED,(int(j*80+80/2),int(i*80+80+80/2)),radius)
            else:
                pygame.draw.circle(screen,YELLOW,(int(j*80+80/2),int(i*80+80+80/2)),radius)
    pygame.display.update()

def insertJeton(c,tour):
    global count
    for i in range(row):
        if matrix[(row - 1) - i][c] == 0:
            matrix[(row - 1) - i][c]=tour
            count+=1
            win(matrix,1,1)
            win(matrix,2,1)
            pygame.draw.rect(screen,BLACK,(0,7*80,col*80,80))
            label1=font.render(str(player_one*100),1,RED)
            screen.blit(label1,(70,580))
            label1=font.render(str(player_two*100),1,YELLOW)
            screen.blit(label1,(450,580))
            pygame.display.update()
            if tour == 1:
                pygame.draw.circle(screen,YELLOW,(posx,int(80/2)),radius)
                return 2
            else:
                pygame.draw.circle(screen,RED,(posx,int(80/2)),radius)
                return 1
    return tour

def possible_choice(matrix):
    liste=[]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            x = 5 - j
            if matrix[x][i] == 0:
                liste.append((x,i))
                break
    return liste
def win(matrix,player,test):
    winner=0
    global player_one
    global player_two
    for i in range(3):
        for j in range(7):
            if matrix[i][j]==player and matrix[i+1][j]==player and matrix[i+2][j]==player and matrix[i+3][j]==player:
                winner+=1000
                if test == 1:
                    matrix[i][j],matrix[i+1][j],matrix[i+2][j],matrix[i+3][j]=player+2,player+2,player+2,player+2
                    if player == 1:
                        player_one+=1
                    else:
                        player_two+=1
            elif matrix[i][j]==0 and matrix[i+1][j]==player and matrix[i+2][j]==player and matrix[i+3][j]==player:
                winner+=100
            elif matrix[i][j]==0 and matrix[i+1][j]==0 and matrix[i+2][j]==player and matrix[i+3][j]==player:
                winner+=10
    for i in range(6):
        for j in range(4):
            if matrix[i][j]==player and matrix[i][j+1]==player and matrix[i][j+2]==player and matrix[i][j+3]==player:
                winner+=1000
                if test == 1:
                    matrix[i][j],matrix[i][j+1],matrix[i][j+2],matrix[i][j+3]=player+2,player+2,player+2,player+2
                    if player == 1:
                        player_one+=1
                    else:
                        player_two+=1
            elif matrix[i][j]==0 and matrix[i][j+1]==player and matrix[i][j+2]==player and matrix[i][j+3]==player:
                winner+=100
            elif matrix[i][j]==player and matrix[i][j+1]==player and matrix[i][j+2]==player and matrix[i][j+3]==0:
                winner+=100
            elif matrix[i][j]==0 and matrix[i][j+1]==0 and matrix[i][j+2]==player and matrix[i][j+3]==player:
                winner+=10
            elif matrix[i][j]==player and matrix[i][j+1]==player and matrix[i][j+2]==0 and matrix[i][j+3]==0:
                winner+=10
            elif matrix[i][j]==player and matrix[i][j+1]==0 and matrix[i][j+2]==player and matrix[i][j+3]==player:
                winner+=20
            elif matrix[i][j]==player and matrix[i][j+1]==player and matrix[i][j+2]==0 and matrix[i][j+3]==player:
                winner+=20
    for i in range(3):
        for j in range(4):
            if matrix[i][j]==player and matrix[i+1][j+1]==player and matrix[i+2][j+2]==player and matrix[i+3][j+3]==player:
                winner+=1000
                if test == 1:
                    matrix[i][j],matrix[i+1][j+1],matrix[i+2][j+2],matrix[i+3][j+3]=player+2,player+2,player+2,player+2
                    if player == 1:
                        player_one+=1
                    else:
                        player_two+=1
            elif matrix[i][j]==0 and matrix[i+1][j+1]==player and matrix[i+2][j+2]==player and matrix[i+3][j+3]==player:
                winner+=100
            elif matrix[i][j]==player and matrix[i+1][j+1]==player and matrix[i+2][j+2]==player and matrix[i+3][j+3]==0:
                winner+=100
            elif matrix[i][j]==0 and matrix[i+1][j+1]==0 and matrix[i+2][j+2]==player and matrix[i+3][j+3]==player:
                winner+=10
            elif matrix[i][j]==player and matrix[i+1][j+1]==player and matrix[i+2][j+2]==0 and matrix[i+3][j+3]==0:
                winner+=10
            elif matrix[i][j]==player and matrix[i+1][j+1]==0 and matrix[i+2][j+2]==player and matrix[i+3][j+3]==player:
                winner+=20
            elif matrix[i][j]==player and matrix[i+1][j+1]==player and matrix[i+2][j+2]==0 and matrix[i+3][j+3]==player:
                winner+=20
    for i in range(3):
        for j in range(4):
            j+=3
            if matrix[i][j]==player and matrix[i+1][j-1]==player and matrix[i+2][j-2]==player and matrix[i+3][j-3]==player:
                winner+=1000
                if test == 1:
                    matrix[i][j],matrix[i+1][j-1],matrix[i+2][j-2],matrix[i+3][j-3]=player+2,player+2,player+2,player+2
                    if player == 1:
                        player_one+=1
                    else:
                        player_two+=1
            elif matrix[i][j]==0 and matrix[i+1][j-1]==player and matrix[i+2][j-2]==player and matrix[i+3][j-3]==player:
                winner+=100
            elif matrix[i][j]==player and matrix[i+1][j-1]==player and matrix[i+2][j-2]==player and matrix[i+3][j-3]==0:
                winner+=100
            elif matrix[i][j]==0 and matrix[i+1][j-1]==0 and matrix[i+2][j-2]==player and matrix[i+3][j-3]==player:
                winner+=10
            elif matrix[i][j]==player and matrix[i+1][j-1]==player and matrix[i+2][j-2]==0 and matrix[i+3][j-3]==0:
                winner+=10
            elif matrix[i][j]==player and matrix[i+1][j-1]==0 and matrix[i+2][j-2]==player and matrix[i+3][j-3]==player:
                winner+=10
            elif matrix[i][j]==player and matrix[i+1][j-1]==player and matrix[i+2][j-2]==0 and matrix[i+3][j-3]==player:
                winner+=10
    return winner

def max_choice(matrix):
    score1=win(matrix,1,0)
    score2=win(matrix,2,0)
    score=(score2)-(score1)
    return 1,score

def max_element(mat,level,alpha,beta):
    if level == 2:
        return max_choice(mat)
    else:
        val=-100000
        pos=0
        lst=possible_choice(mat)
        for i in range(len(lst)):
            (x,y)=lst[i]
            matrix[x][y]=2
            best,value=min_element(matrix,level+1,alpha,beta)
            matrix[x][y]=0
            if val < value:
                val=value
                pos=y
            if   beta <= val:
                return pos,val
            alpha=max(alpha,val)
        return pos,val

def min_element(mat,level,alpha,beta):
    if level == 4:
        return max_choice(mat)
    else:
        val=100000
        pos=0
        lst=possible_choice(mat)
        for i in range(len(lst)):
            (x,y)=lst[i]
            matrix[x][y]=1
            best,value=max_element(matrix,level+1,alpha,beta)
            matrix[x][y]=0
            if value < val:
                val=value
                pos=y
            if val <= alpha:
                return pos,val
            beta=min(val,beta)
        return pos,val

def alphabeta(tour):
    alpha=-100000
    beta=100000
    y,z=max_element(matrix,0,alpha,beta)
    return insertJeton(y,tour)

pygame.init()
matrix=np.zeros((row, col))
pygame.display.set_caption('Alpha & Beta')
screen = pygame.display.set_mode((col*80,(row+2)*80))
font=pygame.font.SysFont("monospace",50)
creeGrille(matrix)
pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if tour == 1:
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen,BLACK,(0,0,col*80,80))
                posx=event.pos[0]
                if tour == 1:
                    pygame.draw.circle(screen,RED,(posx,int(80/2)),radius)
                else:
                    pygame.draw.circle(screen,YELLOW,(posx,int(80/2)),radius)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen,BLACK,(0,0,col*80,80))
                    posx=event.pos[0]
                    c=int(math.floor(posx/80))
                    tour=insertJeton(c,tour)
                    creeGrille(matrix)
                    if tour == 2:
                        tour=alphabeta(tour)
                        creeGrille(matrix)
    if count == 42:
        break
pygame.draw.rect(screen,BLACK,(0,0,col*80,80))
if player_one > player_two:
    label=font.render('You win',1,RED)
    screen.blit(label,(175,10))
elif player_one < player_two:
    label=font.render("Alpha & Beta Win",1,YELLOW)
    screen.blit(label,(40,10))
else:
    label=font.render('null',1,RED)
    screen.blit(label,(220,10))
pygame.display.update()
time.sleep(5)
