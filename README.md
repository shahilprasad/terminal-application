# Terminal Application

### Links
- [GitHub Repository](https://github.com/shahilprasad/terminal-application)

### Installation
Please note: The following installation steps were developed on a mac and may have issues installing on other operating systems. The following steps also assume that the user has python and git already installed on their systen. If either isn't installed, please install the lastest version available.

1. From the projects GitHub repository, click the green '< > Code' button which wil bring up a drop down menu. From here you will need to ensure the 'HTTPS' option is underlined and then you may copy the URL provided by GitHub.

2. You will then need to open your systems command line (e.g Terminal) and enter the following code.
```git clone https://github.com/shahilprasad/terminal-application.git```

3. You will then need to navigate into the folder containing the code for the application within the cloned folder.
```cd terminal-application/src```

4. Next, you will need to enter ```bash run_setup.sh``` into the command line to install the requirements for the application to run correctly.

5. Finally, you may enter ```bash run_app.sh``` into the command line to run the application.

### Help
#### System Requirements
Operating System:

Windows 7 or higher

Mac OS X 10.11 or higher

4 GB RAM

5 GB free disk space
#### Dependenices
- jsonschema==4.19.1
- pytest==7.4.2

#### Packages and Modules
- jsoschema
- pytest
- datetime
- os
- json

## Horse Stable Manager

##### Feature 1: Main Menu
Upon entering the appliction, users will be directed to the main menu of the application where they will be prompted to enter an input to proceed further. The main menu will allow the user to use a CRUD (Create, read, update, delete) style interface to manage the horse stable. There will also be additional fetures to view race logs and also add new race results for any horse. The final menu option will allow the user to exit the applicaiton with a single character input.

##### Feature 2: Add a horse
This feature will allow the user to add a horse to the database. The user will be promoted to firstly enter the horses' name. Once the user has provided a name, they will then be promoted to enter the horses' age, followed by the its currents health status, and finally their diet. On successful entry, the horse will be added to the database. In the instance where the user makes an invalid entry, such as entering a string when promoted for the horses' age, they will receive an error message and be promoted to try again.

##### Feature 3: Remove a horse
THis features allows the user to remove a horse from the database. If the user provides an input of a name already in the database, they will receive a response to confirm the horse has been removed. Alternitively, if the horse is not in the datbase, they will receive a response advising that no horse has been found.

##### Feature 4: Update horse details
This feature allows the user to update the details of an exisiting horse within the database. It can be utilised to update the name, age, health status or diet of a horse. If a horse is not found when entering its name, the user will me notified that horse does not exist.

##### Feature 5: View horse details
Allows the user to view the details of all the horses that exist in the database. The terminal will draw data from the database and show each horse on a new line in the terminal. The detais will inlcude the horse name, age, health status and diet.

##### Feature 6: Add race results
Allows the user to add a race result which will be added to the database. User will be prompted to input the name of the horse, followed by the date and result of the race. On successful entry, the horse will be added to the database. In the instance where the user makes an invalid entry, such as entering a date in the wrong format, they will receive an error message and be promoted to try again.

##### Feature 7: View race logs
Allows the user to view all race results that exist in the database. All data will be drawn from the json database. The data will incude the name of a horse, the date of the race, and the position the horse finished in the race.

### Implementation
For project management I utilised the Trello's online platform. I created a workspace to input all the tasks that I needed to do to complete the assignemnt. Tasks were placed in either the To-Do, doing, next up, or end tasks section and was updated regularly. Under the define features section of the trello board I worked through each feature by creating a checklist of tasks required to be completed to have the feature implemented. Once all features were completed, I was able to move the status of feature implementation into the 'Done' section of the Trello board.

![Screenhot of Treollo board](/docs/Trello-19Oct.png)
![Screenhot of Treollo board](/docs/Trello-20Oct.png)
![Screenhot of Treollo board](/docs/Trello-24Oct.png)
![Screenhot of Treollo board](/docs/Trello-25Oct.png)
![Screenhot of Treollo board](/docs/Trello-26Oct.png)
![Screenhot of Treollo board](/docs/Trello-27Oct.png)
![Screenhot of Treollo board](/docs/Trello-29Oct.png)
![Screenhot of feature 1 checklist](/docs/Feature-1.png)
![Screenhot of feature 2 checklist](/docs/Feature-2.png)
![Screenhot of feature 3 checklist](/docs/Feature-3.png)
![Screenhot of feature 4 checklist](/docs/Feature-4.png)
![Screenhot of feature 5 checklist](/docs/Feature-5.png)
![Screenhot of feature 6 checklist](/docs/Feature-6.png)
![Screenhot of feature 7 checklist](/docs/Feature-7.png)

### Styling
The PEP8 Style Guide was followed in making this python applicaiton.

### Refrences
- Python 3.12.0 documentation (no date) 3.12.0 Documentation. Available at: https://docs.python.org/3/.
- Real Python (2022) Working with JSON data in python, Real Python. Real Python. Available at: https://realpython.com/python-json/. 
- Learn Python - Full Course for Beginners tutorial (2018) YouTube. Available at: https://youtu.be/rfscVS0vtbw). 
- van Rossum, G., Warsaw, B. and Coghlan, N. (2023). PEP 8 – Style Guide for Python Code | peps.python.org. [online] peps.python.org. Available at: https://peps.python.org/pep-0008/.
- Python Software Foundation (2023). Datetime — Basic Date and Time Types — Python 3.7.2 Documentation. [online] Python.org. Available at: https://docs.python.org/3/library/datetime.html.
- www.gnu.org. (2022). Bash Reference Manual. [online] Available at: https://www.gnu.org/software/bash/manual/bash.html.