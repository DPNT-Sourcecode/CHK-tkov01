class CheckoutSolution:
    def checkout(self, skus):
     prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}

     for item in skus:
            if item not in prices:
                return -1

            item_counts = {
                 'A': skus.count('A'), 'B': skus.count('B'), 'C': skus.count('C'),
                 'D': skus.count('D'), 'E': skus.count('E'), 'F': skus.count('F')
}


    free_Bs = item_counts['E'] // 2
    item_counts['B'] = max(0, item_counts['B'] - free_Bs)


    total_bill = 0
    count_A = item_counts['A']
    total_bill += (count_A // 5) * 200
    remaining_A = count_A % 5
    total_bill += (remaining_A // 3) * 130
    total_bill += (remaining_A % 3) * prices['A']

    count_B = item_counts['B']
    total_bill += (count_B // 2) * 45
    total_bill += (count_B % 2) * prices['B']

    count_F = item_counts['F']
    total_bill += (count_F // 3) * 20
    total_bill += (count_F % 3) * prices['F']

    total_bill += item_counts['C'] * prices['C']
    total_bill += item_counts['D'] * prices['D']
    total_bill += item_counts['E'] * prices['E']

    return total_bill
