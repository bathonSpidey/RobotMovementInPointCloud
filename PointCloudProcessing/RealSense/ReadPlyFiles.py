import numpy as np
import open3d

def main():
    cloud = open3d.io.read_point_cloud("out.ply")
    open3d.visualization.draw_geometries([cloud])

if __name__ == "__main__":
    main()