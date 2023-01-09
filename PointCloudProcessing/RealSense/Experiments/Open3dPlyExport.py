import pyrealsense2 as rs
import cv2
from datetime import datetime
import open3d as o3d
import os
import numpy as np


if __name__ == '__main__':
    align = rs.align(rs.stream.color)
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
    pipeline = rs.pipeline()
    profile = pipeline.start(config)
    intr = profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()
    pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(intr.width, intr.height, intr.fx, intr.fy, intr.ppx,
                                                                 intr.ppy)
    pointcloud = o3d.geometry.PointCloud()
    vis = o3d.visualization.Visualizer()
    vis.create_window("Pointcloud")
    added = False
    while True:
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)
        color_frame = aligned_frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())
        depth_frame = aligned_frames.get_depth_frame()
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image1 = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)
        depth = o3d.geometry.Image(depth_image)
        color = o3d.geometry.Image(color_image)
        rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(color, depth, convert_rgb_to_intensity=False)
        pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, pinhole_camera_intrinsic)
        depth_color_frame = rs.colorizer().colorize(depth_frame)
        depth_color_image = np.asanyarray(depth_color_frame.get_data())
        cv2.imshow('Color Stream', color_image1)
        cv2.imshow('Depth Stream', depth_color_image)
        if not added:
            vis.add_geometry(pcd)
            added = True

        #vis.update_geometry()
        vis.poll_events()
        vis.update_renderer()
        key = cv2.waitKey(1)
        if key == ord("a"):
            print("Writing...")
            o3d.io.write_point_cloud("test.ply", pcd)
        if key in (27, ord("q")):
            vis.destroy_window()
            cv2.destroyAllWindows()
            break
    pipeline.stop()









