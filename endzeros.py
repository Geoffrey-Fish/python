
def end_zeros(num: int) -> int:
    # your code here
    nuller = [int(x) for x in str(num)]
    count = 0
    while len(nuller) > 0 :
        if nuller[-1] == 0 :
            nuller.pop(-1)
            count += 1
        else :
              return count
    return count

here = print(input("please"))
ergebnis = end_zeros(here)
print(ergebnis)
