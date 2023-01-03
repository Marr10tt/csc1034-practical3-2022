import sys
import time
import argparse
import random
from functools import wraps 
import threading

nodeList = {}

#loads the graph by reading the text file and inputting data to a dictionary
def load_graph(args):  
    #stores the graph as a dictionary  
    graph = {
        
    }
    # Iterate through the file line by line
    for line in args.datafile:
        # And split each line into two URLs
        node, target = line.split()

        #updates the graph to contain the node and its targets
        #checks to see if the node is already in dict, if not it adds it, if yes, appends the new target
        if node in graph.keys():
            graph[node].append(target)
        else:
            graph.update({node: []})
            graph[node].append(target)

    return graph

#prints out the statistics of the graph (number of nodes and edges)
def print_stats(graph):
    #calculates the number of nodes
    nodes = len(graph)
    #calculate the number of edges
    edges = 0
    for key in graph:
        edges+=len(graph[key])
    print("Number of nodes:", nodes)
    print("number of edges:", edges)

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args)+str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    
    return wrapper

@memoize
def stochastic_page_rank(graph, args):
    global nodeList

    #procedurally creates node classes and adds them to a list
    for keys in graph:
        nodeList.update({keys : 0})
    
    ##random walkers section

    #loops for the amount of walkers currently active
    for i in range (0, int(args.repeats/8)):
        currentNode = random.choice(list(graph))
        nodeList[currentNode]+=1
        #loops for a walkers steps
        for x in range (0, args.steps):
            currentNode = random.choice(graph[currentNode])
            nodeList[currentNode]+=1

    #returns the dictionary containing each node on the graph and its corresponding page rank
    return nodeList

def distribution_page_rank(graph, args):
    nodeList = {

    }

    #assigns each node a name and value in the nodeList dict
    for keys in graph:
        nodeList.update({keys : int(0)})
    
    #main loop
    i = int(0)
    for i in range (0, args.steps):
        for keys in nodeList:
            nodeList[keys] += (1/len(graph))/len(graph[keys])

    return nodeList


## additional arguments passed, defaults set as necessary
parser = argparse.ArgumentParser(description="Estimates page ranks from link information")
parser.add_argument('datafile', nargs='?', type=argparse.FileType('r'), default='school_web.txt',
                    help="Textfile of links among web pages as URL tuples")
parser.add_argument('-m', '--method', choices=('stochastic', 'distribution'), default='stochastic',
                    help="selected page rank algorithm")
parser.add_argument('-r', '--repeats', type=int, default=1_000_000, help="number of repetitions")
parser.add_argument('-s', '--steps', type=int, default=100, help="number of steps a walker takes")
parser.add_argument('-n', '--number', type=int, default=20, help="number of results shown")

##main "parent" function where all required functions are called
if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    algorithm = distribution_page_rank  #if args.method == 'distribution' else stochastic_page_rank
    graph = load_graph(args)
    print_stats(graph)

    start = time.time()
    ranking = algorithm(graph, args)
    if algorithm != distribution_page_rank:
        t1 = threading.Thread(target=stochastic_page_rank, args=(graph, args))
        t2 = threading.Thread(target=stochastic_page_rank, args=(graph, args))
        t3 = threading.Thread(target=stochastic_page_rank, args=(graph, args))
        t4 = threading.Thread(target=stochastic_page_rank, args=(graph, args))
        t5 = threading.Thread(target=stochastic_page_rank, args=(graph, args))
        t6 = threading.Thread(target=stochastic_page_rank, args=(graph, args))
        t7 = threading.Thread(target=stochastic_page_rank, args=(graph, args))
        t8 = threading.Thread(target=stochastic_page_rank, args=(graph, args))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
    #calculates page rank for each node using n and the amount of keys
    for keys in nodeList:
        nodeList[keys] = nodeList[keys]/args.repeats
    stop = time.time()
    time = stop - start

    top = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    sys.stderr.write(f"Top {args.number} pages:\n")
    print('\n'.join(f'{100*v:.2f}\t{k}' for k,v in top[:args.number]))
    sys.stderr.write(f"Calculation took {time:.2f} seconds.\n")
