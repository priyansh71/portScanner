import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Given string is in hexadecimal format, it can be converted to bytes form by using the inbuilt => bytes.fromhex(string)

hex_bytes = bytes.fromhex(hex_string)

# This hex_bytes byte-array is encoded into base64 by using the base64 module, which returns the output in bytes format as well.

b64_bytes = base64.b64encode(hex_bytes)

# This bytes format can be converted to a normal string by using the .decode() method.

b64_string = b64_bytes.decode()
print(b64_string)
