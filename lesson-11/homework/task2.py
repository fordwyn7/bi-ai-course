import sqlite3

with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()
    
    # Create table named Books if it does not exist
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Author TEXT,
            Year_Published INTEGER,
            Genre TEXT
        )"""
    )
    
    # Inserting data into the Books table
    cursor.execute(
        """INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES
            ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
            ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic'),
            ('1984', 'George Orwell', 1949, 'Dystopian')
        """
    )
    
    # Updating the year of '1984' to 1950
    cursor.execute(
        """
            UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'
        """
    )
    # Selecting all records where Genre is 'Dystopian'
    cursor.execute(
        """
            SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'
        """
    )
    data = cursor.fetchall()
    for row in data:
        print(f"Title: {row[0]}, Author: {row[1]}")
    
    # Deleting all records where Year is lower than 1950 
    cursor.execute(
        """
            DELETE FROM Books WHERE Year_Published < 1950
        """
    )
    
    # Adding a new column named Genre
    cursor.execute(
        """
            ALTER TABLE Books ADD COLUMN Rating INTEGER
        """
    )
    
    cursor.execute(
        """
            UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'
        """
    )
    cursor.execute(
        """
            UPDATE Books SET Rating = 4.7 WHERE Title = '1984'
        """
    )
    cursor.execute(
        """
            UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'
        """
    )
    