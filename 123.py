#temperlature
for i in range(3):
val = input("degree:")
if val[-1] in ['c', 'C']:
    f = 1.8 * float(val[0:-1]) + 32
    print("trun to: %.2fF"%f)
elif val[-1] in ['F', 'f']:
    c = (float(val[0:-1]) - 32) / 1.8
    print("trun to: %.2fc"%c)
else:
    print("wrong")

#PLACE
val = input("location")


