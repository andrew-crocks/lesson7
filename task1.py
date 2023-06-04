def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

person_name = input("Введіть ваше ім'я: ")
person_age = int(input("Введіть ваш вік: "))

greeting = say_hi(person_name, person_age)
print(greeting)