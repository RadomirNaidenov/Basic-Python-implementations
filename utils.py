import copy


def display_menu(join_by: str, menu: list) -> str:
    return f"{join_by}".join(menu)


def is_integer(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def read_input(inputs: list[dict]) -> list:
    return [dict_obj["func"](dict_obj["msg"]) for dict_obj in inputs]


def handle_append(original_list: list, value: str) -> list:
    original_list.append(value)
    return original_list


def handle_extend(original_list: list, value: str) -> list:
    original_list.extend(value)
    return original_list


def handle_insert(original_list: list, index: str, value: str) -> list:
    if not is_integer(index):
        return original_list

    index = int(index)
    original_list.insert(index, value)
    return original_list


def handle_remove(original_list: list, value: str) -> list:
    if not is_integer(value):
        return original_list

    if value in original_list:
        original_list.remove(value)

    return original_list


def handle_pop(original_list: list, index: str) -> list:
    if not is_integer(index):
        return original_list
    index = int(index)
    if index in range(len(original_list)):
        if index != "":
            original_list.pop(index)
        else:
            original_list.pop()

    return original_list


def handle_clear(lst: list) -> list:
    lst.clear()
    return lst


def handle_index(lst: list, value: str) -> list:
    if value not in lst:
        return lst

    index = lst.index(value)
    print(index)
    return lst


def handle_count(lst: list, value: str) -> list:
    if value not in lst:
        return lst
    if not is_integer(value):
        counted_elements = lst.count(value)
        print(counted_elements)
        return lst

    value = int(value)
    counted_elements = lst.count(value)
    print(counted_elements)
    return lst


def handle_sort(lst: list) -> list:
    lst.sort()
    return lst


def handle_reverse(lst: list) -> list:
    lst.reverse()
    return lst


def handle_copy(lst: list) -> list:
    shallow_copy = copy.copy(lst)
    return shallow_copy


