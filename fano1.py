from typing import List, Tuple

INPUT_FILE_NAME = "fano.txt"


class Node:
    def __init__(self, letter: str, probability: float):
        self.letter = letter
        self.probability = probability
        self.code = ""  # итоговый двоичный код


def parse_file(file_name: str) -> List[Node]:
    with open(file_name) as file:
        lines = file.readlines()
    letters = lines[0].split()
    probabilities = list(map(float, lines[1].replace(",", ".").split()))
    assert len(letters) == len(probabilities), "Кол-во букв и вероятностей в файле должны совпадать"

    nodes = []
    for letter, probability in zip(letters, probabilities):
        nodes.append(Node(letter, probability))
    return nodes


def sort_nodes(nodes: List[Node]) -> List[Node]:
    return sorted(nodes, key=lambda node: node.probability, reverse=True)


def divide_into_similar_sums(nodes: List[Node]) -> Tuple[List[Node], List[Node]]:
    assert len(nodes) >= 2
    total_sum: float = sum([node.probability for node in nodes])
    difference = total_sum
    right_sum = total_sum
    left_sum = 0.0
    right_group_left_bound_index = 0
    for i in range(len(nodes)):
        left_sum += nodes[i].probability
        right_sum -= nodes[i].probability
        current_difference = abs(right_sum - left_sum)
        if current_difference < difference:
            difference = current_difference
            right_group_left_bound_index = i + 1
    return nodes[0:right_group_left_bound_index], nodes[right_group_left_bound_index:]


def fano(nodes: List[Node]) -> List[Node]:
    if len(nodes) == 1:
        return nodes
    left_nodes, right_nodes = divide_into_similar_sums(nodes)
    for node in left_nodes:
        node.code += "0"
    for node in right_nodes:
        node.code += "1"
    left_nodes = fano(left_nodes)
    right_nodes = fano(right_nodes)
    return left_nodes + right_nodes


def encode_with_nodes(string: str, nodes: List[Node]) -> str:
    mapping = {}
    for node in nodes:
        mapping[node.letter] = node.code
    return "".join(mapping[char] for char in string)


def get_letter(nodes, value):
    for i in range(len(nodes)):
        if value == nodes[i].code:
            return nodes[i].letter


def fano_decode(fano_dict):
    fano_str = input('enter string to decode: ')
    buffer = ''
    result = ''

    for letter in fano_str:
        buffer += letter

        if get_letter(fano_dict, buffer):
            result += get_letter(fano_dict, buffer)
            buffer = ''
    print('string from file to decode : ', fano_str)
    print('decoded string: ', result)
    return result


def main():
    nodes = parse_file(INPUT_FILE_NAME)

    nodes = sort_nodes(nodes)
    nodes = fano(nodes)

    fano_decode(nodes)


if __name__ == "__main__":
    main()