# This challenge has the exact same logic as the 3rd one, this one being an extended version of the last one.
# i.e. We don't know which string will hold the most "English" message when xorred with a particular
#  char from amongst the 256 chars.

import requests
from bs4 import BeautifulSoup

source = requests.get("https://cryptopals.com/static/challenge-data/4.txt").text
soup =  BeautifulSoup(source, 'lxml')
text = soup.find('p').text

with open('file.txt','w') as fileW:
    fileW.write(text)

with open('file.txt', 'r') as fileR:
    val = fileR.readlines()
 
# The above code takes all the possible strings from the website and stores it into an array named "val."
# The array has 327 hex strings.

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

def xorer(input, char):
    output = b''
    for byte in input:
        output += chr(byte ^ char).encode()
    return output

# The same functions as the 3rd challenge which calculates the 'English score' and xorred array of any entered string

big = []
final = []

# Now , we want to create an array (named big) that contains 327 arrays. Each array (is named b and) contains 256 possible
# after-xorring-decrypted-message-data of a particular string.

#(1) Then we want to sort each of the 327 arrays such that the last object of each of them contains the data of the most-
# "English score" having decryted form of that string. This is exactly what we did last time, but now we have 327 such strings.

#(2) All such objects which have the largest score wrt a string are pushed into an array (named final), which now contains 327 objects.
# Again, we sort all of these objects based on their "English score" and the one with the largest score is the last object.

for hexstring in val :
    string = bytes.fromhex(hexstring)
    b = []
    big.append(b)
    for iterator in range(256):
        message = xorer(string, iterator)
        score = scorer(message)
        data = {
            'message': message.strip(b'\n').decode() ,
            'score': score,
            'key': iterator,
            'lineNumber' : val.index(hexstring) + 1
            }
        b.append(data)
    primary = sorted(b, key=lambda x: x['score'])[-1] ##refer #(1)
    final.append(primary)

secondary = sorted(final, key=lambda x: x['score'])[-1] ##refer #(2)
print(secondary)