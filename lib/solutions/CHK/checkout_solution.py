from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):
        # The full price list for all items in Round 4
        prices = {
            'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
            'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40,
            'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20, 'U': 40,
            'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50
        }

        # Step 1: Immediately check if any item in the basket is invalid.
        if any(item not in prices for item in skus):
            return -1

        # Step 2: Use a Counter to get the quantity of each item.
        item_counts = Counter(skus)
        
        # Step 3: Apply all "get a different item free" offers first.
        # This works by reducing the count of the item that becomes free.
        item_counts['B'] = max(0, item_counts['B'] - (item_counts['E'] // 2))
        item_counts['M'] = max(0, item_counts['M'] - (item_counts['N'] // 3))
        item_counts['Q'] = max(0, item_counts['Q'] - (item_counts['R'] // 3))
        
        # Step 4: Handle "buy X get one of the same free" offers.
        # This is the same as paying for fewer items.
        item_counts['F'] -= item_counts['F'] // 3
        item_counts['U'] -= item_counts['U'] // 4

        # Step 5: Define all multi-buy offers.
        # IMPORTANT: They are sorted from the best deal to the worst for each item.
        multi_buy_offers = {
            'A': [(5, 200), (3, 130)],
            'B': [(2, 45)],
            'H': [(10, 80), (5, 45)],
            'K': [(2, 150)],
            'P': [(5, 200)],
            'Q': [(3, 80)],
            'V': [(3, 130), (2, 90)]
        }

        total_bill = 0

        # Step 6: Loop through the items that have multi-buy offers.
        for item, offers in multi_buy_offers.items():
            count = item_counts[item]
            for offer_count, offer_price in offers:
                # Calculate how many times this specific offer can be applied.
                num_deals = count // offer_count
                total_bill += num_deals * offer_price
                # Update the remaining count of the item.
                count %= offer_count
            
            # Add the cost of any items that are left over after the offers.
            total_bill += count * prices[item]
            # Set the item's count to 0 so we don't accidentally charge for it again.
            item_counts[item] = 0

        # Step 7: Calculate the cost for all remaining items.
        # This loop will now only include items that had no multi-buy offers.
        for item, count in item_counts.items():
            total_bill += count * prices[item]

        return total_bill