names = ["Bruno", "Joao", "Bernardo", "Barbara", "Brian"]

def start_with_b(name: list) -> list:
    """This is a docstring
    
    Esta é uma docstring

    Args:
        name (_type_): _description_

    Returns:
        _type_: _description_
    """
    return name[0].lower() == "b"

names_with_b = list(filter(start_with_b, names))

[print(nome) for nome in names_with_b]