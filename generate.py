import os.path as osp

from tqdm import trange

from taskverse.base import JointTaskGenerator
from taskverse.imageqa.sticker_2d import *
from taskverse.imageqa.tabletop_3d import *
from taskverse.task_store import TaskStore
from taskverse.videoqa.metadata import *

path = '/mnt/sdb1/dynabench-source/'
save_dir = '/mnt/sdb1/benchverse-test'

# metadata = VideoSceneGraphMetaData('./annotations', osp.join(path, 'agqa_video'))
#
# generator = WhatObjectVideoSceneGraphTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df.sample(10000, ignore_index=True)
# df.to_pickle(osp.join(save_dir, 'sg-whatobjectvideo.pkl'))
# print(len(df))
#
# generator = WhatRelationVideoSceneGraphTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df.sample(10000, ignore_index=True)
# df.to_pickle(osp.join(save_dir, 'sg-whatrelationvideo.pkl'))
# print(len(df))
#
#
# generator = WhatActionVideoSceneGraphTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df.sample(10000, ignore_index=True)
# df.to_pickle(osp.join(save_dir, 'sg-whatactionvideo.pkl'))
# print(len(df))
#
# generators = {
# 			'what object'               : WhatObjectVideoSceneGraphTaskGenerator,
# 			'what relation'              : WhatRelationVideoSceneGraphTaskGenerator,
# 			'what action'           : WhatActionVideoSceneGraphTaskGenerator,
# }
# generator = JointTaskGenerator(metadata, generators)
# save_path = osp.join(save_dir, 'scene_graph_video.parquet')  # save_dir to save task plans to a parquet
# task_store = TaskStore(output_file=save_path, schema=generator.schema, buffer_size=1e6)
# generator.enumerate_task_plans(task_store)
# task_store.close()
# print(generator.stats)


# ======================================

# metadata = ObjaverseVideoMetaData('./annotations', blender_path='/mnt/sdc1/dynabench/blender-4.0.1-linux-x64/blender', assets_path=osp.join(path, '3d_assets'))
# nodes = [n for n, d in metadata.taxonomy.out_degree() if d == 0]
#
# generator = WhatMovementVideoGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['are other objects moving'] == 'No']
# df = df[df['attribute type'].isna()]
# df.to_csv(osp.join(save_dir, '3d-whatmovevideo.csv'), index=False)
# print(len(df))
#
# generator = WhatAttributeMovementVideoGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['are other objects moving'] == 'No']
# df.to_csv(osp.join(save_dir, '3d-whatattributemovevideo.csv'), index=False)
# print(len(df))
#
#
# generator = WhereMovementVideoGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['are other objects moving'] == 'No']
# df = df[df['attribute type'].isna()]
# df.to_csv(osp.join(save_dir, '3d-wheremovevideo.csv'), index=False)
# print(len(df))
#
# generator = WhatRotationVideoGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['are other objects rotating'] == 'No']
# df = df[df['attribute type'].isna()]
# df.to_csv(osp.join(save_dir, '3d-whatrotatevideo.csv'), index=False)
# print(len(df))
#
#
#
# generator = WhatAttributeRotationVideoGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['are other objects rotating'] == 'No']
# df.to_csv(osp.join(save_dir, '3d-whatattributerotatevideo.csv'), index=False)
# print(len(df))
#
#
# generator = WhereRotationVideoGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['reference category'].isnull()]
# df = df[df['are other objects rotating'] == 'No']
# df = df[df['attribute type'].isna()]
# df.to_csv(osp.join(save_dir, '3d-whererotatevideo.csv'), index=False)
# print(len(df))
#
# generators = {
# 			'what move'          : WhatMovementVideoGridTaskGenerator,
# 			'where move'         : WhereMovementVideoGridTaskGenerator,
# 			'what attribute move': WhatAttributeMovementVideoGridTaskGenerator,
# 			'what rotate'          : WhatRotationVideoGridTaskGenerator,
# 			'where rotate'         : WhereRotationVideoGridTaskGenerator,
# 			'what attribute rotate': WhatAttributeRotationVideoGridTaskGenerator,
# }
# generator = JointTaskGenerator(metadata, generators)
# save_path = osp.join(save_dir, '3d_grid_video.parquet')  # save_dir to save task plans to a parquet
# task_store = TaskStore(output_file=save_path, schema=generator.schema, buffer_size=1e6)
# generator.enumerate_task_plans(task_store)
# task_store.close()
# print(generator.stats)


# ======================================

