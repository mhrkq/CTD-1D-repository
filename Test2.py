input_result = []
input1 = str(input("question"))
while input1 != 'done':
input_result.append(input1)
input1 = input("question")

choice = {}
choice['Awfully Chocolate'] = ["East" , "East Coast" , "Dessert"]
result = []

def test():
for cat in input_result:
for k , v in choice.items():
  if cat in v and k not in result:
    result.append(k)
return result
print(test())
