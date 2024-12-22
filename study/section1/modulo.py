A = 24
B = 15
C = 7

print((A + B) % C, (A % C + B % C) % C) # addition
print((A - B) % C, (A % C - B % C) % C) # subtraction
print((A * B) % C, ((A % C) * (B % C)) % C) # multiplication