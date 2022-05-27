# import module
import string

def read_file_content(filename):
    """This function reads the content of a given file and returns it as a string."""
    fhandle = open(filename)
    text = fhandle.read()
    return text

def count_words():
    """This function counts the occurence of words in a text file."""
    text = read_file_content("./story.txt")
    text = text.strip()
    text = text.translate(text.maketrans("", "", string.punctuation))
    words = text.lower().split()
    
    occurences = {}
    for word in words:
        if word in occurences:
            occurences[word] = occurences[word] + 1
        else:
            occurences[word] = 1
    return occurences
            
print(count_words())