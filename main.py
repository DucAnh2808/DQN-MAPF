import os
from multiAGVscene.Layout import Layout  # layout
from multiAGVscene.Explorer_test import Explorer  # explorer
from multiAGVscene.Scene_test import Scene  # Scene
from algorithm.MADQN_structure.Controller_run import MADQNAgentController as modelController
# from task_app.task_assignment import task_assignment, get_info_values
import numpy as np

def main():
    dim = 5
    ss_x_width, ss_y_width, ss_x_num, ss_y_num, ps_num = 1, 1, 4, 4, 4
    layout_list = layout_8.MatrixLayout
    task_list = None

    layout = Layout(storage_station_x_width=ss_x_width, storage_station_y_width=ss_y_width,
                    storage_station_x_num=ss_x_num, storage_station_y_num=ss_y_num,
                    picking_station_number=ps_num, layout_list=layout_list, task_list=task_list)
    explorer_num = 20
    explorer_group = []
    for i in range(explorer_num):
        veh_name = "veh" + str(i + 1)
        explorer = Explorer(layout, veh_name=veh_name, icon_name=veh_name)
        explorer_group.append(explorer)
    """ 3. create scene """
    multi_agv_scene = Scene(layout, explorer_group)

    control_type = {0: "train_NN", 1: "use_NN", 2: "A_star", 3:"Manual"}
    control_mode = 1

    if control_mode in [2, 3]:
        multi_agv_scene.run_game(control_pattern=control_type[control_mode])
    if control_mode in [0, 1]:
        map_xdim = layout.scene_x_width
        map_ydim = layout.scene_y_width
        print(map_xdim)
        print(map_ydim)
        max_task = len(layout.storage_station_list)
        agent = modelController(multi_agv_scene, map_xdim = dim, map_ydim = dim, max_task=max_task,
                                control_mode=control_type[control_mode], state_number=3)
        agent.model_run()

dim_x3 = 31
dim_5 = 41
dim_6 = 21
# dim_5 = 51
# dim_6 = 20  

class layout_4():
    MatrixPicking = []
    for i in range(0, dim_x3):
        if i % 4 == 1 or i % 4 == 2:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_x3):
        if i % 4 == 1:
            MatrixStorage.append(1.000)
        elif i%4 == 2:
            MatrixStorage.append(1.000)
        else:
            MatrixStorage.append(0.000)

    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0, dim_x3 - 1):
        MatrixZ.append(0.000)

    MatrixStorage2 = []
    for i in range (0, 3):
        MatrixStorage2.append(MatrixStorage)

    MatrixLayout = []
    MatrixLayout.append(MatrixZ)
    
    MatrixLayout = MatrixLayout + MatrixStorage2
    # MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2
    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2

    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2

    # MatrixLayout.append(MatrixZ)
    # MatrixLayout = MatrixLayout + MatrixStorage2
    # MatrixLayout.append(MatrixZ)
    # MatrixLayout = MatrixLayout + MatrixStorage2
    # MatrixLayout.append(MatrixZ)
    # MatrixLayout = MatrixLayout + MatrixStorage2

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)    
    MatrixLayout.append(MatrixPicking)
    # MatrixLayout.append(MatrixZ)
    # MatrixLayout.append(MatrixZ)
    print("x: ",len(MatrixLayout[0]))
    print("y: ",len(MatrixLayout))

class layout_5():
    MatrixPicking = []
    for i in range(0, dim_5):
        if i % 2 == 1:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_5):
        if i % 2 == 1:
            MatrixStorage.append(1.000)
        else:
            MatrixStorage.append(0.000)
    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0,dim_5 - 1):
        MatrixZ.append(0.000)
        
    # MatrixStorage2 = []
    # for i in range (0, 5):
    #     MatrixStorage2.append(MatrixStorage)
    MatrixLayout = []
    MatrixLayout.append(MatrixZ)
    for i in range (1, dim_6):
        MatrixLayout.append(MatrixStorage)
        MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixPicking)    

class layout_6():
    MatrixPicking = []
    for i in range(0, dim_5):
        if i % 10 == 0:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_5):
        if i % 3 == 0:
            MatrixStorage.append(0.000)
        else:
            MatrixStorage.append(1.000)
    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0,dim_5 - 1):
        MatrixZ.append(0.000)
        
    # MatrixStorage2 = []
    # for i in range (0, 5):
    #     MatrixStorage2.append(MatrixStorage)
    MatrixLayout = []
    MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    for i in range (1, dim_6):
        MatrixLayout.append(MatrixStorage)
        MatrixLayout.append(MatrixStorage)
        MatrixLayout.append(MatrixStorage)
        MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixPicking)    

