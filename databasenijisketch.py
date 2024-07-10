
#Combined Code 
import sqlite3

# Function to establish a connection to the SQLite database
def connect_db():
    conn = sqlite3.connect('/Users/yaminshweyihtay/Downloads/nijisketchdata.db')
    return conn

# Function to insert a new reservation into the database
def insert_reservation(guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Reservation (guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (guest_name, guest_phone, guest_email, reservation_date, reservation_time, num_guests, special_requests))
    conn.commit()
    conn.close()

# Function to retrieve all reservations from the database
def get_all_reservations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Reservation")
    reservations = cursor.fetchall()
    conn.close()
    return reservations

# # Main script to test the database functions
# if __name__ == "__main__":
#     # Example usage: Insert a new reservation
#     insert_reservation('sweet', '123-456-7890', 'johndoe@example.com', '2024-06-30', '19:00', 4)

#     # Example usage: Retrieve all reservations
#     reservations = get_all_reservations()
#     for reservation in reservations:
#         print(reservation)
