# komentarze
x = 5 #zmienna przechowuje liczbe całkowitą (int)
name = "bartek" #zmienna przechowuje ciąg znaków (string)
is_human = True #zmienna przechowuje wartosc logiczną (bool)

#przykłady deklaracji zmiennych
text = "to jest ciąg znaków"
number = 25
float_variable = 2.4
logic_variable = True

#sprawdzenie tykow zmiennych

print(type(text)) #str
print(type(number)) #
print(type(float_variable))
print(type(logic_variable))


color, is_fruit, quantity = "red", True, 2

#przypisywanie dwoch zmiennych do tej samej wartosci

j = k = "jabłko"
print(j, k)

#wyswietlanie zawartosci zmiennych

print(color)
print(is_fruit)
print(quantity)

#laczenie ciagow znakow

first_part = "SLI"
second_part = "MAK"
full_text = first_part + second_part
print(full_text)

#zmiana typów zmiennych

string_age = "10"
int_age = int(string_age) #konwersja string do int
print(type(string_age))
print(type(int_age))

int_quantity = 5
float_quantity = float(int_quantity) #konwersja int na float
print(type(int_quantity))
print(type(float_quantity))

int_height = 180
string_height = str(int_height) #konwersja int na str
print(type(int_height))
print(type(string_height))

#usunięcie zmiennej z pamięci

del_variable = 10
print(del_variable)
del del_variable
print(del_variable) #błąd, nie ma zmiennej w pamięci


