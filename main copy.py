a = 12
b = 5
c = 125

def is_int(a):
    return a - int(a) <= 1e-5

# ============= Without C ========== #
print("Process without c")
rslt = pow(a, b)

print("a**b:", rslt)

print("a:", pow(rslt, (1.0 / b)))