from conn import create_connection

def view_listings():
    connection = create_connection()
    if connection is None:
        print("Database connection failed")
        return []
    
    try:
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
        
        return results
    except Exception as e:
        print(f"Error fetching listings: {e}")
        return []
    finally:
        if connection.is_connected():
            connection.close()

def get_listings_json():
    """Return listings in JSON format for web API"""
    connection = create_connection()
    if connection is None:
        return []
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT title, address, distance_from_campus, price, facilities, contact, description FROM listings"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error fetching listings: {e}")
        return []
    finally:
        if connection.is_connected():
            connection.close()