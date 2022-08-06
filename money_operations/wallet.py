

class Wallet():

    def __init__(self, id, amount_usd, amount_pln, amount_eur, amount_btc):
        self.id = id
        self.amount_usd = amount_usd
        self.amount_pln = amount_pln
        self.amount_eur = amount_eur
        self.amount_btc = amount_btc

    def __str__(self):
        return f"{self.id} BTC: {self.amount_btc} USD: {self.amount_usd}"