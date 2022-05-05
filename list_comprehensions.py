
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = [list(x) for x in zip(species, population)]
endangered = [stat[0] for stat in pop_info if stat[1]<2500]

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
#map_testing = ["Fruit: "+fruit for fruit in lst_check]
map_testing = [x for x in map(lambda item: "Fruit: " + item, lst_check)]

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = [i for i in filter(lambda x: "B" == x[0], countries)]

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3 = [i for i in zip(filter(lambda x:len(x)>3, l1), filter(lambda x: len(x)>3, l2))]



# _______________________________>


def sublist(numbers):
    elem = 0
    output = []
    while numbers[elem] < 5:
        output.append(numbers[elem])
        elem += 1
    return output
    
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three = [k for k in sorted(medals.keys(), key=lambda k:medals[k])]
sortedm = sorted(medals.keys(), key=lambda k:medals[k])
sm = [k for k in sorted(medals.keys(), key=lambda k:medals[k], reverse=True)]
top_three = sm[:3]

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = [k for k in sorted(groceries.keys(), key=lambda k:groceries[k], reverse=True)]

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key=lambda x: ex_lst[1][1])
lsort = map(lambda k: k[1][1],ex_lst)