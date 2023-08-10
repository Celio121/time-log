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


    if len(sys.argv) == 2:
        choice = sys.argv[1]
    else:
        choice = input("Choose an option (1, 2, or 3): ")

    if choice == '1':
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        time_in(firstname, lastname)
        print("Sign-In recorded.")

    elif choice == '2':
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        time_out(firstname, lastname)
        print("Sign-Out recorded.")
    
    elif choice == '3':
        print("Exiting...")
        sys.exit(0)
        
    else:
        print("Invalid choice. Please enter either '1', '2', or '3'.")
        sys.exit(1)