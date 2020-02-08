def FPB(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            fpb = i
            
    return fpb
no1 = 1000
no2 = 1250
print("FPB dari", no1,"dan", no2," =", FPB(no1, no2))
