#  ������-1: ���� ������������ ����� ����� (����� ������� ����������).
# ������� ���������� ����� ��������� ����� (������� ������ ���� �������).
# ���������:
# * ������������ ������ ������ � ����������� ���������� � ����� while;
# * ��� ������� ������ ������ � ����������� ����� for.


number = int(input('Enter a number '))
i = 0
while i < len(number):
print(number[i])
i += 1
print("The programm has been successfully executed")
	
	
#or ***to complete***
number = int(input('Enter a number '))
for i in number:
i = 0
    print(number[i])
	i += 1
print("The programm has been successfully executed")
	
    

# ������-2: �������� �������� ���� ���������� ��������� � ������������.
# �������� �������� ���������� �������. ������� ����� �������� �� �����.
# ���������:
# * ������������ ������� ������� ����� �������������� ���������� 
#   ��� ����� �������������� ��������
# �� ����� ������ ������ ���:
# print("a = ", b, "b = ", a) - ��� ������������ �������!

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
print("a = " , a, " b = " , b)
a,b = b,a
print(" a = ", a, " b = ", b)

#or

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
print("a = " , a, " b = " , b)
c = a
print("c = " , b, " b = " , c)

# ������-3: ��������� � ������������ ��� �������.
# ���� ��� ���� 18 ���, ��������: "������ ��������",
# ����� "��������, ����������� ������ �������� ������ � 18 ���"

user_age = "18"
permission = int(input("Enter your age: "))
if permission >= int(user_age):
    print("You are welcome to use our service")
else:
    print("Sorry, the service is not avaliable for people under 18")

#or
user_age = int(input("Enter your age: "))
if user_age < 18:
    access = False
    print("Sorry, the service is not avaliable for people under 18")
	
else:
    access = True	
    print("You are welcome to use our service")
    
	
	
	
# homework/ normal

# ������-1: ���� ������������ ����� �����, ������� ����� ������� ����� ����� �����.
# ��������, ������ x = 58375.
# ����� ������� ������������ ����� � ������ �����, �.�. 8.
# ���������������, ��� �� �� ����� ��� ����� �������.
# ����� �������� � ���� ������ ������������.
# ���������:
# * ������������ ������ ������ � ����������� ���������� � ����� while;
# * ��� ������� � ��������� ������ ������ � ����������� ����� for.

x = 98765
print("Max number in the string" , x, end = " ")
max_number = 9
while True:
    if max_number = 9:
        break
else:
        continue
    print(max_number)
	max_number +=1


#or

x = 98765
print("Max number in the string" , x, end = " ")
max_number = 9
max_number = str(x)
for digit in x:
print(digit)

# ������-2: �������� �������� ���� ���������� ��������� � ������������.
# �������� �������� ���������� �������. ������� ����� �������� �� �����.
# ������ ������, ��������� ������ ��� ����������.
# ���������:
# * ������������ ������� ������� ����� �������� ��� �������;
# * ��� ������� � ��������� �������������� ����������� �������� Python.
   

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
a = b
b = a
print(a,b)
  
# ������-3: �������� ���������, ����������� ����� ����������� ��������� ����
# ax** + bx + c = 0.
# ������������ ��������� �������� �������������.
# ��� ���������� ����������� ����� �������������� �������� sqrt() ������ math:
# import math
# math.sqrt(4) - ��������� ������ ����� 4

import math

ax** + bx + c = 0


 a = int(input("Enter number for a "))
 x = int(input("Enter number for x"))
 b = int(input("Enter number for b"))
 c = int(input("Enter number for c"))
 
 








# �������-1:
# ���� ������ ��������� �������� � �������������� � ������� ����������:
# 	���: a == a**2
# 	���������: True
# 	���: a == a*2
# 	���������: True
# 	���: a > 999999
# 	���������: True

# ������: ���� ���� ����� ���������� a,
# ���� ����� ��������, ��� � �������� �� ����������? 

bool True False
bool= False if
bool (0)
bool (' ')
bool (False)

# ��� ���� �������� �������� a > 999999  bool = True
 

	
