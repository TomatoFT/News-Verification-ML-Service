import mysql.connector


def table_exists(table_name, connection):
    try:
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a SHOW TABLES query to retrieve all table names
        cursor.execute("SHOW TABLES")

        # Fetch all table names returned by the query
        tables = cursor.fetchall()

        # Check if the specified table exists in the list of tables
        if (table_name,) in tables:
            return True
        else:
            return False

    except mysql.connector.Error as error:
        print(f"Error accessing MySQL: {error}")


# Connect to the MySQL database
def get_connection_to_mysql():
    connection = mysql.connector.connect(
        host="db",
        port="3306",
        user="root",
        password="uit-news",
        database="verification",
    )

    return connection


connection = get_connection_to_mysql()
table_name = "2_News_article"
# Create a cursor object to execute SQL statements
cursor = connection.cursor()


def create_table_in_db(connection, cursor, table_name):
    create_table_query = """
        CREATE TABLE {} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Title VARCHAR(255),
        Source VARCHAR(255),
        Content LONGTEXT,
        Is_verified VARCHAR(255)
        )
        """.format(
        table_name
    )

    # Execute the create table query
    cursor.execute(create_table_query)

    # Commit the changes to the database
    connection.commit()


if not table_exists(table_name, connection=connection):
    create_table_in_db(table_name=table_name, connection=connection, cursor=cursor)
else:
    pass


# Execute the SQL statements to load the data
def load_the_data_to_db(
    data, table_name=table_name, connection=connection, cursor=cursor
):
    print(data)
    try:
        sql = f"INSERT INTO {table_name} (Source, Title, Content, Is_verified) VALUES (%s, %s, %s, %s)"
        values = (
            data["Source"],
            data["Title"],
            data["Content"],
            # data["Summarization"],
            # data["Categories"],
            data["Is_verified"],
        )
        cursor.execute(sql, values)
        # Commit the changes to the database
        connection.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as error:
        # Handle the error
        print(f"Failed to insert data into MySQL table: {error}")


# load_the_data_to_db(connection, cursor)
# connection.close()


def observe_the_data_from_table(table_name=table_name, cursor=cursor):
    # Execute a SELECT query to fetch data from the table
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Process and display the data
    for row in rows:
        print(row)

    return "Successfully observe"

def count_data(table_name=table_name, cursor=cursor):
    query = f"SELECT COUNT(*) FROM {table_name}"

    cursor.execute(query)

    return cursor.fetchall()

def count_data_with_condition(condition, table_name=table_name, cursor=cursor):
    query = f"SELECT COUNT(*) FROM {table_name} WHERE {condition}"

    cursor.execute(query)

    return cursor.fetchall()