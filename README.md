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
This assignment explored different ways to think about connectedness of characters within a novel. the csv saved to ```out``` shows three types of centrality (connectedness) among nodes. Degree centrality counts the number of edges connected to a single node, which plays into the intuition that the more edges a node has the more important it is. Eigenvector centrality is a measure of how well a single node is connected to other nodes in terms of shared edges to other important nodes. It plays into the intuition that important nodes are connected to other important nodes. Lastly, betweenness centrality looks at whether nodes are important for communication between other nodes. It plays into the intuition that it is important if a node connects other nodes in the network.

To calculate these centrality types, I used ```networkx```. I then created a merged data frame of all three types of centrality and the node in question using ```pandas```, which is then saved to ```out``` 

The script furthermore creates a visualization of the network of characters within the novel. The visual element is an important part of understanding networks. To do this, I also used ```networkx``` and saved the figure in ```out``` with ```matplotlib.pyplot```

## 3. Usage ```network_analysis.py```
To run the code you should:
- Pull this repository with this folder structure 
- Install the packages in ```requirements.txt```
- Set your current working directory to the level above ```src```
- Place the data in ```in```
- Write in the command line either: ```python src/network_analysis.py -f "file name"``` or: ```python src/network_analysis.py -d "directory name"```
  - The outputs in ```out``` was created with: ```python src/assignment3.py -f "1H4.csv"```

## 4. Discussion of Results
