def reverse_string(s):
    new_str = ""             #Initialize an empty string  to store the new string
    i = len(s)-1             #Set the index 'i' to the last character in the string
    while i >= 0:            #Loop until the index reaches the beginning of the string
        new_str += s[i]      #Append the character at position 'i' to the result string
        i -= 1               #Decrease the index by 1 to move to the previous character
    return new_str


