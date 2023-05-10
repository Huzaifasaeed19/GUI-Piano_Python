from tkinter import *
from tkinter.font import Font
import time;
import datetime
import pygame

pygame.init()
root = Tk()
root.title("Piano")
root.geometry('1352x700+0+0')

root.configure(background="white")

#main frame
ABC = Frame(root, bg="#ab967d",bd=20, relief=RIDGE)
ABC.grid()

ABC1 = Frame(ABC, bg="Black", bd=15, relief=RIDGE,height=100)
ABC1.grid()
ABC4 = Frame(ABC, bg="#ab967d", bd=10, relief=RIDGE, width=100)  #the whole division of keys
ABC4.grid()
ABC2 = Frame(ABC4, bg="#ab967d", relief=RIDGE) #the Whole Division of black keys
ABC2.grid()
ABC3 = Frame(ABC4, bg="#ab967d",  relief=RIDGE) #the whole Division of White Keys
ABC3.grid()

#============================================= BLACK KEYS =====================================================

def value_Cs(event=NONE):
    str1.set("C#")
    sound = pygame.mixer.Sound("Music_Notes\C#.mp3")
    sound.play()

def value_Ds(event=NONE):
    str1.set("D#")
    sound = pygame.mixer.Sound("Music_Notes\D#.mp3")
    sound.play()

def value_Fs(event=NONE):
    str1.set("F#")
    sound = pygame.mixer.Sound("Music_Notes\F#.mp3")
    sound.play()

def value_Gs(event=NONE):
    str1.set("G#")
    sound = pygame.mixer.Sound("Music_Notes\G#.mp3")
    sound.play()

def value_As(event=NONE):
    str1.set("A#")
    sound = pygame.mixer.Sound("Music_Notes\A#.mp3")
    sound.play()

def value_Cs1(event=NONE):
    str1.set("C#")
    sound = pygame.mixer.Sound("Music_Notes\C#1.mp3")
    sound.play()

def value_Ds1(event=NONE):
    str1.set("D#")
    sound = pygame.mixer.Sound("Music_Notes\D#1.mp3")
    sound.play()

def value_Fs1(event=NONE):
    str1.set("F#")
    sound = pygame.mixer.Sound("Music_Notes\F#1.mp3")
    sound.play()

def value_Gs1(event=NONE):
    str1.set("G#")
    sound = pygame.mixer.Sound("Music_Notes\G#1.mp3")
    sound.play()

def value_As1(event=NONE):
    str1.set("A#")
    sound = pygame.mixer.Sound("Music_Notes\A#1.mp3")
    sound.play()

def value_Cs2(event=NONE):
    str1.set("C#")
    sound = pygame.mixer.Sound("Music_Notes\C#2.mp3")
    sound.play()

def value_Ds2(event=NONE):
    str1.set("D#")
    sound = pygame.mixer.Sound("Music_Notes\D#2.mp3")
    sound.play()



#======================================== White Keys  ==========================================================

def value_C(event=NONE):
    str1.set("C")
    sound = pygame.mixer.Sound("Music_Notes\C1.mp3")
    sound.play()
    
def value_D(event=NONE):
    str1.set("D")
    sound = pygame.mixer.Sound("Music_Notes\D1.mp3")
    sound.play()
    
def value_E(event=NONE):
    str1.set("E")
    sound = pygame.mixer.Sound("Music_Notes\E1.mp3")
    sound.play()
    
def value_F(event=NONE):
    str1.set("F")
    sound = pygame.mixer.Sound("Music_Notes\F1.mp3")
    sound.play()

def value_G(event=NONE):
    str1.set("G")
    sound = pygame.mixer.Sound("Music_Notes\G1.mp3")
    sound.play()

def value_A(event=NONE):
    str1.set("A")
    sound = pygame.mixer.Sound("Music_Notes\A1.mp3")
    sound.play()

def value_B(event=NONE):
    str1.set("B")
    sound = pygame.mixer.Sound("Music_Notes\B1.mp3")
    sound.play()

def value_C1(event=NONE):
    str1.set("C")
    sound = pygame.mixer.Sound("Music_Notes\C2.mp3")
    sound.play()

