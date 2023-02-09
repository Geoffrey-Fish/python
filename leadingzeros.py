def beginning_zeros(number: str) -> int:
    number2 =str(number)
    count = 0
    for i in number2:
        if i == '0':
            count += 1
        else:
            break
    return count
print(beginning_zeros('0000000000010110'))