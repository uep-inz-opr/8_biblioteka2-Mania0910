import csv

class Polaczenia:
    # biblioteka csv, klasa DictReader, biblioteka Pandas(nie ma na sprawdzarce)
    def __init__(self, file_name:str):
        # self.file_name = file_name
        self.file_name = file_name
        file = open(file_name)
        self.csvreader = csv.reader(file)
        self.header = []
        self.header = next(self.csvreader)

        self.rows = []
        for row in self.csvreader:
            self.rows.append(row)
        file.close()

    def pobierz_najczesciej_dzwoniacego(self):
        nadawca_z_najwieksza_liczba_polaczen = (0,0)
        for row in self.rows:
            ilosc_polaczen = 0
            # print(row)
            for row2 in self.rows:
                if row[0] == row2[0]:
                    ilosc_polaczen += 1
            if ilosc_polaczen > nadawca_z_najwieksza_liczba_polaczen[1]:
                nadawca_z_najwieksza_liczba_polaczen = (int(row[0]), ilosc_polaczen)
        print(nadawca_z_najwieksza_liczba_polaczen)



polaczenia = Polaczenia("phoneCalls.csv")
polaczenia.pobierz_najczesciej_dzwoniacego()

if __name__=='__main__':
    print(Polaczenia(input()).pobierz_najczesciej_dzwoniacego())