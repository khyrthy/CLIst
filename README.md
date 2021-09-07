# CLIst

A CLI-based To-Do List written in Python  
Made for tty-friends

## Using CList

Here's a guide about how to use Clist

### List of Commands

Here are all the commands that CList understands:
* `clist help `  
  List CList Commands and valid arguments

* `clist list (project)`  
  List tasks globally/in a project (the project argument is not required)

* `clist add project`  
  Add a project to the taskboard

* `clist add task [project]`  
  Add a task to a project
  
* `clist remove project [project]`  
  Remove an entire project from the taskboard

* `clist remove task [project] [task index]`
  Remove a task from a project

* `clist check [project] [task index]`  
  Mark a task as done in a specific project

### Exporting taskboards

CLIst saves your tasks and your project into a file named `projects.table` at `~/.local/share/clist/projects.table` You can eventually export it and share it