def value_D1(event=NONE):
    str1.set("D")
    sound = pygame.mixer.Sound("Music_Notes\D2.mp3")
    sound.play()

def value_E1(event=NONE):
    str1.set("E")
    sound = pygame.mixer.Sound("Music_Notes\E2.mp3")
    sound.play()

def value_F1(event=NONE):
    str1.set("F")
    sound = pygame.mixer.Sound("Music_Notes\F2.mp3")
    sound.play()

def value_G1(event=NONE):
    str1.set("G")
    sound = pygame.mixer.Sound("Music_Notes\G2.mp3")
    sound.play()

def value_A1(event=NONE):
    str1.set("A")
    sound = pygame.mixer.Sound("Music_Notes\A2.mp3")
    sound.play()

def value_B1(event=NONE):
    str1.set("B")
    sound = pygame.mixer.Sound("Music_Notes\B2.mp3")
    sound.play()

def value_C2(event=NONE):
    str1.set("C")
    sound = pygame.mixer.Sound("Music_Notes\C3.mp3")
    sound.play()

def value_D2(event=NONE):
    str1.set("D")
    sound = pygame.mixer.Sound("Music_Notes\D3.mp3")
    sound.play()

def value_E2(event=NONE):
    str1.set("E")
    sound = pygame.mixer.Sound("Music_Notes\E3.mp3")
    sound.play()

#======================================== Lable With Title ==========================================================
title="CGA Project by 20BSCS039 & 20BSCS050"
Label(ABC1,text=title, font=('Ink Free',23,"bold"),padx=8,pady=0, bd=4, bg="black", fg="White", 
justify=CENTER).grid(row=0,column=0, columnspan=11)

#======================================== Display Sections on Top==========================================================
str1=StringVar()
str1.set("Musical Notes")
Date1=StringVar()
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

txtDate=Entry(ABC1,text="Musical", font=('vivaldi',18), bd=34, bg="black", fg="white", width=29,
justify=CENTER).grid(row=1,column=0,pady=1)


txtDisplay=Entry(ABC1,textvariable=str1, font=('Lucida Handwriting',18, "bold"), bd=34, bg="black", fg="white", width=29,
justify=CENTER).grid(row=1,column=1,pady=1)


txtTime=Entry(ABC1,text="Notes", font=('vivaldi',18), bd=34, bg="black", fg="white", width=29,
justify=CENTER).grid(row=1,column=2,pady=1)

#======================================== Piano keys ==========================================================

btnCs=Button(ABC2,height=5,width=4 , bd=4 ,text="C#", font=('Times',18,), bg="Black",fg="white" , command=value_Cs)
btnCs.grid(row=0,column=0,padx=5, pady=5)
btnDs=Button(ABC2,height=5,width=4 , bd=4 ,text="D#", font=('Times',18,), bg="Black",fg="white", command=value_Ds)
btnDs.grid(row=0,column=2,padx=5, pady=5)


btnSpace2=Button(ABC2,state=DISABLED ,height=4,width=9 , bg="#ab967d",relief=FLAT ,fg="white")
btnSpace2.grid(row=0,column=3,padx=0, pady=0)


btnFs=Button(ABC2,height=5,width=4 , bd=4 ,text="F#", font=('Times',18,), bg="Black",fg="white" ,command=value_Fs )
btnFs.grid(row=0,column=4,padx=5, pady=5)
btnGs=Button(ABC2,height=5,width=4 , bd=4 ,text="G#", font=('Times',18,), bg="Black",fg="white" ,command=value_Gs )
btnGs.grid(row=0,column=6,padx=5, pady=5)
btnAs=Button(ABC2,height=5,width=4 , bd=4 ,text="A#", font=('Times',18,), bg="Black",fg="white", command=value_As)
btnAs.grid(row=0,column=8,padx=5, pady=5)


btnSpace5=Button(ABC2,state=DISABLED ,height=4,width=9 , bg="#ab967d",relief=FLAT ,fg="white")
btnSpace5.grid(row=0,column=9,padx=0, pady=0)


