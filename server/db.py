import sqlite3

# sample code

def dict_factory(cursor, row):
 fields = []
 # Extract column names from cursor description
 for column in cursor.description:
    fields.append(column[0])

 # Create a dictionary where keys are column names and values are row values
 result_dict = {}
 for i in range(len(fields)):
    result_dict[fields[i]] = row[i]

 return result_dict

# End of sample code

class DB:
    def __init__(self, dbfilename):
        try:
            with open(dbfilename, 'x') as file:
                pass
        except FileExistsError:
            pass
        self.dbfilename = dbfilename
        self.connection = sqlite3.connect(dbfilename)
        self.cursor = self.connection.cursor()
        # Initialize table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                age INTEGER,
                rank TEXT,
                kills INTEGER
            )
        """)
        self.connection.commit()
        
    def readAllRecords(self):
        self.cursor.execute("SELECT * FROM messages")
        rows = self.cursor.fetchall()
        all = []
        for row in rows:
            d= dict_factory(self.cursor, row)
            all.append(d)
        print("the rows are", rows)
        return all
    
    def editRecord(self, id, d):
        data = [d["name"], d["description"], d["age"], d["rank"], d["kills"], id]
        self.cursor.execute("Update messages SET name=?, description=?, age=?, rank=?, kills=? where id = ?;", data)
        self.connection.commit()
    
    def saveRecord(self, record):
        data = [record["name"], record["description"], record["age"], record["rank"], record["kills"]]
        # self.cursor.execute("INSERT INTO messages (name, description, length, rating) VALUES ('testing', 'something goes here', 3.2, 5)")
        self.cursor.execute("INSERT INTO messages (name, description, age, rank, kills) VALUES (?, ?, ?, ?, ?)", data)
        self.connection.commit()
        
    def deleteRecord(self, id):
        self.cursor.execute("DELETE from messages where id = ?", [id])
        self.connection.commit()
        
    def close(self):
        self.connection.close()
        
if __name__ == "__main__":
    db = DB("messages.db")
    db.readAllRecords()
    db.saveRecord(1)
    db.readAllRecords()
    db.close()
