with open("data.bin", "rb") as f:
    encoded_data = f.read()

decode_data = bytes([(b - 42) % 256 for b in encoded_data])

with open("decoded_data.jpg", "wb") as f:
    f.write(decode_data)

print("check file 'decoded_data.jpg'")