# import libaries 
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import argparse

# load file
def load_filename(filename): 
    path = os.path.join("in", "network_data", 
                        filename)
    return path

# load directory
def load_directory(directory):
    path = os.path.join("in", directory)
    file_list = os.listdir(path)
    return path, file_list

# load edgelist
def read_csv(path): 
    return pd.read_csv(path, sep="\t", index_col=False)

# create a network visualization 
def network(data, filename):
    # create network 
    G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"])
    nx.draw_networkx(G, with_labels=True, node_size=20, font_size=10)
    # define outpath
    outpath = os.path.join("out", f"network_{filename[0:filename.index(f'.')]}.png") 
    # save figure
    plt.savefig(outpath, dpi=300, bbox_inches="tight")
    # clear figure so we can make another visualization
    plt.clf()

# degree centrality
def centrality(data, filename):
    G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"])
    degree = nx.degree_centrality(G)
    degree_df = pd.DataFrame(degree.items())
    degree_new = degree_df.rename(columns = {0: "node", 1: "degree"})
    ev = nx.eigenvector_centrality(G)
    eigenvector_df = pd.DataFrame(ev.items())
    eigenvector_new = eigenvector_df.rename(columns = {0: "node", 1: "eigenvector"})
    bc = nx.betweenness_centrality(G)
    betweenness_df = pd.DataFrame(bc.items())
    betweenness_new = betweenness_df.rename(columns = {0: "node", 1: "betweenness"})
    merged = pd.merge(pd.merge(degree_new, betweenness_new, on = "node"), eigenvector_new, on = "node")
    outpath = os.path.join("out", f"network_{filename[0:filename.index(f'.')]}.csv") 
    merged.to_csv(outpath, index=False, encoding = "utf-8")

def parse_args():
    # initialize argparse
    ap = argparse.ArgumentParser()
    # add command line parameters 
    ap.add_argument("-f", "--filename", required=False, help="The filename to use")
    ap.add_argument("-d", "--directory", required=False, help="The directory to use")
    args = vars(ap.parse_args())
    # return list og arguments
    return args    
    
# let's get the code to run!
def main(): 
    args = parse_args()
    if args["filename"] is not None and args["filename"].endswith(".csv"):
        path = load_filename(args["filename"])
        data = read_csv(path)
        network(data, args["filename"])
        centrality(data, args["filename"])
    elif args["directory"] is not None:
        results = load_directory(args["directory"])
        for filename in results[1]:
            if filename.endswith(".csv"):
                path = f"{results[0]}/{filename}"
                data = read_csv(path)
                network(data, filename)
                centrality(data, filename)
            else:
                pass
    else:
        pass
    
if __name__ == "__main__":
    main()

