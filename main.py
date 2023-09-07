# pobierać dane o osobie:
# - imię, nazwisko, pesel
# - zapisać dane użytkownika takie jak płeć oraz datę urodzenia jako zmienne
# - umożliwić danych zapis do pliku
# - umożliwić odczyt danych z pliku
# - stworzyć menu, w któym użytkownik będzie mógł dodawać nowe osoby, odczytywać ich dane, oraz zapisywać/wczytywać dane z pliku

class Osoba:
    def __init__(self, imie='', nazwisko='', pesel=''):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__pesel = self.sprawdz(pesel)
        self.__plec = self.getPlec()
        self.__dataurodzin = self.getData()

    def getData(self, pesel=None):
        if pesel is None:
            pesel = self.__pesel
        rok = 1800
        mieschk = int(pesel[2:4]) // 10
        miesidx = 2
        while True:
            rok += 100
            if mieschk < miesidx:
                rok += int(pesel[:2])
                mies = int(pesel[2:4]) - 10 * (miesidx - 2)
                break
            miesidx += 2
        dzien = int(pesel[4:6])
        return {"d": dzien, "m": mies, "r": rok}

    def getPlec(self, pesel=None):
        if pesel is None:
            pesel = self.__pesel
        return "kobieta" if int(pesel[10]) % 2 == 0 else "mężczyzna"

    def getPesel(self):
        return self.__pesel

    #pobierzImie
    #pobierzNazwisko
    #pobierzDate - spróbować uzwględnić datę US
    #pobierzPlec - potencjalnie jest

    def sprawdz(self, pesel=None):
        # c1·1 + c2·3 + c3·7 + c4·9 + c5·1 + c6·3 + c7·7 + c8·9 + c9·1 + c10·3 + c11·1
        if pesel is None:
            pesel = self.__pesel

        return pesel if str(int(pesel[0]) * 1 + int(pesel[1]) * 3 + int(pesel[2]) * 7 + int(pesel[3]) * 9 +
                            int(pesel[4]) * 1 + int(pesel[5]) * 3 + int(pesel[6]) * 7 + int(pesel[7]) * 9 +
                            int(pesel[8]) * 1 + int(pesel[9]) * 3 + int(pesel[10]) * 1)[-1] == '0' else False

    def __str__(self):
        return f"{self.__imie};{self.__nazwisko};{self.__plec};{self.__pesel};" \
               f"{('0' if self.__dataurodzin['d'] < 10 else '') + str(self.__dataurodzin['d'])}-" \
               f"{('0' if self.__dataurodzin['m'] < 10 else '') + str(self.__dataurodzin['m'])}-" \
               f"{str(self.__dataurodzin['r'])}"
#MM/DD/RRRR
#08/23/1997

class Osoby:
    def __init__(self, *osoba:Osoba):
        self.__lista = list(osoba)

    def dodaj(self, osoba:Osoba):
        self.__lista.append(osoba)

    def pobierz(self, index:int=0):
        return self.__lista[index]

    def pobierz(self, szukaj:str):
        for o in self.__lista:
            if o.getPesel() == szukaj:
                return o
        return None

    def zapiszPlik(self, nazwa = None):
        if nazwa is None:
            nazwa = "undefined.txt"
        with open(nazwa,"wt") as f:
            for o in self.__lista:
                f.write(str(o) + "\n")

    def odczytPlik(self, nazwa = None):
        self.__lista = []
        if nazwa is None:
            nazwa = "undefined"
        with open(nazwa, "r+") as f:
            for linia in f:
                tmp = linia.split(";")
                self.__lista.append(Osoba(tmp[0], tmp[1], tmp[3]))

    def __str__(self):
        ret = ""
        for o in self.__lista:
            #zmienić wyświetlanie na coś w rodzaju:
            #Dane osobowe:
            #Imię: {imię} <- o.pobierzImie()
            #Nazwisko: {nazwisko} <- o.pobierzNazwisko()
            #Płeć: {plec} <- o.pobierzPlec()
            #Data urodzenia: {dataurodzenia} <- o.pobierzDateUrodzenia()
            ret += str(o) + ", "
        return ret


osoby = Osoby(Osoba('Janina', 'Cichecka', '49050756486'), Osoba('Karolina', 'Zajdel', '99100334148'))
osoby.dodaj(Osoba('Jarosław', 'Rudlicki', '04321469973'))

print(osoby.pobierz('04321469973'))

osoby.zapiszPlik("mojabaza.txt")
osoby.odczytPlik("mojabaza.txt")

print(osoby)


noweosoby = Osoby()
noweosoby.odczytPlik("mojabaza.txt")
print(osoby)

#pesel = ('04321469973',
#         '86030169513',
#         '81101524211',
#         '80042171515',
#         '49050756486',
#         '99100334148',
#         '78103099661',
#         '62051517236',
#         '70111332831',
#         '57032997118')

