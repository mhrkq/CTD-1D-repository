ls = []        #list to take in the data
ls_key = []    #list to take in key
ls_value = []  #list to take in value
dict_in = {}   #dictionary which takes key and value
dict_out = {}  #dictionary to store subdictionary which contains key and value

#read csv file and convert the data into nested dictionary
with open("ctd_planning.csv","r") as f:
    ls = f.read().split("\n")
    ls_key = ls[0].split(",")
    for i in range(1,len(ls)):
        ls_value = ls[i].split(",")
        dict_in = dict(zip(ls_key,ls_value))
        dict_out[i] = dict_in
    f.close()
