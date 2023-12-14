"""
This is the entry of the project.
This project amis at testing rl algorithm on pathfinding for multi AGVs
You can run this project by following steps:
1.create multi_scene
2.choose running mode
3.run model

We provide DQN, DDQN, PG, AC, etc. algorithms
We also provide AG-DQN algorithms, behavioral cloning trick.
"""
import os
from multiAGVscene.Layout import Layout  # layout
from multiAGVscene.Explorer import Explorer  # explorer
from multiAGVscene.Scene import Scene  # Scene
from algorithm.Manager.ExpertManager import Expert as Expert
from algorithm.DQN_structure.Controller import DQNAgentController as modelController1
# from algorithm.AC_structure.Controller import ACAgentController as modelController
# from algorithm.PG_structure.Controller import PGAgentController as modelController
from algorithm.MADQN_structure.Controller import MADQNAgentController as modelController
# sys.path.append('/DOAN2/code/Reinforcement-learning-for-multi-AGV-pathfinding/src')

def main():

    """--------------create multiAGV object--------------"""
    """ 1.create layout """
    ss_x_width, ss_y_width, ss_x_num, ss_y_num, ps_num = 1, 1, 4, 4, 4
    layout_list = None
    task_list = None
    layout = Layout(storage_station_x_width=ss_x_width, storage_station_y_width=ss_y_width,
                    storage_station_x_num=ss_x_num, storage_station_y_num=ss_y_num,
                    picking_station_number=ps_num, layout_list=layout_list, task_list=task_list)

    explorer_num = 3
    explorer_group = []
    for i in range(explorer_num):
        veh_name = "veh" + str(i + 1)
        explorer = Explorer(layout, veh_name=veh_name, icon_name=veh_name)
        explorer_group.append(explorer)
    """ 3. create scene """
    multi_agv_scene = Scene(layout, explorer_group)

    control_type = {0: "train_NN", 1: "use_NN", 2: "A_star", 3: "manual", 4: "Expert"}
    control_mode = 1

    if control_mode in [2, 3]:
        multi_agv_scene.run_game(control_pattern=control_type[control_mode])
    if control_mode in [4]:
        expert = Expert(multi_agv_scene, ss_x_width, ss_y_width, ss_x_num, ss_y_num, ps_num, explorer_num)
        expert.create_data_by_self(times=750)
    if control_mode in [0, 1]:
        map_xdim = layout.scene_x_width
        map_ydim = layout.scene_y_width
        print(map_xdim)
        print(map_ydim)
        max_task = len(layout.storage_station_list)
        agent = modelController(multi_agv_scene, map_xdim = 7, map_ydim = 7, max_task=max_task,
                                control_mode=control_type[control_mode], state_number=3)
        agent.model_run()

if __name__ == '__main__':
    main()
