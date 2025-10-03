def encode_string(s):
    
    if not s:
        return ""  # Return empty string if input is empty

    encoded = ""  # This variable will store the final encoded string
    count = 1     # Initialize count for the first character

    # Loop through the string starting from index 1 (second character)
    for i in range(1, len(s)):
       
        if s[i] == s[i-1]:
            count += 1  # Same character as before, increase the count
        else:
            # Append previous character and its count to the encoded string
            encoded += s[i-1] + str(count)
            count = 1  # Reset count for the new character

    # After the loop ends, we need to add the last run of characters
    encoded += s[-1] + str(count)

    return encoded  

s = input("Enter a string: ")
print("Encoded:", encode_string(s))

