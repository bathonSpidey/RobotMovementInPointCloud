import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt


def main():
    pcd = o3d.io.read_point_cloud("outOutlier.ply")
    plane_model, inliers = pcd.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=1000)
    inlier_cloud = pcd.select_by_index(inliers)
    outlier_cloud = pcd.select_by_index(inliers, invert=True)
    inlier_cloud.paint_uniform_color([1, 0, 0])
    o3d.io.write_point_cloud("outInlier.ply", inlier_cloud)
    o3d.io.write_point_cloud("outOutlier.ply", outlier_cloud)
    outlier_cloud.paint_uniform_color([0.0, 0.0, 1])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
    labels = np.array(pcd.cluster_dbscan(eps=0.05, min_points=20))
    max_label = labels.max()
    colors = plt.get_cmap("tab20")(labels / (max_label
                                             if max_label > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([pcd])

if __name__ == '__main__':
    main()