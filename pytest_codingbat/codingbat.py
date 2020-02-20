def first_last6(numbers: list) -> bool:
    if numbers[0] == 6 or numbers[-1] == 6:
        return True
    else:
        return False


def same_first_last(numbers: list) -> bool:
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False


def make_pi():
    return [3, 1, 4]
