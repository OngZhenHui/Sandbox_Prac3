total_gophers = 1000
print("Welcome to the Gohper Population Simulator!\nStarting population: 1000")

import random
for i in range(10):
    print("\nYear {}\n****".format(i + 1))
    pop_increase = int(random.randint(10,20) / 100 * total_gophers)
    pop_decrease = int(random.randint(5,25) / 100 * total_gophers)
    total_gophers = total_gophers - pop_decrease + pop_increase
    print("{} gophers were born. {} died.\nPopulation: {}".format(pop_increase, pop_decrease, total_gophers))