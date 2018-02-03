def spliter(lista, index):
    res = []
    tbefore = lista[:index]
    tafter = lista[(index+1):]
    res += tbefore
    while len(lista[index]) > 0:
        res += lista[index][0]
        lista[index] = lista[index][1:]
    res += tafter
    return res

def checker(lista):
    lar = len(lista)
    index = 0
    while index < lar:
        if (len(lista[index]) > 1):
            lista = spliter(lista, index)
            index+=1
        else:
            index+=1
    return lista

def compress(text):
    res = []
    prev = ''
    count = 0
    while len(text) > 0:
        if prev == '':
            prev = text[0]
            count += 1
            text = text[1:]
        elif prev != text[0]:
            res += [str(count)+prev]
            count = 1
            prev = text[0]
            text = text[1:]
        else:
            count += 1
            text = text[1:]
    res += [str(count) + prev]
    return res

def cleaner(text):
    res = ''
    while len(text) > 0:
        res += text[0]
        text = text[1:]
    return res
def main(string):
    text = string.split()
    text = checker(text)
    text = compress(text)
    text = cleaner(text)
    print(text)

main("XXXX")
main("XXXXFGGGJJ")
main("DDDDDDDDAA")
main("XXXXFGGGJJ")