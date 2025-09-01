from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):
        # Updated prices for Round 5
        prices = {
            'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
            'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40,
            'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40,
            'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21
        }

        if any(item not in prices for item in skus):
            return -1

        item_counts = Counter(skus)
        
        item_counts['B'] = max(0, item_counts['B'] - (item_counts['E'] // 2))
        item_counts['M'] = max(0, item_counts['M'] - (item_counts['N'] // 3))
        item_counts['Q'] = max(0, item_counts['Q'] - (item_counts['R'] // 3))
        
        item_counts['F'] -= item_counts['F'] // 3
        item_counts['U'] -= item_counts['U'] // 4

        total_bill = 0

        group_offer_items = ['Z', 'S', 'T', 'Y', 'X'] # Sorted by price, descending
        
        total_group_items = sum(item_counts[item] for item in group_offer_items)
        
        
        num_group_deals = total_group_items // 3
        total_bill += num_group_deals * 45
        
        items_in_deal = num_group_deals * 3
        for item in group_offer_items:
            if items_in_deal == 0:
                break
            
            count_to_remove = min(item_counts[item], items_in_deal)
            item_counts[item] -= count_to_remove
            items_in_deal -= count_to_remove

        multi_buy_offers = {
            'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'H': [(10, 80), (5, 45)],
            'K': [(2, 120)], 'P': [(5, 200)], 'Q': [(3, 80)], 'V': [(3, 130), (2, 90)]
        }

        for item, offers in multi_buy_offers.items():
            count = item_counts[item]
            for offer_count, offer_price in offers:
                num_deals = count // offer_count
                total_bill += num_deals * offer_price
                count %= offer_count
            
            total_bill += count * prices[item]
            item_counts[item] = 0

        for item, count in item_counts.items():
            total_bill += count * prices[item]

        return total_bill