def get_letter(dictionary, value):
    for k, val in dictionary.items():
        if val == value:
            return k

def get_string():
    with open("str_to_decode.txt", "r") as file:
        file_str = file.read()
    return file_str

def fano_decode(**fano_dict):
    fano_str = get_string()
    buffer = ''
    result = ''

    for letter in fano_str:
        buffer += letter

        if get_letter(fano_dict, buffer):
            result += get_letter(fano_dict, buffer)
            buffer = ''

    print('string from file: ', fano_str)
    return result
