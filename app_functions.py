import tkinter as tk

def new_icon(parent, app_name, num):

    menu_item = tk.Button(parent,
                            bg="blue", 
                            fg="white",
                            font=("Arial", 18), 
                            text=app_name, 
                            height=5, 
                            width=10, 
                            activebackground="green", 
                            relief="raised",
                            wraplength=150,
                            command=lambda: on_click(app_name),
                            name="application_"+str(num))
    print(menu_item)
    if int(num % 2) == 0:
        menu_item.grid(row=0, column=int(num/2), padx=5, pady=5)
    elif int(num % 2) == 1:
        menu_item.grid(row=1, column=int((num-1)/2), padx=5, pady=5)
        
def on_click(application_name):
    name = str(application_name).replace(" ","")
    print(f"A button was clicked - {name} - So go do something. \
        \nWrite an app that will do something wit the given information and call something cool! ")
    
    
