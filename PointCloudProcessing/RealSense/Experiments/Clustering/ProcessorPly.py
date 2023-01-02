import open3d
import numpy as np


def main():
    cloud = open3d.io.read_point_cloud("out.ply")
    newPcd= open3d.geometry.PointCloud()
    np.save("depths.txt", cloud.points)
    colors = np.asarray(cloud.colors)
    allIndexesFluff = np.where(np.asarray(cloud.points) <= -0.9)
    for i in range(len(colors)):
        print(i)
        if i in allIndexesFluff[0]:
            colors[i] = [1.,0.,0.]
        else:
            colors[i] = [0,1.,0.]

    cloud.colors = open3d.utility.Vector3dVector(colors)
    open3d.visualization.draw_geometries([cloud])






if __name__ == "__main__":
    main()
