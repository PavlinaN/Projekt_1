# Seznam registrovanych uzivatelu
text = """
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+"""
cara = '_'*60

vycisteny_text = []
for slovo in text.split():
    if slovo.isalnum() == 1:
        vycisteny_text.append(slovo)

users = {}

for i in range(2,len(vycisteny_text),2):
    users[vycisteny_text[i]] = vycisteny_text[i + 1]
print(users)

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


# Prihlaseni
name = input('username: ')
password = input('password: ')
print(cara)
registered = users.get(str(name)) == password

if not registered:
    print('Unfortunately, you`re not registrated, terminating the program!')
    print(cara)
else:
    print('Welcome to the app, ' + name.capitalize() + '! \nWe have 3 texts to be analyzed.\n' + cara)
    # vybrat mezi třemi texty

    vyber = (input('Enter a number btw. 1 and 3 to select: '))

    print(cara)

    if not vyber.isnumeric():
        print('No number entered, terminating the program!')
        print(cara)

    else:

        vyber_cislo = int(vyber) - 1

        vyber_textu = [*range(len(TEXTS))]

        if vyber_cislo not in vyber_textu:
            print('This number is not in the allowed range, terminating the program!')
            print(cara)
        else:

    #Analyza textu - rozdeleni a ocisteni

            vybrany_text = TEXTS[int(vyber)-1]
            pripraveny_text = []

            for slovo in vybrany_text.split():
                pripraveny_text.append(slovo.strip(".:;,"))

            dicti = {}
    # počet slov
            for slovo in pripraveny_text:
                if slovo not in dicti:
                   dicti[slovo] = 1
                else:
                    dicti[slovo] +=1
            pocet_slov = sum(dicti.values())
            print('There are ' + str(pocet_slov) + ' words in the selected text.')

    # počty slov a cislic
            velke_pismeno = 0
            kapitalky = 0
            male_pismeno = 0
            cisla = {}

            for slovo in pripraveny_text:
                if str(slovo).istitle():
                    velke_pismeno = int(velke_pismeno) + 1
                if str(slovo).isupper():
                    kapitalky = int(kapitalky) + 1
                if str(slovo).islower():
                    male_pismeno = int(male_pismeno) + 1
                if slovo.isnumeric():
                    if slovo not in cisla:
                        cisla[slovo] = 1
                    else:
                        cisla[slovo] += 1
            print('There are ' + str(velke_pismeno) + ' titlecase words.')
            print('There are ' + str(kapitalky) + ' uppercase words.')
            print('There are ' + str(male_pismeno) + ' lowercase words.')
    #suma_cisel, hodnota_cisel)
            pocet_cisel = sum(cisla.values())
            print('There are ' + str(pocet_cisel) + ' numeric strings')
            hodnota_cisel = 0
            for key in cisla:
                hodnota_cisel += int(key)
            print('The sum of all the numbers is: ' + str(hodnota_cisel))
            print(cara)
    #zjisteni delky slov
            dicti2 = {}
            for slovo2 in pripraveny_text:
                if len(slovo2) not in dicti2:
                    dicti2[len(slovo2)] = 1
                else:
                    dicti2[len(slovo2)] += 1

    #tisk grafu

            order = 0

            max_len = max(dicti2.keys()) + 5
            print('LEN' + '\t|OCCURENCES' + (max_len - 10) * ' ' + '|NR.\n ' + cara)
            for key in dicti2.keys():
                order += 1
                print(str(order) + '\t|' + ('*'* key ) + (max_len - key) * ' ' + '|' + str(dicti2[key]))


