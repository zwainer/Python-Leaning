from tkinter import *

fuckable = Tk()

fuckable.title("Hello To the World Help me <3")

fuckable.geometry("600x800")
    # Itong fucntion na to is tinitignan nya kung may 
    #     nagpindot ng check sa checkbox
def shit():
    if (sex.get()== 1):

        Slap_Me_Harder.configure('Times New Roman', 30)
        print ("fuck you")

    else:

        print("Tang ina mo pa din")

# This part set the window




sex = IntVar()

fuckable.configure(
                    bg= 'black'

                    )

Slap_Me_Harder = Checkbutton(fuckable, 
                             text="CLICK ME NO VIRUS",
                             variable  = sex,
                             onvalue= 1, 
                             offvalue=0,
                             command = shit,
                             font=('Times New Roman', 50),
                             fg = "yellow",
                             bg ='black'
                             
                            )

Slap_Me_Harder.pack()

fuckable.mainloop()


