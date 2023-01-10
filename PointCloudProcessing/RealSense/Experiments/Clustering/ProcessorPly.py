import open3d
import numpy as np
import math


def main():
    cloud = open3d.io.read_point_cloud("out.ply")
    newPcd= open3d.geometry.PointCloud()
    np.savetxt("depths.out", cloud.points)
    colors = np.asarray(cloud.colors)
    normalized=[]
    for i in colors:
        normalized.append(math.sqrt(i[0]**2+ i[1]**2+i[2]**2))
    print(max(normalized))
    allIndexesRequired = np.where(np.asarray(normalized) > 0.5)
    onTable = np.where(np.asarray(normalized) <= 0.2)
    onTableNormalized=[]
    for i in range(len(colors)):
        if i in allIndexesRequired[0]:
            colors[i] = [0.,0.,1.]
            onTableNormalized.append(normalized[i])

        else:
            np.delete(colors, i, 0)

    print(onTableNormalized)
    allIndexesRequired = np.where(np.asarray(onTableNormalized) > 1.)
    for i in range(len(colors)):
        if i in allIndexesRequired[0]:
            colors[i] = [1., 0., 0.]
    cloud.colors = open3d.utility.Vector3dVector(colors)
    open3d.visualization.draw_geometries([cloud])

if __name__ == "__main__":
    main()
