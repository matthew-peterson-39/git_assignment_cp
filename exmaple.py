import os
import json

def main():
    # load list.json
    TASK_JSON = './python/tasks.json'
    task_list = initialize_task_list(TASK_JSON)
    display_menu()
    menu_input = get_menu_input()
    #start loop
    if menu_input == 1: # View
        display_without_numbers(task_list)
    elif menu_input == 2: # Mark Complete
        display_with_numbers(task_list)
        pass
    return print('Program Finished.')

# Returns a list of objects if file is found with items. If file is not found, or file is empty, 
# a file is created and an empty list is returned.s 
def initialize_task_list(TASK_JSON):
    if os.path.exists(TASK_JSON):
        with open(TASK_JSON) as TASK_JSON:
            try:
                doc = json.load(TASK_JSON)
            except json.JSONDecodeError:
                doc = []
            finally:
                return doc
    else:
        with open(TASK_JSON, 'w') as TASK_JSON:
            json.dump([], TASK_JSON)
            doc = []
        return doc

def display_menu():
    print('1. View List\n2. Mark Complete\n3. Add\n4. Remove\n\nPress any other button to exit.\n')

def display_without_numbers(task_list):
    print("\n*** TODO LIST ***\n")
    for item in task_list:
        if item["completed"] == True:
            print(f'{item["name"]} [x]')
        else:
            print(f'{item["name"]} [ ]')
    return

def display_with_numbers(task_list):
    list_number = 1
    print("\n*** TODO LIST ***\n")
    for item in task_list:
        if item["completed"] == True:
            print(f'{list_number}. {item["name"]} [x]')
        else:
            print(f'{list_number}. {item["name"]} [ ]')
        list_number += 1
    return

def get_menu_input():
    try:
        menu_input = int(input('--> Menu selection:'))
    except ValueError:
        return print('Invalid menu input.')
    return menu_input   
# is this where we want the add function?

main()