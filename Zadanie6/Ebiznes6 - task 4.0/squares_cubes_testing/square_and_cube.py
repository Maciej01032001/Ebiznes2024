def square_root(x):
    if x < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return x ** (1 / 2)


def cube_root(x):
    if x < 0:
        return -(-x) ** (1 / 3)
    else:
        return x ** (1 / 3)


def area_of_square(side):
    if side < 0:
        raise ValueError("Side length cannot be smaller than 0.")
    return side ** 2


def area_of_cube(side):
    if side < 0:
        raise ValueError("Side length cannot be smaller than 0.")
    return 6 * (side ** 2)


def volume_of_cube(side):
    if side < 0:
        raise ValueError("Side length cannot be smaller than 0.")
    return side ** 3


def perimeter_of_square(side):
    if side < 0:
        raise ValueError("Side length cannot be smaller than 0.")
    return 4 * side


def perimeter_of_cube(side):
    if side < 0:
        raise ValueError("Side length cannot be smaller than 0.")
    return 12 * side
