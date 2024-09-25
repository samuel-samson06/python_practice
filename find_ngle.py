import math
print("find angles")
ab = float(input("Len AB::"))
bc = float(input("LEN BC::"))
half_length_hyp = math.sqrt(ab**2 + bc**2)*0.5
print(f"{math.floor(math.degrees(math.atan(ab / bc)))}º")
