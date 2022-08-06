

class Transaction():

    def __init__(self, id="", currency="", wallet_from_id="", wallet_to_id="", amount="") -> None:
        self.id = id
        self.currency = currency
        self.wallet_from_id = wallet_from_id
        self.wallet_to_id = wallet_to_id
        self.amount = amount

    def make_transaction(self, session, db_operator, recipient_username):

        recipent_user = db_operator.find_match(
            "Users", "username", recipient_username)

        recipent_id = recipent_user[5]

        cell_name = ['id', 'currency',
                     'wallet_from_id', 'wallet_to_id', 'amount']

        values = [1, self.currency, self.wallet_from_id,
                  recipent_id, self.amount]

        db_operator.write_data("Transactions", cell_name, values)

        selected_currency = f"amount_{self.currency.lower()}"

        recipent_new_amount = ""

        db_operator.update_data_one_item(
            "Wallets", selected_currency, recipent_new_amount, "id", recipent_id)

        sender_new_amount = session.wallet.selected_currency - self.amount

        db_operator.update_data_one_item(
            "Wallets", selected_currency, sender_new_amount, "id", session.user.id)
