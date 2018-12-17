import sys

def search(operators: list, phone_number: str):
    telephone = phone_number.replace('+', '')
    best_match = {}
    for operator in operators:
        for prefix in range(1, len(telephone)):
            if telephone[:prefix] in operator.prices:
                best_match[operator.name] = float(operator.get_price(telephone[:prefix]))

    if not len(best_match):
        Exception('{} cannot be dialed by any operator'.format(phone_number))

    cheap_price = sys.float_info.max
    cheap_operator = ''
    for i in best_match:
        if cheap_price > best_match[i]:
            cheap_price = best_match[i]
            cheap_operator = i

    return cheap_price, cheap_operator
                
