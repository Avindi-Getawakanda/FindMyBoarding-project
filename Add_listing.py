from conn import create_connection

def add_listing(owner_id, title, image_path, address, distance, price, facilities, contact, description):    
    cursor = connection.cursor()
    query = "INSERT INTO listings (title, image_path, address, distance_from_campus, price, facilities, contact, description, owner_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (title, image_path, address, distance, price, facilities, contact, description, owner_id))
    connection.commit()
    print("Listing added successfully.")
    connection.close()

connection=create_connection()