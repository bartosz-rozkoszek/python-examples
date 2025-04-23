# tupla zawierająca wartości tekstowe

fruits = ("jablko", "pomarancza", "sliwka")

# tupla zawierająca liczby

numbers = (5,8,2,6,9)

# tupla zawierająca wartości logiczne

logic = (True, False, True)

# tupla zawierająca wartości mieszane

mixed = (True, "jablko", 5)

# tworzenie tupli za pomocą konstruktora

tuple_constructor = tuple(("krzeslo", "stolik", "monitor"))

# sprawdzenie typu zmiennej tuple_constructor

print(type(tuple_constructor))

#dostęp do danych tupli za pomocą 

print(fruits[0])
print(fruits[-1])
print(fruits[2:4])
print(fruits[:3])
print(fruits[2:])

#zmiana wartości tupli za pomocą konwesji listy ponieważ tupla nie jest modyfikowana
x = list(fruits)
print(type(fruits))
print(type(x))
x[0] = "kiwi"
fruits = tuple(x)
print(fruits)
print(type(fruits))

#dodawanie danych do tupli poprzez konwersji 

y = list(fruits)
y.append("jablko")
fruits = tuple(y)
print(fruits)

# usuwanie danej do  tupli za pomocą konwersji

z = list(tuple_constructor)
z.remove("monitor")
tuple_constructor = tuple(z)
tuple_constructor

#destrukturyzowanie tupli czyli przypisywanie wartosci tupli do zmiennych

print(fruits)
(kiwi, orange, plum, apple) = fruits 
print(kiwi)
print(orange)
print(plum)
print(apple)

#destrukturyzacja przypisywanie zbiorów wartosci do tablicy

(first, second, *more) = numbers
print(first)
print(second)
print(more)

#łączonie dwóch tupli w jedną nową tuple

twotuples = numbers + logic
print(twotuples)

#zapisanie do nowej tupli zdwojonej tupli

logic2 = logic *2
print(logic2)

#metoda count umożliwia zliczenie wystąpień danej wartosci

print(logic2.count(True))

#metodaindex umożliwia uzyskanie informacji na którym miejscu w tupli znajduje sie dana wartość

print(numbers.index(5))