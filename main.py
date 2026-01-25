import sqlite3
import sys
import unicodedata


class Bank1:

    @staticmethod
    def clean(text):
        text = text.casefold()
        text = unicodedata.normalize("NFD", text)
        text = "".join(c for c in text if unicodedata.category(c) != "Mn")
        text = text.replace(" ", "")
        return text

    def enter_bank(self):
        not_found = True
        while True:
            have_account = input("Do you have an account? (y/n) or If you are admin type (a) >>>")
            if have_account == "n":
                print("Please create an account!")
                while self.insert_db():
                    self.insert_db()
                print("Your entry to the bank has been accepted!")
                print(f"Welcome :)")
                break
            elif have_account == "y":
                firstname = input("Please type your accounts firstname >>")
                lastname = input("Please type your accounts lastname >>")
                password = input("Please type your accounts password >>")
                if firstname != "" and lastname != "" and password != "":
                    rows = cursor.execute("SELECT firstname, lastname, password, amount FROM bank_users").fetchall()
                    for user in rows:
                        if user[0] == firstname and user[1] == lastname and user[2] == password:
                            print("Your entry to the bank has been accepted!")
                            print(f"Welcome, {firstname} {lastname}  :)")
                            not_found = False
                            break
                    if not_found:
                        print("No such account was found!")
                    else:
                        break

                else:
                    print("One of the fields are empty! Please try again!")

            elif have_account == "a":
                admin_name = input("Type admin name >>")
                admin_password = input("Type admin password >>")
                if admin_name == "admin" and admin_password == "root123":
                    print("Your entry to the bank has been accepted!")
                    print(f"Welcome :)")
                    break
                else:
                    print("Admin code is wrong!")

            else:
                print("Please enter a valid value!")

        return True

    def is_user_unique(self, firstname, lastname):
        rows = cursor.execute("SELECT firstname, lastname, password, amount FROM bank_users").fetchall()
        for user in rows:
            if self.clean(user[0]).replace(' ', '') == self.clean(firstname).replace(' ', '') and self.clean(user[1]).replace(' ', '') == self.clean(lastname).replace(' ', ''):
                return False

        return True

    def insert_db(self):
        firstname = input("Firstname >>")
        lastname = input("Lastname >>")
        if self.is_user_unique(str(firstname), str(lastname)):
            password = input("Please create a password >>")
            if firstname != "" and lastname != "" and password != "":
                cursor.execute(f"INSERT INTO bank_users VALUES ('{firstname}', '{lastname}', '{password}', '{0}')")
                connection.commit()
                print("Account has been created!")
                return False
            else:
                print("One of the fields are empty! Please try again!")
                self.insert_db()
        else:
            print("Name is already in the database!")
            print("Please try a different name!")
            self.insert_db()

    def edit_db(self):
        firstname = input("Type the firstname of the person you'd like to edit >>")
        lastname = input("Type the lastname of the person you'd like to edit >>")
        password = input("Type the password of the person you'd like to edit >>")
        field = input("Which field would you like to edit: firstname, lastname or password >>")
        updated_field = input("What would you like to update it to >>")
        try:
            cursor.execute(f"UPDATE bank_users SET {field} = ? WHERE firstname = ? AND lastname = ? AND password = ?",
                           (updated_field, firstname, lastname, password))
            connection.commit()
            print("Successfully updated user!")
        except Exception:
            print("You entered incorrect values!")
            while True:
                tekrar = input(
                    "If you don't want just type 'exit' to quit, or if you want to try again type 'yes' >>>")
                if tekrar == "yes":
                    self.edit_db()
                    break
                elif tekrar == "exit":
                    break
                else:
                    print("Please enter a valid value!")

    def get_user_info_db(self):
        target_firstname = input("Please type the firstname of the person you'd like to see information about >>")
        target_lastname = input("Please type the lastname of the person you'd like to see information about >>")
        target_password = input("Please type the password of the person you'd like to see information about >>")
        try:
            rows = cursor.execute(
                "SELECT firstname, lastname, password, amount FROM bank_users WHERE firstname = ? AND lastname = ? AND password = ?",
                (target_firstname, target_lastname, target_password)).fetchall()
            firstname = rows[0][0]
            lastname = rows[0][1]  # rows [(firstname, lastname, password, amount)]
            password = rows[0][2]
            amount = rows[0][3]
            print(
                f"{firstname} {lastname}'s account has {amount}TL and its password is {password}.")
        except Exception:
            print("No such account was found!")
            while True:
                tekrar = input(
                    "If you don't want just type 'exit' to quit, or if you want to try again type 'yes' >>>")
                if tekrar == "yes":
                    self.get_user_info_db()
                    break
                elif tekrar == "exit":
                    break
                else:
                    print("Please enter a valid value!")

    def delete_db(self):
        firstname = input("Type the firstname of the person that you would like to delete >>")
        lastname = input("Type the lastname of the person that you would like to delete >>")
        password = input("Type the password of the person that you would like to delete >>")
        if firstname != "" and lastname != "" and password != "":
            cursor.execute("DELETE FROM bank_users WHERE firstname = ? AND lastname = ? AND password = ?",
                           (firstname, lastname, password))
            connection.commit()
            if cursor.rowcount == 0:
                print("There aren't any account which has these values!")
                while True:
                    tekrar = input(
                        "If you don't want just type 'exit' to quit, or if you want to try again type 'yes' >>>")
                    if tekrar == "yes":
                        self.delete_db()
                        break
                    elif tekrar == "exit":
                        break
                    else:
                        print("Please enter a valid value!")
            else:
                print("Account successfully deleted!")

        else:
            print("One of the fields are empty!")
            while True:
                tekrar = input("If you don't want just type 'exit' to quit, or if you want to try again type 'yes' >>>")
                if tekrar == "yes":
                    self.delete_db()
                    break
                elif tekrar == "exit":
                    break
                else:
                    print("Please enter a valid value!")


