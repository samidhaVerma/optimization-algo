# Samidha M. Verma

from population import *
import random

target = "Sam"
n = 1000
mutation_rate = 0.01
population = generate_population(n, len(target))
temp = 0

fitness = []
deleted = []

for i in range(n):
    fitness.append(compute_fitness(population[i], target))
    print("".join(population[i]))

while (temp != 1):
    matingpool = mating_pool(population, fitness)
    
    new_population = []
    new_fitness = []
    
    for _ in range(n):
        partnerA = matingpool[random.randint(0, len(matingpool))]
        partnerB = matingpool[random.randint(0, len(matingpool))]
        child = crossover(partnerA, partnerB)
        child = mutation(child, mutation_rate)
        
        new_population.append(child)
    
    for i in range(n):
        new_fitness.append(compute_fitness(new_population[i], target)) 
        if (new_fitness[i] == 100):
            temp = 1
            print("".join(new_population[i]))
            print("Target reached!")
            break 
    fitness = new_fitness
    population = new_population
