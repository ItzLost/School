class Stock:
    def __init__(self) -> None:
        self.qt_farine = 0
        self.nb_oeufs = 0 
        self.qt_beurre = 0

    def ajouter_beurre(self, qt: int) -> None:
        self.qt_beurre += qt

    def ajouter_farine(self, qt: int) -> None:
        self.qt_farine += qt

    def ajouter_oeuf(self, qt: int) -> None:
        self.nb_oeufs += qt

    def afficher(self) -> None:
        print(f"""
farine: {self.qt_farine}
oeufs: {self.nb_oeufs}
beurre: {self.qt_beurre}""")
        
    def stock_suffisant_brioche(self) -> bool:
        if self.qt_beurre >= 175 and self.nb_oeufs >= 4 and self.qt_farine >= 350:
            return True
        
    def produire(self) -> int:
        res = 0
        while self.stock_suffisant_brioche():
            self.qt_beurre -= 175
            self.qt_farine -= 350
            self.nb_oeufs -= 4
            res += 1

        return res
    
stock = Stock()
stock.ajouter_beurre(1000)
stock.ajouter_farine(1000)
stock.ajouter_oeuf(10)

print(stock.produire())
# 2
# Cette valeur représente le nombre de brioches produite

stock.afficher()
''' farine: 300
oeufs: 2
beurre: 650 '''