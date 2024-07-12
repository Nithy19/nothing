#testing clone
#ifelse1
#========
#mark=int(input("Mark:"))
#if(mark>35):
# print("Pass")
#else:
# print("Fail")

#ifelse2
#========
#income=int(input("Income:"))
#if(income==7000):
# print("eligible")
#else:
# print("notelgble")


#ifelse 3
#========
#a= int(input("num1:"))
#b=int(input("num2:"))
#c=a%b
#if(c==0):
#    print("dividedby")
#else:
#    print("notdivided",c)

#ifelse 4
#========
#a=int(input("num1"))
#if(a%3 ==0 | a%5==0):
#if(a%3==0 and a%5==0):
#    print("divided by 5 and 3")
#elif(a%3==0):
#    print("divided by 3")
#elif(a%5==0):
#    print("divided 5")
#else:
#    print("not")
    
#ifelse 5
#========

#a=int(input("num"))
#if(a%2==0):
#    print("EVEN:",a)
#else:
#    print("ODD",a)
    
#ifelse 6
#========

#a= int(input("score:"))
#if(a<=35):
#    print("poor stdnt")
#elif(a>35 and a<=70):
#    print("avrg stdnt")
#elif(a>70 and a<=100):
#    print("good stdnt")
#else:
#    print("mark not definred")

#ifelse 7
#========
#a=int(input("numA:"))
#b=int(input("numB:"))
#opt=input("+,-,/,%,*    :")
#if(opt=="+"):
#    c=a+b
#    print("val C:",c)
#elif(opt=="-"):
#    c=a-b
#    print("val C:",c)
#elif(opt=="/"):
#    c=a/b
#    print("val C:",c)
#elif(opt =="*"):
#    c=a*b
#    print("val C:",c)
#elif(opt=="%"):
#    c=a%b
#    if(c== 0):
#        print("EVEN")
#    else:
#          print("odd")
#    print("val C:",c)
#else:
#    print("invalid symboll")
    
#ifelse 8
#========

#scr=int(input("scre:"))
#if(scr>=70):
#    print("eligble give details")
#    a=input("name:")
#    b=int(input("Age:"))
#    c=input("ADDRESS:")
#    print("NAME:",a,"Age:",b,"Address:",c)
#else:
#    print("notelgible")

#ifelse 9
#========

#sal=int(input("salary:"))
#age=int(input("Age"))

#if(sal>=20000 or age<=25):
#    ln=int(input("loan amt:"))
#    if(ln<=50000):
#        print("eligible for loan")
#   else:
#        print("not eligible for loan")

#else:
#    print("sal or age not meet for loan")
    
#ifelse 10
#=========

a=int(input("SUB1:"))
b=int(input("SUB2:"))
c=int(input("SUB3:"))
d=int(input("SUB4:"))
e=int(input("SUB5:"))
print("marks",a,b,c,d,e)
f=(a+b+c+d+e)/5
if(f < 35 ):
    print("class req",f)
else:
    print("not req",f)










