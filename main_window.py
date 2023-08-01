def test():
    print("Hello world")

def app():
    import tkinter as tk
    import grid_window

    #create root window
    root = tk.Tk()
    root.title("PC Monitor GUI")
    root.resizable(0,0)
    root.attributes('-fullscreen',True)
    root.config(bg="black")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # print(f"Screen Resolution: {screen_width} by {screen_height}")

    #create the items for the app
    frame0 = tk.Frame(root, bg="black")
    frame0.grid(sticky="we")
    temp1 = tk.Label(frame0, text=f"Resolution: {screen_width} by {screen_height}", font=("Arial", 12), bg="White", fg="black")
    temp2 = tk.Button(frame0, text="Press to Close", font=("Arial", 18), bg="White", fg="black", command=exit, cursor="circle")
    welcome = tk.Label(frame0, bg="red", fg="black", text="Please select an option to start", font=("Helvetica",18), height=2)
    scrollbar = tk.Scrollbar(frame0, orient="horizontal", bg="red")
    frame1 = tk.Frame(scrollbar, bg="pink")

    #place the items for the app
    temp1.grid(row=0, column=2,)#delete when no longer needed
    temp2.grid(row=0, column=1,)#delete when no longer needed
    welcome.grid(row=0, column=0, sticky="we")
    scrollbar.grid(row=1, column=0, columnspan=3, sticky="we")
    frame1.grid(row=0, column=0, sticky="we")
    grid_window.grid_window(frame1)

    root.mainloop()