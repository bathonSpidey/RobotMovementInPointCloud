import open3d
import numpy as np
import math


def main():
    cloud = open3d.io.read_point_cloud("out.ply")
    colors = np.asarray(cloud.colors)
    depths = np.asarray(cloud.points)
    print(depths[0])
    normalized = []
    for i in depths:
        normalized.append(math.sqrt(i[2]**2 + i[1]**2 + i[0]**2))

    print(max(normalized))
    print(min(normalized))
    allIndexesRequired = np.where(np.asarray(normalized) > 1.)
    table = np.where(np.asarray(normalized) <= 0.5)
    onTable = np.where(table[0] >= 0.3)
    onTableNormalized=[]
    for i in range(len(colors)):
        if i in allIndexesRequired[0]:
            colors[i] = [1.,1.,1.]
        elif i in table[0]:
            colors[i] = [1.,0,0]
        elif i in onTable[0]:
            colors[i] = [0.,1.,0.]
        else:
            colors[i] = [1.,1.,1.]

    #allIndexesRequired = np.where(np.asarray(onTableNormalized) > 1.)
    #for i in range(len(colors)):
        #if i in allIndexesRequired[0]:
            #colors[i] = [1., 0., 0.]
    cloud.colors = open3d.utility.Vector3dVector(colors)
    open3d.visualization.draw_geometries([cloud])

if __name__ == "__main__":
    main()
