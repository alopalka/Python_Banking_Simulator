

class Transaction():

    def __init__(self,id="",currency="",wallet_from_id="",wallet_to_id="",amount="") -> None:
        self.id=id
        self.currency=currency
        self.wallet_from_id=wallet_from_id
        self.wallet_to_id=wallet_to_id
        self.amount=amount

    def make_transaction(self,session,db_operator,recipient_username):
        
        recipent_user=db_operator.find_match("Users","username",recipient_username)

        recipent_id=recipent_user[5]

        

