from tkinter import *
import random
root=Tk()
root.title("SORT RANDOM LIST")
root.geometry("9999x9999")
root.configure(bg="cyan")

alpha_list = ["A", "B", "C", "D", "E","F", "G", "H", "I", "J","K", "L", "M", "N", "O","P", "Q", "R", "S", "T","U", "V", "W", "X", "Y","Z"]
print(alpha_list)
random = Label(root)

def randomword():
    randomno = random.randint(0,25)
    print(randomno)
    random2 = alpha_list[randomno]
    print("Random Word is", random2)
    randomno = random.sample(range(0,10),5)
    random["text"] = str(random2)
    randomno.sort()
    
btn1 = Button(root)
btn1 = Button(root, text = "Generate Random Word", command=randomword)    
btn1.place(relx = 0.5,rely = 0.5, anchor = CENTER)

random.place(relx=0.5,rely=0.6, anchor=CENTER)
    
root.mainloop()