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






