def is_equal(array1: list, array2: list) -> bool:
    for i in range(len(array1)):
        try:
            if array1[i] != array2[i]:
                return False
        except IndexError:
            return False
    return True


def after_add_path(array: list[str], path: str):
    for index in range(len(array)):
        array[index] = path + array[index]
    return array


def before_add_path(array: list[str], path: str):
    for index in range(len(array)):
        array[index] = array[index] + path
    return array