metadata = Objaverse3DMetaData('annotations', blender_path='/mnt/sdc1/dynabench/blender-4.0.1-linux-x64/blender', assets_path=osp.join(path, '3d_assets'))
nodes = [n for n, d in metadata.taxonomy.out_degree() if d == 0]

# generator = WhatDistance3DGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['reference category'].isin(nodes)]
# df = df.groupby(['target category', 'distance type']).sample(10, random_state=42)
# df.to_csv(osp.join(save_dir, '3d-whatdistance.csv'), index=False)
# print(len(df))
#
# generator = WhereDistance3DGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['reference category'].isin(nodes)]
# df = df.groupby(['target category', 'distance type']).sample(10, random_state=42)
# df.to_csv(osp.join(save_dir, '3d-wheredistance.csv'), index=False)
# print(len(df))
#
# generator = WhatAttributeDistance3DGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['reference category'].isin(nodes)]
# df = df.groupby(['target category', 'distance type']).sample(10, random_state=42)
# df.to_csv(osp.join(save_dir, '3d-whatattributedistance.csv'), index=False)
# print(len(df))
#
#
#
# generator = WhatSize3DGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df.to_csv(osp.join(save_dir, '3d-whatsize.csv'), index=False)
# print(len(df))
#
# generator = WhatAttributeSize3DGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df.to_csv(osp.join(save_dir, '3d-whatattributesize.csv'), index=False)
# print(len(df))
#
# generator = WhereSize3DGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['reference category'].isnull()]
# df.to_csv(osp.join(save_dir, '3d-wheresize.csv'), index=False)
# print(len(df))


generator = What3DGridTaskGenerator(metadata)
task_store = TaskStore(generator.schema)
generator.enumerate_task_plans(task_store)
df = task_store.return_df()

from taskverse import constant

constant.IMAGE_H = 224

task1 = generator.generate(df.iloc[0].dropna().to_dict(), return_data=True, seed=0)
task2 = generator.generate(df.iloc[0].dropna().to_dict(), return_data=True)
task3 = generator.generate(df.iloc[0].dropna().to_dict(), return_data=True, seed=0)

df = df[df['target category'].isin(nodes)]
df = df[df['reference category'].isnull()]
df = df[~df['attribute type'].isna()]
df.to_csv(osp.join(save_dir, '3d-what.csv'), index=False)
print(len(df))

generator = Where3DGridTaskGenerator(metadata)
task_store = TaskStore(generator.schema)
generator.enumerate_task_plans(task_store)
df = task_store.return_df()
df = df[df['target category'].isin(nodes)]
df = df[df['reference category'].isnull()]
df = df[~df['attribute type'].isna()]
df.to_csv(osp.join(save_dir, '3d-where.csv'), index=False)
print(len(df))

generator = WhatAttribute3DGridTaskGenerator(metadata)
task_store = TaskStore(generator.schema)
generator.enumerate_task_plans(task_store)
df = task_store.return_df()
df = df[df['target category'].isin(nodes)]
df = df[df['reference category'].isnull()]
df.to_csv(osp.join(save_dir, '3d-whatattribute.csv'), index=False)
print(len(df))

generator = WhereAttribute3DGridTaskGenerator(metadata)
task_store = TaskStore(generator.schema)
generator.enumerate_task_plans(task_store)
df = task_store.return_df()
df = df[df['target category'].isin(nodes)]
df = df[df['reference category'].isnull()]
df.to_csv(osp.join(save_dir, '3d-whereattribute.csv'), index=False)
print(len(df))

generator = HowMany3DGridTaskGenerator(metadata)
task_store = TaskStore(generator.schema)
generator.enumerate_task_plans(task_store)
df = task_store.return_df()
df = df[df['target category'].isin(nodes) | df['target category'].isna()]
df.to_csv(osp.join(save_dir, '3d-howmany.csv'), index=False)
print(len(df))
#
# generators = {
# 			'what'               : What3DGridTaskGenerator,
# 			'where'              : Where3DGridTaskGenerator,
# 			'how many'           : HowMany3DGridTaskGenerator,
# 			'what attribute'     : WhatAttribute3DGridTaskGenerator,
# 			'where attribute'    : WhereAttribute3DGridTaskGenerator,
# 			'what size'          : WhatSize3DGridTaskGenerator,
# 			'where size'         : WhereSize3DGridTaskGenerator,
# 			'what attribute size': WhatAttributeSize3DGridTaskGenerator,
# 			'what distance'          : WhatDistance3DGridTaskGenerator,
# 			'where distance'         : WhereDistance3DGridTaskGenerator,
# 			'what attribute distance': WhatAttributeDistance3DGridTaskGenerator,
# }
# generator = JointTaskGenerator(metadata, generators)
# save_path = osp.join(save_dir, '3d_grid.parquet')  # save_dir to save task plans to a parquet
# task_store = TaskStore(output_file=save_path, schema=generator.schema, buffer_size=1e6)
# generator.enumerate_task_plans(task_store)
# task_store.close()
# print(generator.stats)


