#i want to make a stone paper scissors game :
#stone=1
#paper=0
#scissors=-1


import random

values={"s":1, "p":0, "sc":-1}
names={1:"stone", 0:"paper", -1:"scissor"}

you=input("Enter the choice:")
compchoice=random.choice([1,0,-1])

yourvalue=values[you]

print(f"your choice:{names[yourvalue]}\ncomputers chioce:{names[compchoice]}")

if compchoice==yourvalue:
    print("its draw")

else:

    if compchoice==1 and yourvalue==0:
        print("you win")
   
    if compchoice==1 and yourvalue==-1:
        print("you lose")
   
    if compchoice==0 and yourvalue==1:
        print("you lose")
   
    if compchoice==0 and yourvalue==-1:
        print("you win")
   
    if compchoice==-1 and yourvalue==1:
        print("you win")
   
    if compchoice==-1 and yourvalue==0:
        print("you lose")
   