btnCs1=Button(ABC2,height=5,width=4 , bd=4 ,text="C#", font=('Times',18,), bg="Black",fg="white", command=value_Cs1)
btnCs1.grid(row=0,column=10,padx=5, pady=5)
btnDs1=Button(ABC2,height=5,width=4 , bd=4 ,text="D#", font=('Times',18,), bg="Black",fg="white", command=value_Ds1)
btnDs1.grid(row=0,column=12,padx=5, pady=5)

btnSpace5=Button(ABC2,state=DISABLED ,height=4,width=9 , bg="#ab967d",relief=FLAT ,fg="white")
btnSpace5.grid(row=0,column=13,padx=0, pady=0)

btnFF1=Button(ABC2,height=5,width=4 , bd=4 ,text="F#", font=('Times',18,), bg="Black",fg="white", command=value_Fs1)
btnFF1.grid(row=0,column=14,padx=5, pady=5)
btnGG1=Button(ABC2,height=5,width=4 , bd=4 ,text="G#", font=('Times',18,), bg="Black",fg="white", command=value_Gs1)
btnGG1.grid(row=0,column=16,padx=5, pady=5)
btnBB1=Button(ABC2,height=5,width=4 , bd=4 ,text="A#", font=('Times',18,), bg="Black",fg="white", command=value_As1)
btnBB1.grid(row=0,column=18,padx=5, pady=5)


btnSpace9=Button(ABC2,state=DISABLED ,height=4,width=9 , bg="#ab967d",relief=FLAT ,fg="white")
btnSpace9.grid(row=0,column=19,padx=0, pady=0)
# akdgkak

btnCs1=Button(ABC2,height=5,width=4 , bd=4 ,text="C#", font=('Times',18,), bg="Black",fg="white", command=value_Cs2)
btnCs1.grid(row=0,column=20,padx=5, pady=5)
btnDs1=Button(ABC2,height=5,width=4 , bd=4 ,text="D#", font=('Times',18,), bg="Black",fg="white", command=value_Ds2)
btnDs1.grid(row=0,column=22,padx=5, pady=5)


btnSpace9=Button(ABC2,state=DISABLED ,height=4,width=9 , bg="#ab967d",relief=FLAT ,fg="white")
btnSpace9.grid(row=0,column=19,padx=0, pady=0)

#==================================================================================================
btnC=Button(ABC3,height=8,width=4 , bd=4 ,text="C", font=('Times',18,), bg="white",fg="Black" ,command=value_C)
btnC.grid(row=0,column=0,padx=5, pady=5)
btnD=Button(ABC3,height=8,width=4 , bd=4 ,text="D", font=('Times',18,), bg="white",fg="Black" ,command=value_D)
btnD.grid(row=0,column=1,padx=5, pady=5)
btnE=Button(ABC3,height=8,width=4 , bd=4 ,text="E", font=('Times',18,), bg="white",fg="Black" ,command=value_E)
btnE.grid(row=0,column=2,padx=5, pady=5)
btnF=Button(ABC3,height=8,width=4 , bd=4 ,text="F", font=('Times',18,), bg="white",fg="Black" ,command=value_F)
btnF.grid(row=0,column=3,padx=5, pady=5)

btnG=Button(ABC3,height=8,width=4 , bd=4 ,text="G", font=('Times',18,), bg="white",fg="Black", command=value_G)
btnG.grid(row=0,column=4,padx=5, pady=5)
btnA=Button(ABC3,height=8,width=4 , bd=4 ,text="A", font=('Times',18,), bg="white",fg="Black", command=value_A)
btnA.grid(row=0,column=5,padx=5, pady=5)
btnB=Button(ABC3,height=8,width=4 , bd=4 ,text="B", font=('Times',18,), bg="white",fg="Black", command=value_B)
btnB.grid(row=0,column=6,padx=5, pady=5)
btnC1=Button(ABC3,height=8,width=4 , bd=4 ,text="C", font=('Times',18,), bg="white",fg="Black", command=value_C1)
btnC1.grid(row=0,column=7,padx=5, pady=5)

