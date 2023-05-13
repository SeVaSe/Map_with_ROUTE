import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.image import imread
import tkinter as tk


# def choose():
#     list_Points = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'q', 'r', 'w', 't', 'y',                                                    КОГДА НИБУДЬ ДОДЕЛАЮ ПОЛНОСТЬЮ, НО НЕ СЕЙЧАС
#                    'u', 'i', 'o', 'p', 's', 'h', 'j', 'k', 'l', 'z', 'x', 'v',
#                    'n', 'm', 'q1', 'w1', 'e1', 'r1', 't1', 'y1', 'u1', 'i1', 'o1',
#                    'p1',  'a1', 's1', 'd1', 'f1', 'g1', 'h1']
#
#
# root = tk.Tk()
#
# button_Test_A = tk.Button(root, text="firs", command=choose)
# button_Test_B = tk.Button(root, text="sec", command=choose)
#
#
# root.mainloop()


def draw_route(a, b):
    # Определение координат точек
    # 16Y - коридор, 28Y - лестницы
    points = {'a': (7.25, 12), 'b': (11.5, 12), 'c': (15.4, 12),
              'd': (3.8, 16), 'e': (7, 16), 'f': (11.3, 16),
              'g': (15, 16), 'q': (9, 16), 'r': (9, 21),
              'w': (15, 21), 't': (11.3, 21), 'y': (18, 16),
              'u': (18, 28), 'i': (21, 16), 'o': (21, 21),
              'p': (26, 16), 's': (24, 22), 'h': (26, 22),
              'j': (26.6, 5), 'k': (29, 22), 'l': (34, 16),
              'z': (34, 28), 'x': (34, 12), 'v': (46, 16),
              'n': (38, 16), 'm': (41, 16), 'q1': (41, 22),
              'w1': (41, 12), 'e1': (46, 22), 'r1': (46, 12),
              't1': (38, 22), 'y1': (26, 34), 'u1': (26, 43),
              'i1': (20, 43), 'o1': (13, 43), 'p1': (34, 43),
              'a1': (26, 48), 's1': (20, 47), 'd1': (13, 47),
              'f1': (8, 43), 'g1': (13, 40), 'h1': (20, 40),
              }

    # Создание графа
    G = nx.Graph()

    # Добавление вершин в граф
    for point in points:
        G.add_node(point, pos=points[point])

    # Добавление ребер между вершинами
    G.add_edge('f', 'g')
    G.add_edge('d', 'e')
    G.add_edge('e', 'f')
    G.add_edge('e', 'a')
    G.add_edge('f', 'b')
    G.add_edge('g', 'c')
    G.add_edge('q', 'e')
    G.add_edge('q', 'f')
    G.add_edge('q', 'r')
    G.add_edge('g', 'w')
    G.add_edge('f', 't')
    G.add_edge('y', 'g')
    G.add_edge('y', 'u')
    G.add_edge('y', 'i')
    G.add_edge('i', 'o')
    G.add_edge('i', 'p')
    G.add_edge('p', 'h')
    G.add_edge('p', 'j')
    G.add_edge('p', 'l')
    G.add_edge('k', 'h')
    G.add_edge('s', 'h')
    G.add_edge('l', 'x')
    G.add_edge('l', 'z')
    G.add_edge('l', 'n')
    G.add_edge('n', 'm')
    G.add_edge('m', 'v')
    G.add_edge('m', 'w1')
    G.add_edge('m', 'q1')
    G.add_edge('v', 'r1')
    G.add_edge('v', 'e1')
    G.add_edge('n', 't1')
    G.add_edge('h', 'y1')
    G.add_edge('y1', 'u1')
    G.add_edge('u1', 'a1')
    G.add_edge('u1', 'p1')
    G.add_edge('u1', 'i1')
    G.add_edge('i1', 's1')
    G.add_edge('i1', 'h1')
    G.add_edge('i1', 'o1')
    G.add_edge('o1', 'f1')
    G.add_edge('o1', 'g1')
    G.add_edge('o1', 'd1')

    # Импорт изображения и отображение его на графике
    img1 = imread('floor_kip_1.jpg')

    plt.imshow(img1, extent=[0, 50, 0, 50], alpha=1)

    # Построение маршрута от точки А до точки Б
    path = nx.shortest_path(G, source=a, target=b)

    # Отображение точек и маршрута + размер точек и текста этих точек
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_size=50, font_size=10)
    plt.plot([pos[node][0] for node in path],
             [pos[node][1] for node in path],
             color='r', linewidth=1)

    plt.show()




def stop_prog():
    # проверка на флаг
    flag_quest = input("Закончить ? yes или no: ")
    if flag_quest == "yes":
        print("программа закончена")
        return False
    else:
        return True



flag = True
while flag:
    print("""Доступные точки для: 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'q', 'r', 'w', 't', 'y',
                     'u', 'i', 'o', 'p', 's', 'h', 'j', 'k', 'l', 'z', 'x', 'v',
                     'n', 'm', 'q1', 'w1', 'e1', 'r1', 't1', 'y1', 'u1', 'i1', 'o1',
                     'p1', 'a1', 's1', 'd1', 'f1', 'g1', 'h1'""")

    a = input("Введите кабинет или место где вы щас находитесь: ")
    b = input("Введите точку финиша: ")

    draw_route(a, b)
    flag = stop_prog()
