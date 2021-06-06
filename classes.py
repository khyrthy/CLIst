# File containing classes for CLIst
from colorama import *

class Table:
    def __init__(self):

        self.projects = []

    def add_project(self):

        name = input(Fore.CYAN + "Add a name for the new project : " + Style.RESET_ALL)

        if name.split(" ")[0] == name and name.lower() == name:
            
            self.projects.append(Project(name))

        elif name.split(" ")[0] != name:

            print(Fore.RED + "Project name must not contain spaces." + Style.RESET_ALL)

        elif name.lower() != name:

            print(Fore.RED + "Project name must not contain uppercase characters." + Style.RESET_ALL)

    def rm_project(self, project):

        found = False
        i = 0

        for e in self.projects:

            if e.name == project:

                found = True
                del self.projects[i]
                print(Fore.GREEN + "Deleted project " + project + "." + Style.RESET_ALL)
            i += 1

        if not found:

            print(Fore.RED + "Can't find project " + project + "." + Style.RESET_ALL)





class Project:
    def __init__(self, name):


        self.name = name
        del name

        self.tasks = []
        self.achieved = []

        print(Fore.GREEN + "Created new project " + self.name + "." + Style.RESET_ALL)

    def add_task(self):

        self.tasks.append(input(Fore.CYAN + "Add a label for your task : " + Style.RESET_ALL))
        print(Fore.GREEN + "Successfully created task #" + str(len(self.tasks)) + " : " + self.tasks[len(self.tasks)-1] + "." + Style.RESET_ALL)

    def rm_task(self, index):

        try:
            del self.tasks[index - 1]
            print(Fore.GREEN + "Successfully removed task #" + str(len(self.tasks)) + "." + Style.RESET_ALL)

        except IndexError:

            print(Fore.RED + "Can't found task #" + str(index) + " in " + self.name + Style.RESET_ALL)

    def check_task(self, index):

        print(Fore.CYAN + "[x] " + self.tasks[index - 1] + Style.RESET_ALL)

        self.achieved.append(self.tasks[index - 1])
        del self.tasks[index - 1]


        
