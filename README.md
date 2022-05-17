## 1. Assignment 3 - Network Analysis
In this assignment, you are going to write a ```.py``` script which can be used for network analysis. As we saw last week, pretty much anything can be formalised as a network. We're not going to focus on creating the edgelists for this project; instead, the goal is to have a script that would work the same way on _any_ input data, as long as the input format is correct. 

So, as test data, I recommend that you use the files in the folder called ```network_data```. However, the final script should be able to be resused and work on any undirected, weighted edgelist with the same column names.

Your script should do the following:

- If the user enters a _single filename_ as an argument on the command line:
  - Load that edgelist
  - Perform network analysis using ```networkx```
  - Save a simple visualisation
  - Save a CSV which shows the following for every node:
    - name; degree; betweenness centrality; eigenvector_centrality
- If the user enters a _directory name_ as an argument on the command line:
  - Do all of the above steps for every edgelist in the directory
  - Save a separate visualisation and CSV for each file


## 2. Methods

## 3. Usage ```network_analysis.py```
To run the code you should:
- Pull this repository with this folder structure 
- Install the packages in ```requirements.txt```
- Set your current working directory to the level above ```src```
- Place the data in ```in```
- Write in the command line either: ```python src/network_analysis.py -f "file name"``` or: ```python src/network_analysis.py -d "directory name"```
  - The outputs in ```out``` was created with: ```python src/assignment3.py -f "1H4.csv"```

## 4. Discussion of Results
