#!/usr/bin/env python3
# CLIst main file

import pickle, sys, os
from classes import Table
from colorama import *

# Load the existing table or create a new one
try:
    open(os.path.join(os.getenv("HOME"), ".local/share/clist", "projects.table"), "r").close()
    table = pickle.load(open(os.path.join(os.getenv("HOME"), ".local/share/clist", "projects.table"), "rb"))

except FileNotFoundError:
    table = Table()

if not len(sys.argv) == 1:

    if sys.argv[1] == "help":

        print(Fore.CYAN + "CLIst help" + Style.RESET_ALL)

        print()

        print(Fore.CYAN + "clist list {project}" + Style.RESET_ALL)
        print("List all the projects and assigned tasks or tasks in a project.")

        print()
        print(Fore.CYAN + "clist add [task/project] {project}" + Style.RESET_ALL)
        print("Add a project or add a task in a project")

        print()
        print(Fore.CYAN + "clist check [project] [task index]" + Style.RESET_ALL)
        print("Mark a task as done")

        print()
        print(Fore.CYAN + "clist remove project [project]")
        print("clist remove task [project] [task index]" + Style.RESET_ALL)
        print("Delete a project or delete a task in a project")

    # List command : list all the projects and tasks or project's tasks
    elif sys.argv[1] == "list":

        # clist list
        if len(sys.argv) == 2:

            # Will check if projects table isn't empty.
            # If so, will display a "No Project" message.
            if not len(table.projects) == 0:

                print(Fore.CYAN + "All tasks :" + Style.RESET_ALL)
                for project in table.projects:
                    print()
                    print(Fore.CYAN + project.name + Style.RESET_ALL)

                    if not len(project.achieved) == 0:
                        for checked in project.achieved:
                            print("[x] " + checked)

                        print()

                    # Check if project's taskslist is empty
                    # If so, it will display a "No task" message
                    if not len(project.tasks) == 0:
                        i = 1
                        for task in project.tasks:
                            print("[" + str(i) + "] " + task)
                            i += 1

                    # Will display a "No task remaining" message if all the tasks are marked as done
                    elif len(project.tasks) == 0 and not len(project.achieved) == 0:
                        print("No task remaining.")

                    # Simply display a "No Task" message if the list is completely blank
                    else:
                        print("No task.")

            # Display a "No project" message if the table is empty
            else:
                print(Fore.CYAN + "You didn't added any project. Add a project with  :\n" + Style.RESET_ALL + "clist add project")

        # Accepts a [project] argument to display list of tasks in a specific project
        elif len(sys.argv) == 3:

            # Search for the project in the table
            found = False
            for project in table.projects:

                if project.name == sys.argv[2]:

                    found = True
                    print(Fore.CYAN + "Tasks in " + project.name + ": " + Style.RESET_ALL)

                    if not len(project.achieved) == 0:
                        for checked in project.achieved:
                            print("[x] " + checked)

                        print()

                    if not len(project.tasks) == 0:
                        i = 1
                        for task in project.tasks:
                            print("[" + str(i) + "] " + task)
                            i += 1

                    else:
                        print("No task.")

            if not found:
                print(Fore.RED + "Can't find project " + sys.argv[2] + "." + Style.RESET_ALL)

        else:

            print(Fore.RED + "Incorrect arguments count. \nUsage :" + Style.RESET_ALL)
            print("clist list")
            print("clist list [project]")

    elif sys.argv[1] == "check":

        if len(sys.argv) == 4:

            found = False

            for project in table.projects:

                if project.name == sys.argv[2]:

                    found = True

                    try:
                        project.check_task(int(sys.argv[3]))

                    except ValueError:

                        print(Fore.RED + sys.argv[3] + " : Invalid index" + Style.RESET_ALL)

                    except IndexError:

                        print(Fore.RED + "Task index " + sys.argv[3] + " is out of range." + Style.RESET_ALL)

        else:

            print(Fore.RED + "Invalid argument count. See clist help for more info." + Style.RESET_ALL)

    elif sys.argv[1] == "add":

        if not len(sys.argv) == 2:

            if sys.argv[2] == "project":

                table.add_project()

            elif sys.argv[2] == "task":

                if not len(sys.argv) == 3:

                    found = False

                    for project in table.projects:

                        if project.name == sys.argv[3]:
                            found = True
                            project.add_task()

                    if not found:

                        print(Fore.RED + "Can't found project " + sys.argv[3] + "." + Style.RESET_ALL)
                        print("List available projects using : \nclist list")

                else:

                    print(Fore.RED + "Excepting project name" + Style.RESET_ALL)
                    print(Fore.RED + "Correct usage :" + Style.RESET_ALL)
                    print("clist add task [project]")

    elif sys.argv[1] == "remove":

        if not len(sys.argv) == 2:

            if sys.argv[2] == "project":

                table.rm_project(sys.argv[3])

            elif sys.argv[2] == "task":

                try:
                    found = False

                    for project in table.projects:

                        if project.name == sys.argv[3]:

                            try:
                                found = True
                                project.rm_task(int(sys.argv[4]))
                            except ValueError:
                                print(Fore.RED + sys.argv[4] + " : Invalid index" + Style.RESET_ALL)

                    if not found:

                        print(Fore.RED + "Can't find project " + sys.argv[3] + Style.RESET_ALL)

                except IndexError:
                    print(Fore.RED + "Invalid argument count. See clist help for help." + Style.RESET_ALL)

            else:

                print(Fore.RED + "Unknown option : " + sys.argv[2] + "." + Style.RESET_ALL)

        else:
            print(Fore.RED + "Must enter task/project option. See clist help for more information" + Style.RESET_ALL)


    else:

        print(Fore.RED + sys.argv[1] + " : unknown option." + Style.RESET_ALL)

else:

    print(Fore.RED + "You must specify an option." + Style.RESET_ALL)




# Save the changes to the table
pickle.dump(table, open(os.path.join(os.getenv("HOME"), ".local/share/clist", "projects.table"), "wb"))
