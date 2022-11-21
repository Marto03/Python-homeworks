# задачата не работи , не успях да измисля как да я довърша

def get_collection_builder(col_type):

    if isinstance(col_type, tuple):
        for text in range(1, 5):
            current_parameter = input(f"Input parameter {text}: ")
            tuple.__add__(current_parameter)
        return tuple, col_type

    elif isinstance(col_type, list):
        list_1 = []
        for text in range(1, 5):
            current_parameter = input(f"Input parameter {text}: ")
            list_1.append(current_parameter)
        return list_1, col_type
    elif isinstance(col_type, set):
        set_1 = {}
        for text in range(1, 5):
            current_parameter = input(f"Input parameter {text}: ")
            set_1.add(current_parameter)
        return set_1, col_type
    return col_type

print(get_collection_builder([list]))