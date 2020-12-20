from tkinter import Tk , Label , Entry , Button , StringVar , RAISED , RIDGE , GROOVE


root = Tk()
root.title("Second Degree Equation (ax2 + bx + c)")
root.resizable(0 , 0)
root.geometry("720x480")
root.configure(background = "#546E7A" , bd = 5+2+2+1)


def calculate(resolver):
    if resolver == "second_degree_calculator":
        try:
            a = int(sv_a.get())
            b = int(sv_b.get())
            c = int(sv_c.get())
            x = int(sv_x.get())
            result = a * (x**2) + b * x + c
            en_result.set(f"{result}")
        except:
            pass


Label(root , text = "Enter a :" , font = ("SimHei" , 15 , "bold") , bg = "#FFEB3B" , fg = "#000" , relief = RIDGE , bd = 5 ).place(x = 0 , y = 20)

sv_a = StringVar()
en01 = Entry(root , textvariable = sv_a , font = ("Courier" , 15 , "bold") , bg = "#fff" , fg = "#3E2723" , relief = GROOVE , bd = 5 , justify = "center")
en01.place(x = 120 , y = 20)

Label(root , text = "Enter b :" , font = ("SimHei" , 15 , "bold") , bg = "#FFEB3B" , fg = "#000" , relief = RIDGE , bd = 5 ).place(x = 0 , y = 100)

sv_b = StringVar()
en02 = Entry(root , textvariable = sv_b , font = ("Courier" , 15 , "bold") , bg = "#fff" , fg = "#3E2723" , relief = GROOVE , bd = 5 , justify = "center")
en02.place(x = 120 , y = 100)

Label(root , text = "Enter c :" , font = ("SimHei" , 15 , "bold") , bg = "#FFEB3B" , fg = "#000" , relief = RIDGE , bd = 5 ).place(x = 0 , y = 180)

sv_c = StringVar()
en03 = Entry(root , textvariable = sv_c , font = ("Courier" , 15 , "bold") , bg = "#fff" , fg = "#3E2723" , relief = GROOVE , bd = 5 , justify = "center")
en03.place(x = 120 , y = 180)

Label(root , text = "Enter x :" , font = ("SimHei" , 15 , "bold") , bg = "#FFEB3B" , fg = "#000" , relief = RIDGE , bd = 5 ).place(x = 0 , y = 260)

sv_x = StringVar()
en04 = Entry(root , textvariable = sv_x , font = ("Courier" , 15 , "bold") , bg = "#fff" , fg = "#3E2723" , relief = GROOVE , bd = 5 , justify = "center")
en04.place(x = 120 , y = 260)

Label(root , text = "ax2 + bx + c" , font = ("SimHei" , 15 , "bold") , bg = "#FF5722" , fg = "#fff" , relief = RIDGE , bd = 10 ).place(x = 487 , y = 5)

Label(root , text = "RESULT" , font = ("SimHei" , 35 , "bold") , bg = "#4E342E" , fg = "#fff" , relief = RIDGE , bd = 10 ).place(x = 450 , y = 75)

en_result = StringVar()
en05 = Entry(root , textvariable = en_result , font = ("Courier" , 15 , "bold") , bg = "#fff" , fg = "#3E2723" , relief = GROOVE , bd = 5 , justify = "center")
en05.place(x = 450 , y = 180 , height = 100)
en05.configure(width = 17)

btn01 = Button(root , text = "Calculate" , command = lambda : calculate ("second_degree_calculator") , font = ("SimHei" , 15 , "bold") , bg = "#F4511E" , fg = "#fff" , relief = RAISED , bd = 10)
btn01.place(x = 195 , y = 335)
btn01.configure(width = 25)

root.mainloop()