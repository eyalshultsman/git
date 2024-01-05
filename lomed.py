num = int(input("enter the number"))
amount= int(input("enter the length of bits"))
nbinar = ""
binar = bin(num)
temp =amount-len(binar)+2
if temp <0:
     print("the number of bits you entered is lower than the required number of bits")
else: 
     binar = temp*"0"+ bin(num)[2:]
     i = len(binar) - 1
     while (binar[i] != "1"):
        nbinar+="0"
        i-=1
     nbinar+="1"
     while (i > 0):
        i -= 1
        if binar[i] == "1":
            nbinar+="0"
        if binar[i] == "0":
            nbinar+="1"
     print(nbinar[::-1])


