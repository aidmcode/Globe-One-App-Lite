from CTkMessagebox import CTkMessagebox
from datetime import *
import json
import os

def show_error(title, message):
    CTkMessagebox(title=title, message=message, icon ="cancel")
def show_success(title, message):
    CTkMessagebox(title=title, message=message, icon ="check")

class System:
    def __init__(self, acc_number, acc_pin):
        self.acc_number = acc_number
        self.acc_pin = acc_pin     
        self.empty_acc_data = {"balance": 0, "promos": {}, "transac_history": {}}
        
    def register(self):
        with open(f"{self.acc_number}.json", mode = "w+") as a:
            json.dump(self.empty_acc_data, a)
            account_details={}
            account_details[self.acc_number] = self.acc_pin

            #checks if the accounts file exists, if not, create one with blank account data
            if os.path.exists("accounts.json"):
                with open("accounts.json", mode = "r+") as a:
                    loaded_accs = json.load(a)
                loaded_accs.append(account_details)
                
            else:
                loaded_accs = [account_details]
            with open("accounts.json", mode = "w+") as a:
                json.dump(loaded_accs, a) 
        
    def login(self):
        if os.path.exists("accounts.json"):
            with open("accounts.json", mode = "r+") as a:
                load_accs = json.load(a)
            accs_list = []
            pins_list = []
            for accs in load_accs:
                for i in accs.keys():
                    accs_list.append(i)
                for j in accs.values():
                    pins_list.append(j)

            #creates dictionary containing accounts and their pins
            acc_details = dict(zip(accs_list, pins_list)) 

            #returns integer values used for validation in the main python file
            if self.acc_number not in accs_list:
                return -1
            elif self.acc_pin != acc_details[self.acc_number]:
                return -2
            else:
                return 1
        else:
            return -3

    def transaction_history(self, transactions, purchasetime):
        with open(f"{self.acc_number}.json", mode = "r+") as f:
            acc_data = json.load(f)
            acc_data["transac_history"][transactions] = purchasetime

        with open(f"{self.acc_number}.json", mode = "w+") as f:
            json.dump(acc_data, f, indent=4, separators=(',',': '))

    def buyload(self, amount):
        with open(f"{self.acc_number}.json", mode = "r+") as f:
            acc_data = json.load(f)
            acc_data["balance"] += int(amount)
            show_success("BUY LOAD", f"P{amount} WAS ADDED TO YOUR ACCOUNT BALANCE")
            purchasetime = DateTime(0).get_purchasetime()
            
        with open(f"{self.acc_number}.json", mode = "w+") as f:
            json.dump(acc_data, f, indent=4, separators=(',',': '))

        transactions = f'P{amount} was added to your load balance.'
        self.transaction_history(transactions, purchasetime) #add to transaction history
       
    def buypromo(self, promo, price, duration):
        with open(f"{self.acc_number}.json", mode = "r+") as f:
            acc_data = json.load(f)
            
            if promo in acc_data["promos"]:
                show_error("ERROR", "YOU HAVE ALREADY SUBSCRIBED TO THIS PROMO")
            #check if user have sufficient load balance
            elif acc_data["balance"] < int(price):
                show_error("ERROR", "INSUFFICIENT BALANCE")
            else:
                purchasetime = DateTime(duration).get_purchasetime()
                expiration = DateTime(duration).get_expiration()

                acc_data["promos"][promo] = [purchasetime, expiration] #add to active promos
                acc_data["balance"] -= int(price) #deduct promo price to load balance
                show_success("BUY PROMO", "YOU HAVE SUCCESSFULLY SUBSCRIBED TO " + promo)
                with open(f"{self.acc_number}.json", mode = "w+") as f:
                    json.dump(acc_data, f, indent=4, separators=(',',': '))
                transactions = f'Subscribed to {promo}'
                
                self.transaction_history(transactions, purchasetime)
    
    def sendload(self, recipient, amount):
        with open(f"{self.acc_number}.json", mode = "r+") as f:
            user_data = json.load(f)

            #check if user have sufficient load balance
            if user_data["balance"] < int(amount):
                show_error("ERROR", "INSUFFICIENT BALANCE")
            elif int(amount) < 10 or int(amount) > 2000:
                show_error("ERROR", "ENTER AMOUNT BETWEEN P10 TO P2,000 ONLY")
            else:
                user_data["balance"] -= int(amount) #deduct the amount to sender's load balance
                user_transactions = f'You have sent P{amount} to {recipient}'
                purchasetime = DateTime(0).get_purchasetime()
                user_data["transac_history"][user_transactions] = purchasetime
                show_success("SEND LOAD", f"SUCCESSFULLY SENT P{amount} TO {recipient}")
                with open(f"{self.acc_number}.json", mode = "w+") as f:
                    json.dump(user_data, f, indent=4, separators=(',',': '))

                with open(f"{recipient}.json", mode = "r+") as f:
                    recipient_data = json.load(f)
                    recipient_data["balance"] += int(amount) #add the amount to recipient's load balance

                    transactions = f'{self.acc_number} sent P{amount} to your account balance.'
                    recipient_data["transac_history"][transactions] = purchasetime

                with open(f"{recipient}.json", mode = "w+") as f:
                    json.dump(recipient_data, f, indent=4, separators=(',',': '))
 

class DateTime:
    def __init__(self, promo_duration):
        self.promo_duration = promo_duration
        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day
        self.hour = datetime.now().hour
        self.time = str(datetime.now()).split(" ")[1][:5] #get only hour and minute
    #Get current date and time
    def get_purchasetime(self):
        purchasetime = f'{self.month}-{self.day}-{self.year} {self.time}'
        return purchasetime
    #Calculate Expiration date and time
    def get_expiration(self):
        combine = self.promo_duration + self.day
        if self.month == 12 and combine > 31:
            expday = combine - 31
            self.year += 1
            self.month += 1
        elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11 and combine > 30:
                expday = combine - 30
                self.month += 1
        elif self.month == 2 and combine > 28:
                expday = combine - 28
                self.month += 1
        else:
            if combine > 31:
                expday = combine - 31
                self.month += 1
            else:
                expday = combine

        expiration_date = f'{self.month}-{expday}-{self.year} {self.time}'
        return expiration_date        
        


    




