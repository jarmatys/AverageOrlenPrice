import urllib.request
import datetime

#ustalamy parametry wyszukiwania
FuelType = "ONEkodiesel"
Year = "2018"

#Pobieramy stronę orlena z danymi na temat ceny paliw na dany dzień i konwertujemy na tekst
response = urllib.request.urlopen('https://www.orlen.pl/PL/DlaBiznesu/HurtoweCenyPaliw/Strony/archiwum-cen.aspx?Fuel='+FuelType+'&Year='+Year)
html = response.read()
done = str(html,"utf-8")

dates = []
prices = []

#Konwertujemy dane, wyciągamy według zależności daty i ceny, a nastepnie umieszczamy je w listach dates i prices
temp = []
for sign in done:

    if sign.isdigit() or sign == "-" or sign == " ":
        temp.append(sign)

    #By wykryć datę w ciągu znaków, należy rozpoznać spację a następnie sprawdzić czy ilość liczb w tymczasowym słowniku jest równa 15
    if sign == " ":
        if(len(temp) != 15):
            temp.clear()
        else:
            #Konwertujemy datę na objekt datetime i zapisujemy do listy dates
            date_time_str = "".join(temp[0:10])
            date_time = datetime.datetime.strptime(date_time_str, '%d-%m-%Y')
            dates.append(date_time.date())
            #Zapisujemy cenę do listy prices
            prices.append(int("".join(temp[10:14])))

#Łączymy dane w słownik
data_dict = dict(zip(dates,prices))

#Prosimy uzytkownika o wpisane przedziału czasowego
DateFrom = input("Podaj datę od której chcesz liczyć(DD-MM-RRRR): ")
DateTo = input("Podaj datę do której chcesz liczyć(DD-MM-RRRR): ")

DateFromObj = datetime.datetime.strptime(DateFrom,'%d-%m-%Y').date()
DateToObj = datetime.datetime.strptime(DateTo,'%d-%m-%Y').date()

#Liczymy średnią w przedziale wzorem na średnią arytmetyczną
AveragePrice = 0
LoopCounter = 0
for date,price in data_dict.items():
    if(date >= DateFromObj and date <= DateToObj):
        AveragePrice += price
        LoopCounter += 1
#Poinformuj użytkownika o liczbę dni z jego przezdziału
print("\nLiczone dla: "+ str((DateToObj-DateFromObj).days)+" dni.")

#Pokazujemy wynik dla użytkownika
print("\nŚrednia cena w przedziale: "+ str(DateFromObj) + " <-> " + str(DateToObj) + " | Wynosi: "+ str(round(AveragePrice/LoopCounter,2))+"\n")

