import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()  # создаём объект графа

# определяем список узлов (ID узлов)

# определяем список рёбер
# список кортежей, каждый из которых представляет ребро
# кортеж (id_1, id_2) означает, что узлы id_1 и id_2 соединены ребром
edgelist = [["Mannheim", "Frankfurt", 85], ["Mannheim", "Karlsruhe", 80], ["Erfurt",
"Wurzburg", 186], ["Munchen", "Numberg", 167], ["Munchen", "Augsburg", 84], ["Munchen",
"Kassel", 502], ["Numberg", "Stuttgart", 183], ["Numberg", "Wurzburg", 103], ["Numberg",
"Munchen", 167], ["Stuttgart", "Numberg", 183], ["Augsburg", "Munchen", 84], ["Augsburg",
"Karlsruhe", 250], ["Kassel", "Munchen", 502], ["Kassel", "Frankfurt", 173], ["Frankfurt",
"Mannheim", 85], ["Frankfurt", "Wurzburg", 217], ["Frankfurt", "Kassel", 173],
["Wurzburg", "Numberg", 103], ["Wurzburg", "Erfurt", 186], ["Wurzburg", "Frankfurt", 217],
["Karlsruhe", "Mannheim", 80], ["Karlsruhe", "Augsburg", 250],["Mumbai", "Delhi",400],
["Delhi", "Kolkata",500],["Kolkata", "Bangalore",600],["TX", "NY",1200],["ALB", "NY",800]]
# добавляем информацию в объект графа
for edge in edgelist:
    G.add_edge(edge[0],edge[1], weight = edge[2])

print(nx.shortest_path(G, "Stuttgart", "Frankfurt" , weight="weight"))
print(nx.shortest_path_length(G, "Stuttgart", "Frankfurt" , weight="weight"))
# рисуем граф и отображаем его
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()