# ======================================

# metadata = SceneGraphMetaData('./annotations', scene_graph_folder=osp.join(path, 'vg'))
#
# # generator = WhatObjectSceneGraphTaskGenerator(metadata)
# # task_store = TaskStore(generator.schema)
# # generator.enumerate_task_plans(task_store)
# # df = task_store.return_df()
# # df = df.sample(10000, ignore_index=True)
# # df.to_pickle(osp.join(save_dir, 'sg-whatobject.pkl'))
# # print(len(df.groupby('object')))
# #
# # generator = WhatAttributeSceneGraphTaskGenerator(metadata)
# # task_store = TaskStore(generator.schema)
# # generator.enumerate_task_plans(task_store)
# # df = task_store.return_df()
# # df = df.sample(10000, ignore_index=True)
# # df.to_pickle(osp.join(save_dir, 'sg-whatattribute.pkl'))
# # print(len(df.groupby('attribute')))
#
# generator = WhatRelationSceneGraphTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df.sample(10000, ignore_index=True)
# df.to_pickle(osp.join(save_dir, 'sg-whatrelation.pkl'))
# print(len(df.groupby('relation')))
#
# generators = {
# 	'what object'   : WhatObjectSceneGraphTaskGenerator,
# 	'what attribute': WhatAttributeSceneGraphTaskGenerator,
# 	'what relation' : WhatRelationSceneGraphTaskGenerator,
# }
# generator = JointTaskGenerator(metadata, generators)
#
# save_path = osp.join(save_dir, 'scene_graph.parquet')  # path to save task plans to a parquet
# task_store = TaskStore(output_file=save_path, schema=generator.schema, buffer_size=1e6)
# generator.enumerate_task_plans(task_store)
# task_store.close()
# print(generator.stats)


# ======================================

metadata = Objaverse2DMetaData('annotations', image_folder=osp.join(path, 'object_images'))
nodes = [n for n, d in metadata.taxonomy.out_degree() if d == 0]

# generator = WhatGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['reference category'].isnull()]
# df = df[~df['attribute type'].isna()]
# df.to_csv(osp.join(save_dir, 'grid-what.csv'), index=False)
# print(len(df))
#
# generator = WhereGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['reference category'].isnull()]
# df = df[~df['attribute type'].isna()]
# df.to_csv(osp.join(save_dir, 'grid-where.csv'), index=False)
# print(len(df))
#
# generator = WhatAttributeGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['reference category'].isnull()]
# df.to_csv(osp.join(save_dir, 'grid-whatattribute.csv'), index=False)
# print(len(df))
#
# generator = WhereAttributeGridTaskGenerator(metadata)
# task_store = TaskStore(generator.schema)
# generator.enumerate_task_plans(task_store)
# df = task_store.return_df()
# df = df[df['target category'].isin(nodes)]
# df = df[df['reference category'].isnull()]
# df.to_csv(osp.join(save_dir, 'grid-whereattribute.csv'), index=False)
# print(len(df))

generator = HowManyGridTaskGenerator(metadata)
task_store = TaskStore(generator.schema)
generator.enumerate_task_plans(task_store)
df = task_store.return_df()
df = df[df['target category'].isin(nodes) | df['target category'].isna()]
df.to_csv(osp.join(save_dir, 'grid-howmany.csv'), index=False)
print(len(df))

for i in trange(len(df)):
	try:
		task = generator.generate(df.iloc[i].dropna().to_dict(), return_data=False)
	except:
		a = 1
	a = 1

generators = {
	'what'           : WhatGridTaskGenerator,
	'where'          : WhereGridTaskGenerator,
	'how many'       : HowManyGridTaskGenerator,
	'what attribute' : WhatAttributeGridTaskGenerator,
	'where attribute': WhereAttributeGridTaskGenerator,
}
generator = JointTaskGenerator(metadata, generators)
save_path = osp.join(save_dir, '2d_grid.parquet')  # save_dir to save task plans to a parquet
task_store = TaskStore(output_file=save_path, schema=generator.schema, buffer_size=1e6)
generator.enumerate_task_plans(task_store)
task_store.close()
print(generator.stats)
