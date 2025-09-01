
        class CheckoutSolution:
        def checkout(self, skus):
# Price list from the rules
           prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}


for item in skus:
    if item not in prices:
            return -1

    total_bill = 0

    count_A = skus.count('A')
# Add the price for the special offer (groups of 3)
        total_bill += (count_A // 3) * 130
# Add the price for any leftover 'A's
        total_bill += (count_A % 3) * prices['A']


    count_B = skus.count('B')
# Add the price for the special offer (groups of 2)
        total_bill += (count_B // 2) * 45
# Add the price for any leftover 'B's
        total_bill += (count_B % 2) * prices['B']

    total_bill += skus.count('C') * prices['C']
    total_bill += skus.count('D') * prices['D']


        return total_bill