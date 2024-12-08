from conn import create_connection

def view_listings():
    cursor = connection.cursor()
    query = "SELECT title, address, distance_from_campus, price, facilities, contact, description FROM listings"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print("Title: ", row[0])
        print("Address: ", row[1])
        print("Distance: ", row[2], " km")
        print("Price: ", row[3], " Rs.")
        print("Facilities: ", row[4])
        print("Contact: ", row[5])
        print("Description: ", row[6])
        print()


connection=create_connection()