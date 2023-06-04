def second_index(string, substring):
    first_index = string.find(substring)
    if first_index == -1:
        return None
    second_index = string.find(substring, first_index + 1)
    if second_index == -1:
        return None
    return second_index

if __name__ == '__main__':
    str1 = input("Введіть рядок: ")
    str2 = input("Введіть підстроку для пошуку: ")
    result = second_index(str1, str2)
    print("Індекс другого входження:", result)
