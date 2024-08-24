import networkx as nx
import networkx
import matplotlib.pyplot as plt
import pylab as plt
import itertools
import networkx as nx
from networkx.algorithms import community

G = nx.Graph()
G.add_edges_from([('Dr.Rahmani', 'Dr.Khanjari',{'weight': 100}), ('Dr.Rahmani', 'Dr.Ashtiani',{'weight': 200}), ('Dr.Ashtiani', 'Dr.Khanjari',{'weight': 300}), ('Dr.etemadi', 'Dr.Khanjari',{'weight': 300}), ('Dr.Parsa', 'Dr.Mozaieni',{'weight': 100}),
                 ('Dr.Parsa', 'Dr.Jahed',{'weight': 100}), ('Dr.Rahmani', 'Dr.Ashtiani',{'weight': 400}), ('Dr.etemadi', 'Dr.Jahed'  ,{'weight': 100}), ('Dr.movahedi', 'Dr.etemadi',{'weight': 200}), ('Dr.Khanjari', 'Dr.movahedi',{'weight': 100}) ,('Dr.Jahed', 'Dr.Minaii',{'weight': 300}) ,('Dr.Mozaieni', 'Dr,maleki',{'weight': 100}),('Dr.Minaii', 'Dr.Kangavari',{'weight': 100}),('Dr.Mozaieni', 'Dr.Entezari',{'weight': 100}) ,('Dr,maleki', 'Dr.Rashidi',{'weight': 100}),('Dr,maleki', 'Dr.Smali',{'weight': 100}) ,('Dr.Khanjari', 'Dr.Smali',{'weight': 100})])

communities_generator = nx.community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)


communities_generator = community.girvan_newman(G)



print("--------------------------------------------------------------------------------------------------------------")
print("1.View Of network Professor IUST")
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