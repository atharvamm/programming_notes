import sqlite3

# Function to create a new database or connect to an existing one
def create_db(db_name):
    try:
        connection = sqlite3.connect(db_name)
        connection.close()
        print(f"Database '{db_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")

# Function to create a new table in the database
def create_table(db_name, table_name, schema):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema});"
        cursor.execute(create_table_sql)
        connection.commit()
        connection.close()
        print(f"Table '{table_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# Function to insert data into a table
def insert_data(db_name, table_name, data):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        insert_sql = f"INSERT INTO {table_name} VALUES "
        for record in data:
            insert_sql += "(" + ", ".join([str(x) for x in record]) + "),"
        print(insert_sql)
        cursor.execute(insert_sql[:-1]+";")
        connection.commit()
        connection.close()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

# Function to query data from a table
def query_table(db_name, table_name, columns=None, condition=None):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        if columns is None:
            columns = "*"

        query_sql = f"SELECT {columns} FROM {table_name}"
        if condition:
            query_sql += f" WHERE {condition}"

        cursor.execute(query_sql)
        data = cursor.fetchall()
        connection.close()

        if data:
            return data
        else:
            print("No data found.")
            return None
    except sqlite3.Error as e:
        print(f"Error querying data: {e}")
        return None

# Function to delete data from a table based on a condition
def delete_data(db_name, table_name, condition):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        delete_sql = f"DELETE FROM {table_name} WHERE {condition};"
        cursor.execute(delete_sql)
        connection.commit()
        connection.close()
        print("Data deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting data: {e}")


# Function to drop a table in the database
def drop_table(db_name, table_name):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        drop_table_sql = f"DROP TABLE IF EXISTS {table_name};"
        cursor.execute(drop_table_sql)
        connection.commit()
        connection.close()
        print(f"Table '{table_name}' dropped successfully.")
    except sqlite3.Error as e:
        print(f"Error dropping table: {e}")

def run_query(db_name, query):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        print("Query Run.")
    except sqlite3.Error as e:
        print(f"Error with Query: {e}")


# Example usage:
# drop_table("my_database.db", "employees")
# create_db("my_database.db")
# create_table("my_database.db", "employees", "id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT")
# insert_data("my_database.db", "employees", (1, 'Alice', 60000, 'HR'))
# query_result = query_table("my_database.db", "employees")
# delete_data("my_database.db", "employees", "id=1")