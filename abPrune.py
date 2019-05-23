
'''
Class: CPSC 427 
Team Member 1: Andrew Abbott
Team Member 2: None
Submitted By Andrew Abbott
GU Username: aabbott
File Name: abPrune.py
Demonstrates AB Pruning:
--reads file representation of a graph as input
--converts the file to a dictionary representation of a tree
--implements the pseudo-code found on slide 28, E:Adversarial Games
--the pseudo-code is from a classic book on AI (Nilsson, N. (1998). Artificial Intelligence: A New Synthesis. Morgan Kaufmann)
--Jeff Wheadon (GU, class of 2018) wrote the core maxVal and minVal.
Usage 1:  python <program name> <file name> <player> <depth bound>
        python proj9_abPrune.py abEx5.txt max 3

Usage 2: The program can also be run from idle, in which case the parameters have to be hard-coded

'''

import sys

def maxVal(graph,node,alpha,beta,depth,depthBound):
    depth = depth + 1 
    v = float("-inf")
    #print(type(depthBound))
    if(depth < depthBound):
        print(node)
        if isinstance(node,int):
            return node
        
        for child in graph.get(node):
            v1 = minVal(graph,child,alpha,beta,depth,depthBound)
            if v is None or v1 > v:
                v = v1
            if beta is not None:
                if v1 >= beta:
                    return v
            if alpha is None or v1 > alpha:
     
               alpha = v1

    return v

def minVal(graph,node,alpha,beta,depth,depthBound):
    depth = depth + 1
    v = float("inf")
    #print(type(depthBound))
    if (depth < depthBound):
        print (node)
        if isinstance(node,int):
            return node
        
        for child in graph.get(node):
            v1 = maxVal(graph,child,alpha,beta,depth,depthBound)
            if v is None or v1 < v:
                v = v1
            if alpha is not None:
                if v1 <= alpha:
                    return v
            if beta is None or v1 < beta:
                beta = v1
    ''''
    else:
        if (isinstance(node, str)):
            v = charHuristic(node)
        else: 
            v = node
    '''
    return v

def charHuristic(node):
    return ord(node)

'''
Convert file to dictionary rep. of a graph.
S C
C A D E
A P B
P 2 3
B 5 99
D R 42
R 0
E T V
T 2 1
V 9 11

The left-most characters are parent nodes.
The first line indicates that the starting node is C.
The function constructs a dictionary, extracts the root and deletes its entry, leaving, in
this case, the dictionary representation of example 5:

graph = {'C' : ['A', 'D', 'E'],
             'A' : ['P', 'B'],
             'P' : [2,3],
             'B' : [5,99],
             'D' : ['R', 42],
             'R' : [0],
             'E' : ['T', 'V'],
             'T' : [2,1],
             'V' : [9,11]
             }
'''
def read_graph(file_name):
    #construct a dictionary from the input file
    with open(file_name) as fin:
        rows = (line.rstrip() for line in fin)
        graph = {r[0]: r[1:].split() for r in rows}
    
    #transform leaf nodes from strings to numeric values
    for key in graph.keys():
        for idx, child in enumerate(graph[key]):
            if not(child.isalpha()):
                graph[key][idx] = int(child)
            
    #extract and remove root information from the dictionary
    root = graph['S'][0]
    del graph['S']
   
    return str(root),graph

def AB(graph,root,alpha,beta,player,depth,depthBound):
    if player == 'max':
        maxVal(graph,root,alpha,beta,depth,depthBound)
    else:
        minVal(graph,root,alpha,beta,depth,depthBound)
        
        

def main():
    if len(sys.argv) > 2:           #parameters come from command line  
        file_name = sys.argv[1]  
        player = sys.argv[2]
        depthBound = int(sys.argv[3])
    else:
        file_name = 'abEx1.txt'     #default
        player = 'max'
        depthBound = 3

    depth = 0
    root, graph = read_graph(file_name)
    print('DepthBound: ' + str(depthBound))
    AB(graph,root, None, None, player, depth, depthBound+1)
    

main()
