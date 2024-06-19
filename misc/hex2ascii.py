def h_2_a(hex_string):
    hex_string = hex_string.strip()
    bytes_obj = bytes.fromhex(hex_string)
    text = bytes_obj.decode("utf-8")
    return text

c = "caf33472c6e0b2de339c1de893f78e67088cd6b1586a581c6f8e87b5596"
print(h_2_a(c))
for i, char in enumerate(c):
    print(f"Position: {i}, Character: '{char}'")