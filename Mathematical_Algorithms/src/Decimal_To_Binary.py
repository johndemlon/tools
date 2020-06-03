'''PYTHON 3
Author: S Sandeep Pillai (github.com/Corruption13) 
Decimal to Binary converter.

This is a complete decimal to binary converted which accepts any fractional or whole decimal values; The fractional accuracy can be set below.
'''
decimal_accuracy = 7


def dtbconverter(num):      # Function inputs a float value and returns a list as output
                            # Reasoning for list instead of integer: to avoid integer overflow error.

    whole= []                                   # The part before decimal point
    fractional = ['.']                          # The part after decimal point

    decimal = round(num%1, decimal_accuracy)    # Extract fractional number part of decimal
    w_num = int(num)                            # Extract whole number part of decimal.

    i=0     # Some fractional decimal numbers have infinite binary values, so we limit this loop below.

    #Loop to find binary of decimal part
    while(decimal!=1 and i<decimal_accuracy):
            decimal = decimal*2
            fractional.append(int(decimal//1))
            decimal = round(decimal%1, decimal_accuracy)
            if(decimal == 0): break # Removes trailing zeros.
            i = i + 1
    
    #Loop to find binary of whole number part.
    while(w_num!=0):
        whole.append(w_num%2)
        w_num = w_num//2
    whole.reverse()

    return whole + fractional  ### End of dtbconverter() - 16 lines


#Test lines.
number = float(input("Enter ANY base-10 Number: "))
print("The Binary Equivalant: " , *dtbconverter(number))
