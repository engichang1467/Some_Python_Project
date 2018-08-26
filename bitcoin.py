#########################
#                       #
#    CMPT 120 Fall      #
#                       #
#      Assignment 1     #
#                       #
# Author: Michael Chang #
#                       #
#########################
print("Hi! Python will guide you through exchanging currency process")
rateRatio= input("What is the bitcoin rate in CAD?(1bit=?CAD)")
#Part A
#Part A will look at the conversion of word/byte/bitcoins to Canadian dollar (CAD)
Question = input("Do you want to do the calculation(a)?type yes or no")
y= "yes"
n= "no"

if (Question==y):
    bitcoin=int(input("provide the number of bitcoins you want to exchange.  "))
    bytecoin=int(input("provide the number of bytecoins you want to exchange.  "))
    wordcoin=int(input("provide the number of wordcoins you want to exchange.  "))
    BitTotal=bitcoin*1+bytecoin*8+wordcoin*32
    print("Your total Bitcoin amount in BC is:",BitTotal)
    print()
    print("TRACE -- Rate =", rateRatio)
    print()
    print(BitTotal, "BC corresponts to:",BitTotal*int(rateRatio),"CAD$")
    print()
    print("TRACE -- Calculation(a) is done")
    print()
    print()
#Part B
#This part looks at converting CAD to word/byte/bitcoins in order from largest to smallest
    print("Calculation (b)")
    print()
    import math as m
    Q2=int(input("Please type the amount in CADS$: "))
    CanadianDollars=m.floor(int(Q2/int(rateRatio)))
    WordCoins = m.floor(int(CanadianDollars//32))
    ByteCoins= (m.floor(int(CanadianDollars-(WordCoins*32))//8))
    BitCoins= m.floor(int(CanadianDollars-((WordCoins*32)+(ByteCoins*8))))
    change= m.floor(Q2-(((WordCoins*32)+(ByteCoins*8)+BitCoins)*2000))
    print("The coins you receive is as follows:")
    
    print("TRACE -- coins available with aount of CAD$")
    print(BitCoins,"Bitcoins")
    print(ByteCoins,"Bytecoins")
    print(WordCoins,"Wordcoins")
    print(change, "is your change ")
    print()
    print("Calculation (b) is done")
    print()
    print("TRACE -- Calculation (b) is done")
    print()
    print()
#Part C
#Here we encript a secret code that represents the results of part B
    print("Welcome to the part C of this program. We'll be creating a string to ")
    print()

    import math
    if int(BitCoins%2 ==0):
        v1 = ("$$")
        print("TRACE the number of bitcoins in (b) is even")
    else:
        v1=("$")
        print("TRACE the number of bitcoins in (b) is odd")
    v2=("**")
    v3=("W"*WordCoins)
    v4=("**")
    v5=("B"*ByteCoins)
    v6=("**")
    v7=(math.sqrt(Q2))
    v12=str(v7)
    
    import random
    v9 = round(v7)
    v10= str(v9)[1]
    v11=random.randint(0,int(v10))
    everything = str(v1)+str(v2)+str(v3)+str(v4)+str(v5)+str(v6)+str(v9)
    print("TRACE the square root of the total money amount(",str(Q2),") is:", str(v7))
    print("TRACE the string until and including the int square root is:", str(everything))
    print("TRACE the length of the string so far is:", len(str(everything)))
    if (len(everything)%2==0):
        v8 = ("2")
        print("TRACE the length of the string is even.")
    else:
        v8 = ("1")
        print("TRACE the length of the string is odd.")
    print("TRACE the digit after the decimal point in the square root is:", v12[4])
    print("TRACE the random number between 0 and ", str(v10), "is", str(v11))
    vfinal=("!"*int(v11))
    print("TRACE the number of exclamation points at the end of the string is ", str(v11))
    print("The final secret secret code string is: ")
    last=everything+v8+vfinal
    print(last)
    print("Thank you for taking part in this program. BYE")
#This program is finished
    
else:
#This program gives users the option to skip Part A
#Part B
#This part looks at converting CAD to word/byte/bitcoins in order from largest to smallest
    print("Calculation (b)")
    print()
    import math as m
    Q2=int(input("Please type the amount in CADS$: "))
    CanadianDollars=m.floor(int(Q2/int(rateRatio)))
    WordCoins = m.floor(int(CanadianDollars//32))
    ByteCoins= (m.floor(int(CanadianDollars-(WordCoins*32))//8))
    BitCoins= m.floor(int(CanadianDollars-((WordCoins*32)+(ByteCoins*8))))
    change= m.floor(Q2-(((WordCoins*32)+(ByteCoins*8)+BitCoins)*2000))
    print("The coins you receive is as follows:")
    
    print("TRACE -- coins available with aount of CAD$")
    print(BitCoins,"Bitcoins")
    print(ByteCoins,"Bytecoins")
    print(WordCoins,"Wordcoins")
    print(change, "is your change ")
    print()
    print("Calculation (b) is done")
    print()
    print("TRACE -- Calculation (b) is done")
    print()
    print()
#Part c
#Here we encript a secret code that represents the results of part B
    print("Welcome to the part C of this program. We'll be creating a string to ")
    print()

    import math
    if int(BitCoins%2 ==0):
        v1 = ("$$")
        print("TRACE the number of bitcoins in (b) is even")
    else:
        v1=("$")
        print("TRACE the number of bitcoins in (b) is odd")
    v2=("**")
    v3=("W"*WordCoins)
    v4=("**")
    v5=("B"*ByteCoins)
    v6=("**")
    v7=(math.sqrt(Q2))
    v12=str(v7)
    
    import random
    v9 = round(v7)
    v10= str(v9)[2]
    v11=random.randint(0,int(v10))
    everything = str(v1)+str(v2)+str(v3)+str(v4)+str(v5)+str(v6)+str(v9)
    print("TRACE the square root of the total money amount(",str(Q2),") is:", str(v7))
    print("TRACE the string until and including the int square root is:", str(everything))
    print("TRACE the length of the string so far is:", len(str(everything)))
    if (len(everything)%2==0):
        v8 = ("2")
        print("TRACE the length of the string is even.")
    else:
        v8 = ("1")
        print("TRACE the length of the string is odd.")
    print("TRACE the digit after the decimal point in the square root is:", v12[4])
    print("TRACE the random number between 0 and ", str(v10), "is", str(v11))
    vfinal=("!"*int(v11))
    print("TRACE the number of exclamation points at the end of the string is ", str(v11))
    print("The final secret secret code string is: ")
    last=everything+v8+vfinal
    print(last)
    print("Thank you for taking part in this program. BYE")
#This program is finished
