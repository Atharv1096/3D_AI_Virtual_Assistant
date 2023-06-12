from .myfunctions import *

def Mathematics(myinput,resmy):
    adders = ["addition","add","plus","+","added"]
    for adder in adders:
        if adder in myinput:
            print("Addition: "+str(addition(resmy)))
            break

    '''if("addition" or "add" or "plus" or "+" or "added") in myinput:
        print(str(addition(resmy)))'''


    subtractors = ["subtract","substract","subtraction","subtracted"]
    for subtractor in subtractors:
        if subtractor in myinput:
            print("Subtraction: "+str(subtraction(resmy,0)))
            break

    '''if ("subtract" or "substract" or "subtraction" or "subtracted") in myinput:
        print(str(subtraction(resmy,0)))'''

    subtractors2 = ["minus"]
    for subtractor2 in subtractors2:
        if subtractor2 in myinput:
            print("Subtraction: "+str(subtraction(resmy,1)))
            break

    '''if("minus" or "-") in myinput:
        print(str(subtraction(resmy,1)))'''

    divisors = ["div","division","divided","by","/","upon"]
    for divisor in divisors:
        if divisor in myinput:
            print("Division: "+str(division(resmy)))
            break

    '''if("div" or "division" or "divided" or "by" or "/") in myinput:
        print(str(division(resmy)))'''

    multipliers = ["multiply","into","multiplication"]
    for multiplier in multipliers:
        if multiplier in myinput:
            print("Multiplication: "+str(multiplication(resmy)))
            break

    averagers = ["average"]
    for averager in averagers:
        if averager in myinput:
            print("Average: "+str(average(resmy)))
            break
    
    factorialers = ["factorial"]
    for factorialer in factorialers:
        if factorialer in myinput:
            print("Factorial: "+str(factorial(resmy)))
            break

    binars = ["binary"]
    for binar in binars:
        if binar in myinput:
            num = resmy[0]
            mlist=[]
            for value in DecimalToBinary(num,mlist):
                print(value, end='')
            break
    
    squarers = ["square"]
    for squarer in squarers:
        if squarer in myinput:
            print("Square: "+str(square(resmy)))
            break

    cubers = ["cube"]
    for cuber in cubers:
        if cuber in myinput:
            print("Cube: "+str(cube(resmy)))
            break

    powerers = ["power"]
    for powerer in powerers:
        if powerer in myinput:
            print("Power: "+str(power(resmy)))
            break

    siners = ["sin","sine"]
    for siner in siners:
        if siner in myinput:
            print("Sin: "+str(sin(resmy)))
            break

    cosers = ["cos","cosin","cosine"]
    for coser in cosers:
        if coser in myinput:
            print("Cosin: "+str(cos(resmy)))
            break

    taners = ["tan","tangent"]
    for taner in taners:
        if taner in myinput:
            print("Tan: "+str(tan(resmy)))
            break

    Coters = ["cot","cotan","cotangent"]
    for Coter in Coters:
        if Coter in myinput:
            print("Cot in decimal: "+str(cot(resmy)))
            #print("Cot in fraction: "+str(cotfract(resmy)))
            break

    secers = ["sec","secant"]
    for secer in secers:
        if secer in myinput:
            print("Sec: "+str(sec(resmy)))
            break

    cosecers = ["cosec","cosecant"]
    for cosecer in cosecers:
        if cosecer in myinput:
            print("Cosec: "+str(cosec(resmy)))
            break

    derivators = ["derivative","derivate"]
    for derivator in derivators:
        if derivator in myinput:
            print("Derivative : "+str(derivate(resmy)))
            break
    
    