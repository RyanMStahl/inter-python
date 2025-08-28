def parse(string):
    if not isinstance(string, str):
        raise ValueError("input is not of type string")
    return float(string)

