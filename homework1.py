'''
Name: Amira Johnson
andrewID: amiraj
Homework 1 
September 21st, 2023
'''


'''
Problem 4a - Heuristic Approach
    - Goal: A greedy algorithm that repeatedly picks the genome that contains   
        the most reads that need to be accounted for. Do this until we have a 
        set of genomes that contains all reads.
    - Input: A set of genomes G, the number of reads n, and the number of  
            genomes m. 
    - Rule: g_{i, j} = 1 if genome i contains read j else 0. 
    - Output: The smallest subset of genomes containing all the reads.

    Example: 
        G = {{1, 0, 0, 1, 1, 1}, 
             {0, 1, 0, 1, 0, 0},
             {0, 0, 1, 0, 1, 1}}
        n = 6, m = 3
'''

def get_best_genome(G, n, m, reads_found, reads_left):
    best_genome = []
    max_found = 0
    for genome in G:
        current_found = 0
        for i in range(len(genome)):
            if genome[i] == 1 and reads_found[i] == 0: #if the genome hasnt been found
                current_found += 1
            
        if current_found > max_found: #update if we found more than what the last genome did.
            max_found = current_found
            best_genome = genome
    #need to remove the best genome from G 
    
    #now loop through best genome and update reads_found and reads_left
    if best_genome != []:
        for i in range(len(best_genome)):
            if best_genome[i] == 1 and reads_found[i] == 0:
                reads_left -=1
                reads_found[i] = 1
        G.remove(best_genome)
    return G, reads_found, best_genome, reads_left


def heuristic_approach(G, n, m):
    g_prime = []
    reads_found = [0 for i in range(n)]
    reads_left = n

    while reads_left > 0:
        if G != []:
            G, reads_found, best_genome, reads_left = get_best_genome(G, n, m, reads_found, reads_left)
            if best_genome not in g_prime and best_genome != []:
                g_prime.append(best_genome)
            if best_genome == []: return g_prime
        else: return []
    return g_prime       


# G = [[1, 1, 1, 1, 0, 1], 
#      [1, 1, 0, 1, 0, 0], 
#      [1, 0, 0, 1, 1, 1]]
# n = 6
# m = 3 

# print(heuristic_approach(G, n, m))

################################################################################
################################################################################

'''
Problem 4b
    - Goal: A brute-force approach that tries every subset of genomes
    - Input: A set of genomes G, the number of reads n, and the number of  
            genomes m. 
    - Rule: g_{i, j} = 1 if genome i contains read j else 0. 
    - Output: The smallest subset of genomes containing all the reads.
'''

#Powerset function adopted from:
#https://towardsdatascience.com/the-subsets-powerset-of-a-set-in-python-3-18e06bd85678

def classical_iterative(elems):
    powerset_size = 2**len(elems)
    counter = 0
    j = 0
 
    for counter in range(0, powerset_size):
        results = []
        for j in range(0, len(elems)):
            # take the element if on bit position j it says to take it (i.e. 1 appears)
            if((counter & (1 << j)) > 0):
                results.append(elems[j])
        yield results
 
#checks if the input subset covers all genes n
def is_valid_subset(subset, n):
    reads_left = n
    reads = [0 for i in range(n)]
    for s in subset:
        for i in range(len(s)):
            if s[i] == 1 and reads[i] == 0:
                reads[i] = 1
                reads_left -= 1
    return reads_left == 0


def brute_force_approach(G, n, m):
    powerset = classical_iterative(G)
    for subset in powerset:
        has_all = is_valid_subset(subset, n)
        if has_all: return subset
    return []

# print("brute force")
# G = [[1, 1, 0, 1, 0, 1], 
#      [1, 1, 0, 1, 0, 0], 
#      [1, 0, 1, 1, 1, 1]]
# n = 6
# m = 3 
# print(brute_force_approach(G, n, m))


'''
Problem e: Test your methods by creating a wrapper program that takes as input m, n, and a number of
iterations k. For each iteration, it should generate a random problem instance by filling in each
element of gij to be 0 or 1 with 50 percent probability. It should record the average solution size and
the average time to derive a solution for each method over all iterations. Run your program for
k = 100 and m = n = 1, m = n = 2, m = n = 3, etc., until one of the methods becomes too slow
to be practical. Return a plots of the average solution size and the average time required for each
methods as a function of n.
'''
import random
import timeit as time

def wrapper(m, n, k):
    brute_force_sum = 0
    brute_force_count = 0

    heuristic_sum = 0
    heuristic_count = 0

    genomes = [[0 for i in range(n)] for i in range(m)]
    for i in range(k):
        for genome in genomes:
            for j in range(n):
                random_number = random.randint(0, 10)
                if random_number < 5:
                    genome[j] = 0
                else:
                    genome[j] = 1
        #method 1: heuristic
        sol1 = heuristic_approach(genomes, n, m)
        heuristic_sum += len(sol1)
        heuristic_count += time.timeit(str(sol1))
        #method 2:
        sol2 = brute_force_approach(genomes, n, m)
        brute_force_sum += len(sol2)
        brute_force_count += time.timeit(str(sol2))
    h_avg = heuristic_sum / k
    bf_avg = brute_force_sum / k
    time_avg_hv = heuristic_count / k
    time_avg_bf = brute_force_count / k

    return h_avg, bf_avg, time_avg_hv, time_avg_bf

for i in range(0, 20, 1):
    h_avg, bf_avg, time_avg_hv, time_avg_bf = wrapper(i, i, 100)
    # total = time.timeit(str(wrapper(i, i, 100)), number = 1)
    print(i, i, 100)
    print("h average: ", h_avg)
    print("bf_average: ", bf_avg)
    print("time avg hv = ", time_avg_hv)
    print("time avg bf = ", time_avg_bf)
    print("\n")





