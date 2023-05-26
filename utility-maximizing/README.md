# Context
In the real world, you may have multiple decisions to make. You know how much they would make you feel, with 10 being ecstatic and 1 being "I wish I never did it". This isn't just limited to happiness (e.g. Utility = 6/10 happiness, Cost = $250), but also to quantity (e.g. Utility = 10 cars, Cost = $50,000).

The script simulates a model called Utility Maximization, which is a concept used by economists to determine the best decision to make based on the trade-off between the utility (happiness or satisfaction) and the cost of an action. The script works by taking input for the name of the item, the utility and cost of the item, and then calculates the utility maximizing formula to determine the best decision to make.

For example, imagine you have 3 choices of rollercoasters. The first ride gives you 10/10 happiness but will cost 80 minutes of line waiting. The second ride gives you 8/10 happiness but will only cost 60 minutes of waiting. The third ride gives you 6/10 happiness but will only cost 40 minutes of waiting. The program will output the third option, as it offers the highest satisfaction (6/10) for the lowest cost (40 minutes of waiting).

Through these calculations, the program will assume that the goal is to maximize satisfaction (utility + cost). However, you can also use this script to make business decisions by inputting different values for the utility and cost of each item.

https://corporatefinanceinstitute.com/resources/economics/utility-maximization/

OpenAI was used to make the script.

# Prerequisite
N/A
# How TO RUN
- Run program with your favourite python gui/command line
# How TO USE
Modify the section: {'name': 'Item1', 'utility': NUMBERX, 'cost': NUMBERY}
