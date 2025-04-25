def sum_of_digits(number):
    number = str(number)               #Typecasting the number to a string so we can loop through digits
    i = len(number) - 1                #Set the index to the last digit
    summation = 0                      #Initialize summation to 0
    while i >= 0:                      #Loop backwards through the string
        summation += int(number[i])    #Convert the character at position 'i' to an int and add to summation
        i -= 1                         #Move to the previous digit
    return summation


