# задачата не работи , не успях да измисля как да я направя
col_type = list[input("Input: ")]
def get_collection_builder(col_type):

    if isinstance(col_type, tuple):
        for text in range(1, 5):
            current_parameter = input((f"Input parameter {text}: "))

        return col_type
    elif isinstance(col_type, list):
        for text in range(1, 5):
            current_parameter = input([f"Input parameter {text}:"])
    elif isinstance(col_type, set):
        for text in range(1, 5):
            current_parameter = input({f"Input parameter {text}: "})
    return col_type

print(get_collection_builder(type(col_type)))