#jocelyn
#02/12/2025
#word count

#int
#function
def word_count(text):
    words = text.split(" ") # splits up the words without the spaces
    count = len(words) # counts the words
    print(count) # prints the number of words
    print(words) # prints the words

    #count = words
    #print(count)

#main
word_count("This is an example of a text supplies for AP computer science") # 8

# 1. The program should take the text input as a parameter.
# 2. Use a list to store individual words from the sentence. Look up split()
# 3. Display the list of words.
# 4. Count the number of words in the sentence.
# 5. Display the total word count.
