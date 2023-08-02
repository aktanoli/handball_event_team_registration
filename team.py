class Team:
    # Create A Constructor With Parameters
    # init Method For Class Team
    def __init__(self, id_, date, name, type_, fee_paid):
        self.__id = id_
        self.__date = date
        self.__name = name
        self.__type = type_
        self.__fee_paid = fee_paid
        #Initially, Cancellation Date of Team Participation Will Be Empty.
        self.__cancel_date = None

    # Access the Fields Methods (Setters & Getters)
    def get_id(self):
        return self.__id

    def get_paid_fee(self):
        return self.__fee_paid

    def get_type(self):
        return self.__type

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_type(self, type_):
        self.__type = type_

    def set_fee_paid(self, fee_paid):
        self.__fee_paid = fee_paid

    def set_date_cancel(self, cancel_date):
        self.__cancel_date = cancel_date

    def get_cancel_date(self):
        return self.__cancel_date

    # Get a data to write the object to txt file.
    def get_data_for_file(self):
        return f"{self.__id},{self.__date},{self.__name},{self.__type},{self.__fee_paid},{self.__cancel_date}"
    
    
    # It will be called when (function print() ) a Team instance.
    # Object is represent as string.
    def __str__(self):
        outcome = f"ID: {self.__id}\n"
        outcome += f"Name: {self.__name}\n"
        outcome += f"Registration Date: {self.__date}\n"
        outcome += f"Type: {self.__type}\n"
        if self.__fee_paid:
            outcome += f"Have You Paid The Fee: YES\n"
        else:
            outcome += f"Have You Paid The Fee: NO\n"
        if self.__cancel_date:
            outcome += f"Participation Date Cancel: {self.__cancel_date}\n"
        return outcome