class Bank2(Bank1):
    def __init__(self):
        self.admin = Admin()

    def enter_system(self):
        if self.enter_bank():
            self.select_options()

    def select_options(self):
        while True:
            options = input("""
    ---------------------------------------------------
    Type "0" to exit from system
    Type "1" to insert a new user
    Type "2" to delete user
    Type "3" to edit user
    Type "4" to get user information
    Type "5" to withdraw money
    Type "6" to deposit money
    Type "7" to display users (online admin can access)
    Type "8" to delete users (online admin can access)
    ---------------------------------------------------
    >>>""")

            if options == "0":
                self.exit_system()
            elif options == "1":
                self.insert_db()
            elif options == "2":
                self.delete_db()
            elif options == "3":
                self.edit_db()
            elif options == "4":
                self.get_user_info_db()
            elif options == "5":
                self.withdraw_money()
            elif options == "6":
                self.deposit_money()
            elif options == "7":
                self.admin.display_db()
            elif options == "8":
                self.admin.admin_delete_db()
            else:
                print("Please enter a valid value!")

    @staticmethod
    def exit_system():
        cursor.close()
        connection.close()
        sys.exit()

    def withdraw_money(self):
        firstname = input("Type the firstname of your account which you want to withdraw money from >>")
        lastname = input("Type the lastname of your account which you want to withdraw money from >>")
        password = input("Type the password of your account which you want to withdraw money from >>")
        try:
            rows = cursor.execute(
                "SELECT firstname, lastname, password, amount FROM bank_users WHERE firstname = ? AND lastname = ? AND password = ?",
                (firstname, lastname, password)).fetchall()
            amount = rows[0][3]
            amount_of_withdraw = int(input("How much money(TL) do you want to withdraw >>"))
            if amount_of_withdraw <= amount:
                amount -= amount_of_withdraw
                cursor.execute(
                    f"UPDATE bank_users SET amount = ? WHERE firstname = ? AND lastname = ? AND password = ?",
                    (amount, firstname, lastname, password))
                connection.commit()
                rows = cursor.execute(
                    "SELECT firstname, lastname, password, amount FROM bank_users WHERE firstname = ? AND lastname = ? AND password = ?",
                    (firstname, lastname, password)).fetchall()
                amount = rows[0][3]
                print("Successfully withdraw money!")
                print(f"Total balance >>> {amount}")
            else:
                print("The amount of money you are trying to withdraw is not available in your total balance!")
                while True:
                    tekrar = input(
                        "If you don't want just type 'exit' to quit, or if you want to try again type 'yes' >>>")
                    if tekrar == "yes":
                        self.withdraw_money()
                        break
                    elif tekrar == "exit":
                        break
                    else:
                        print("Please enter a valid value!")
        except Exception:
            print("No such account was found!")
            while True:
                tekrar = input(
                    "If you don't want just type 'exit' to quit, or if you want to try again type 'yes' >>>")
                if tekrar == "yes":
                    self.withdraw_money()
                    break
                elif tekrar == "exit":
                    break
                else:
                    print("Please enter a valid value!")

    def deposit_money(self):
        firstname = input("Type the firstname of your account which you want to deposit money to >>")
        lastname = input("Type the lastname of your account which you want to deposit money to >>")
        password = input("Type the password of your account which you want to deposit money to >>")
        amount_of_deposit = input("How much money(TL) do you want to deposit >>")
        try:
            cursor.execute(f"UPDATE bank_users SET amount = ? WHERE firstname = ? AND lastname = ? AND password = ?",
                           (amount_of_deposit, firstname, lastname, password))
            connection.commit()
            rows = cursor.execute(
                "SELECT firstname, lastname, password, amount FROM bank_users WHERE firstname = ? AND lastname = ? AND password = ?",
                (firstname, lastname, password)).fetchall()
            amount = rows[0][3]
            print("Successfully deposit money!")
            print(f"Total balance >>> {amount}")
        except Exception:
            print("No such account was found!")
            while True:
                tekrar = input(
                    "If you don't want just type 'exit' to quit, or if you want to try again type 'yes' >>>")
                if tekrar == "yes":
                    self.deposit_money()
                    break
                elif tekrar == "exit":
                    break
                else:
                    print("Please enter a valid value!")


