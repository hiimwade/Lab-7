"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')
import sqlite3
def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    con = sqlite3.connect('social_network.db')

    cur = con.cursor
    create_ppl_tbl_query= """
    CREATE TABLE IF NOT EXISTS people
    (
        id      INTEGER PRIMARY KEY,
        name    TEXT NOT NULL,
        email   TEXT NOT NULL,
        address TEXT NOT NULL,
        city    TEXT NOT NULL,
        province TEXT NOT NULL,
        bio     TEXT,
        age     INTEGER,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL
    );
    """
    cur.execute(create_ppl_tbl_query)
    con.commit
    con.close
    

    # Hint: See example code in lab instructions entitled "Creating a Table"
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    import sqlite3
    from datetime import datetime

    con = sqlite3.connect('social_network.db')
    cur = con.cursor
    add_person_query = """
    INSERT INTO people
    (
        name,
        email,
        address,
        city,
        province,
        bio,
        age,
        created_at,
        updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""
    new_person =('Bob Loblaw',
                 'bob.loblaw@whatever.net',
                 '123 Fake St.',
                 'Fakesville',
                 'Fake Edward Island',
                 'Enjoys making funny sounds when talking.',
                46,
                 datetime.now(),
                 datetime.now())
    
    cur.execute(add_person_query, new_person)
    con.commit()
    con.close

    from faker import Faker
    fake = Faker()
    
    
    for _ in range(200):
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = fake.random_int(min=1, max=100)
        email = fake.email()
        created_at = datetime.now()
        updated_at = created_at



                
                 







    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    return

if __name__ == '__main__':
   main()