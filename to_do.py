tasks = []

def create():
    new = input('Enter you new upcoming task: ')
    new
    tasks.append(new)

def delete():
    try:
        task_no = int(input('Enter the # of task you want to delete: '))
        if task_no >= 0 and task_no <= len(tasks):
            tasks.pop(task_no)
        else:
            print('Task was not found')
    except:
        print('Invalid inpur')

def list_task():
    print('These are the tasks')
    for task in tasks:
        print(task)

if __name__ == "__main__":

    print("Welcome to the to-do list app")
    while True:
        print('\n')
        print('Please select one of the following options')
        print('\n')
        print('1. Add new task\n'
              '2. Delete an old task\n'
              '3. List all tasks\n'
              '4. Quit')

        choice = input('Enter your choice: ')


        if choice == '1':
            create()

        elif choice == '2':
            delete()

        elif choice == '3':
            list_task()

        elif choice == '4':
            quit()

        else:
            print('You entered the incorrect option! Please select the right option')