#string and numeric values can operate together with *
A,B=2,3
Txt="@"
print(2*Txt*3)

#string and string can operate with +
A,B="2",3
Txt="@"
print((A+Txt)*B)  #concatenation of string with +

#numeric values can operate with all arithmetic operators
A,B=2,3
C=4
print(A+B*C)

#Arithmetic expression with intefer and float will result in float
A,B=10,5.0
C=A*B     #becomes float
print(C)

#Result of division operatore with two integers will be float
A,B=1,2
C=A/B
print(C)

#integer division --gives final result as integer(closest-lesser or equal).
#                 --with float gives integer value in terms of float(5.0).

A,B=1.5,3
D=5
C=A//B
print(C,D//B,A/B)

#modular division --gives remaider
#                 --remainder is negative when denominator is negative.

a,b=-5,2
c=a%b
print(c)

a,b=-5,-2
c=a%b
print(c)