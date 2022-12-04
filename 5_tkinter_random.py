# Tkinter GUI Interface
from tkinter import *
from tkinter import messagebox

# Others
import time
import random

# Global Variables
ls = []
ls_key = []
ls_value = []
dict_in = {}
dict_out = {}
dict_show = {}

# Open csv file to retrieve data and place all in dictionary
with open("ctd_planning.csv","r") as f:
    ls = f.read().split("\n")
    ls_key = ls[0].split(",")
    # Zip the key-value pairs in dict_in for each planning, and combine all inside dict_out
    for i in range(1,len(ls)):
        ls_value = ls[i].split(",")
        dict_in = dict(zip(ls_key,ls_value))
        dict_out[i] = dict_in
    f.close()



##### Functions Defined ######

# For each filter button clicked, create window2 to display the filtering options
def filtering(category):
    global window2, dict_show
    window2 = Toplevel(window)
    window2.title(category.capitalize())
    if category == 'pax' or category == 'time':
        if category == 'pax':
            label_2 = Label(window2, text="Input number between 2 - 10")
        elif category == 'time':
            label_2 = Label(window2, text="Input number between 0.5 - 16")
        entry_2 = Entry(window2, width=10)
        btn_2 = Button(window2, text="Done", width=10, height=2, command=lambda: filtering2(category, entry_2.get()))

        label_2.grid(row=0, column=0, padx=5, pady=5)
        entry_2.grid(row=1, column=0, padx=5, pady=5)
        btn_2.grid(row=2, column=0, padx=5, pady=5)
    elif category == 'occasion':
        label_occasion2 = Label(window2, text="Choose one")
        btn_occasion20 = Button(window2, text="None", width=10, height=2, command=lambda: filtering2(category, ""))
        btn_occasion21 = Button(window2, text="Date", width=10, height=2, command=lambda: filtering2(category, btn_occasion21["text"]))
        btn_occasion22 = Button(window2, text="Friends", width=10, height=2, command=lambda: filtering2(category, btn_occasion22["text"]))

        label_occasion2.grid(row=0, column=0, padx=5, pady=5)
        btn_occasion20.grid(row=1, column=0, padx=5, pady=5)
        btn_occasion21.grid(row=2, column=0, padx=5, pady=5)
        btn_occasion22.grid(row=3, column=0, padx=5, pady=5)
    elif category == 'location':
        label_location2 = Label(window2, text="Choose one")
        btn_location20 = Button(window2, text="None", width=10, height=2, command=lambda: filtering2(category, ""))
        btn_location21 = Button(window2, text="Sentosa", width=10, height=2, command=lambda: filtering2(category, btn_location21["text"]))
        btn_location22 = Button(window2, text="Home", width=10, height=2, command=lambda: filtering2(category, btn_location22["text"]))
        btn_location23 = Button(window2, text="North", width=10, height=2, command=lambda: filtering2(category, btn_location23["text"]))
        btn_location24 = Button(window2, text="Central", width=10, height=2, command=lambda: filtering2(category, btn_location24["text"]))
        btn_location25 = Button(window2, text="East", width=10, height=2, command=lambda: filtering2(category, btn_location25["text"]))
        btn_location26 = Button(window2, text="West", width=10, height=2, command=lambda: filtering2(category, btn_location26["text"]))

        label_location2.grid(row=0, column=0, padx=5, pady=5)
        btn_location20.grid(row=0, column=1, padx=5, pady=5)
        btn_location21.grid(row=1, column=0, padx=5, pady=5)
        btn_location22.grid(row=1, column=1, padx=5, pady=5)
        btn_location23.grid(row=2, column=0, padx=5, pady=5)
        btn_location24.grid(row=2, column=1, padx=5, pady=5)
        btn_location25.grid(row=3, column=0, padx=5, pady=5)
        btn_location26.grid(row=3, column=1, padx=5, pady=5)
    elif category == 'price':
        label_price2 = Label(window2, text="Choose one")
        btn_price20 = Button(window2, text="None", width=10, height=2, command=lambda: filtering2(category, ""))
        btn_price21 = Button(window2, text="$", width=10, height=2, command=lambda: filtering2(category, btn_price21["text"]))
        btn_price22 = Button(window2, text="$$", width=10, height=2, command=lambda: filtering2(category, btn_price22["text"]))
        btn_price23 = Button(window2, text="$$$", width=10, height=2, command=lambda: filtering2(category, btn_price23["text"]))
        btn_price24 = Button(window2, text="$$$$", width=10, height=2, command=lambda: filtering2(category, btn_price24["text"]))

        label_price2.grid(row=0, column=0, padx=5, pady=5)
        btn_price20.grid(row=0, column=1, padx=5, pady=5)
        btn_price21.grid(row=1, column=0, padx=5, pady=5)
        btn_price22.grid(row=1, column=1, padx=5, pady=5)
        btn_price23.grid(row=2, column=0, padx=5, pady=5)
        btn_price24.grid(row=2, column=1, padx=5, pady=5)
    elif category == 'clear':
        filtering2(category, "")
    elif category == 'random':
        window2.destroy()
        keys = list(dict_show.keys())
        random.shuffle(keys)
        display2(keys[0])

