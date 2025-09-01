class CheckoutSolution:
    def checkout(self, skus):

        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}


        for item in skus:
            if item not in prices:
                return -1


        item_counts = {
            'A': skus.count('A'),
            'B': skus.count('B'),
            'C': skus.count('C'),
            'D': skus.count('D'),
            'E': skus.count('E')
}


# This offer reduces the number of 'B's we need to charge for.
        free_Bs = item_counts['E'] // 2
# Use max(0, ...) to ensure the count doesn't go below zero.
        item_counts['B'] = max(0, item_counts['B'] - free_Bs)

        total_bill = 0


        count_A = item_counts['A']
        total_bill += (count_A // 5) * 200 # Add price for groups of 5
        remaining_A = count_A % 5 # See what's left
        total_bill += (remaining_A // 3) * 130 # Add price for groups of 3 from the remainder
        total_bill += (remaining_A % 3) * prices['A'] # Add price for the final leftovers

        count_B = item_counts['B']
        total_bill += (count_B // 2) * 45 # Add price for groups of 2
        total_bill += (count_B % 2) * prices['B'] # Add price for the rest


        total_bill += item_counts['C'] * prices['C']
        total_bill += item_counts['D'] * prices['D']
        total_bill += item_counts['E'] * prices['E']

        return total_bill


