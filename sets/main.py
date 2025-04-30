#tworzenie setów z danymi o różnym typie

fruits = {"jabłko", "pomarańcza", "śliwka"}
numbers = {3, 4, 6, 9}
logic = {True, False}
mixed = {True, 9, "krzesło"}
list = ["monitor", "myszka"]


#tworzenie setu za pomocą konstruktora

setcConstructor = set((" pomidor", "marchew", "papryka"))

#sprawdzanie typu zmiennej fruits

print(type(fruits))

#sprawdzanie długosci sety 

print(len(numbers))

#rozszerzanie setu o inny set

mixed.update(numbers)
print(mixed)
logic.update(list)
print(logic)

#dodawanie elementów do setu

fruits.add("kiwi")
print (fruits)

#usuwanie danej z setu

logic.remove(True)
print(logic)
logic.discard("myszka")
print(logic)

#usuwanie losowej danej z setu

print(numbers)
numbers.pop()
print(numbers)

#czyszczenie setu

logic.clear()
print(logic)

#usuwanie setu z pamięci

del logic


#łączenie dwóch setów
fruitsNumbers = fruits.union(numbers)
print(fruitsNumbers)

mixedLogic = mixed | numbers
print(mixedLogic)
