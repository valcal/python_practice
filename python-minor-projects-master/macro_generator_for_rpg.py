'''
Generator makr do roll20.
Revision: 29.12.2020
Developed by: Marcin Mierzejewski
'''
# Imports and declarations

from random import randint
import os

finish = 0

def generate_input_data(imie):
    umiejetnosci_wejsciowe = []
    akcje_wejsciowe = []
    f = open("lista_umiejetnosci.txt", "r", encoding='utf8')
    f1 = f.readlines()
    for x in f1:
            umiejetnosci_wejsciowe.append(x.rstrip("\n"))
    f.close()
    f = open("lista_akcji.txt", "r", encoding='utf8')
    f1 = f.readlines()
    for x in f1:
        akcje_wejsciowe.append(x.rstrip("\n"))
    f.close()
    f = open("{} makra.txt".format(imie), "w+")
    f.write("----- {} - Umiejętności wejściowe: -----\n\n".format(imie))
    for line in umiejetnosci_wejsciowe:
        f.write("{}\n".format(line))
    f.write("\n\n----- {} - Akcje wejściowe: -----\n\n".format(imie))
    for line in akcje_wejsciowe:
        f.write("{}\n".format(line))
    f.write('\n\n')
    f.close()
    print("\nDane wejsciowe wyexportowane!\n")

# Funkcja odpowiedzialna za generowanie makra na testy cech i ich modyfikatorów.
def generate_attributes_macro(imie):
    lista_cech = ['Siła', 'Wytrwałość', 'Zręczność', 'Spostrzegawczość', 'Inteligencja', 'Siła Woli', 'Charyzma', 'Szczęście', 'Umiejętności Bojowe', 'Umiejętności Strzeleckie', 'Talent Magiczny', 'Przeznaczenie']
    znaki = ['{', '}']
    makro = ['?{Wybierz cechę|' + '\n']
    for cecha in lista_cech:
        makro.append('{} [@{}{}{}],{} - test cechy {}:\n'.format(cecha, znaki[0], cecha, znaki[1], imie, cecha) + '/r @{' + '{}'.format(cecha) + '} - 1d20 + ?{Modyfikator')
        if cecha == 'Siła' or cecha == 'Wytrwałość' or cecha == 'Zręczność' or cecha == 'Umiejętności Bojowe' or cecha == 'Umiejętności Strzeleckie':
            makro.append('&#125; + @{selected|bar1} ')
        elif cecha == 'Spostrzegawczość' or cecha == "Inteligencja" or cecha == 'Siła Woli' or cecha == 'Talent Magiczny':
            makro.append('&#125; + @{selected|bar2} ')
        elif cecha == 'Charyzma':
            makro.append('&#125; + @{selected|bar3} ')
        elif cecha == 'Szczęście':
            makro.append('&#125; ')
        if cecha == 'Przeznaczenie':
            makro.append('&#125; }')
        else:
            makro.append('|\n')
        if cecha != "Przeznaczenie":
            makro.append('{} - Mod [@{}{}|{}|max{}],{} - test modyfikatora cechy {}:'.format(cecha, znaki[0], imie, cecha, znaki[1], imie, cecha) + '\n' + '/r @{' + '{}|{}|max'.format(imie, cecha) + '} - 1d20 + ?{Modyfikator')
            if cecha == 'Siła' or cecha == 'Wytrwałość' or cecha == 'Zręczność' or cecha == 'Umiejętności Bojowe' or cecha == 'Umiejętności Strzeleckie':
                makro.append('&#125; + @{selected|bar1} |\n')
            elif cecha == 'Spostrzegawczość' or cecha == "Inteligencja" or cecha == 'Siła Woli' or cecha == 'Talent Magiczny':
                makro.append('&#125; + @{selected|bar2} |\n')
            elif cecha == 'Charyzma':
                makro.append('&#125; + @{selected|bar3} |\n')
            elif cecha == 'Szczęście':
                makro.append('&#125; |\n')
    f = open("{} makra.txt".format(imie), "a")
    f.write("----- Test Cechy -----\n\n")
    for line in makro:
        f.write("{}".format(line))
    f.write('\n\n')
    f.close()
    print("\nMakro cech wyexportowane!\n")

