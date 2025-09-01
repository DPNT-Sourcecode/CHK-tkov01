class CheckoutSolution:
# The 'checkout' function MUST be indented once to be inside the class
    def checkout(self, skus):
# All the code for the function MUST be indented again
        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

        for item in skus:
            if item not in prices:
                return -1

        total_bill = 0

        count_A = skus.count('A')
        total_bill += (count_A // 3) * 130
        total_bill += (count_A % 3) * prices['A']

        count_B = skus.count('B')
        total_bill += (count_B // 2) * 45
        total_bill += (count_B % 2) * prices['B']

        total_bill += skus.count('C') * prices['C']
        total_bill += skus.count('D') * prices['D']

        return total_bill
