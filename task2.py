def correct_sentence(sentence):
    if sentence[-1] != '.':
        sentence = sentence.capitalize() + '.'
    else:
        sentence = sentence.capitalize()

    return sentence

user_input = input("Введіть речення: ")

corrected_sentence = correct_sentence(user_input)
print(corrected_sentence)