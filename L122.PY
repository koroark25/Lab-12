#Breanna Eafon Katherine O'roarke

import string

def sentence_to_list(input_sentence):
    input_sentence = input_sentence.translate(str.maketrans('', '', string.punctuation))
    output_list = input_sentence.split()
    return output_list

my_sentence = "This is a sample sentence with some puntuation, like a comma."
my_list = sentence_to_list(my_sentence)
print(my_list)
