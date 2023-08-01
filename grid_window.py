menus = ["Netflix", "Prime", "Some Gucci lights", "Central Heating", "Kids stuff", "Shopping apps", "Weather", "Time", "Calendar", "News and Sports", ]

def grid_window(parent):

    import app_functions

    num = 0
    
    for name in menus:
        app_functions.new_icon(parent, name, num)
        #print(name)
        num += 1
        
