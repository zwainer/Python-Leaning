from tkinter import *

# defining yung window parang yung mismong square

bintana = Tk()

 

# to show text, use label widget 
sex = Label(bintana,
             text="Hello po sa inyong lahat <3")

sex2 = Label(bintana,
             text="Masarap ba ang missionary?")


sex.grid(row=0,
         column=0

         )

sex2.grid(row=1,
         column=0

            )



bintana.mainloop()
