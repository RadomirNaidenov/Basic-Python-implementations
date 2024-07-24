import utils


menu = [
    "Choose a list operation:",
    "1. Append",
    "2. Extend",
    "3. Insert",
    "4. Remove",
    "5. Pop",
    "6. Clear",
    "7. Index",
    "8. Count",
    "9. Sort",
    "10. Reverse",
    "11. Copy",
    "12. Exit",
]

choices_menu = {
    "1": {
        "executor": lambda lst, value: utils.handle_append(lst, value),
        "input_msgs": [
            {"func": input, "msg": "Give some value to add in the list"},
        ]
    },
    "2": {
        "executor": lambda lst, value: utils.handle_extend(lst, value),
        "input_msgs": [
            {"func": input, "msg": "Give some value to extend"},
        ]
    },
    "3": {
        "executor": lambda lst, index, value: utils.handle_insert(lst, index, value),
        "input_msgs": [
            {"func": input, "msg": "Give some index"},
            {"func": input, "msg": "Give some value to insert in the list"},
        ]
    },
    "4": {
        "executor": lambda lst, value: utils.handle_remove(lst, value),
        "input_msgs": [
          {"func": input, "msg": "Give some value to remove"}
        ]
    },
    "5": {
        "executor": lambda lst, index: utils.handle_pop(lst, index),
        "input_msgs": [
            {"func": input, "msg": "Give some index to pop"}
        ]
    },
    "6": {
        "executor": lambda lst: utils.handle_clear(lst),
        "input_msgs": [
            
        ]

    },
    "7": {
        "executor": lambda lst, value: utils.handle_index(lst, value),
        "input_msgs": [
            {"func": input, "msg": "Give some value to find"}
        ]
    },
    "8": {
        "executor": lambda lst, value: utils.handle_count(lst, value),
        "input_msgs": [
            {"func": input, "msg": "Give some value to be counted"}
        ]
    },
    "9": {
        "executor": lambda lst: utils.handle_sort(lst),
        "input_msgs": [

        ]
    },
    "10": {
        "executor": lambda lst: utils.handle_reverse(lst),
        "input_msgs": [

        ]
    },
    "11": {
        "executor": lambda lst: utils.handle_copy(lst),
        "input_msgs": [

        ]
    },
    "12": {
        "executor": lambda x: exit(),

        "input_msgs": []
    },
}

enter_choice_msg = "Enter your choice (1-12):"