morse_dict = {'a': '.-',
              'b': '-...',
              'c': '-.-.',
              'd': '-..',
              'e': '.',
              'f': '..-.',
              'g': '--.',
              'h': '....',
              'i': '..',
              'j': '.---',
              'k': '-.-',
              'l': '.-..',
              'm': '--',
              'n': '-.',
              'o': '---',
              'p': '.--.',
              'q': '--.-',
              'r': '.-.',
              's': '...',
              't': '-',
              'u': '..-',
              'v': '...-',
              'w': '.--',
              'x': '-..-',
              'y': '-.--',
              'z': '--..',
              '0': '-----',
              '1': '.----',
              '2': '..---',
              '3': '...--',
              '4': '....-',
              '5': '.....',
              '6': '-....',
              '7': '--...',
              '8': '---..',
              '9': '----.',
              '&': '.-...',
              "'": '.----.',
              '@': '.--.-.',
              ')': '-.--.-',
              '(': '-.--.',
              ':': '---...',
              ',': '--..--',
              '=': '-...-',
              '!': '-.-.--',
              '.': '.-.-.-',
              '-': '-....-',
              '+': '.-.-.',
              '"': '.-..-.',
              '?': '..--..',
              '/': '-..-.',
              ' ': '/'
              }


def encode_morse(character_input):
    morse_code = ""
    for char in character_input.lower():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
    print(morse_code)
    return morse_code


def decode_morse(morse_code):
    text = ' '
    for code in morse_code.split():
        for key, val in morse_dict.items():
            if code == val:
                text += key
    print(text)
    return text


encode_morse('food')
decode_morse('..-. --- --- -..')
