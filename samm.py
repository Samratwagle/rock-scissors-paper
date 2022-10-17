#author @ samrat!!!!

from tkinter import*
import pygame
from pygame import mixer
from PIL import Image,ImageTk


from random import randint

pygame.mixer.init()
mixer.music.load("back.mp3")
mixer.music.play(-1)


root= Tk()

def update():
    color="%05x" %randint(0,0xFFFFFF)
    root.config(background ='#fcba03' + color)
    root.after(1000, update)

update()

root.title("Rock Scissors Paper")
root.configure(background="#9b59b6")

#importer les images
rock_img=ImageTk.PhotoImage(Image.open("rock.png"))
sc_img=ImageTk.PhotoImage(Image.open("sc.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper.png"))


#insert picture

user_label=Label(root,image=rock_img)
comp_label=Label(root,image=sc_img)
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#♦scores
playerscore=Label(root,text=0,font=100,bg="#9b59b6",fg='white')
computerscore=Label(root,text=0,font=100,bg="#9b59b6",fg='white')
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators

user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg='white').grid(row=0,column=3)
comp_indicator=Label(root,font=50,text="computer",bg="#9b59b6",fg='white').grid(row=0,column=1)

#messages

msg=Label(root,font=80,bg="#9b59b6",fg='white')
msg.grid(row=3,column=2)

def updatemessage(x):
    msg['text']=x
    
def updateuserscore():
    score=int(playerscore["text"])
    score+=1
    playerscore["text"]=str(score)
  
        


def updatecompscore():
    score=int(computerscore["text"])
    score+=1
    computerscore["text"]=str(score)
    
    
def checkwin(player,computer):
    if player==computer:
        updatemessage("its a tie!")
    elif player=="rock":
        if computer=="paper":
            updatemessage("you loose")
            updatecompscore()
        
        else:
            updatemessage("you win")
            updateuserscore()
    elif player=="paper":
        if computer=="scissor":
            updatemessage("you loose")
            updatecompscore()
        else:
            updatemessage("you win")
            updateuserscore()
    elif player=="scissor":
        if computer=="rock":
            updatemessage('you loose')
            updatecompscore()
            
        else:
            updatemessage("you win")
            updateuserscore()
    else:
        pass            
            
            
            
    
            
       
    

    
    

choices=["rock","paper","scissor"]




    







        
            
        

def updatechoice(x):
    
    #pygame.mixer.music.load("click.mp3")
    #pygame.mixer.music.play()
    
    tone=mixer.Sound("click.mp3")
    tone.play()
    
    
    #computer
    compchoice=choices[randint(0,2)]
    
    if compchoice=="rock":
        
        comp_label.configure(image=rock_img)
        
    elif compchoice=="paper":
        comp_label.configure(image=paper_img)
    else:
        
         
        comp_label.configure(image=sc_img)
    
            
        
    if x=="rock":
        user_label.configure(image=rock_img)
        
        
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=sc_img)
        
    
    checkwin(x, compchoice)
  
        
        

#♥buttons
rock=Button(root,width=20,height=2,text="Rock",bg="#FF3E4D",fg="white",command=lambda:updatechoice("rock")).grid(row=2,column=1)
scissors=Button(root,width=20,height=2,text="Scissor",bg="green",fg="white",command=lambda:updatechoice("scissor")).grid(row=2,column=2)
paper=Button(root,width=20,height=2,text="Paper",bg="#BD0690",fg="white",command=lambda:updatechoice("paper")).grid(row=2,column=3)

root.mainloop()