class Admin:
    def admin_delete_db(self):
        print("You must be authorized to perform this operation!")
        print("If you are not an admin, you can exit by typing (exit). To continue, type (yes)!")
        admin = input(">>>")
        if admin == "exit":
            pass
        elif admin == "yes":
            admin_name = input("Type your admin name >>")
            admin_password = input("Type your admin password >>")
            if admin_name == "admin" and admin_password == "root123":
                rows = cursor.execute(
                    "SELECT firstname, lastname, password, amount FROM bank_users ORDER BY firstname ASC, lastname ASC").fetchall()

                print("Bank_users: ")
                for user in rows:
                    print(f"-firstname: {user[0]} -lastname: {user[1]} -password: {user[2]} -amount: {user[3]}")

                firstname = input("Type the firstname of the person that you would like to delete >>")
                lastname = input("Type the lastname of the person that you would like to delete >>")
                if firstname != "" and lastname != "":
                    cursor.execute("DELETE FROM bank_users WHERE firstname = ? AND lastname = ?",
                                   (firstname, lastname))
                    connection.commit()
                    if cursor.rowcount == 0:
                        print("There aren't any account which has these values!")
                        while True:
                            tekrar = input(
                                "If you don't want just type 'exit' to quit, or if you want to try again type 'yes' >>>")
                            if tekrar == "yes":
                                self.admin_delete_db()
                                break
                            elif tekrar == "exit":
                                break
                            else:
                                print("Please enter a valid value!")
                    else:
                        print("Account successfully deleted!")

                else:
                    print("One of the fields are empty!")
                    while True:
                        tekrar = input(
                            "If you don't want just type 'exit' to quit, or if you want to try again type 'yes' >>>")
                        if tekrar == "yes":
                            self.admin_delete_db()
                            break
                        elif tekrar == "exit":
                            break
                        else:
                            print("Please enter a valid value!")
            else:
                print("You entered incorrect values!")
                self.admin_delete_db()
        else:
            print("Please enter a valid value!")
            self.admin_delete_db()

    def display_db(self):
        print("You must be authorized to perform this operation!")
        print("If you are not an admin, you can exit by typing (exit). To continue, type (yes)!")
        admin = input(">>>")
        if admin == "exit":
            pass
        elif admin == "yes":
            admin_name = input("Type your admin name >>")
            admin_password = input("Type your admin password >>")
            if admin_name == "admin" and admin_password == "root123":
                rows = cursor.execute(
                    "SELECT firstname, lastname, password, amount FROM bank_users ORDER BY firstname ASC, lastname ASC").fetchall()

                print("Bank_users: ")
                for user in rows:
                    print(f"-firstname: {user[0]} -lastname: {user[1]} -password: {user[2]} -amount: {user[3]}")
            else:
                print("You entered incorrect values!")
                self.display_db()
        else:
            print("Please enter a valid value!")
            self.display_db()


connection = sqlite3.connect("bank_users.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE bank_users (firstname TEXT, lastname TEXT, password TEXT, amount INTEGER)")
except Exception as e:
    pass


bank = Bank2()

bank.enter_system()
