# Combinatorial-Algorithms-Assignment-1

GENEREAL REMARKS:
Team Size: 2 students
Language: Python

Problem Description: Given an undirected graph, find all sets of vertives that form an induced paaw subgraph. A paw graph consists of a triangle with an additional vertex connected to exactly one vertex of the triangle.

Input Format: 
First line: n m (number of vertives and edges)
Next m lines: v w (edges between vertices, numbered from 0 to n-1)

Output Format:
One set of vertices per line in lexicographic order (e.g., [0, 1, 2, 3])
If no induced paws exist, print an appropriate message

Example, for input:
7 10
1 2
1 3
2 3
3 4
2 4
0 1
0 4
6 4
5 3
2 6

The program should print:
[0,1,2,3] 
[0,2,3,4] 
[0,2,4,6] 
[1,2,3,5] 
[1,2,3,6] 
[1,2,4,6] 
[2,3,4,5] 

While for input:
6 12 
0 1 
0 3 
1 3 
2 1 
2 4 
4 1 
5 3 
5 4 
3 4 
0 2 
0 5 
2 5
The program should print that it found no paws in the graph.


---

ISSUES TO BE FIXED:

1. Assignment 1, Exercise 1, issue 1:
   Check if "continue" is allowed to be use!
2. Assignment 1, Exercise 2, issue 1:
   Both of ds_comb_ass_1-2.py and gpt_comb_ass_1-2.py have issues with printing the output after reading all the inputs. Fix it!!!

---

CA_notes:

This is the notes file made by Ray221f for reviewing, not aim at uploading on M**dle


