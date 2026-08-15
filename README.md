# CampusCompass 🎓



#### Video Demo: https://youtu.be/3t2eRp4AsgQ



#### Description:

CampusCompass is a web application designed to help university students organize and manage their academic life in one place.

The application allows students to keep track of tasks, assignments, and attendance through a personalized dashboard.

At its core, CampusCompass is designed to be a friendly university buddy that helps students stay organized, keep track of what matters, and feel a little more in control of THEIR academic life.



## Why CampusCompass?

CampusCompass was inspired by a very personal reason: I am about to begin university myself. With university life just around the corner, I started thinking about the things I would need to keep track of once classes, assignments, deadlines, subjects, and attendance all became part of my daily routine. That is where the idea for CampusCompass came from.

Being a student who is about to start university, this project became more than just another programming assignment to me. I wanted to build something that I could genuinely use myself while navigating my own university life, rather than creating an application simply to demonstrate what I had learned.

The original idea for CampusCompass was much larger and included several additional features. However, with my own university life about to begin, I was working within a limited timeframe. I therefore chose to focus on two areas I knew I would genuinely need as a student: managing academic tasks and assignments, and keeping track of attendance.



## What Can CampusCompass Do?


CampusCompass brings the most important parts of a student's academic routine together through a personalized dashboard. After creating an account, students can manage their subjects, tasks and assignments, and attendance, with their information stored separately from other users.


*User Accounts*

Students can create an account using their name, username, email, and password, and log in to access their personal dashboard. Passwords are securely hashed before being stored in the database, and each student's academic information is associated with their individual account.


*Task Management*

Students can add tasks and assignments with a title, description, and due date. These tasks appear on the dashboard in due-date order, making upcoming deadlines easier to see. Once a task is finished, it can be marked as completed or deleted when it is no longer needed.


*Attendance Tracking*

CampusCompass allows students to record whether they attended or missed a class for each subject. It keeps track of classes attended and total classes, and automatically calculates the attendance percentage. Attendance at or above 75% is displayed as meeting the required threshold, while attendance below 75% is highlighted as a warning.


*Personalized Dashboard*

The dashboard acts as the central space of CampusCompass. It welcomes the logged-in student by name and brings their tasks and quick access to attendance together in one place, giving them a simple overview of what they need to keep track of.



## How It Works

CampusCompass begins with a simple account-based login system. A new student can register by providing their name, username, email, and password. Once registered, they can log in and access their personalized dashboard. If a user is already logged in, visiting the homepage takes them directly to the dashboard.

From the dashboard, students can add tasks by providing a title, description, and due date. These tasks are stored in the database and displayed in order of their due dates. Students can mark completed tasks or remove tasks that are no longer needed.

The attendance section works separately but follows the same personalized approach. Students can add their subjects and then record whether they attended or missed each class. CampusCompass updates the attendance records and calculates the percentage automatically, allowing students to see their current attendance at a glance.

When a student logs out, their session is cleared and they are returned to the homepage. Logging in again restores access to their own academic information.



## Design Choices

*Why Flask*
I chose Flask as the framework because it allowed me to build the application in Python while keeping the structure of the project relatively simple. It also made it easier to connect the different pages of the application with the database and manage user sessions.

*Why SQLite*
I chose SQLite for my database because CampusCompass is a relatively lightweight application and does not require the complexity of a larger database system. SQLite was sufficient for storing users, tasks, subjects, and attendance records while allowing the application to maintain relationships between a student's account and their academic information.

*Why the dashboard*
I chose to use a personalized dashboard rather than separate starting points for every feature because the dashboard acts as the central space of CampusCompass. It gives students an immediate overview of what needs their attention as soon as they log in, making the experience feel more like checking in with a uni buddy than navigating through a collection of separate tools.

*How did I design the interface*
For the interface, I used Bootstrap alongside my own CSS, but I wanted the overall design to go beyond simply being functional. I wanted CampusCompass to feel cute, friendly, aesthetic and genuinely fun to use - something students would actually want to keep coming back to, even when it contains dreadful things like assignments, deadlines and attendance.

*Why did I prioritize these features?*
I chose to prioritize task management and attendance when deciding which features to implement within the available time because they addressed two of the most immediate challenges students face. The original idea included more functionality, but due to the time crunch, I decided to focus on these two areas rather than rush to include everything as planned and end up with many unfinished features.



## Files and Their Purpose

*app.py*
`app.py` is the main file of CampusCompass and contains the Flask application itself. It defines all of the application's routes and controls how the different parts of the platform work. It handles user registration and login, maintains user sessions, displays the personalized dashboard, and manages tasks, subjects, and attendance. It also connects the application to the SQLite database whenever information needs to be stored, retrieved, updated, or deleted.

