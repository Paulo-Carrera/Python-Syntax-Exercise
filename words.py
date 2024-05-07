def print_upper_words(words,start_letter):
    """
    Enter a list of words
    Returns the words uppercased
    """
    for i in words :
        if i[0] == start_letter:
            print(i.upper())
            found_word = True
    if not found_word:
        print("No words apply.")






print_upper_words(['hello','goodbye'] , 'h') 