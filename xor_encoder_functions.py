from operator import xor
import numpy as np


def repeat_to_at_least_length(s, wanted):
    """Repeats a string up until length wanted

    Args:
        s (Str): String to repeat
        wanted (int): length desired

    Returns:
        Str: Repeated string at desired length
    """
    return str(s * (wanted//len(s) + 1))[:wanted]


def convert_string_to_binary(plaintext: str):
    """Converts a given string into a binary representation under ASCII encoding

    Args:
        plaintext (str): String that we wish to convert into ASCII and then binary

    Returns:
        as_binary (List): List of binary digits that represent the plaintext
    """
    as_binary = []
    for char in plaintext:
        # converts each character into ASCII representation then into the binary form of that and adds to a list
        as_binary.append(np.binary_repr(ord(char), width=8))
    return as_binary


def convert_binary_to_string(binary_text: list):
    """Converts a binary into base 10 equivalent and then converts it to ASCII

    Args:
        binary_text (List): List of 8 bit binary numbers as Strings

    Returns:
        List: List of characters
    """
    as_plaintext = []
    for num in binary_text:
        #convert binary string into a base 10 int, then into aascii equivalent
        as_plaintext.append(chr(int(num,2)))
    as_plaintext = ''.join(as_plaintext)
    return as_plaintext


def xor_lists(plain_or_cipher: list, key_binary: list):
    """Takes 2 equally long lists in the form [1,0,1,0] etc and computes an XOR function, returning the binary output in 8bit (1byte) groups

    Args:
        plain_or_cipher (List): _description_
        key_binary (List): _description_

    Returns:
        _type_: _description_
    """
    ciphertext_binary = []
    #flatten plain_or_cipher and key_binary
    plain_or_cipher = [y for x in plain_or_cipher for y in x]
    key_binary = [y for x in key_binary for y in x]
    #Apply XOR function to each 2 binary digit pair and append to ciphertext_binary
    for x in range(len(plain_or_cipher)):
        ciphertext_binary.append(xor(int(plain_or_cipher[x]), int(key_binary[x])))

    #convert ciphertext backk into bytes as currently is is in the form [0,1,0,1] etc
    for x in range(len(ciphertext_binary)):
        #convert each character binary digit into str - form ['0','1','0','1'] etc
        ciphertext_binary[x] = str(ciphertext_binary[x])
    #concatenate the individual binary digits (as strings) together into 1 string form 0101 etc
    ciphertext_binary = ''.join(ciphertext_binary)
    #split the string into a list of 8bit long strings - example is only 4 bits but min length is 8 and will always be in multiples of 8
    ciphertext_binary = [ciphertext_binary[i:i+8] for i in range(0, len(ciphertext_binary), 8)]
    return ciphertext_binary

def convert_using_cipher(text: str, key: str):
    """Pipeline function that takes a text input (plain or cipher) and applies the key under a binary XOR function, returning the ASCII encoded string output

    Args:
        text (str): plain or cipher text that is en/decoded using XOR
        key (str): key used for the ciphering

    Returns:
        converted_from_binary (str): string of plain or ciphertext that has been converted from the 'text' arugment passed
    """
    text_binary = convert_string_to_binary(text)
    key_binary = convert_string_to_binary(key)
    converted_binary = xor_lists(text_binary, key_binary)
    converted_from_binary = convert_binary_to_string(converted_binary)
    return converted_from_binary

def generate_encoder():
    """Main encoder function that asks user for plaintext and key inputs, and outputs a cipher/pliantext after using XOR encoding
    """
    #input plain/cipher and assert that it is not empty
    plain = input('Please enter a plain / cipher text to encode or decode: ')
    assert len(plain) > 0, "text to encode or decode is empty"

    #input key for encoding or decoding and assert that it is not empty
    key = input('Please enter the key that you wish to use for the encryption or decryption: ')
    assert len(key) > 0, "key is empty"

    #key gets repeated until it is the same length as the plaintext (or reduced in length if smaller)
    key = repeat_to_at_least_length(key, len(plain))

    # en/decrypts the input message using the key
    input_encrypted = convert_using_cipher(plain, key)
    print(f'The text calculated using the input and key is: \n{input_encrypted}')

    # en/decrypts the en/decrypted text using the key, output should be the same as the initial input message
    # input_solved = convert_using_cipher(input_encrypted, key)
    # print(f'The input calculated using the key on the en/decrypted text is: \n{input_solved}')

    #Wipe current file and create new empty file to store encrypted message
    file = open('encryption.txt', 'w')
    file.write(input_encrypted)
    file.close()

    