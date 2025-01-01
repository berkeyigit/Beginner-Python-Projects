
#Sınıf olusturuyor ve altına functionları giriyoruz
class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add (self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 - self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("Sifira bölme yapilamaz. ")
    
#Sayilari aliyoruz
num1 = float(input("Lütfen birinci sayiyi giriniz : "))
num2 = float(input("Lütfen ikinci sayiyi giriniz : "))

calc = Calculator(num1,num2)

print("Yapmak istediginiz islemi secin : \n1. Toplama\n2. Cikarma\n3. Carpma\n4. Bölme")
operation = input("Seciminizi yapiniz(1/2/3/4) : ")

#Kosul ile girilen inputa gore islem functionunu cagiriyoruz.
if operation == "1":
    result = calc.add()
    print(f"Sonuç : {result}")
elif operation == "2":
    result = calc.subtract()
    print(f"Sonuç : {result}")
elif operation == "3":
    result = calc.multiply()
    print(f"Sonuç : {result}")
elif operation == "4":
    result = calc.divide()
    print(f"Sonuç : {result}")
else:
    print("Gecersiz secim")