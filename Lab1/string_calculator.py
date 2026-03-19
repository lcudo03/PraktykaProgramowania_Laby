import re

def Add(numbers: str) -> int:
    if numbers == "":
        return 0
    if numbers.__contains__(",\n") or numbers.__contains__("\n,"):
        raise ValueError("Double separator")
    parts = re.split(r"[,\n]", numbers)
    for part in parts:
        if not part.isdigit():
            raise ValueError("Not a number")
    return sum(int(part) for part in parts)