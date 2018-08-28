def pig_it(text):
    new_text = text.split(' ')
    temp_array = []
    new_string = ''

    for x in new_text:
        new_string = x
        word = new_string[1:] + new_string[0] + "ay"
        temp_array.append(word)
        new_string = []
        print(temp_array)
        print(" ".join(temp_array))

pig_it('Pig latin is cool')
