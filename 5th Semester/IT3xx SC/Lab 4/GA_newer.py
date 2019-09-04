import random

def eval_fitness(population):
    fitness = []
    for person in population:
        a = person[0]
        b = person[1]
        c = person[2]
        d = person[3]
        # function
        r = a + (2*b) + (3*c) + (4*d)
        fitness.append(r)
    return fitness

def selection(fitness): 
    total = sum(fitness)
    probability = [(f/total) for f in fitness]
    probability.insert(0,0.0)
    cumulation = [probability[0]]
    for i in range(1,len(probability)):
        cumulation.append(probability[i] + cumulation[-1])
    
    selection_rank = []
    pred_rand = [random.uniform(0,1) for i in range(len(fitness))]
    
    for pred in pred_rand:
        for i in range(1,len(cumulation)):
            if (pred > cumulation[i-1]) and (pred < cumulation[i]):
                selection_rank.append(i)
                break
    
    return selection_rank

def crossover():
    pass

def mutation():
    pass

def genetic_algorithm(pop_size,no_chromosomes):
    population = [
        [random.randrange(1,100) for i in range(no_chromosomes)] for j in range(pop_size)
    ]

    termination_condition = True
    for i in range(1):
        fitness = eval_fitness(population)
        selection_rank = selection(fitness)
        crossover()
        mutation()

def main():
    genetic_algorithm(6,4)

if __name__ == '__main__':
    main()