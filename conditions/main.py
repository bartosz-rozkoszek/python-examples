a = 10
b = 5

#struktura warunków w pythonie

if a > b:
    print("a jest większe od b")
elif a < b:
    print("a jest mniejsze od b")
else: 
    print("a i b są równe")

# warunek jednoliniowy

print("a i b są równe") if a == b else print("a i b nie są równe")

# warunek z łącznikiem and i gdy oba dostają true to wyświetli sie komunikat

if b >= 5 and a <= 10:
    print("a jest mniejsze lub równe 10 a b jest wieksze lub równe 5 ")

#warunek z łącznikiem or gdy jeden jest prawidłowy to wyświetli sie komunikat

if a != 10 or b > 3:
    print("a nie jest równe 10 lub b jest większe od 3")

#warunek z argumentem pass używany jest gdy deklarujemy warunek bez jego ciała

if b > a:
    pass

#sprawdzenie czy element jest w liscie

fruits = ["jabłko","pomarańcza","śliwka"]
if "jabłko" in fruits:
    print("jabłko znajduje się w liście owoce")

    #sprawdzenie za pomocąwarunku czy dany element istnieje w liście

    car = {
        "producent": "bmw",
        "model": "e46"
    }

#sprawdzanie za pomocą warunku czy klucz istnieje w słowniku i czy zawiera wartość e36

    if "model" in car:
        print("w słowniku określony jest model")
        if car["model"] == "e36":
            print("modelem auta jest e36")
