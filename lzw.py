text = 'dwdwe'


def coder_bwt(text):
    Input = text

    table = [Input[i:] + Input[:i] for i in range(len(Input))]  # Table of rotations of string

    table = sorted(table)

    last_column = [row[-1:] for row in table]  # Last characters of each row
    bwt = ''.join(last_column)

    index = 0
    for i in range(len(table)):
        if Input == table[i]:
            index = i
            break

    return bwt, index


def compress(uncompressed):
    dict_size = 256
    # dictionary = dict((chr(i), i) for i in range(dict_size))
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    result = [bin(res) for res in result]
    return result


def assembly1(mas):
    res = ""

    for i in mas:
        res += str(i) + " "

    return res


print(assembly1(compress(coder_bwt(text)[0])), coder_bwt(text)[1])
