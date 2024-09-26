import sqlite3

def insert_one_row(
        database_name: str,
        table_name: str,
        columns_name: str,
        values: str
) -> None:
    """
    Inserts a row into a table in the specified SQLite database.

    Args:
        database_name (str): The name of the database (without the `.db` extension).
        table_name (str): The name of the table where the row will be inserted.
        columns_name (str): The names of the columns (comma-separated) where the values will be inserted.
        values (str): The values to be inserted (comma-separated and enclosed in single quotes).

    Returns:
        None: This function does not return any value.
        )

    """
    
    database_name2 = f'{database_name}.db'
    
    conn = sqlite3.connect(database_name2)
    cursor = conn.cursor()

    query = f"""
    INSERT INTO {table_name} ({columns_name})
    VALUES ({values})
    """
    cursor.execute(query)
    conn.commit()
    conn.close()
    return None
