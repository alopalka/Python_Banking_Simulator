import time


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

    def is_possible(self, session, db_operator, recipient_username):

        user_in_db = db_operator.find_match(
            "Users", "username", recipient_username)

        if user_in_db == None:
            return False

        selected_currency = f"amount_{self.currency.lower()}"

        sender_amount_before = getattr(
            session.wallet, selected_currency)

        if self.amount<0:
            if abs(self.amount)>sender_amount_before:
                return False

        return True

    def make_transaction(self, session, db_operator, recipient_username):

        posibility_bool = self.is_possible(
            session, db_operator, recipient_username)

        if not posibility_bool:
            print("\n Inserted data are incorrect...")
            time.sleep(3)
            return False

        highest_transaction_id = self.find_newest_transaction(db_operator)
        recipent_user = db_operator.find_match(
            "Users", "username", recipient_username)
        recipent_id = recipent_user[5]

        selected_currency = f"amount_{self.currency.lower()}"

        if selected_currency == "amount_usd":
            wallet_cell_id = "1"
        elif selected_currency == "amount_pln":
            wallet_cell_id = "2"
        elif selected_currency == "amount_eur":
            wallet_cell_id = "3"
        elif selected_currency == "amount_btc":
            wallet_cell_id = "4"

        recipent_wallet = db_operator.find_match("Wallets", "id", recipent_id)
        recipent_amount_before = recipent_wallet[int(wallet_cell_id)]
        recipent_new_amount = recipent_amount_before + float(self.amount)

        cell_names = ['id', 'currency',
                      'wallet_from_id', 'wallet_to_id', 'amount']

        values = [highest_transaction_id+1, self.currency, self.wallet_from_id,
                  recipent_id, self.amount]

        db_operator.write_data("Transactions", cell_names, values)

        db_operator.update_data_one_item(
            "Wallets", selected_currency, recipent_new_amount, "id", recipent_id)

        session.refresh_wallet(db_operator)

        return True
