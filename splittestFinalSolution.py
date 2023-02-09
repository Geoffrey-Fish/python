def split_pairs(a):
    inp = str(a)
    x = 0
    y = 1
    liste = []
    puffer = str()
    if len(inp) % 2 != 0 :
        inp +='_'
    while x < len(list(inp)):
        puffer = str(inp[x]+inp[y])
        liste.append(puffer)
        x += 2
        y += 2

    return liste

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

   # This was the way to it:
   # def split_pairs(a):
   # inp = str(a)
   # x = 0
   # y = 1
   # liste = []
   # puffer = str()
   # if len(inp) % 2 != 0 :
   #     inp +='_'
   # while x < len(list(inp)):
   #     puffer = str(inp[x]+inp[y])
   #     liste.append(puffer)
   #     x += 2
   #     y += 2


   # return liste



#mc = split_pairs("abcde")
#print(mc)