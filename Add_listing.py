from conn import create_connection

def add_listing(owner_id, title, image_path, address, distance, price, facilities, contact, description):    
    connection = create_connection()
    if connection is None:
        raise Exception("Database connection failed")
    
    try:
        cursor = connection.cursor()
        query = "INSERT INTO listings (title, image_path, address, distance_from_campus, price, facilities, contact, description, owner_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (title, image_path, address, distance, price, facilities, contact, description, owner_id))
        connection.commit()
        print("Listing added successfully.")
        return True
    except Exception as e:
        print(f"Error adding listing: {e}")
        connection.rollback()
        raise e
    finally:
        if connection.is_connected():
            connection.close()