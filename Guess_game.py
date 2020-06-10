import tkinter
import random
root = tkinter.Tk()
root.title("Guess Game")
root.configure(bg='#add8e6')
heading = tkinter.Label(root, text = "Welcome to the Game" , bg = "white")
heading.place(relx=0.5, rely=0.1, anchor='center')
root.geometry("500x500")

computer_guess = random.randint(1,10)

def check():
    
    user_guess = int(value.get())
    if(computer_guess > user_guess):
        msg = "Guess a higher value"
    elif(computer_guess < user_guess):
        msg = "Guess a lower value"
    elif(computer_guess == user_guess):
        msg = "Yaay!! You win!!"
    else :
        msg = "Please try again"    
    result["text"] = msg
    value.delete(0,5)

def reset():
    global computer_guess
    computer_guess = random.randint(1,10)
    result["text"] = " You are ready to go again!"
    value.delete(0,5)

#text
heading2 = tkinter.Label(root, text = "Let's start the game!" , fg = "blue" , bg = "white")
heading2.place(relx=0.5, rely=0.2, anchor='center')

result = tkinter.Label(root, text = "Guess a number between 1 and 10 ." , fg = "blue" ,bg = "white")
result.place(relx=0.5, rely=0.3, anchor='center')


#text2

value = tkinter.Entry(root, width = 4 ,bg="white")
value.place(relx=0.5, rely=0.4, anchor='center')

buttoncheck = tkinter.Button(root, text = "CHECK" , fg = "green" , command = check , bg="white")
buttoncheck.place(relx=0.3, rely=0.5, anchor='center')

buttonreset = tkinter.Button(root, text = "RESET" , fg = "red" , command = reset , bg = "white")
buttonreset.place(relx=0.7, rely=0.5, anchor='center')
root.mainloop()