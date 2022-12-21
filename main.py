morse_dict = {'a': '.- ',
              'b': '-... ',
              'c': '-.-. ',
              'd': '-.. ',
              'e': '. ',
              'f': '--. ',
              'g': '--. ',
              'h': '.... ',
              'i': '.. ',
              'j': '.--- ',
              'k': '-.- ',
              'l': '.-.. ',
              'm': '-- ',
              'n': '-. ',
              'o': '--- ',
              'p': '.--. ',
              'q': '--.- ',
              'r': '.-. ',
              's': '... ',
              't': '- ',
              'u': '..- ',
              'v': '...- ',
              'w': '.-- ',
              'x': '-..- ',
              'y': '-.-- ',
              'z': '--.. ',
              '0': '----- ',
              '1': '.---- ',
              '2': '..--- ',
              '3': '...-- ',
              '4': '....- ',
              '5': '..... ',
              '6': '-.... ',
              '7': '--... ',
              '8': '---.. ',
              '9': '----. ',
              '&': '.-... ',
              "'": '.----. ',
              '@': '.--.-. ',
              ')': '-.--.- ',
              '(': '-.--. ',
              ':': '---... ',
              ',': '--..-- ',
              '=': '-...- ',
              '!': '-.-.-- ',
              '.': '.-.-.- ',
              '-': '-....- ',
              '+': '.-.-. ',
              '"': '.-..-. ',
              '?': '..--.. ',
              '/': '-..-. ',
              ' ': ' / '
              }


def translate():
    morse_code = []
    list_of_characters = []
    character_input = input("Enter any characters here: ").lower()

    for char in character_input:
        list_of_characters.append(char)
    for item in list_of_characters:
        if item in morse_dict:
            morse_code.append(morse_dict[item])
        else:
            print(f"{item} is not in the morse dictionary")
    print(str(morse_code).strip('[]').replace('\'', ''))


translate()
