class CheckoutSolution:
    def checkout(self, skus):
# Price list for Round 3
        prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}

# Check for any invalid items in the basket first
        for item in skus:
            if item not in prices:
                return -1

# Count how many of each item we have
        item_counts = {
            'A': skus.count('A'), 'B': skus.count('B'), 'C': skus.count('C'),
            'D': skus.count('D'), 'E': skus.count('E'), 'F': skus.count('F')
}

# Handle the "2E get one B free" offer first
        free_Bs = item_counts['E'] // 2
        item_counts['B'] = max(0, item_counts['B'] - free_Bs)

        total_bill = 0

# Handle item 'A' (5A offer before 3A offer)
        count_A = item_counts['A']
        total_bill += (count_A // 5) * 200
        remaining_A = count_A % 5
        total_bill += (remaining_A // 3) * 130
        total_bill += (remaining_A % 3) * prices['A']

# Handle item 'B' (using the new count)
        count_B = item_counts['B']
        total_bill += (count_B // 2) * 45
        total_bill += (count_B % 2) * prices['B']

# Handle item 'F' (3 for the price of 2)
        count_F = item_counts['F']
        total_bill += (count_F // 3) * 20
        total_bill += (count_F % 3) * prices['F']

# Handle items C, D, and E
        total_bill += item_counts['C'] * prices['C']
        total_bill += item_counts['D'] * prices['D']
        total_bill += item_counts['E'] * prices['E']

        return total_bill
