from datetime import datetime
import sqlite3
import sys

def db_create(): # Creating the table database
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS timelogs(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           firstname VARCHAR(20) NOT NULL,
                           lastname VARCHAR(20) NOT NULL,
                           signing BOOLEAN NOT NULL,
                           time DATETIME NOT NULL)""")
        except Exception as e:
            print(f"Error creating table: {e}")

def time_in(firstname, lastname): # time in inputting data into database
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""INSERT INTO timelogs(
                       firstname,
                       lastname,
                       signing,
                       time
                    ) VALUES (?, ?, ?, ?)""", (firstname, lastname, True, current_time,))
        connection.commit()

def time_out(firstname, lastname): # time out inputting data into database
    with sqlite3.connect("timelogged.db") as connection:
        cursor = connection.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""INSERT INTO timelogs(
                       firstname,
                       lastname,
                       signing,
                       time
                    ) VALUES (?, ?, ?, ?)""", (firstname, lastname, False, current_time,))
        connection.commit()

if __name__ == '__main__': # Run the code using app.py name
    db_create()

    while True: # Selecting the operation which the user is requesting to input their name
        print("Choose an option:")
        print("1. Sign In")
        print("2. Sign Out")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1': # signing in option
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            time_in(firstname, lastname)
            print("Sign-In recorded.")

        elif choice == '2': #signing out option
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            time_out(firstname, lastname)
            print("Sign-Out recorded.")

        elif choice == '3': # exiting the operation
            print("Exiting...")
            break  # Exit the loop and end the program
        
        else:
            print("Invalid choice. Please enter either '1', '2', or '3'.")