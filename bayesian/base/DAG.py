import numpy as np
from typing import Tuple, Dict, List

import networkx as nx


class DAG(nx.DiGraph):

    def __init__(self, edges_bunch):
        super().__init__(edges_bunch)
        cycles = []
        try:
            cycles = nx.find_cycle(self)
        except nx.NetworkXNoCycle:
            pass
        else:
            error_message = 'Cycles are not allowed in Directed Grafical Models.\n'
            error_message += 'Cycle find in path trought edges:'
            error_message += ''.join([f'({u},{v}) ' for u, v in cycles])

    def add_node(self, node: Tuple, weigth=None):
        if isinstance(node, tuple) and len(node) == 2 and isinstance(node[1], Dict):
            node, attr = node
            if attr.get('weigth', None) is None:
                attr['weigth'] = weigth
        super().add_node(node, weigth=weigth)

    def add_nodes_from(self, nodes: List, weigths: List = None):
        if weigths:
            if len(nodes) != len(weigths):
                raise ValueError(
                    'The number of "nodes" and "weigths" should be equal')
            for node, weigth in zip(nodes, weigths):
                self.add_node(node, weigth)
        else:
            for node in nodes:
                self.add_node(nodes)

    def add_edge(self, u_of_edge, v_of_edge, weigth=None):
        super().add_edge(u_of_edge, v_of_edge, weigth=weigth)

    def add_edges_from(self, edges_bunch: List[Tuple], weigths: List = None):
        if weigths:
            if len(edges_bunch) != len(weigths):
                raise ValueError(
                    'The number of "weigths" for the amount of edges should be equal')
            for edge, weigth in zip(edges_bunch, weigths):
                self.add_edge(edge, weigth)
        else:
            for edge in edges_bunch:
                self.add_edge(edge)

    def get_parents(self, node):
        return list(self.predecessors(node))

    def get_children(self, node):
        return list(self.successors(node))

    def markov_blanket(self, node):
        childres = self.get_children(node)
        parents = self.get_parents(node)
        blanket = childres + parents
        for children in childres:
            blanket.extend(self.get_parents(children))
        blanket = set(blanket)
        blanket.discard(node)
        return list(blanket)
