import sqlite3
import csv

csv_filename = "polaczenia_duze.csv"
sqlite_filename = 'polaczenia_duze.sqlite'

class Polaczenia:

    def __init__(self):
        self.file_name = csv_filename
        file = open(self.file_name)
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

    def pokaz_sume_polaczen_nadawcow_i_czas_ostatniego_polaczenia_odbiorcy(self):
        identyfikatory_nadawcow = eval(input())
        # print(type(identyfikatory_nadawcow))

        conn = sqlite3.connect(sqlite_filename)
        c = conn.cursor()

        lista_sum_polaczen = []
        if isinstance(identyfikatory_nadawcow, int):
            c.execute("SELECT SUM(duration) FROM polaczenia WHERE from_subscriber = " + str(identyfikatory_nadawcow))
            lista_sum_polaczen.append(c.fetchone()[0]) 
        else: 
            for nadawca in identyfikatory_nadawcow:
                c.execute("SELECT SUM(duration) FROM polaczenia WHERE from_subscriber = " + str(nadawca))
                lista_sum_polaczen.append(c.fetchone()[0]) 
        

        print(tuple(lista_sum_polaczen))
        conn.close()



if __name__=='__main__':
    Polaczenia().pokaz_sume_polaczen_nadawcow_i_czas_ostatniego_polaczenia_odbiorcy()