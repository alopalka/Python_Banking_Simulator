

class Wallet():

    def __init__(self, id, amount_usd, amount_pln, amount_eur, amount_btc) -> None:
        self.id = id
        self.amount_usd = amount_usd
        self.amount_pln = amount_pln
        self.amount_eur = amount_eur
        self.amount_btc = amount_btc

    def create_empty(self, db_operator) -> None:
        cell_names = ['id', 'amount_usd',
                      'amount_pln', 'amount_eur', 'amount_btc']
        values = [self.id, self.amount_usd, self.amount_pln,
                  self.amount_eur, self.amount_btc]
        db_operator.write_data("Wallets", cell_names, values)

    def __str__(self):
        return f" USD : {'%.2f'%self.amount_usd}\n" + f" PLN : {'%.2f'%self.amount_pln}\n" + f" EUR : {'%.2f'%self.amount_eur}\n" + f" BTC : {'%.8f'%self.amount_btc}\n"
