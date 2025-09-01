
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
#  Errsa's pricebook
price_book = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

special_offers = {
    'A' : {'count' : 3, 'price' : 130},
    'B' : {'count' : 2, 'price' : 45}
}

for item in skus:
    if item not in price_book :
        return -1
    
    item_counts = {
        'A' : skus.count('A'),
        'B' : skus.count('B'),
        'C' : skus.count('C'),
        'D' : skus.count('D')
    }
total_bill = 0

count_A = item_counts['A']
offer_A = special_offers['A']
total_bill += (count_A // offer_A ['count'])* price_book['A']


count_B = item_counts['B']
offer_B = special_offers['B']
total_bill += (count_B // offer_B ['count'])* price_book['B']


total_bill += item_counts['C']* price_book['C']

total_bill += item_counts['D']* price_book['D']

return total_bill