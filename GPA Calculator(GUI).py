from tkinter import *
#import tkinter
root = Tk()

Label_1 = Label(root, text = "How many credit hours have you done and got..?" )
Label_1.grid(column = 0 , row = 0 , columnspan = 2 ) 

A_plus = Entry(root)
A_plus.grid(column = 1 , row = 1  )
A_plus.insert(0, 0)

A = Entry(root)
A.grid(column = 1 , row = 2 )
A.insert(0, 0)

B_plus = Entry(root)
B_plus.grid(column = 1 , row = 3 )
B_plus.insert(0, 0)

B = Entry(root)
B.grid(column = 1 , row = 4 )
B.insert(0, 0)

C_plus = Entry(root)
C_plus.grid(column = 1 , row = 5 )
C_plus.insert(0, 0)

C = Entry(root)
C.grid(column = 1 , row = 6 )
C.insert(0, 0)

D_plus = Entry(root)
D_plus.grid(column = 1 , row = 7 )
D_plus.insert(0, 0)

D = Entry(root)
D.grid(column = 1 , row = 8 )
D.insert(0, 0)

F = Entry(root)
F.grid(column = 1 , row = 9 )
F.insert(0, 0)

DN = Entry(root)
DN.grid(column = 1 , row = 10 )
DN.insert(0, 0)


Label_Ap = Label(root, text = "A+" )
Label_Ap.grid(column = 0 , row = 1 )
Label_A = Label(root, text = "A" )
Label_A.grid(column = 0 , row = 2 )
Label_Bp = Label(root, text = "B+" )
Label_Bp.grid(column = 0 , row = 3 )
Label_B = Label(root, text = "B" )
Label_B.grid(column = 0 , row = 4 )
Label_Cp = Label(root, text = "C+" )
Label_Cp.grid(column = 0 , row = 5 )
Label_C = Label(root, text = "C" )
Label_C.grid(column = 0 , row = 6 )
Label_Dp = Label(root, text = "D+" )
Label_Dp.grid(column = 0 , row = 7 )
Label_D = Label(root, text = "D" )
Label_D.grid(column = 0 , row = 8 )
Label_F = Label(root, text = "F" )
Label_F.grid(column = 0 , row = 9 )
Label_DN = Label(root, text = "DN" )
Label_DN.grid(column = 0 , row = 10 )

def calculate_GPA():
    total_hours=(int(A_plus.get()) + int(A.get()) + int(B_plus.get()) + int(B.get()) + int(C_plus.get()) + int(C.get()) + int(D_plus.get()) + int(D.get()) + int(F.get()) + int(DN.get()))
    weight_A_plus = int(A_plus.get()) * 4
    weight_A = int(A.get()) *3.75
    weight_B_plus = int(B_plus.get()) *3.5
    weight_B = int(B.get()) *3
    weight_C_plus = int(C_plus.get()) *2.5
    weight_C = int(C.get()) *2
    weight_D_plus = int(D_plus.get()) *1.5
    weight_D = int(D.get()) *1
    weight_F = int(F.get()) *0
    weight_DN = int(DN.get()) *0
    total_weight=(weight_A_plus + weight_A + weight_B_plus + weight_B + weight_C_plus + weight_C + weight_D_plus + weight_D + weight_F + weight_DN)
    GPA = round((total_weight)/(total_hours) ,3 )
    Label_GPA = Label(root, text = "Your GPA is "+ str(GPA)+" out of 4")
    Label_GPA.grid(column = 2 , row = 3) 
    return GPA

Button_1 = Button(root, text="Calculate GPA",command=calculate_GPA , padx = 20 , pady = 5 )
Button_1.grid(column = 2 , row = 1)

root.mainloop()
