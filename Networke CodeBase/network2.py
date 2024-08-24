import networkx as nx
import networkx
import matplotlib.pyplot as plt
import pylab as plt
import itertools
import networkx as nx
from networkx.algorithms import community

G = nx.Graph()
G.add_edges_from([('SaraYounesi', 'Abed Ebadi',{'weight': 100}), ('SaraYounesi', 'Nezakati',{'weight': 200}), ('Nezakati', 'Abed Ebadi',{'weight': 300}), ('Deniz Ahmadi', 'Abed Ebadi',{'weight': 300}), ('Deniz Ahmadi', 'kia',{'weight': 100}),
                 ('mamad', 'arshia',{'weight': 100}), ('SaraYounesi', 'kia',{'weight': 400}), ('AliSalimi', 'mamad'  ,{'weight': 100}), ('kia', 'arshia',{'weight': 200}), ('AliSalimi', 'Aria',{'weight': 100}) ,('mamad', 'Amiri',{'weight': 300}) ,('mamad', 'pakdaman',{'weight': 100}),('mamad', 'hanie',{'weight': 100}),('hanie', 'narges',{'weight': 100}) ,('narges', 'pakdaman',{'weight': 100}),('hanie', 'sana',{'weight': 100}) ,('Amiri', 'sana',{'weight': 100})])

communities_generator = nx.community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)


communities_generator = community.girvan_newman(G)



print("--------------------------------------------------------------------------------------------------------------")
print("1.View Of network Student IUSR")
print("--------------------------------------------------------------------------------------------------------------")
print(G)
print('1.Community detection', sorted(map(sorted, next_level_communities)))
print("--------------------------------------------------------------------------------------------------------------")
print('2.Modularity 1 ', nx.community.greedy_modularity_communities(G))
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print('3.Modularity 2', nx.community.naive_greedy_modularity_communities(G))
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print('4 Measuring partitions', nx.community.modularity(G, nx.community.label_propagation_communities(G)))
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print('5.girvan_newman', tuple(sorted(c) for c in next(communities_generator)))
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")