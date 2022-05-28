def find_anagrams(first_string, second_string):
    """
    This function finds if two given strings are anagrams.
    """
    
    #filter non alphabet character
    first_string = "".join(letter for letter in first_string if letter.isalpha())
    second_string = "".join(letter for letter in second_string if letter.isalpha())
    
    #compare the sorted strings. The function must be case insensitive.
    if sorted(first_string.lower()) == sorted(second_string.lower()):
        return True
    else:
        return False

# astronomer and moon starter
print(find_anagrams("Astronomer.", "Moon starer"))
# a gentleman and elegant man
print(find_anagrams("a gentleman", "elegant man"))
# the country side and no city dust here
 