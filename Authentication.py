from conn import create_connection

def register_owner(email, password):   
    cursor = connection.cursor()
    query = "INSERT INTO owner (email, password) VALUES (%s, %s)"
    cursor.execute(query, (email, password))
    connection.commit()
    print("Owner registered successfully.")


def owner_login(email, password):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM owner WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    if result:
        return result  # Return owner details if login is successful
    else:
        return None
    

connection=create_connection()

