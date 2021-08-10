# # __________ E letter ______________
for r_e in range(7):
    for c_e in range(5):
        if c_e == 0 or ((r_e == 0 or r_e == 3 or r_e == 6) and (c_e > 0)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()
# # __________ b letter ______________
for r_b in range(7):
    for c_b in range(5):
        if (c_b == 0 or c_b == 4) or ((r_b == 0 or r_b == 3 or r_b == 6) and (0 < c_b < 4)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()
# # __________ R letter ______________
for r_r in range(7):
    for c_r in range(5):
        if c_r == 0 or (c_r == 4 and (r_r != 0 and r_r != 3) or (r_r == 0 or r_r == 3) and (0 < c_r < 4)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()
# # __________ A letter ______________
for r_a in range(7):
    for c_a in range(5):
        if ((c_a == 0 or c_a == 4) and r_a != 0) or (r_a == 0 or r_a == 3) and (0 < c_a < 4):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()
# # __________ H letter ______________
for r_h in range(7):
    for c_h in range(5):
        if c_h == 0 or c_h == 4 or (r_h == 3 and (0 < c_h < 4)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()
# # __________ E letter ______________
for r_e in range(7):
    for c_e in range(5):
        if c_e == 0 or ((r_e == 0 or r_e == 3 or r_e == 6) and (c_e > 0)):
            print("*", end="")
        else:
            print(end=" ")
    print()
print()
# # __________ M letter ______________
for r_m in range(7):
    for c_m in range(7):
        if c_m == 0 or c_m == 6 or ((r_m == c_m) and (0 < c_m < 4)) or (r_m == 1 and c_m == 5) or (r_m == 2 and c_m == 4):
            print("*", end="")
        else:
            print(end=" ")
    print()
