keys = ("Гідроген", "Гелій", "Літій", "Берилій", "Бор", "Карбон", "Нітроген", "Оксиген")
dct = dict()

for k in keys:
    dct[k] = input("Element for " + k + " : ")


sortedAsc = dict(sorted(dct.items(), key=lambda item: item[0]))
print(sortedAsc)
