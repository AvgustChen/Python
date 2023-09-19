import random

_results = {}
def gen_puzzle():
    game_dict = {'Зимой и летом одним цветом': ['ёлка', 'ель', 'ёлочка'],
                 'Не лает не кусает, а в дом не пускает': ['замок', 'замочек'],
                 'Висит груша, нельзя скушать': ['лампа', 'лампа']}
    while game_dict:
        key = random.choice(list(game_dict))
        yield key, game_dict.pop(key)


def my_game(count: int):
    global _results
    for puzzle in gen_puzzle():
        riddle, answer = puzzle
        temp_count = 1
        answer = list(map(lambda x: x.lower(), answer))
        while temp_count <= count:
            user_str = input(riddle + ': ').lower()
            if user_str in answer:
                _results[riddle] = temp_count
                break
            temp_count += 1
        else:
            _results[riddle] = 0


def show_results():
    global _results
    result = ['Результаты: ']
    max_len = len(max(list(_results), key=len)) + 2
    for riddle, count in _results.items():
        result.append(f'{riddle+":":<{max_len}} Отгадана с {count} попытки')

    return  '\n'.join(result)
