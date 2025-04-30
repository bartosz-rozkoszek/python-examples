car = {
    "producent": "toyota",
    "model": "corolla",
    "rocznik": 2003,
    "bite": False
}

# sprawdzenie ilosci elemantów słownika

print(len(car))

#sprawdzenie typu zmiennej car

print(type(car))
#tworzenie słownika za pomocą konstruktora
dictConstructor = dict(producent = "BMW", Model = "E36", rocznik = 1998, bite = True)

#wyciąganie ze słownika wartosci o kluczu model

print(car["model"])

#wyciąganie ze słownika wartosci o kluczu producent

print(car.get("producent"))

#wyświetlanie nazw kluczy

print(car.keys())

# przypisanie do klucza model wartosci e46

dictConstructor["model"] = "E46"
print(dictConstructor)

#sprawdzanie wartosci słownika

print(car.values())

#wyświetlenie zbiorów wartosci klucz : wartość w słowniku

print(car.items())

# dodanie nowej danej do słownika
car.update({"kolor": "srebrny"})
print(car)

car["przebieg"] = 140000
print(car)

#usuwanie elemantu o kluczu kolor

car.pop("kolor")
print(car)

#usunięcie ostatnio dodanego elementu

car.popitem()
print(car)

#wyczyszczenie słownika

dictConstructor.clear()
print(dictConstructor)

#skopiowanie słownika do nowej zmiennej

newCar = car.copy()
newCar2 = dict(car)


cars = {
    "auto1": {
        "producent": "toyota",
        "model": "yaris",
        "rocznik": 2007
    }
    "auto2": {
        "producent": "bmw",
        "model": "E36",
        "rocznik": 2003

    }
    "auto3": {
        "producent": "fiat",
        "model": "punto",
        "rocznik": 2010
    }
}
print[cars["auto2"]]