# Funkcja odpowiedzialna za generowanie makra na testy umiejętności na bazie zaimportowanej listy z pliku txt.
def generate_skills_macro(imie):
    lista_umiejetnosci = []
    umiejetnosc_zestaw = []
    f = open("lista_umiejetnosci.txt", "r", encoding='utf8')
    f1 = f.readlines()
    for x in f1:
        umiejetnosc_zestaw.append(x.rstrip("\n"))
        if len(umiejetnosc_zestaw) == 2:
            lista_umiejetnosci.append(umiejetnosc_zestaw)
            umiejetnosc_zestaw = []
    f.close()
    print("Lista umiejętności zaimportowana.")
    print("Zaimportowane umiejętności:\n")
    liczba_umiejetnosci = len(lista_umiejetnosci)
    for number in range(0, liczba_umiejetnosci):
        print("{} - cecha odpowiadająca: {}".format(lista_umiejetnosci[number][0], lista_umiejetnosci[number][1]))
    makro = ['?{Wybierz umiejętność|' + '\n']
    znaki = ['{', '}']
    for umiejetnosc in lista_umiejetnosci:
        makro.append('{} [@{}{}{}],{} - test umiejętności {}:'.format(umiejetnosc[0], znaki[0], umiejetnosc[0], znaki[1], imie, umiejetnosc[0]) + '\n' + '/r @{' + '{}'.format(umiejetnosc[0]) + '} - 1d20 + ?{Modyfikator')
        if umiejetnosc[1] == 'Siła' or umiejetnosc[1] == 'Wytrwałość' or umiejetnosc[1] == 'Zręczność' or umiejetnosc[1] == 'Umiejętności Bojowe' or umiejetnosc[1] == 'Umiejętności Strzeleckie':
            makro.append('&#125; + @{selected|bar1} ')
        elif umiejetnosc[1] == 'Spostrzegawczość' or umiejetnosc[1] == "Inteligencja" or umiejetnosc[1] == 'Siła Woli' or umiejetnosc[1] == 'Talent Magiczny':
            makro.append('&#125; + @{selected|bar2} ')
        elif umiejetnosc[1] == 'Charyzma':
            makro.append('&#125; + @{selected|bar3} ')
        elif umiejetnosc[1] == 'Szczęście':
            makro.append('&#125; ')
        if umiejetnosc[0] == lista_umiejetnosci[-1][0]:
            makro.append('}')
        else:
            makro.append('|\n')
    f = open("{} makra.txt".format(imie), "a")
    f.write("----- Test Umiejętności -----\n\n")
    for line in makro:
        f.write("{}".format(line))
    f.write('\n\n')
    f.close()
    print("\nMakro umiejętności wyexportowane!\n")

# Funkcja odpowiedzialna za generowanie makra na testy umiejętności przy użyciu punktu szczęścia na bazie zaimportowanej listy z pliku txt.
def generate_skills_luck_macro(imie):
    lista_umiejetnosci = []
    umiejetnosc_zestaw = []
    f = open("lista_umiejetnosci.txt", "r", encoding='utf8')
    f1 = f.readlines()
    for x in f1:
        umiejetnosc_zestaw.append(x.rstrip("\n"))
        if len(umiejetnosc_zestaw) == 2:
            lista_umiejetnosci.append(umiejetnosc_zestaw)
            umiejetnosc_zestaw = []
    f.close()
    print("Lista umiejętności zaimportowana.")
    print("Zaimportowane umiejętności:\n")
    liczba_umiejetnosci = len(lista_umiejetnosci)
    for number in range(0, liczba_umiejetnosci):
        print("{} - cecha odpowiadająca: {}".format(lista_umiejetnosci[number][0], lista_umiejetnosci[number][1]))
    makro = ['?{Wybierz umiejętność|' + '\n']
    znaki = ['{', '}']
    for umiejetnosc in lista_umiejetnosci:
        makro.append('{} - szczęście [@{}{}|{}|max{}],{} - test umiejętności {} z użyciem Punktu Szczęścia:'.format(umiejetnosc[0], znaki[0], imie, umiejetnosc[0], znaki[1], imie, umiejetnosc[0]) + '\n' + '/r @{' + '{}|{}|max'.format(imie, umiejetnosc[0]) + '} - 1d20 + ?{Modyfikator')
        if umiejetnosc[1] == 'Siła' or umiejetnosc[1] == 'Wytrwałość' or umiejetnosc[1] == 'Zręczność' or umiejetnosc[1] == 'Umiejętności Bojowe' or umiejetnosc[1] == 'Umiejętności Strzeleckie':
            makro.append('&#125; + @{selected|bar1} ')
        elif umiejetnosc[1] == 'Spostrzegawczość' or umiejetnosc[1] == "Inteligencja" or umiejetnosc[1] == 'Siła Woli' or umiejetnosc[1] == 'Talent Magiczny':
            makro.append('&#125; + @{selected|bar2} ')
        elif umiejetnosc[1] == 'Charyzma':
            makro.append('&#125; + @{selected|bar3} ')
        elif umiejetnosc[1] == 'Szczęście':
            makro.append('&#125; ')
        if umiejetnosc[0] == lista_umiejetnosci[-1][0]:
            makro.append('}')
        else:
            makro.append('|\n')
    f = open("{} makra.txt".format(imie), "a")
    f.write("----- Test Umiejętności - Szczęście -----\n\n")
    for line in makro:
        f.write("{}".format(line))
    f.write('\n\n')
    f.close()
    print("\nMakro umiejętności - test szczęścia wyexportowane!\n")

