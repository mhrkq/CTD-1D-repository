displaycat = "Categories" + "\n1. Locations" +"\n2. Activities "+"\n3. Food"
print("Welcome to Ai Stead Mai. What lobang you need today?")
print("Enter 'done' after confirming input")
print(displaycat)


input_result = []
input1 = str(input("Select option"))

Locations = "1"
if input1 == Locations:
    option1 = "Locations" + "\n1. North" +"\n2. South"+"\n3. East" +"\n4. West" +"\n5. Central"
    print(option1)
Activities = "2"
if input1 == Activities:
    option1 = "Activities" + "\n1. idk museum or some shit" +"\n2. Ice Skating"+"\n3. Karaoke" +"\n4. Bowling" +"\n5. Movies"
    print(option1)
    
while input1 != 'done':
    input_result.append(input1)
    input1 = input("question")   

choice = {}
choice['Golden Village Katong'] = ["East" , "Movies" , "2"]
choice['Sinpopo'] = ["1" , "2" , "5"]
choice['Selegie Soya Bean'] = ["1" , "2" , "4"]
result = []

def test():
    for cat in input_result:
        for k , v in choice.items():
            
            if cat in v and k not in result:
                result.append(k)
    return result
print(test())
