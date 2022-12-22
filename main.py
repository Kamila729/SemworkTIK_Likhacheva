import json


def get_string():
    with open("str_to_encode.txt", "r") as file:
        file_str = file.read()
    return file_str


def bwt_code(encode_str):
    inp_str = list(encode_str)
    move_list = []

    ''' Move list - list of all available permutations for string '''
    for i in range(len(inp_str)):
        word = encode_str[-1] + encode_str[:-1]
        new = ''.join(word)
        encode_str = new
        move_list.append(new)
        i += 1

    sorted_move_list = sorted(move_list)

    bwt_str = ''

    original_str = move_list[-1]
    original_str_index = 0

    ''' BWT string - returns last characters of each string in Move list (alphabetical sorted) '''
    for i in range(len(inp_str)):
        if sorted_move_list[i] == original_str:
            original_str_index = i

        element = sorted_move_list[i]
        last = element[- 1]
        i += 1
        bwt_str += str(last)

    ''' Function returns 2 values - BWT encoded string [0] and original string position [1] '''
    return bwt_str, original_str_index



def lzw_compress(uncompressed):
    """Compress a string to a list of output symbols."""

    '''Create dict with alphabet'''
    dict_size = 0
    dictionary = {}

    ct = 0
    for i in range(len(uncompressed)):
        if uncompressed[i] not in dictionary:
            dictionary[uncompressed[i]] = ct
            ct += 1
            dict_size += 1

    '''write this dict in file to further decoding'''
    with open("alphabet.txt", "w") as file:
        file.write(json.dumps(dictionary))

    ''' Add to alphabet dict new values(character combinations) '''
    w = ""
    int_result = []
    for char in uncompressed:
        wc = w + char
        if wc in dictionary:
            w = wc
        else:
            int_result.append(dictionary[w])
            ''' Add combination to dict '''
            dictionary[wc] = dict_size
            dict_size += 1
            w = char

    if w:
        int_result.append(dictionary[w])
    ''' переводим алфавит в двоичный восьмибитный'''
    bin_result = []

    for elem in int_result:
        bin_elem = (bin(elem)[2::])
        while len(bin_elem) < 8:
            bin_elem = '0' + bin_elem
        bin_result.append(bin_elem)

    return bin_result


def main():

    str_to_encode = get_string()

    bwt_coded_str = bwt_code(str_to_encode)[0]

    bwt_string_number = bwt_code(str_to_encode)[1]

    lzw_compressed = lzw_compress(bwt_coded_str)






    with open("encoded_file", "w") as file:
        file.write(str(bwt_string_number) + '\n')
        file.write(' '.join(lzw_compressed))

    return bwt_string_number, lzw_compressed


if __name__ == '__main__':
    main()