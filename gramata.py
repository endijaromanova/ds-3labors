class Gramata:
    def __init__(self):      #izveido metodi, kas tiek automātiski izsaukta
        self.kontakti = {}   #izveido hash tabulu

    def add (self, numurs, vards):     #saglabā tabulā datus pēc atslēgas 'numurs', un tās vērtības 'vards'
        self.kontakti[numurs] = vards

    def delete (self, numurs):         #ja tabulā ievade skarīt ar atslēgu, to izdzēš kopā ar tās vērtību
        if numurs in self.kontakti:
            del self.kontakti[numurs]

    def find (self, numurs):             #ja tabulā ievade sakrīt ar atslēgu, tā atgriež vērtību, ja ne - "not found"
        if numurs in self.kontakti:
            return self.kontakti[numurs] #atgriež 'numurs' VĒRTĪBU ('vards')
        else:
            return "not found"

def main():
    skaits = int(input())   #cik reizes lietotājs veiks komandas
    gramata = Gramata()
    for _ in range (skaits):      #cikliski iet cauri komandām, kamēr sasniedz ievadīto komandu skaitu
        sadale = input().split()
        komanda = sadale[0]
        if komanda == "add":
            gramata.add(sadale[1], sadale[2])
        elif komanda == "delete":
            numurs = sadale[1]
            gramata.delete(numurs)
        elif komanda == "find":
            print(gramata.find(sadale[1]))

main()
