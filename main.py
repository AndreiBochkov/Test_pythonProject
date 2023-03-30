import datetime


class User:
    _id = -1
    _name = ""
    _phone = ""
    _email = ""
    _money = ""
    _orders = list()

    def __init__(self, id, name="", _phone="", email=""):
        self._id = id
        self._name = name
        self._phone = _phone
        self._email = email

    def create_Order(self):
        self._orders.append(Order())
        return self._orders[-1]

    def __str__(self):
        return f"User {self._name} with a balance {self._money} and orders {self._orders}"

    def __repr__(self):
        return f"USER {self._name} "


class Order:
    _id = -1
    _user = None
    _item = list()
    _cost = 0
    _datetime = datetime.datetime.now()
    _isconfirmed = False
    _ispaid = False

    def __init__(self, id, user):
        self._id = id
        self._user = _user
        self._phone = _phone
        self._email = email

    def add_item(self, item):
        self._items.append(item)
        self._cost += item.get_cost()

    def __str__(self):
        return f"Order {self._order}"

    def __repr__(self):
        return f"ORDER {self._name} "


class Item:
    _name = ""
    _cost = 0
    _description = ""

    def get_cost(self):
        return self._cost

    def __str__(self):
        return f""

    def __repr__(self):
        return f"ITEM {self._name} "


Ivan = User()

