#!/usr/bin/env python

# Samidha M. Verma

import random
import string
import numpy as np

def generate_population(n, l):
    population = []
    for i in range (0, n * l):
        population.append(random.choice(string.ascii_letters))
    population = np.reshape(population, (n, l))
    return population

def compute_fitness(x, target):
    length = len(target)
    fitness = 0
    for i in range(0, length):
        if (x[i] == target[i]):
            fitness = fitness + 1
    fitness = (int) (fitness / length * 100)
    return fitness

def mating_pool(pop, fitness):
    matingpool = []
    for i in range(0, len(pop)):
        if (fitness[i] == 0):
            break
        for j in range(fitness[i]):
            matingpool.append(pop[i])
    return matingpool

def crossover(parentA, parentB):
    child = parentA
    mid = random.randint(0, len(parentA))
    for i in range(0, len(parentA)):
        if(i < mid):
            child[i] = parentA[i]
        else:
            child[i] = parentB[i]
    return child

def mutation(x, rate):
    for i in range(0, len(x)):
        if (random.uniform(0, 1) < rate):
            x[i] = random.choice(string.ascii_letters)
    return x
