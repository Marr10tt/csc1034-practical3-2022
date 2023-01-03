import sys
import os
import time
import argparse

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


def stochastic_page_rank(graph, args):
    """Stochastic PageRank estimation

    Parameters:
    graph -- a graph object as returned by load_graph()
    args -- arguments named tuple

    Returns:
    A dict that assigns each page its hit frequency

    This function estimates the Page Rank by counting how frequently
    a random walk that starts on a random node will after n_steps end
    on each node of the given graph.
    """
    raise RuntimeError("This function is not implemented yet.")


def distribution_page_rank(graph, args):
    """Probabilistic PageRank estimation

    Parameters:
    graph -- a graph object as returned by load_graph()
    args -- arguments named tuple

    Returns:
    A dict that assigns each page its probability to be reached

    This function estimates the Page Rank by iteratively calculating
    the probability that a random walker is currently on any node.
    """
    raise RuntimeError("This function is not implemented yet.")

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
    algorithm = distribution_page_rank if args.method == 'distribution' else stochastic_page_rank
    print ("H")
    graph = load_graph(args)
    print("H")
    print_stats(graph)

    start = time.time()
    ranking = algorithm(graph, args)
    stop = time.time()
    time = stop - start

    top = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    sys.stderr.write(f"Top {args.number} pages:\n")
    print('\n'.join(f'{100*v:.2f}\t{k}' for k,v in top[:args.number]))
    sys.stderr.write(f"Calculation took {time:.2f} seconds.\n")
