list=[156,200,367,490,55,68,75,555]
for item in list:
    if item>500:
        break
    elif item>150:
        continue
    elif item%5==0:
        print(item)