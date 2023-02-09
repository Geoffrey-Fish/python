import re

str = "My name is Jeff. Hi Jeff!"
pattern = r"Jeff"
newstr = re.sub(pattern, "Miri", str)
print(newstr)

pattern2 = r"ice(-)?cream"
if re.match(pattern2, "ice-cream"):
    print("Match1")
if re.match(pattern2, "icecream"):
    print("Match2")
if re.match(pattern2, "sausages"):
    print("Match3")
if re.match(pattern2, "ice--ice"):
    print("Match4")

pattern3 = r"9{1,3}$"
if re.match(pattern3, "9"):
    print("1Match")
if re.match(pattern3, "999"):
    print("2Match")
if re.match(pattern3, "9999"):
    print("3Match")


pattern4 = r"a(bc)(de)(f(g)h)i"
match =re.match(pattern4, "abcdefghi")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())