# Funkcja odpowiedzialna za generowanie makra na akcje natychmiastowe.
def generate_instant_actions_macro(imie):
    lista_akcji = [['Ruch','1'], ['Skok','3'], ['Doskok','2'], ['Legnięcie','2'], ['Powstanie','3'], ['Chwyt','1'], ['Wyciągnięcie/Schowanie Przedmiotu','2'], ['Przygotowanie','3']]
    znaki = ['{', '}']
    makro = ['?{Wybierz akcję|' + '\n']
    for akcja in lista_akcji:
        makro.append('{} [{} PA],{} - wykonuje akcję {}: [[{} &{}tracker:-&#125;]]'.format(akcja[0], akcja[1], imie, akcja[0], akcja[1], znaki[0]))
        if akcja == lista_akcji[-1]:
            makro.append('}')
        else:
            makro.append('|\n')
    f = open("{} makra.txt".format(imie), "a")
    f.write("----- Akcje Natychmiastowe -----\n\n")
    for line in makro:
        f.write("{}".format(line))
    f.write('\n\n')
    f.close()
    print("Makro akcji natychmiastowych wyexportowane!\n")

# Funkcja odpowiedzialna za generowanie makra na stałe akcje deklarowane.
def generate_declared_actions_macro(imie):
    lista_akcji = []
    akcja = []
    f = open("lista_akcji.txt", "r", encoding='utf8')
    f1 = f.readlines()
    for x in f1:
        akcja.append(x.rstrip("\n"))
        if len(akcja) == 3:
            lista_akcji.append(akcja)
            akcja = []
    f.close()
    print("Lista akcji zaimportowana.")
    print("Zaimportowane akcje:\n")
    liczba_akcji = len(lista_akcji)
    for number in range(0, liczba_akcji):
        print("{}".format(lista_akcji[number]))
    makro = ['?{Wybierz akcję|' + '\n']
    znaki = ['{', '}']
    for akcja in lista_akcji:
        makro.append('{} [{}PA],{} deklaruje akcję {}. [[{} &{}tracker:-&#125;]]'.format(akcja[0], akcja[1], imie, akcja[0], akcja[1], znaki[0]))
        if akcja == lista_akcji[-1]:
            makro.append('}')
        else:
            makro.append('|\n')
    f = open("{} makra.txt".format(imie), "a")
    f.write("----- Akcje Deklarowane -----\n\n")
    for line in makro:
        f.write("{}".format(line))
    f.write('\n\n')
    f.close()
    print("\nMakro akcji deklarowanych wyexportowane!\n")

