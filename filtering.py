ls = []
ls_key = []
ls_value = []
dict_in = {}
dict_out = {}
with open("ctd_planning.csv","r") as f:
    ls = f.read().split("\n")
    ls_key = ls[0].split(",")
    for i in range(1,len(ls)):
        ls_value = ls[i].split(",")
        dict_in = dict(zip(ls_key,ls_value))
        dict_out[i] = dict_in
    f.close()
#print(dict_out)

userpax = input("Enter no. of people (2 - 10): ")
userOccasion = input("Enter Occasion (Date / Friends): ")
userLocation = input("Enter Location (North / South / East / West / Sentosa / Home): ")
usertime = input("Enter time (0.5 - 16): ")
userPrice = input("Enter Price ($ / $$ / $$$ / $$$$): ")

filterpax = userpax != ""
filterOccasion = userOccasion != ""
filterLocation = userLocation != ""
filtertime = usertime != ""
filterPrice = userPrice != ""
    
dict_show = {}    

for i in range(1,len(dict_out)):
    """
    print(float(dict_out[i]['pax_min']))
    print(float(dict_out[i]['pax_max']))
    print(dict_out[i]['Occasion'])
    print(dict_out[i]['Location'])
    print(float(dict_out[i]['time_min']))
    print(float(dict_out[i]['time_max']))
    print(dict_out[i]['Price'])
    """
    appendd = True
    if filterpax:
        if float(dict_out[i]['pax_min']) <= float(userpax) <= float(dict_out[i]['pax_max']):
            pass
        else:
            appendd = False
    if filterOccasion:
        if userOccasion in dict_out[i]['Occasion']:
            pass
        else:
            appendd = False
    if filterLocation:
        if userLocation in dict_out[i]['Location']:
            pass
        else:
            appendd = False
    if filtertime:
        if float(dict_out[i]['time_min']) <= float(usertime) <= float(dict_out[i]['time_max']):
            pass
        else:
            appendd = False
    if filterPrice:
        if userPrice == dict_out[i]['Price']:
            pass
        else:
            appendd = False
    if appendd:
        dict_show[i] = dict_out[i]

for key in dict_show:
    print("*****")
    print(dict_show[key])
