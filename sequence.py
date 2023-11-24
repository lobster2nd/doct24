def sequence(n):
    result = ""
    for i in range(1, n+1):
        result += str(i) * i
    return result


n = int(input("Введите количество элементов: "))
output = sequence(n)
print(output)
