# project
 # Hospital Management System.
    #### Video Demo:  <URL HERE>
#### Description: 
The hospital management system facilitates the synchronization of hospitals’ works by ensuring that patients’ records, doctors’schedules, and appointments are kept in one place. It is a python-based application that is dedicated to offer healthcare facilities with an efficient way of organizing and automating their administrative tasks resulting in improved overall efficiency levels and patient care.

##### Features

User Authentication: Users log in using their details to access different roles (Administrator, Doctor or Receptionist) functionality-wise.

Patient Management: Add new patients, view existing patient records, update patient information.

Doctor Management: Create profiles for new doctors based on specialization; view current doctor profiles/schedules.

Appointment Booking: Patients can book appointments for specific days/times with the physicians concerned.

View Appointments: Upcoming appointments displaying details such as name of patient, name of doctor and date of appointment can be shown here.

Data Persistence: The data about patients, doctors and appointments are saved into JSON files hence they remain intact when it comes to persistence within sessions.

##### Project Structure

project.py : python script that has the main functions of the application; user authentication, adding/editing/viewing/deleting patients and doctors and booking/ viewing/ updating or deleting appointments.

test_project.py: python script thas has the function of testing whether the project.py functions work as intended.

requirements.txt: List of Python packages needed for running the application, which also include inflect and pytest.

data/: A folder that keeps JSON files where patient, doctor and appointment details are stored.

README.md: A document containing an outline of the project, its features and how to use it.

##### Usage

Clone the repository: git clone <repository_url>

Install the required packages: pip install -r requirements.txt

Run the application: python project.py

##### Files

project.py: This is where all key features of the Hospital Management System reside. It consists of user authentication, patient and doctor management, appointment booking and viewing appointments. The main function determines what happens in the program when a user gives an input based on his or her role privilege.

requirements.txt: It contains Python packages required by this application. These are such as inflect used to change numbers into words and pytest that enables one to run test cases easily.

data/: It has three files namely patients.json, doctors.json and appointments.json (contain data about patients, doctors and appointments respectively) in JSON format for storing user data in between sessions so as to allow easy retrieval & manipulation of these records.

README.md: This documentation file provides an overview of the project, its features and how to use it. It also explains the project structure, design choices, and rationale behind certain decisions.

##### Design Choices

Data Persistence: JSON files were chosen for storing patient, doctor and appointment data due to their simplicity and ease of use. This allows for data integrity and availability across sessions, ensuring that important information is not lost between application runs.

Modular Code: The application is structured into separate functions for different functionalities such as user authentication, patient management ,doctor management and appointment booking. This modular approach enhances code readability, maintainability and scalability making it easy to expand or modify the application.

User Roles: The application implements user roles (admin, doctor,receptionist) with role-based permissions restricting access to specific functionalities. This enhances security while ensuring that sensitive information is only accessed by authorized users.

Testability: The code has been designed with easy testability in mind – each functionality has its own test cases done in pytest framework. That means that the user can be confident in regard to whether our program works correctly under different scenarios or not.

The Hospital Management System is a super handy tool for efficiently managing hospital operations. It's designed with a user-friendly interface that healthcare professionals can easily navigate to provide top-notch patient care. The main goal is to simplify administrative tasks, boost workflow efficiency, and ultimately improve the quality of care that healthcare facilities offer.