# After inputing a valid input for filtering, change the filter buttons names according to the filtered option chosen
# If no input was entered, leave it as empty string
# Destroys the window afterwards
def filtering2(category, input2):
    global btn_pax, btn_time, btn_occasion, btn_location, btn_price
    if input2 != "":
        if category == 'pax' or category == 'time':
            try:
                float(input2)
                if category == 'pax':
                    if 2 <= float(input2) <= 10:
                        btn_pax["text"] = "{}\n{}".format(category.capitalize(), input2)
                    else:
                        messagebox.showwarning("Warning", "Out of Range, Try Again")
                        window2.destroy()
                elif category == 'time':
                    if 0.5 <= float(input2) <= 16:
                        btn_time["text"] = "{} in hours\n{}".format(category.capitalize(), input2)
                    else:
                        messagebox.showwarning("Warning", "Out of Range, Try Again")
                        window2.destroy()
            except:
                messagebox.showwarning("Warning", "Wrong Input, Try Again")
                window2.destroy()
        elif category == 'occasion':
            btn_occasion["text"] = "{}\n{}".format(category.capitalize(), input2)
        elif category == 'location':
            btn_location["text"] = "{}\n{}".format(category.capitalize(), input2)
        elif category == 'price':
            btn_price["text"] = "{}\n{}".format(category.capitalize(), input2)
    else:
        if category == 'pax':
            btn_pax["text"] = category.capitalize()
        elif category == 'time':
            btn_time["text"] = "{} in hours".format(category.capitalize())
        elif category == 'occasion':
            btn_occasion["text"] = category.capitalize()
        elif category == 'location':
            btn_location["text"] = category.capitalize()
        elif category == 'price':
            btn_price["text"] = category.capitalize()
        if category == 'clear':
            btn_pax["text"] = "Pax"
            btn_time["text"] = "Time in hours"
            btn_occasion["text"] = "Occasion"
            btn_location["text"] = "Location"
            btn_price["text"] = "Price"

    window2.destroy()
    display()

# Create frame_display which is destroyable for updating the informations to display
# Display all the information as individual buttons after filtering
def display():
    global frame2, frame_display, btn_pax, btn_time, btn_occasion, btn_location, btn_price
    global dict_show
    frame_display.destroy()
    frame_display = Frame(frame2, background="green")
    frame_display.pack()

    canvas = Canvas(frame_display, background="green", width=625, height=500)
    vsb = Scrollbar(frame_display, orient="vertical", command=canvas.yview)
    hsb = Scrollbar(frame_display, orient="horizontal", command=canvas.xview)

    frame_display.grid_rowconfigure(0, weight=1)
    frame_display.grid_columnconfigure(0, weight=1)
    canvas.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
    canvas.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    userpax = btn_pax["text"].replace("Pax","").replace("\n","")
    userOccasion = btn_occasion["text"].replace("Occasion","").replace("\n","")
    userLocation = btn_location["text"].replace("Location","").replace("\n","")
    usertime = btn_time["text"].replace("Time in hours","").replace("\n","")
    userPrice = btn_price["text"].replace("Price","").replace("\n","")

    filterpax = userpax != ""
    filterOccasion = userOccasion != ""
    filterLocation = userLocation != ""
    filtertime = usertime != ""
    filterPrice = userPrice != ""

    dict_show = {}
    for i in range(1,len(dict_out)):
        appendd = True
        if filterpax:
            if float(userpax) <= float(dict_out[i]['pax_min']) or float(userpax) >= float(dict_out[i]['pax_max']):
                appendd = False
        if filterOccasion:
            if userOccasion not in dict_out[i]['Occasion']:
                appendd = False
        if filterLocation:
            if userLocation not in dict_out[i]['Location']:
                appendd = False
        if filtertime:
            if float(usertime) <= float(dict_out[i]['time_min']) or float(usertime) >= float(dict_out[i]['time_max']):
                appendd = False
        if filterPrice:
            if userPrice != dict_out[i]['Price']:
                appendd = False
        if appendd:
            dict_show[i] = dict_out[i]

    label_display = Label(frame_display, text=" PLACES TO GO : ", font=("Arial", 8, "bold"))
    canvas.create_window(260, 0, anchor="nw", window=label_display)

    i = 0
    j = 25
    dict_btn = {}
    for key in dict_show:
        def func(x=key):
            return display2(x)
        dict_btn[key] = Button(canvas, text=dict_show[key]['Title'], width=15, height=2, command=func)
        canvas.create_window(i, j, anchor="nw", window=dict_btn[key])
        i+=125
        if i>=600:
            i = 0
            j+=50

    canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

