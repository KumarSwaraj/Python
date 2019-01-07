Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[]
>>> for i in range(2000, 3201):
	if (i%7==0) and (i%5!=0):
		l.append(str(i))
