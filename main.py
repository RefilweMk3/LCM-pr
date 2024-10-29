import math

num1 = int(input("Enter the Largest number: "))
num2 = int(input("Enter the smallest number: "))

def calcu_lcm(a,b):
    return abs(a * b) // math.gcd(a,b)

lcm_value = calcu_lcm(num1, num2)
print("LCM is:", lcm_value)