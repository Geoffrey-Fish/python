import re
pattern = r"spam"
if re.match(pattern, "eggsamsausagespam") :
    print("Match")
else :
    print("no Match")

if re.search(pattern, "eggspamsausagespam") :
    print("Match")
else :
    print("No Match")

print(re.findall(pattern, "eggspamsausagespam"))

dingens = (re.finditer(pattern, "eggspamsausagespam"))
print(dingens)
