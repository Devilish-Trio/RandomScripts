def maximize_utility(items, budget):
  # Initialize total utility to 0
  total_utility = 0

  # Sort the items by utility-to-cost ratio
  items.sort(key=lambda x: x['utility'] / x['cost'], reverse=True)

  # Iterate through the items and add as much as we can afford
  best_item = None
  for i, item in enumerate(items):
    if budget >= item['cost']:
      budget -= item['cost']
      total_utility += item['utility']
      best_item = item
    else:
      break

  # Output the rankings in plain English
  rankings = {0: "#1", 1: "#2", 2: "#3"}
  for i, item in enumerate(items):
    ranking = rankings.get(i, f"{i+1}th")
    print(f"{item['name']} with {item['utility'] / item['cost']:.3f} is the {ranking} best option")

  if best_item:
    print(f"The best item to purchase is {best_item['name']} with a utility of {best_item['utility']} and a cost of {best_item['cost']}")

  return total_utility

# Test the function with some sample data
items = [
  {'name': 'Item1', 'utility': 10, 'cost': 80},
  {'name': 'Item2', 'utility': 9, 'cost': 70},
  {'name': 'Item3', 'utility': 6, 'cost': 40},
  {'name': 'Item4', 'utility': 5, 'cost': 350},
]
budget = 150

print(maximize_utility(items, budget))  # Expected output: 15 (1 Item1 + 1 Item2)
