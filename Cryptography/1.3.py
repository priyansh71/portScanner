# Single-byte XOR cipher

# In this question, we have to find the key "byte" that has been used for xorring.

# The hint for this challenge comes from the Achievment Unlocked note given below, which talks about Etaoin-Shrdlu and character
# frequency. If every byte of a byte-string is xorred against a single character and then presented, there are a total of
# 256 possible decrypted messages [256 ASCII table characters]

# These decrypted message texts will include not only alphabets but all types of characters from the keyboard. While a human eye may
# be able to look through them and find the most "English" message as the actual decrypted text, making Python code do this is a 
# different thing, and this is where Etaoin-Shrdlu comes into play, which maps each letter of the english alphabet to a number
# that represents the normalized frequency of letter in the english language in general.

def scorer(input):
    frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([frequencies.get(chr(char),0) for char in input.lower()])
    
# The above table is based on Etaoin-Shrdlu and when given an input text, it returns the 'score' of the input text i.e. looks for the 
# each alphabet in the input and finds its corresponding frequency number. After summing all the alphabets' frequency using the table 
# data, it returns the 'score' , which in turn represents how "English" the input is.


def xorer(input, char):
    output = b''
    for byte in input:
        output += chr(byte ^ char).encode()
    return output


# The above function is a xorer, i.e. it takes in an input byte (amongst any of the ASCII table ones) and xores that input byte
# against each of the bytes of the input string.
# byte ^ char produces an integer and the corresponding character is found out by using chr() and is appended to the output, thus 
# the loop produces the xorred-byte-array i.e. 'output'
# Alternatively, we can also use xor from the pwntools module which directly xores two byte-arrays without a need for a loop.


hexstring = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
string = bytes.fromhex(hexstring)

# The hexstring is converted to bytes by using the fromhex() method , so that it can be xorred upon as a byte-array.

array = []
for char in range(256):
    message = xorer(string, char)
    score = scorer(message)
    data = {
        'message': message.decode() ,
        'score': score,
        'key': char
        }
    array.append(data)

# The above code initializes an empty array and pushes the data of all the 256 possible strings into it by running through a loop 
# which provide the ASCII code of each byte. The firstly initialized functions are using for calculating the score and xorring.

solution = sorted(array, key=lambda x: x['score'])[-1]
print(solution)

# The array consits of 256 objects which all have data of possible decrypted messages. We have to find the object which has the
# largest value of "score" amongst the 256 strings, as that object will contain the information of the most "English" message that got 
# decrypted. We use the sorted fucntion, and use the score as our parameter of classification. As default sorting is ascending, the 
# decrypted text will be the last one.