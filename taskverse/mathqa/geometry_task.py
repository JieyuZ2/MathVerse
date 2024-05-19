from typing import Dict, List, Tuple

import numpy as np 
from tqdm import tqdm

from ..base import TaskGenerator
from ..task_store import TaskStore
from utils import *
# PERI_SIDE_ONE_RANGE, PERI_SIDE_TWO_RANGE, PERI_SIDE_THREE_RANGE, 
#     make_single_prod, make_pair_prod, make_triplet_prod

class Template(Enum):
    PERIMETER_TEMPLATES = 'MathVerse/math_anotations/perimeter_templates.json'

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
            'question'  : question.replace('_', ' '),
            'answer'    : answer.replace('_', ' '),
            'task_plan' : self._task_plan_to_str(task_plan)
            
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
        'side_three'        : 'float'
        # 'solution'          : 'float',
    }

    def __init__(self, seed=42):
        super.__init__(seed=seed)
        self.side_one_range = PERI_SIDE_ONE_RANGE
        self.side_two_range = PERI_SIDE_TWO_RANGE
        self.side_three_range = PERI_SIDE_THREE_RANGE
        self.int_to_peri_list = int_to_peri_list
        
    def handle_templates(template_path):
        # iterate through json file and seperate into different number of params
        templates_by_num_params = {}

        with open(file_path, 'r') as file:
            templates_data = json.load(file)

        # Iterate over each template
        for template_name, template_info in templates_data.items():
            num_params = template_info["num_params"]
            template_text = template_info["text"]

            # Add the template text to the corresponding list based on the number of parameters
            if num_params not in templates_by_num_params:
                templates_by_num_params[num_params] = []
            templates_by_num_params[num_params].append(template_text)

        return templates_by_num_params

    def enumerate_task_plans(self, task_store: TaskStore):
        single = make_single_prod(self.side_one_range)
        pairs = make_pair_prod(self.side_one_range, self.side_three_range)
        triplets = make_triplet_prod(self.side_one_range, self.side_two_range, self.side_three_range)
        
        template_path = Template.PERIMETER_TEMPLATES
        template_breakdown = handle_templates(template_path)
        
        for param_count, templates in template_breakdown.items():
            peri_list = locals()[self.int_to_peri_list[param_count]]
            
            for template in tqdm(templates, desc=f"Enumerating templates with {param_count} params"):
                for group in peri_list:
                    params = [param if param is not None else None for param in group]
                    while len(params) < 3:
                        params.append(None)

                    task_plan = {
                        'question_template': template,
                        'side_one': params[0],
                        'side_two': params[1],
                        'side_three': params[2]
                    }
                    
                    task_store.add(task_plan)
                
            
    def _generate_task(self, task_plan) -> Tuple[str | List[str] | Dict]:
        
        pass
    
# class AreaGenerator(GeoPlanGenerator):
#     schema = {

#     }

#     def __init__(self, seed=42):
#         super.__init__(seed=seed)
    
#     def enumerate_task_plans(self, task_store: TaskStore):
#         return super().enumerate_task_plans(task_store)
    
#     def _generate_task(self, task_plan) -> Tuple[str | List[str] | Dict]:
#         return super()._generate_task(task_plan)


