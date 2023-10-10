import os
import json

TASK_JSON = 'tasks.json'

def main():
    # load list.json
    task_list = initialize_task_list(TASK_JSON)
    display_menu()
    menu_input = get_int_input('Menu')
    print(menu_input)
    if menu_input == 1: # View
        display_without_numbers(task_list)
    elif menu_input == 2: # Mark Complete
        mark_complete(task_list)
    elif menu_input == 3: # Add Task
        add_task(task_list)
    elif menu_input == 4: #Remove Task
        remove_task(task_list)
    elif menu_input == 5: #Edit Task
        edit_task(task_list)
        

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
    print('1. View List\n2. Mark Complete\n3. Add\n4. Remove\n5. Edit\nPress any other button to exit.\n')

def display_without_numbers(task_list):
    print("\n*** TODO LIST ***\n")
    for item in task_list:
        if item["completed"] == True:
            print(f'{item["name"]} [x]')
        else:
            print(f'{item["name"]} [ ]')
    print("This is your moment")
    return

def display_with_numbers(task_list):
    list_number = 0
    print("\n*** TODO LIST ***\n")
    for item in task_list:
        list_number += 1
        if item["completed"] == True:
            print(f'{list_number}. {item["name"]} [x]')
        else:
            print(f'{list_number}. {item["name"]} [ ]')
        
    print("Your goals are worthwhile")
    return

def get_int_input(prompt): #NOTE if we are off on index, this is why 
    try:
        menu_input = int(input(f'--> {prompt} selection:'))
    except ValueError:
        return print('Invalid menu input.')
    return menu_input 

def get_str_input(prompt):
    try:
        menu_input = input(f'--> {prompt}:')
    except ValueError:
        return print('Invalid menu input.')
    return menu_input   

# TODO : Implement these tasks. Each should take a task_list arguement and returns the updated version of the list after
# item has been added, removed, edited, or completed.
def add_task(task_list):
    task_name = get_str_input('Enter task name: ')
    task_list.append({"name": task_name, "completed": False})
    save_task_list(task_list)
    display_with_numbers(task_list)
    return # task_list

def mark_complete(task_list):
    display_with_numbers(task_list)
    task_index = get_int_input('Which task did you complete?')
    complete_task =task_list[task_index - 1]
    print(complete_task["completed"])
    if complete_task["completed"] == True:
        complete_task["completed"] = False
        print("Give it another shot!")
    else:
        complete_task["completed"] = True
        print("You have completed your task!")
    task_list = task_list
    save_task_list(task_list)
    print(complete_task)
    return # task_list
    

def edit_task(task_list):
    display_with_numbers(task_list)
    index =get_int_input('Which task do you want to edit?')
    task_list[index - 1] = get_str_input('Enter task name: ')
    save_task_list(task_list)
    display_with_numbers(task_list)
    return  # task_list

def remove_task(task_list):
    display_with_numbers(task_list)
    index = get_int_input('Which task do you want to edit?')
    task_list.pop(index - 1)
    save_task_list(task_list)
    display_with_numbers(task_list)
    return # task_list

def save_task_list(task_list):
    with open(TASK_JSON, 'w') as new_save:
        json.dump(task_list, new_save)
        task_list = task_list

main()