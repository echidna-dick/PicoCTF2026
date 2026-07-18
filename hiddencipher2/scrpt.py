encoded_flag = [1344, 1260, 1188, 1332, 804, 1008, 840, 1476, 1308, 624, 1392, 1248, 1140, 1176, 612, 1248, 588, 1320, 1200, 1140,
 1188, 588, 1344, 1248, 612, 1368, 1140, 1224, 660, 684, 612, 1200, 576, 1212, 576, 1500] # you need to paste here your 'encoded flag'
math_arg = 12;      # you need to change this to your awnser in the equasion
flag = []

for i in encoded_flag:
    flag_char = i // math_arg
    flag.append(chr(flag_char))
    
print("".join(flag))

