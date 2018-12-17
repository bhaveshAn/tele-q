class Operator(object):

    def __init__(self, name: str, prices: dict):
        self.name = name
        self.prices = prices

    def get_price(self, prefix: str):
        return self.prices[prefix]

