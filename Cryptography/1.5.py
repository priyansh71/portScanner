# Repeating-key XOR

# Here, instead of using chars from 0-255, we have been given a key, each of whose letters have to be xorred against corresponding
# characters of the given string, and the key has to be repeated until it's length equals len(string).

key = b'ICE'
string = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

# i.e. if len(string) = 7, the key-string that will xorred against string will be ICEICEI

def repeat_xorer(input, key):
    output = b''
    index = -1
    for byte in input:
        if index + 1 == len(key):
            index = 0
        else :
            index += 1
        output += chr(byte ^ key[index]).encode()
    return output

# Above function takes in the string and the key and xorres them repeatedly i.e.
# the if clause makes sure that as soon as the character that is xorring is the last byte of the key, the loop goes to 
# the first position of the key and continues xorring from there again. 

message = repeat_xorer(string , key)
print(message.hex())

# string and key are passed into the function and the hex value of the byte-array is printed.