*create_database.py*
`create_database.py` initializes the CampusCompass database and is intended to be run when setting up the application. It creates the SQLite database and defines the three tables used by the application: `users`, `tasks`, and `attendance`. The `users` table stores account information, the `tasks` table stores each user's academic tasks and assignments, and the `attendance` table stores subjects along with the number of classes attended and the total number of classes. The tables use user IDs to associate academic information with the correct account.

*campuscompass.db*
`campuscompass.db` is the SQLite database used by CampusCompass while the application is running. It stores the persistent data required by the application, including user accounts, tasks, and attendance records. The database allows information to remain available when a user logs out and logs back in, rather than existing only for the duration of a session.

*templates/layout.html*
`layout.html` is the base HTML template used throughout CampusCompass. It contains the shared structure of the application's pages, including the navigation and common elements. It uses Jinja templating to create reusable template blocks that other pages can extend, allowing the same layout to be shared across the application without repeating common HTML code.

*templates/index.html*
`index.html` is the homepage of CampusCompass. It introduces the platform to visitors and provides access to the main entry points of the application, including registration and login.

*templates/register.html*
`register.html` contains the registration form through which a new user provides their full name, username, email, password, and password confirmation before creating an account.

*templates/login.html*
`login.html` contains the login form used by existing users to enter their username and password and access their personal CampusCompass account.

*templates/dashboard.html*
`dashboard.html` displays the personalized dashboard after a user logs in. It welcomes the user by name, displays their tasks in due-date order, and provides access to task management and the attendance tracker. It also allows pending tasks to be marked as completed or deleted.

*templates/add_task.html*
`add_task.html` provides the form for creating a new task. Users can enter a task title, description, and due date, which are then submitted to the Flask application and stored in the database.

*templates/add_subject.html*
`add_subject.html` provides the form for adding a subject to the attendance tracker. The subject is associated with the currently logged-in user's account.

*templates/attendance.html*
`attendance.html` displays the attendance tracker for the logged-in user. It shows each subject, the number of classes attended and total classes, and the calculated attendance percentage. It also provides controls for recording an attended or missed class and deleting a subject.

*static/style.css*
`style.css` contains the custom CSS used to style CampusCompass. While Bootstrap provides the basic responsive structure and components, this file controls the application's own visual identity and helps create the friendly, cute, and aesthetic appearance intended for the platform.

*static/script.js*
`script.js` is included as the JavaScript file for CampusCompass. The current version does not require additional JavaScript functionality, so the file is reserved for future client-side interactions and enhancements.

*requirements.txt*
`requirements.txt` lists the external Python dependency required to run CampusCompass. The project currently requires Flask, while modules such as `sqlite3` are part of Python's standard library and therefore do not need to be listed separately.



## Security and Data

Since CampusCompass stores personal account and academic information, I wanted to make sure that users' data was kept separate and that passwords were not stored directly. Passwords are hashed before being saved to the database and checked against the stored hash when a user logs in. Flask sessions are then used to keep track of the logged-in user throughout the application.

Each user's tasks and attendance records are connected to their own user ID, so the application can retrieve and manage the correct data for each account. I also used parameterized SQL queries when working with user input to avoid directly inserting it into database queries.



## What new did I come across while building CampusCompass?
Building CampusCompass also gave me the opportunity to learn something beyond the concepts directly covered in the course. While the basics of Python, HTML, and SQL were already familiar to me from school, CS50 helped me understand and use them at a much deeper level. During the development of CampusCompass, I also came across Werkzeug, which I used for password hashing and verification. Learning how to use a new library and understand how it fit into my existing Flask application was one of the new challenges I encountered while building the project.



## Future Improvements

While the current version of CampusCompass focuses on task management and attendance tracking, the original idea included several additional features that could be explored in future versions. These include a GPA tracker, study session tracker, Pomodoro timer, subject-based task organization, and deadline reminders.

I would also like to expand the attendance tracker to provide students with a clearer idea of how many classes they can afford to miss while still maintaining the required attendance percentage.

Together, these additions would bring CampusCompass closer to the original idea I had in mind: a single, friendly place where students can organize their academic responsibilities, manage their time, and keep track of their progress throughout university without needing to jump between several different apps.



## Final Thoughts

CampusCompass started as an idea for my CS50 final project, but became something much more personal as I built it. With university just around the corner, I was creating something based on problems I was about to experience myself, which made the project feel much more meaningful than simply completing an assignment.

This is only the first version of CampusCompass, and there is still a lot I would like to build into it. But I am happy that I chose to make something I can genuinely see myself using. For me, CampusCompass is not just a final project; it is the beginning of a little uni buddy that I hope can grow alongside me throughout university.



### This was CampusCompass 1.0. Stay tuned! 🧭✨
