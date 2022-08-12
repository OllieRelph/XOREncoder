from xor_encoder_functions import *

plain = 'hello my name is Ollie'
key = 'some key to test the functions'

#key gets repeated until it is the same length as the plaintext (or reduced in length if smaller)
key = repeat_to_at_least_length(key, len(plain))

ciphertext = convert_using_cipher(plain, key)
print(f'The ciphertext calculated using the plaintext and key is: \n{ciphertext}')

plaintext_solved = convert_using_cipher(ciphertext, key)
print(f'The plaintext calculated using the key on the ciphertext is: \n{plaintext_solved}')

