while True:
    try:
        a=input("enter the 1st number:- ")
        if len(a) == 4:
           break
    except:
        pass
while True:
    try:
        b=input("enter the 1st number:- ")
        if len(b) == 4:
            break
    except:
        pass

a3 = bool(int(a[0]))
a2 = bool(int(a[1]))
a1 = bool(int(a[2]))
a0 = bool(int(a[3]))

b3 = bool(int(b[0]))
b2 = bool(int(b[1]))
b1 = bool(int(b[2]))
b0 = bool(int(b[3]))

and1,and2 = (not(a3) and b3),(a3 and not(b3))
res_3 = not(and1 or and2)

and3,and4 = (not(a2) and b2),(a2 and not(b2))
res_2 = not(and3 or and4)

and5,and6 = (not(a1) and b1),(a1 and not(b1))
res_1 = not(and5 or and6)

and7,and8 = (not(a0) and b0),(a0 and not(b0))
res_0 = not(and7 or and8)

t_and_1 = (res_3 and and3)
t_and_2 = (res_3 and and4)
t_and_3 = (res_3 and res_2 and and5)
t_and_4 = (res_3 and res_2 and and6)
t_and_5 = (res_3 and res_2 and res_1 and and7)
t_and_6 = (res_3 and res_2 and res_1 and and8)

if (and1 or t_and_1 or t_and_3 or t_and_5):
    print(f"{a} ({int(a,2)}) < {b} ({int(b,2)})")
elif (and2 or t_and_2 or t_and_4 or t_and_6):
    print(f"{a} ({int(a,2)}) > {b} ({int(b,2)})")   
elif ( res_3 and res_2 and res_1 and res_0 ):
    print(f"{a} ({int(a,2)}) = {b} ({int(b,2)})")