# Funkcja odpowiedzialna za generowanie makra na test akcji deklarowanych.
def generate_declared_actions_tests_macro(imie):
    lista_akcji = []
    akcja = []
    f = open("lista_akcji.txt", "r", encoding='utf8')
    f1 = f.readlines()
    for x in f1:
        akcja.append(x.rstrip("\n"))
        if len(akcja) == 3:
            lista_akcji.append(akcja)
            akcja = []
    f.close()
    makro = ['?{Wybierz akcję|' + '\n']
    znaki = ['{', '}']
    for akcja in lista_akcji:
        makro.append('{} [@{}{}{}],{} testuje akcję {}:'.format(akcja[0], znaki[0], akcja[2], znaki[1], imie, akcja[0], akcja[1], akcja[1], znaki[0]) + '\n/r @{' + '{}'.format(akcja[2]) + '} - 1d20 + ?{Modyfikator&#125; + @{selected|bar1} ')
        if akcja == lista_akcji[-1]:
            makro.append('}')
        else:
            makro.append('|\n')
    f = open("{} makra.txt".format(imie), "a")
    f.write("----- Test Akcji Deklarowanych -----\n\n")
    for line in makro:
        f.write("{}".format(line))
    f.write('\n\n')
    f.close()
    print("Makro testów akcji deklarowanych wyexportowane!\n")

# Funkcja odpowiedzialna za generowanie makra na test akcji deklarowanych z użyciem punktu szczęścia.
def generate_declared_actions_tests_luck_macro(imie):
    lista_akcji = []
    akcja = []
    f = open("lista_akcji.txt", "r", encoding='utf8')
    f1 = f.readlines()
    for x in f1:
        akcja.append(x.rstrip("\n"))
        if len(akcja) == 3:
            lista_akcji.append(akcja)
            akcja = []
    f.close()
    makro = ['?{Wybierz akcję|' + '\n']
    znaki = ['{', '}']
    for akcja in lista_akcji:
        makro.append('{} - szczęście [@{}{}|{}|max{}],{} testuje akcję {} z użyciem Punktu Szczęścia:'.format(akcja[0], znaki[0], imie, akcja[2], znaki[1], imie, akcja[0], akcja[1], akcja[1], znaki[0]) + '\n/r @{' + '{}|{}|max'.format(imie, akcja[2]) + '} - 1d20 + ?{Modyfikator&#125; + @{selected|bar1} ')
        if akcja == lista_akcji[-1]:
            makro.append('}')
        else:
            makro.append('|\n')
    f = open("{} makra.txt".format(imie), "a")
    f.write("----- Test Akcji Deklarowanych - Szczęście -----\n\n")
    for line in makro:
        f.write("{}".format(line))
    f.write('\n\n')
    f.close()
    print("Makro testów akcji deklarowanych - test szczęścia wyexportowane!\n")

# Funkcja odpowiedzialna za generowanie makra na test inicjatywy.
def generate_initiative_macro(imie):
    znaki = ['{', '}']
    makro = ['{} - test Inicjatywy:'.format(imie) + '\n' + '/r @{}Inicjatywa{} - 1d20 + ?{}Modyfikator{} + @{}selected|bar1{}'.format(znaki[0], znaki[1], znaki[0], znaki[1], znaki[0], znaki[1])]
    f = open("{} makra.txt".format(imie), "a")
    f.write("----- Test Inicjatywy -----\n\n")
    for line in makro:
        f.write("{}".format(line))
    f.write('\n\n')
    f.close()
    print("Makro inicjatywy wyexportowane!\n")

# Blok główny programu
print("Generator makr postaci dla Roll20\n")
while finish != 1:
    print("Menu:")
    print("[1] Generuj makra")
    print("[2] Koniec\n")
    decision = input("Wybierz akcję:")
    if int(decision) == 1:
        imie = input("\nPodaj imie postaci:")
        generate_input_data(imie)
        generate_attributes_macro(imie)
        generate_skills_macro(imie)
        generate_skills_luck_macro(imie)
        generate_instant_actions_macro(imie)
        generate_declared_actions_macro(imie)
        generate_declared_actions_tests_macro(imie)
        generate_declared_actions_tests_luck_macro(imie)
        generate_initiative_macro(imie)
    elif int(decision) == 2:
        print("\n")
        print("Wybrałeć koniec.")
        finish = 1
        break
    else:
        print("\n")
        print("Wybierz poprawną opcję z menu.")
        print("\n")
