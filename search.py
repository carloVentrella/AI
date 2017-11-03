class search:
    def __init__(self, G):
        self.G = G;
        self.root = None;
        self.goal = None;
        self.cmap = {'neutral':'#f2fcfc', 'root':'#FFED79', 'goal':'#FF0099'}
        self.color_map = []

        def setRoot(self, label):
            self.color_map[list(self.G).index(label)] = self.cmap['root']
            return self.G.node[label]

        def setGoal(self, label):
            self.G.node[label]['isGoal'] = True;
            self.color_map[list(self.G).index(label)]= self.cmap['goal']
            return self.G.node[label]

        def draw_network(self, _node_size, _with_labels=True):
            nx.draw_networkx(self.G, node_size=_node_size, node_color=color_map, with_labels=_with_labels)

