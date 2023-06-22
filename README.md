# finalCapstone
name of the project - Last task for the software bootcamp - Task manager project

Description - Capstone Project - Lists, Functions, and String Handling. In this project, you will use lists or dictionaries and functions to extend the
functionality of a simple task management system. This is a program designed for
a small business to help it to manage tasks assigned to each member of a team.

Table of content, please have a look - 

Table of Contents
-----------------
1. Introduction
2. Usage
   2.1. Registering a User
   2.2. Adding a Task
   2.3. Viewing All Tasks
   2.4. Viewing User's Tasks
   2.5. Generating Reports
   2.6. Displaying Statistics
   2.7. Exiting the Program
3. Functions
   3.1. load_data()
   3.2. save_data()
   3.3. reg_user()
   3.4. add_task()
   3.5. view_all()
   3.6. view_mine()
   3.7. generate_reports()
4. Main Program Loop
5. Conclusion

To install and run the project locally, please follow these steps:

1.Clone the repository:
bash
  git clone <repository-url>
  
2. Navigate to the project directory:
bash
  cd task-manager

3.Create a virtual environment (optional but recommended):
  python3 -m venv venv
  
4. Activate the virtual environment:
* For Windows:
  venv\Scripts\activate
  
* For macOS/Linux:
 bash
  source venv/bin/activate

5. Install the required dependencies:
  pip install -r requirements.txt

6. Run the task manager:
  python task_manager.py
Now you can use the task manager application locally on your machine.

Note: The above instructions assume that you have Python 3 and Git installed on your system.
If not, please install them before proceeding. Additionally, if you prefer using a specific Python version, replace python with the appropriate command (e.g., python3).

Feel free to customize the installation instructions based on your specific project setup or any additional steps required.
  
Usage section, instructions -
  
  Usage
Once you have installed the task manager project, follow these instructions to use it:

Start the application:

Open a terminal or command prompt.
Navigate to the project directory.
Activate the virtual environment (if you created one).
Run the task manager by executing the command:
  python task_manager.py
Registration:

To register a new user, type r and press Enter.
Follow the prompts to enter the user details (username and password).
  ![image](https://github.com/savaon/finalCapstone/assets/129174500/e261259e-f325-46b8-9255-9c15a637698f)
Adding a Task:

To add a new task, type a and press Enter.
Enter the task details as prompted (task name, description, due date, and assigned user).
  ![image](https://github.com/savaon/finalCapstone/assets/129174500/61c8b567-3851-48b6-83fa-29affa34198f)
Viewing All Tasks:

To view all tasks, type va and press Enter.
All tasks listed in tasks.txt will be displayed.
  ![image](https://github.com/savaon/finalCapstone/assets/129174500/252eb3c3-1d32-4e78-812d-12fd801e3533)
Viewing User's Tasks:

To view tasks assigned to a specific user, type vm and press Enter.
All tasks assigned to the logged-in user will be displayed.
Each task is numbered for easy identification.
  ![image](https://github.com/savaon/finalCapstone/assets/129174500/372f65ef-8d5b-4c92-9c95-c39978712dfd)
Task Actions:

When viewing user tasks, you can select a specific task by entering its corresponding number.
Choose from the available options:
Mark the task as complete: Enter c and press Enter.
Edit the task details: Enter e and press Enter.
Return to the main menu: Enter -1 and press Enter.
  ![image](https://github.com/savaon/finalCapstone/assets/129174500/7c9294bb-0761-4b47-a72b-501ea6af84e9)
  
Exit:

To exit the application, type e and press Enter.
  ![image](https://github.com/savaon/finalCapstone/assets/129174500/5e44aea9-3e6c-4da3-811a-6f4553ab0f52)
  
Feel free to explore the functionalities of the task manager application.
Customize and adapt the usage instructions based on your specific project implementation.

Note: The screenshots provided are for illustrative purposes and may vary based on the actual implementation and user interface design.
  
  A section for credits that highlights and links to the authors of your
project if the project has been created by more than one person.

  The task manager project was created by:

Vjaceslavs Smonovs: Project lead, main developer.
  https://github.com/savaon
  
 Thank you.




