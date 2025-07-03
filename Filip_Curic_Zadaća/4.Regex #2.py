import re

mail = input("Unesi mail adresu: ")
regex_1 = "[a-zA-Z]+[a-zA-Z]+@fpmoz.sum.ba$"
mail_provjera = re.findall(regex_1,mail)

print(mail_provjera)

eduid = input("Unesi eduId: ")
regex_2 ="^[a-zA-Z][a-zA-Z]+[0-9]*@sum.ba$"
eduid_provjera = re.findall(regex_2,eduid)

print(eduid_provjera)

if mail_provjera and eduid_provjera:
    print("Mail i eduId su ispravni!")
