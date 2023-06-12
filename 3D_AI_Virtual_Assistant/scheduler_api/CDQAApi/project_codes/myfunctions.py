import math
import sympy
def addition(res):
    summ =0
    for val in res:
        summ+=val
    return summ

def subtraction(res,counter):
    if counter==0:
        sub =res[len(res)-1]
        for val in res[:len(res)-1]:
            sub=sub-val

    elif counter ==1:
        sub =res[0]
        for val in res[1:]:
            sub=sub-val
    return sub
    
def multiplication(res):
    multi =1
    
    for val in res:
        multi=multi*val
    return multi

def division(res):
    divi = res[len(res)-1]
    for val in res[:len(res)-1]:
        divi=val/divi
    return divi

def average(res):
    summ = addition(res)
    avg = summ/len(res)
    return avg

def factorial(res):
    fact = 1
    for val in range(1,res[0]+1):
        fact = fact*val
    return fact

def DecimalToBinary(num,mlist):
    
    if num >= 1:
        DecimalToBinary(num // 2,mlist)
    mlist.append(num % 2)
    return mlist

def square(res):
    return(res[0]**2)

def cube(res):
    return(res[0]**3)

def power(res):
    return(res[0]**res[1])

def sin(res):
    return(round(math.sin(res[0]*math.pi/180), 2))

def sinfract(res):
    return(sympy.sin(res[0]))

def cos(res):
    return(round(math.cos(res[0]*math.pi/180), 2))

def cosfract(res):
    return(sympy.cos(res[0]))

def tan(res):
    return(round(math.tan(res[0]*math.pi/180), 2))

def tanfract(res):
    return(sympy.tan(res[0]))

def cot(res):
    return(round(1.0/math.tan(res[0]*math.pi/180), 2))



def cotfract(res):
    ans = str(sympy.tan(res[0]*math.pi/180))
    anslist = ans.split('/')
    return(str(anslist[1]+'/'+str(anslist[0])))

#cotfract([60])

def sec(res):
    return(round(1.0/math.cos(res[0]*math.pi/180), 2))

def secfract(res):
    return(1.0/float(math.cos(res[0])))

def cosec(res):
    return(round(1.0/math.sin(res[0]*math.pi/180), 2))

def cosecfract(res):
    return(1.0/float(math.sin(res[0])))

def derivate(res):
    print("Please enter the function and with respect to what you want to take the derivative: ")
    print("For example: if you want derivative of 2x²+5x+10 with respect to x Enter it like following: ")
    
    print("2*x**2+5*x+10 with respect to x \n")

    print("Additional: if you want second or nth derivative enter 2nd derivative enter like below \n")

    print("2nd derivative of 2*x**2+5*x+10 with respect to x \n")
    eqnstr = input()
    eqnstrlist=[]
    if ("derivative of") in eqnstr:
        eqnstrlist = str(eqnstr).split(" derivative of ")
        eqnstrlist2 = str(eqnstrlist[1]).lower().split(" with respect to ")
        eqnstrlist2 = eqnstrlist[:1]+eqnstrlist2
    else:
        eqnstrlist2 = str(eqnstr).lower().split(" with respect to ")

    if 'st' in eqnstrlist2[0].lower():
        derivative_power = eqnstrlist2[0].lower().replace("st","")
        eqnstrlist2[0] = derivative_power
    if 'nd' in eqnstrlist2[0].lower():
        derivative_power = eqnstrlist2[0].lower().replace("nd","")
        eqnstrlist2[0] = derivative_power
    if 'th' in eqnstrlist2[0].lower():
        derivative_power = eqnstrlist2[0].lower().replace("th","")
        eqnstrlist2[0] = derivative_power
    if len(eqnstrlist2) == 2:
        ans  = sympy.diff(eqnstrlist2[0], eqnstrlist2[1])
    elif len(eqnstrlist2) == 3:
        ans = sympy.diff(eqnstrlist2[1], eqnstrlist2[2], int(eqnstrlist2[0]))
    
    print(eqnstrlist2[1])
    return ans
