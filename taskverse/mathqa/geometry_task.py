from typing import Dict, List, Tuple

import numpy as np
from tqdm import tqdm

from ..base import TaskGenerator
from ..task_store import TaskStore

class GeoPlanGenerator(TaskGenerator):
    def __init__(self, metadata={}, seed=42):
        super().__init__(metadata, seed=seed)
    
    def _task_plan_to_str(self, task_plan) -> str:
        "(Abstract method) task plan to string"

    def _generate_task(self, task_plan) -> Tuple[str, str, List[str], Dict]:
        "(Abstract method) generate task"
        # TODO: COME BACK IN FILL THIS IN AS NOT A ABSTRACT METHOD
    
    def generate(self, task_plan, return_data=True, seed=None):
        if seed is not None:
            self.rng = np.random.default_rng(seed=seed)

        question, answer, options, image_metadata = self._generate_task(task_plan)

        task = {
            'question' : question.replace('_', ' '),
            'answer'   : answer.replace('_', ' '),
            
        }

        # task = {
        #     'question'      : question.replace('_', ' '),
        #     'answer'        : answer.replace('_', ' '),
        #     'options'       : [o.replace('_', ' ') for o in options],
        #     'task_plan'     : self._task_plan_to_str(task_plan),
        #     'image_metadata': image_metadata,
        #     'image'         : self.make_image(image_metadata) if return_data else None
        # }

        return task
    
    # def generate(self, task_plan, seed=None):
    #     if seed == None:
    #         self.rng = np.random.default_rng(seed=seed)

    
class PerimeterGenerator(GeoPlanGenerator):
    schema = {
        'question_template' : 'str',
        'side_one'          : 'float',
        'side_two'          : 'float',
        'side_three'        : 'float',
        'solution'          : 'float',
    }

    def __init__(self, seed=42):
        super.__init__(seed=seed)

    def enumerate_task_plans(self, task_store: TaskStore):
        return super().enumerate_task_plans(task_store)
    
    def _generate_task(self, task_plan) -> Tuple[str | List[str] | Dict]:
        return super()._generate_task(task_plan)
    
# class AreaGenerator(GeoPlanGenerator):
#     schema = {

#     }

#     def __init__(self, seed=42):
#         super.__init__(seed=seed)
    
#     def enumerate_task_plans(self, task_store: TaskStore):
#         return super().enumerate_task_plans(task_store)
    
#     def _generate_task(self, task_plan) -> Tuple[str | List[str] | Dict]:
#         return super()._generate_task(task_plan)


