n = int(input("enter the numbe"))
text= "Hello eyal you are looking good today we are happy to meet you and we hope you would have a good day"
with open('text_as_binary,bin','wb') as file:
    binary_data= text.encode()
    file.write(binary_data)
with open('text_as_binary,bin', "r") as file:
    data = file.read()
    text_data_read = data.decode()

l = text_data_read.lower()
l=l.split()

count = 0
dictionary= {}
for i in l:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
sorted_amount = sorted(dictionary.items(), key=lambda x:x[1], reverse = True)
dictionary=dict(sorted_amount)
i = 0
dickeys = list(dictionary.keys())
while (i < n):
    print (dickeys[i])
    i += 1