class layout_7():
    MatrixPicking = []
    for i in range(0, dim_5):
        if i % 3 == 1 or i % 3 == 2:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_5):
        if i % 3 == 1 or i % 3 == 2:
            MatrixStorage.append(1.000)
        else:
            MatrixStorage.append(0.000)
    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0,dim_5 - 1):
        MatrixZ.append(0.000)
        
    # MatrixStorage2 = []
    # for i in range (0, 5):
    #     MatrixStorage2.append(MatrixStorage)
    MatrixLayout = []
    MatrixLayout.append(MatrixZ)
    for i in range (1, dim_6):
        MatrixLayout.append(MatrixStorage)
        MatrixLayout.append(MatrixZ)

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixPicking)    

class layout_8():
    MatrixPicking = []
    for i in range(0, dim_x3):
        if i % 3 == 1 or i % 3 == 2:
            MatrixPicking.append(2.000)
        else:
            MatrixPicking.append(0.000)
    MatrixStorage = []
    for i in range(0, dim_x3):
        if i % 3 == 1 or i % 3 == 2:
            MatrixStorage.append(1.000)
        else:
            MatrixStorage.append(0.000)

    MatrixZ = []
    MatrixZ.append(0.000)
    for i in range(0, dim_x3 - 1):
        MatrixZ.append(0.000)

    MatrixStorage2 = []
    for i in range (0, 3):
        MatrixStorage2.append(MatrixStorage)

    MatrixLayout = []
    MatrixLayout.append(MatrixZ)
    
    MatrixLayout = MatrixLayout + MatrixStorage2
    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2
    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2

    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2

    MatrixLayout.append(MatrixZ)
    MatrixLayout = MatrixLayout + MatrixStorage2
    # MatrixLayout.append(MatrixZ)
    # MatrixLayout = MatrixLayout + MatrixStorage2
    # MatrixLayout.append(MatrixZ)
    # MatrixLayout = MatrixLayout + MatrixStorage2

    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)
    MatrixLayout.append(MatrixZ)    
    MatrixLayout.append(MatrixPicking)
    print("x: ",len(MatrixLayout[0]))
    print("y: ",len(MatrixLayout))


def task():
    task_list = [(9, 2, 4, 13), (4, 3, 10, 13), (11, 8, 4, 13), (12, 2, 4, 13), (2, 2, 10, 13), (8, 6, 10, 13), (
    11, 11, 10, 13), (12, 9, 4, 13), (3, 8, 4, 13), (3, 11, 4, 13), (9, 10, 4, 13), (10, 3, 4, 13), (6, 11, 10, 13), (
                    3, 9, 10, 13), (12, 6, 10, 13), (9, 8, 4, 13), (2, 3, 10, 13), (12, 5, 4, 13), (9, 11, 4, 13), (
                    8, 11, 4, 13), (5, 2, 10, 13), (2, 6, 10, 13), (11, 5, 10, 13), (2, 5, 4, 13), (5, 10, 4, 13), (
                    11, 9, 4, 13), (5, 8, 4, 13), (10, 2, 4, 13), (4, 2, 4, 13), (5, 3, 4, 13), (2, 9, 10, 13), (
                    11, 3, 10, 13), (11, 2, 4, 13), (3, 5, 4, 13), (6, 2, 4, 13), (3, 2, 4, 13), (8, 8, 10, 13), (
                    2, 8, 4, 13), (6, 8, 4, 13), (5, 7, 4, 13), (8, 7, 4, 13), (6, 6, 10, 13), (8, 2, 4, 13), (
                    6, 9, 4, 13), (5, 11, 10, 13), (12, 3, 4, 13), (6, 10, 4, 13), (12, 8, 10, 13), (8, 10, 10, 13), (
                    9, 9, 4, 13), (4, 5, 10, 13), (11, 6, 4, 13), (3, 6, 4, 13), (10, 5, 10, 13), (8, 9, 10, 13), (
                    5, 9, 4, 13), (3, 3, 10, 13), (9, 7, 4, 13), (2, 11, 10, 13), (6, 7, 4, 13), (9, 3, 4, 13), (
                    12, 11, 4, 13)]
    return task_list
if __name__ == '__main__':
    main()
