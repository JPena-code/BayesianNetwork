import itertools
import numpy as np
import pandas as pd
from typing import Set, Any

import networkx as nx

class DAG(nx.DiGraph):
    
	def __init__(self, *args, **kargs, names=Set{Any}):
		super(DAG, self).__init__(args)
		cycles = []
		try:
			cycles = nx.
		except np.NetworkXNoCycle:
			pass
		else:
			error_message = 'Cycles are not allowed in Directed Grafical Models.\n'
			error_message += 'Cycle find in path trought edges:'
			error_message += ''.join([f'({u},{v}) ' for u, v in nx.find_cycle(self)])


	def __contains__(self, n):
		return super().__contains__(n)
