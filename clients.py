"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or save it into a new attribute and return the value.
        """
        return (self.current_amount - self.starting_amount) / self.account_age
        pass


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    # open file
    with open(filename, "r") as file:
        # read file
        lines = file.readlines()
        # make client objects
        clients = []
        for line in lines:
        # pieces of data are separated by a comma, so we take only the first piece of a line
            name = line.split(",")[0]
            #we now have a string with the name of the client and will add it to clients list
            clients.append(name)
            
            
        # return list
        return clients

    pass


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    # pieces of data are separated by a comma, so we take only the second piece of a line
    with open(filename, "r") as file:
        # read file
        lines = file.readlines()
        # make client objects
        clients = []
        for line in lines:
            name = line.split(",")[1]
            if name == bank:
                #add the first piece of a line to clients list
                clients.append(line.split(",")[0])
            
            
        # return list
        return clients
    pass


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    with open(filename, "r") as file:
        # read file
        lines = file.readlines()
        for line in lines:

            print(line)
            print("*"*50)
            #Find the client that has earned the most money per day.
            #If two people have earned the same amount of money per day, then return the one that has earned it in less time.
            #If no-one has earned money (everyone has less or equal to wat they started with), then return None.

            name = line.split(",")[0]
            account_age = int(line.split(",")[2])
            starting_amount = int(line.split(",")[3])
            current_amount = int(line.split(",")[4])
            money_per_day = (current_amount - starting_amount) / account_age

            earnings = []
            #Find the client that has earned the most money per day.
            if current_amount > starting_amount:
                #add an array to earnings list with the name of the client and the earnings per day and the account age
                earnings += ([name, money_per_day, account_age])
            # if len(earnings) == 0:
            #     return None

            #If two people have earned the same amount of money per day, then return the one that has earned it in less time.

            print (earnings)

            for earning in earnings:
                name = earning[0]
                money_per_day = earning[1]
                account_age = earning[2]
                temp_array = []
                if len(temp_array) == 0:
                    temp_array.append([name, money_per_day, account_age])
                else:
                    if money_per_day > temp_array[0][1]:
                        temp_array[0] = [name, money_per_day, account_age]
                    elif money_per_day == temp_array[0][1]:
                        if account_age < temp_array[0][2]:
                            temp_array[0] = [name, money_per_day, account_age]
                

            #Return only the clients name that says "Highest earnings per day:" at the start
            return "Highest earnings per day: " + temp_array[0][0]   
    pass


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    pass


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]
    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]
    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
