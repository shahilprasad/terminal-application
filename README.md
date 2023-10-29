# Terminal Application

## Table of Contents
- [Links](#links)
- [Installation](#installation)
- [Features](#features)
- [Implementation](#implementation)
- [Styling](#styling)
- [References](#references)

### Links
- [GitHub Repository](https://github.com/shahilprasad/terminal-application)

### Installation
1. From the projects GitHub repository, click the green '< > Code' button which wil bring up a drop down menu. From here you will need to ensure the 'HTTPS' option is underlined and then you may copy the URL provided by GitHub.

2. You will then need to open your systems command line (e.g Terminal) and enter the following code.
```git clone https://github.com/shahilprasad/terminal-application.git```

3. You will then need to navigate into the folder containing the code for the application within the cloned folder.
```cd terminal-application/src```

4. Next, you will need to enter ```bash run_setup.sh``` into the command line to install the requirements for the application to run correctly.

5. Finally, you may enter ```bash run_app.sh``` into the command line to run the application.

## Horse Stable Manager
### Features
Upon entering the appliction, users will be directed to the main menu of the application where they will be prompted to enter an input to proceed further.

##### Feature 1: Add a horse
This feature will allow the user to add a horse to the database. The user will be promoted to firstly enter the horses' name. Once they have provided an input they will then be promoted to enter the horses' age, followed by the its currents health status, and finally the diet. On

##### Feature 2: Remove a horse
THis features allows the user to remove a horse from the database. If the user provides an input of a name already in the database, they will receive a response to confirm the horse has been removed. Alternitively, if the horse is not in the datbase, they will receive a response advising that no horse has been found.

##### Feature 3: Update horse details
This feature allows the user to update the details of an exisiting horse within the database. It can be utilised to update the name, age, health status or diet of a horse. If a horse is not found when entering its name, the user will me notified that horse does not exist.

##### Feature 4: View horse details
Allows the user to view te details of all the horses that exist in the database. 

##### Feature 5: Add race results
Allows the user to add a race result which will be added to the database. User will be prompted to input the name of the horse, followed by the date and result of the race.

##### Feature 6: View race logs
Allows the user to view all race results that exist in the database.

##### Feature 7: Exit the application
User will be able to exit the application by enteriong the corresponding input.

### Implementation

### Styling

### Refrences