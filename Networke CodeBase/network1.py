import networkx as nx
import networkx
import matplotlib.pyplot as plt
import pylab as plt
import itertools
import networkx as nx
from networkx.algorithms import community

G = nx.Graph()
G.add_edges_from([('RezaGplzar', 'ElnazShakerdoost',{'weight': 100}), ('RezaGplzar', 'NikiKarimi',{'weight': 200}), ('NikiKarimi', 'ElnazShakerdoost',{'weight': 300}), ('HootanShakiba', 'ElnazShakerdoost',{'weight': 300}), ('HootanShakiba', 'MahnazAfshar',{'weight': 100}),
                 ('BahramRadan', 'NavidMohammadzadeh',{'weight': 100}), ('RezaGplzar', 'MahnazAfshar',{'weight': 400}), ('FreshtehHosseini', 'BahramRadan'  ,{'weight': 100}), ('MahnazAfshar', 'NavidMohammadzadeh',{'weight': 200}), ('FreshtehHosseini', 'AfsanehPakro',{'weight': 100}) ,('BahramRadan', 'AmirAghaii',{'weight': 300}) ,('BahramRadan', 'DibaZAhedi',{'weight': 100}), ])


communities_generator = nx.community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)


communities_generator = community.girvan_newman(G)



print("--------------------------------------------------------------------------------------------------------------")
print("1.View Of network Iranian Actor and Actress")
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
