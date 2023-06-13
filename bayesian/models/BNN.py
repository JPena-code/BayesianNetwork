import functools
import numpy as np
import collections
from base import DAG


class BayesianNetwork(DAG):

    def __init__(self, edges_bunch, /, seed=None, prior=None):
        super().__init__(edges_bunch)
        self.prior_count = prior
        self.random = np.random.default_rng(seed)
        self.cdps = []
        self.cardinalities = collections.defaultdict()
        self.P = collections.defaultdict()
        self._P_size = collections.defaultdict()

    def add_edge(self, u_edge, v_edge, weigth=None):
        if u_edge == v_edge:
            raise ValueError('Self loops are not allowed.')
        if u_edge in self.nodes and v_edge in self.nodes and self.has_edge(u_edge, v_edge):
            raise ValueError(
                f'Loops are not allowed. Alreaydy exist edge between nodes ({u_edge}, {v_edge}).')
        super().add_edge(u_edge, v_edge, weigth)

    def fit(self):
        pass

    def predict(self):
        pass

    @property
    def root(self):
        return [node for node in self.nodes if len(self.get_parents(node)) == 0]

    @property
    def leaves(self):
        return [node for node in self.nodes if len(self.get_children(node)) == 0]
