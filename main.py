import tkinter as tk 
calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = " "
    text_result.delete(1.0, "end")


    
#window
root = tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
#create buttons
buttons = ["(","*",1,2, 3, "-", 4, 5, 6, "+", 7,"8", "9", "/", ")", 0 ]
number =12
row_loc = 2
column_loc = 0
for b in buttons:
    button = tk.Button(root, text=str(buttons[number]), command=lambda n=number: add_to_calculation(str(buttons[n])), width=5, font=("Arial", 14))
    #if the buttons column
    if column_loc == 4:
        row_loc +=1
        column_loc = 1
    else:
        column_loc += 1
    button.grid(row=row_loc, column=column_loc)
    number -= 1

#final
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2)
root.mainloop()

