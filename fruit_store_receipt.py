# Fruit store Receipt Generator :

bsum = 0
csum = 0
asum = 0
wsum = 0
osum = 0
psum = 0
   
while (True):
    print("------------- Taj Fruit Store -------------")
    print("|            1. Banana                    |")
    print("|            2. Tender Coconut            |")
    print("|            3. Apple                     |")
    print("|            4. Watermelon                |")
    print("|            5. Orange                    |")
    print("|            6. Pear Beauty               |")
    print("|            0. Total Bill                |")
    print("-------------------------------------------")

    fname = int(input("Enter Number : "))

    if fname != 0:
        fquntity = int(input("Enter Quntity : "))

    q = fquntity/500

    if fname == 1:
        banana = 5*fquntity
        bsum = bsum + banana
        print(f"Total Bill is  : {banana}")
        
    elif fname == 2:
        coconut = 40*fquntity
        csum = csum + coconut
        print(f"Total Bill is  : {coconut}")

    elif fname == 3:
        apple = q*50
        asum = asum + apple
        print(f"Total Bill is  : {apple}")
        
    elif fname == 4:
        watermelon = q*20
        wsum = wsum + watermelon
        print(f"Total Bill is  : {watermelon}")
        
    elif fname == 5:
        orange = q*25
        osum = osum + orange
        print(f"Total Bill is  : {orange}")
        
    elif fname == 6:
        pear = q*28
        psum = psum + pear
        print(f"Total Bill is  : {pear}")
        
    elif fname == 0:
        print("\n\n------------- Taj Fruit Store -------------")
        print("|\t\tReceipt     \t\t  |")    
        if bsum != 0:
            print("|\tBanana(Rs.5/peice) " + str(bsum/5) + " = " + str(bsum) + " \t  |")
        if csum != 0:
            print("|\tCoconut(Rs.40/peice)  " + str(csum/40) + " = " + str(csum) + "   |")
        if asum != 0:
            print("|\tApple(Rs.50/500g) " + str(asum/50) + " = " + str(asum) + " \t  |")
        if wsum != 0:
            print("|\tApple(Rs.20/500g) " + str(wsum/20) + " = " + str(wsum) + " \t  |")
        if osum != 0:
            print("|\tApple(Rs.25/500g) " + str(osum/25) + " = " + str(osum) + " \t  |")
        if psum != 0:
            print("|\tApple(Rs.28/500g) " + str(psum/28) + " = " + str(psum) + " \t  |")
        print("|\t\t\t Total = " + str(bsum+csum+asum+wsum+osum+psum) + "\t  |")
        print("-------------------------------------------")
        break
     
    else:
        print("Please Enter Number between 1 to 6.")
        
    
