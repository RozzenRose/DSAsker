async def data_to_string(data):
    purchases = sum([item['price'] for item in data['purchases']])
    incomes = sum([item['quantity'] for item in data['incomes']])
    currency = data['purchases'][0]['currency']
    return f"Покупки: {purchases}{currency}\nДоходы: {incomes}{currency}"
