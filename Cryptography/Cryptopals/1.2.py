# Here, for xorring hex_strings, we need to convert them into base_10 integers
# So, we can do that by using int(hex_string, base)

hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

buffer1 = int( hex_string1 ,16)
buffer2 = int( hex_string2 ,16)

# Now, buffer1 and buffer2 contain the base_10 integer representation of the given hex_strings.
# These two integers can be xorred by using ^ operator.

xor_string = hex(buffer1 ^ buffer2)

# By using hex(), we store the hexadecimal string representation of the output integer in the xor_string variable.

# By default, the output would contain '0x' at the beginning to specify that the result has been printed in hexadecimal format.
# This can be removed by using .strip() method.

print(xor_string.strip('0x'))