# Display more information about the planning
def display2(key):
    window3 = Toplevel(window)
    window3.title(dict_out[key]['Title'])

    label_30 = Label(window3, text="Title : ", font=("Arial", 8, "bold"))
    label_31 = Label(window3, text="Pax : ", font=("Arial", 8, "bold"))
    label_32 = Label(window3, text="Occasion : ", font=("Arial", 8, "bold"))
    label_33 = Label(window3, text="Location : ", font=("Arial", 8, "bold"))
    label_34 = Label(window3, text="Time : ", font=("Arial", 8, "bold"))
    label_35 = Label(window3, text="Price : ", font=("Arial", 8, "bold"))
    label_36 = Label(window3, text="{}".format(dict_out[key]['Title']))
    label_37 = Label(window3, text="{} - {} pax".format(dict_out[key]['pax_min'], dict_out[key]['pax_max']))
    label_38 = Label(window3, text="{}".format(dict_out[key]['Occasion']))
    label_39 = Label(window3, text="{}".format(dict_out[key]['Location']))
    label_40 = Label(window3, text="{} - {} hrs".format(dict_out[key]['time_min'], dict_out[key]['time_max']))
    label_41 = Label(window3, text="{}".format(dict_out[key]['Price']))

    label_30.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    label_31.grid(row=1, column=0, padx=5, pady=5, sticky='w')
    label_32.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    label_33.grid(row=3, column=0, padx=5, pady=5, sticky='w')
    label_34.grid(row=4, column=0, padx=5, pady=5, sticky='w')
    label_35.grid(row=5, column=0, padx=5, pady=5, sticky='w')
    label_36.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    label_37.grid(row=1, column=1, padx=5, pady=5, sticky='w')
    label_38.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    label_39.grid(row=3, column=1, padx=5, pady=5, sticky='w')
    label_40.grid(row=4, column=1, padx=5, pady=5, sticky='w')
    label_41.grid(row=5, column=1, padx=5, pady=5, sticky='w')



##### App Design #####

# Creating Window ############################################################################
window = Tk()
window.title('AI Stead Mai')
window.geometry("800x400")

# Create Frame 1: Filter Buttons #############################################################
frame1 = Frame(window, background="red")
frame1.pack(side=LEFT, anchor=NW)

label_filtering = Label(frame1, text="FILTERS : ", font=("Arial", 8, "bold"))
btn_pax = Button(frame1, text="Pax", font=("Arial", 8, "bold"), width=15, height=2, command=lambda: filtering('pax'))
btn_occasion = Button(frame1, text="Occasion", font=("Arial", 8, "bold"), width=15, height=2, command=lambda: filtering('occasion'))
btn_location = Button(frame1, text="Location", font=("Arial", 8, "bold"), width=15, height=2, command=lambda: filtering('location'))
btn_time = Button(frame1, text="Time in hours", font=("Arial", 8, "bold"), width=15, height=2, command=lambda: filtering('time'))
btn_price = Button(frame1, text="Price", font=("Arial", 8, "bold"), width=15, height=2, command=lambda: filtering('price'))
btn_clear = Button(frame1, text="CLEAR FILTER", font=("Arial", 8, "bold"), width=15, height=2, command=lambda: filtering('clear'))
label_random = Label(frame1, text="RANDOM : ", font=("Arial", 8, "bold"))
btn_random = Button(frame1, text="Random Event", font=("Arial", 8, "bold"), width=15, height=2, command=lambda: filtering('random'))

label_filtering.grid(row=0, column=0, padx=5, pady=5)
btn_pax.grid(row=1, column=0, padx=5, pady=5)
btn_occasion.grid(row=2, column=0, padx=5, pady=5)
btn_location.grid(row=3, column=0, padx=5, pady=5)
btn_time.grid(row=4, column=0, padx=5, pady=5)
btn_price.grid(row=5, column=0, padx=5, pady=5)
btn_clear.grid(row=6, column=0, padx=5, pady=5)
label_random.grid(row=7, column=0, padx=5, pady=5)
btn_random.grid(row=8, column=0, padx=5, pady=5)
# ############################################################################################

# Create Frame 2: Display Planning ###########################################################
frame2 = Frame(window)
frame2.pack(side=LEFT, anchor=N)
frame_display = Frame(frame2)
frame_display.pack()
display()
# ############################################################################################

# Create Frame 3: Machine Status #############################################################
frame3 = Frame(window)
frame3.pack(side=LEFT, anchor=NE)
# ############################################################################################

# Window Loop
window.mainloop()
