import sqlite3


with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    # Creatign table named Roster if it does not exist
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Roster(
            id INTEGER PRIMARY KEY,
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )"""
    )
    # Inserting data into the Roster table
    cursor.execute(
        """INSERT INTO Roster (Name, Species, Age) VALUES
            ('Benjamin Sisko', 'Human', 40),
            ('Jadzia Dax', 'Trill', 300),
            ('Kira Nerys', 'Bajoran', 29)
        """
    )
    # Updating the name of Jadzia Dax to Ezri Dax
    cursor.execute(
        """
            UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'
        """
    )

    cursor.execute(
        """
            SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
        """
    )
    data = cursor.fetchall()
    for row in data:
        print(f"Name: {row[0]}, Age: {row[1]}")
    # Deleting all records where Age is greater than 100
    cursor.execute(
        """
            DELETE FROM Roster WHERE Age > 100
        """
    )
    #  Adding a new column named Rank 
    cursor.execute(
        """
            ALTER TABLE Roster ADD column Rank
        """
    )   
    cursor.execute(
        """
            UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'
        """
    )
    cursor.execute(
        """
            UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'
        """
    )
    cursor.execute(
        """
            UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'
        """
    )
    
    

    