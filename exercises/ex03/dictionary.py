__author__ = """730761985"""


def invert(d: dict[str, str]) -> dict[str, str]:
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            raise KeyError("KeyError Encountered")
        inverted[value] = key
    return inverted


def count(values: list[str]) -> dict[str, int]:
    result = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(colors: dict[str, str]) -> str:
    count = {}
    for name, color in colors.items():
        if color in count:
            count[color] += 1
        else:
            count[color] = 1

    max_color = max(count, key=count.get, default="")
    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = set()
        result[length].add(word)
    return result
