import sqlite3

class DataBaseManipulation:
    def __init__ (self,table,df):
        self.table =table
        self.df = df
        
    def Save(self):
        conn = sqlite3.connect('database')
        c = conn.cursor()
        c.execute(f'CREATE TABLE IF NOT EXISTS {self.table} (Description text, Price text, Link text)')
        conn.commit()
        self.df.to_sql(self.table, conn, if_exists='replace', index = False)
        c.execute(f'''  
        SELECT * FROM {self.table}
          ''')