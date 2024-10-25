def abbreviate_name(full_name):
    words=full_name.split()
    print(words)
    words=['Amit', 'kale']
    new=[word[:2] for word in words]
    print(new)
    abbrvateion =" ".join(new)
    return abbrvateion

full_name="Amit kale"
abbrvateion=abbreviate_name(full_name)
print(abbrvateion)

""""['Amit', 'kale']
['Am', 'ka']
Am ka   result i want"""