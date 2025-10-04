from conn import create_connection

def register_owner(email, password):   
    connection = create_connection()
    if connection is None:
        raise Exception("Database connection failed")
    
    try:
        cursor = connection.cursor()
        
        # Check if email already exists
        check_query = "SELECT email FROM owner WHERE email = %s"
        cursor.execute(check_query, (email,))
        if cursor.fetchone():
            raise Exception("Email already exists")
        
        # Insert new owner
        query = "INSERT INTO owner (email, password) VALUES (%s, %s)"
        cursor.execute(query, (email, password))
        connection.commit()
        print("Owner registered successfully.")
        return True
    except Exception as e:
        print(f"Error registering owner: {e}")
        connection.rollback()
        raise e
    finally:
        if connection.is_connected():
            connection.close()


def owner_login(email, password):
    connection = create_connection()
    if connection is None:
        return None
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM owner WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        return result  # Return owner details if login is successful
    except Exception as e:
        print(f"Error during login: {e}")
        return None
    finally:
        if connection.is_connected():
            connection.close()

