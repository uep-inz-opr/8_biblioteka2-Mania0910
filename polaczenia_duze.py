import sqlite3
import csv

sqlite_filename = 'polaczenia_duze.sqlite'

class Polaczenia:

    def __init__(self, file_name:str):
        self.file_name = file_name
        file = open(file_name)
        self.csvreader = csv.reader(file)
        self.header = []
        self.header = next(self.csvreader)

        conn = sqlite3.connect(sqlite_filename)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS polaczenia
             (from_subscriber INTEGER, to_subscriber INTEGER, datetime TEXT, duration INTEGER, celltower INTEGER)''')
        c.execute("DELETE FROM polaczenia")
  
        for row in self.csvreader:
                row_values_arr = row[0].split(";")
                c.execute("INSERT INTO polaczenia VALUES (" + row_values_arr[0] + ", " + row_values_arr[1] + ", " + row_values_arr[2] + ", " + row_values_arr[3] + ", " + row_values_arr[4] + ")")
        file.close()
        conn.commit()
        conn.close()

    def pobierz_sume_czasow_polaczen(self):
         conn = sqlite3.connect(sqlite_filename)
         c = conn.cursor()
         c.execute("SELECT SUM(duration) FROM polaczenia")
         suma =  c.fetchone()[0]
         conn.close()
         return suma


if __name__=='__main__':
    print(Polaczenia(input()).pobierz_sume_czasow_polaczen())