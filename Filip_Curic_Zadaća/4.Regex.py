import re

unesi = input("Unesite string:")
regex = '^r+.*r+$'
prvi_uvjet = re.match(regex,unesi)

regex_2 = '[0-5]'
drugi_uvjet = re.search(regex_2, unesi)

regex_3 = '\s'
treci_uvjet = re.search(regex_3, unesi)

if prvi_uvjet and drugi_uvjet and treci_uvjet:
    print("ispravno")
