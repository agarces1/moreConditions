#elif allows you to check for different values
country = input("Where are you from? ").upper();
pet = input("What pet do you have? ").upper();

#if country == "Canada": 
#    print("Hello,Eh");
#elif country == "Germany" :
#    print("Guten tag");
#elif country == "France" : 
#    print("Bonjour");
#else:
#    print("404 not found");
 #The and is inly evaluated as TRUE if both conditions are TRUE
#wonLottery = True
#bigWin = True
#if wonLottery AND bigWIn : 
#    print ("You can retire");
#When you use "or" you are saying please do the following if either condition is TRUE
#saturday = True
#sunday = False

#if saturday or sunday : 
#    print('You can sleep in');
#and is evaluated first
#When in doubt put ()
if country == "CANADA" and (pet == "MOOSE"\
    or pet == "BEAVER") :
    print ("Do you play hockey too?");