btnD1=Button(ABC3,height=8,width=4 , bd=4 ,text="D", font=('Times',18,), bg="white",fg="Black", command=value_D1)
btnD1.grid(row=0,column=8,padx=5, pady=5)
btnE1=Button(ABC3,height=8,width=4 , bd=4 ,text="E", font=('Times',18,), bg="white",fg="Black", command=value_E1)
btnE1.grid(row=0,column=9,padx=5, pady=5)
btnF1=Button(ABC3,height=8,width=4 , bd=4 ,text="F", font=('Times',18,), bg="white",fg="Black", command=value_F1)
btnF1.grid(row=0,column=10,padx=5, pady=5)
btnG1=Button(ABC3,height=8,width=4 , bd=4 ,text="G", font=('Times',18,), bg="white",fg="Black", command=value_G1)
btnG1.grid(row=0,column=11,padx=5, pady=5)
btnA1=Button(ABC3,height=8,width=4 , bd=4 ,text="A", font=('Times',18,), bg="white",fg="Black", command=value_A1)
btnA1.grid(row=0,column=12,padx=5, pady=5)
btnB1=Button(ABC3,height=8,width=4 , bd=4 ,text="B", font=('Times',18,), bg="white",fg="Black", command=value_B1)
btnB1.grid(row=0,column=13,padx=5, pady=5)
btnC2=Button(ABC3,height=8,width=4 , bd=4 ,text="C", font=('Times',18,), bg="white",fg="Black", command=value_C2)
btnC2.grid(row=0,column=14,padx=5, pady=5)

btnD2=Button(ABC3,height=8,width=4 , bd=4 ,text="D", font=('Times',18,), bg="white",fg="Black", command=value_D2)
btnD2.grid(row=0,column=15,padx=5, pady=5)
btnE2=Button(ABC3,height=8,width=4 , bd=4 ,text="E", font=('Times',18,), bg="white",fg="Black", command=value_E2)
btnE2.grid(row=0,column=16,padx=5, pady=5)

#===================================== BINDING FOR BLACK KEYS =============================================================
root.bind("<Q>",value_Cs)
root.bind("<W>",value_Ds)
root.bind("<E>",value_Fs)
root.bind("<R>",value_Gs)
root.bind("<T>",value_As)
root.bind("<Y>",value_Cs1)
root.bind("<U>",value_Ds1)

root.bind("<q>",value_Cs)
root.bind("<w>",value_Ds)
root.bind("<e>",value_Fs)
root.bind("<r>",value_Gs)
root.bind("<t>",value_As)
root.bind("<y>",value_Cs1)
root.bind("<u>",value_Ds1)
root.bind("<i>",value_Fs1)
root.bind("<o>",value_Gs1)
root.bind("<p>",value_As1)
root.bind("<[>",value_Cs2)
root.bind("<]>",value_Ds2)
#==================================== BINDING FOR WHITE KEYS ==============================================================

root.bind("<a>",value_C)
root.bind("<s>",value_D)
root.bind("<d>",value_E)
root.bind("<f>",value_F)
root.bind("<g>",value_G)
root.bind("<h>",value_A)
root.bind("<j>",value_B)
root.bind("<k>",value_C1)
root.bind("<l>",value_D1)
root.bind("<;>",value_E1)
root.bind("<'>",value_F1)
root.bind("<\>",value_G1)
root.bind("<z>",value_A1)
root.bind("<x>",value_B1)
root.bind("<c>",value_C2)
root.bind("<v>",value_D2)
root.bind("<b>",value_E2)

root.bind("<A>",value_C)
root.bind("<S>",value_D)
root.bind("<D>",value_E)
root.bind("<F>",value_F)
root.bind("<G>",value_G)
root.bind("<H>",value_A)
root.bind("<J>",value_B)
root.bind("<K>",value_C1)
root.bind("<L>",value_D1)
root.bind("<Z>",value_A1)
root.bind("<X>",value_B1)
root.bind("<C>",value_C2)
root.bind("<V>",value_D2)
root.bind("<B>",value_E2)
#==================================================================================================

root.mainloop()