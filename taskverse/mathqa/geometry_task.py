from typing import Dict, List, Tuple

import numpy as np
from tqdm import tqdm

from ..base import TaskGenerator
from ..task_store import TaskStore

class GeoPlanGenerator(TaskGenerator):
    def __init__(self, metadata={}, seed=42):
        super().__init__(seed=seed)


    def generate(self, task_plan, seed=None):
        if seed == None:
            self.rng = np.random.default_rng(seed=seed)

    
        
