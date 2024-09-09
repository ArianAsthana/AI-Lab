import math

a=int(input("Enter jug A capacity: "))
b=int(input("Enter jug B capacity: "))
ai=int(input("Initially water in Jug A: "))
bi=int(input("Initially water in jug B: "))
af=int(input("Final state of jug A: "))
bf=int(input("Final state of jug B: "))

if a<=0 or b<=0:
    print("Jug capacities must be positive.")
    exit(1)
if ai < 0 or bi < 0 or af < 0 or bf < 0:
    print("Negative values are not allowed.")
    exit(1)

def wjug(a,b,ai,bi,af,bf):
    print("List of operations you can do:\n")
    print("1. Fill Jug A completely")
    print("2. Fill Jug B completely")
    print("3. Empty Jug A completely")
    print("4. Empty Jug B completely")
    print("5. pour from Jug A till Jug B is full or A becomes empty")
    print("6. pour from Jug B till Jug A is full or B becomes empty")
    print("7. Pour all from Jug B to Jug A")
    print("8. Pour all from Jug A to Jug B")

    while ai != af or bi!=bf:
        op = int(input("Enter the operations (1-8): "))

        if op == 1:
            ai = a
        elif op == 2:
            bi = b
        elif op == 3:
            ai = 0
        elif op == 4:
            bi = 0
        elif op == 5:
            pour_amount = min(ai,b - bi)
            ai -= pour_amount
            bi += pour_amount
        elif op == 6:
            pour_amount = min(bi,a - ai)
            bi -= pour_amount
            ai += pour_amount
        elif op == 7:
            pour_amount = min(bi, a-ai)
            ai += pour_amount
            bi -= pour_amount
        elif op == 8:
            pour_amount = min(ai,b - bi)
            bi += pour_amount
            ai -= pour_amount
        else:
            print("Invalid operation. Please choose a number between 1 and 8")
            continue

        print(f"Jug A: {ai}, Jug B: {bi}")

        if ai == af and bi == bf:
            print("Final state reached: Jug A =", ai, ", Jug B =", bi)
            return


    print("Final state reached: Jug A=", ai, ", Jug B=",bi)

gcd = math.gcd(a,b)

if(af <= a and bf <= b) and (af % gcd == bf % gcd == 0):
    wjug(a,b,ai,bi,af,bf)
else:
    print(" The final state is not achievable with the given capacities.")
    exit(1)
    
         













            
