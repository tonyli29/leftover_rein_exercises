def word_counter():
    num_of_words = 1
    x = input() 
    for y in x:
        if y == ' ':
            num_of_words += 1

    print(num_of_words)


word_counter()
