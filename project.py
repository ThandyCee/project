import json
import sys
from datetime import datetime

def authenticate_user():
    users = [
        {"username": "admin", "password": "admin123", "role": "admin", "name": "Admin User"},
        {"username": "drsmith", "password": "doc123", "role": "doctor", "name": "Dr. Smith"},
        {"username": "reception", "password": "rec123", "role": "receptionist", "name": "Receptionist"}
    ]
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    print("Invalid credentials")
    return None

def add_patient():
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    dob = input("Enter patient date of birth (YYYY-MM-DD): ")
    patient = {"name": name, "age": age, "dob": dob}
    try:
        with open('data/patients.json', 'r+') as file:
            data = json.load(file)
            data.append(patient)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open('data/patients.json', 'w') as file:
            json.dump([patient], file, indent=4)
    print(f"Patient {name}, aged {age}, born on {dob}, added successfully.")

def get_all_patients():
    try:
        with open('data/patients.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def add_doctor():
    name = input("Enter doctor name: ")
    specialty = input("Enter doctor specialty: ")
    doctor = {"name": name, "specialty": specialty}
    try:
        with open('data/doctors.json', 'r+') as file:
            data = json.load(file)
            data.append(doctor)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open('data/doctors.json', 'w') as file:
            json.dump([doctor], file, indent=4)
    print(f"Doctor {name}, specialized in {specialty}, added successfully.")

def get_all_doctors():
    try:
        with open('data/doctors.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def book_appointment():
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    appointment = {"patient_name": patient_name, "doctor_name": doctor_name, "date": date}
    try:
        with open('data/appointments.json', 'r+') as file:
            data = json.load(file)
            data.append(appointment)
            file.seek(0)
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open('data/appointments.json', 'w') as file:
            json.dump([appointment], file, indent=4)
    print(f"Appointment for {patient_name} with {doctor_name} on {date} booked successfully.")

def view_appointments():
    try:
        with open('data/appointments.json', 'r') as file:
            data = json.load(file)
            if data:
                for appt in data:
                    print(f"Appointment: {appt['patient_name']} with {appt['doctor_name']} on {appt['date']}")
            else:
                print("No appointments found.")
    except FileNotFoundError:
        print("No appointments found.")

def main():
    user = authenticate_user()
    if user:
        print(f"Welcome {user['role']} {user['name']}")
        while True:
            print("\n1. Add Patient\n2. Add Doctor\n3. Book Appointment\n4. View Appointments\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1' and user['role'] in ['admin', 'receptionist']:
                add_patient()
            elif choice == '2' and user['role'] == 'admin':
                add_doctor()
            elif choice == '3' and user['role'] in ['admin', 'receptionist']:
                book_appointment()
            elif choice == '4' and user['role'] in ['admin', 'doctor']:
                view_appointments()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice or insufficient permissions. Please try again.")

if __name__ == "__main__":
    main()

