from money_operations.wallet import Wallet


class Transaction():

    def __init__(self, id="", currency="", wallet_from_id="", wallet_to_id="", amount="") -> None:
        self.id = id
        self.currency = currency
        self.wallet_from_id = wallet_from_id
        self.wallet_to_id = wallet_to_id
        self.amount = float(amount)

    def find_newest_transaction(self, db_operator):

        highest_transaction_id = db_operator.find_newest(
            cell_name="id", table_name="Transactions")[0]

        return highest_transaction_id

    def make_transaction(self, session, db_operator, recipient_username):

        highest_transaction_id = self.find_newest_transaction(db_operator)

        recipent_user = db_operator.find_match(
            "Users", "username", recipient_username)

        recipent_id = recipent_user[5]

        recipent_wallet = db_operator.find_match("Wallets", "id", recipent_id)

        cell_names = ['id', 'currency',
                      'wallet_from_id', 'wallet_to_id', 'amount']

        values = [highest_transaction_id+1, self.currency, self.wallet_from_id,
                  recipent_id, self.amount]

        db_operator.write_data("Transactions", cell_names, values)

        selected_currency = f"amount_{self.currency.lower()}"

        if selected_currency == "amount_usd":
            wallet_cell_id = "1"
        elif selected_currency == "amount_pln":
            wallet_cell_id = "2"
        elif selected_currency == "amount_eur":
            wallet_cell_id = "3"
        elif selected_currency == "amount_btc":
            wallet_cell_id = "4"

        recipent_new_amount = recipent_wallet[int(
            wallet_cell_id)] + float(self.amount)

        db_operator.update_data_one_item(
            "Wallets", selected_currency, recipent_new_amount, "id", recipent_id)

        sender_new_amount = getattr(
            session.wallet, selected_currency) - self.amount

        if recipent_id != session.user.id:
            sender_new_amount = getattr(
                session.wallet, selected_currency) - self.amount
            db_operator.update_data_one_item(
                "Wallets", selected_currency, sender_new_amount, "id", session.user.id)

        session.refresh_wallet(db_operator)
