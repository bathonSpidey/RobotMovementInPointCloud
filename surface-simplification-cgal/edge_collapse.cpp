#include <CGAL/Simple_cartesian.h>
#include <CGAL/Surface_mesh.h>
#include <CGAL/Surface_mesh_simplification/edge_collapse.h>
#include <CGAL/Surface_mesh_simplification/Policies/Edge_collapse/Count_ratio_stop_predicate.h>
#include <CGAL/Surface_mesh_simplification/Policies/Edge_collapse/Edge_length_cost.h>
#include <CGAL/Surface_mesh_simplification/Policies/Edge_collapse/Midpoint_placement.h>
#include <chrono>
#include <fstream>
#include <iostream>
#include <omp.h>

typedef CGAL::Simple_cartesian<double>               Kernel;
typedef Kernel::Point_3                              Point_3;
typedef CGAL::Surface_mesh<Point_3>                  Surface_mesh;
namespace SMS = CGAL::Surface_mesh_simplification;
int main(int argc, char** argv)
{
	Surface_mesh mesh;
  const std::string filename = CGAL::data_file_path("../meshes/floormeshHighRes.off");
  std::ifstream is(filename);
  if(!is || !(is >> mesh))
  {
    std::cerr << "Invalid mesh: " << filename << std::endl;
    return EXIT_FAILURE;
  }
  std::chrono::steady_clock::time_point start_time = std::chrono::steady_clock::now();
  double stop_ratio = 0.1;
  SMS::Count_ratio_stop_predicate<Surface_mesh> stop(stop_ratio);
  int r = SMS::edge_collapse(mesh, stop);
  std::chrono::steady_clock::time_point end_time = std::chrono::steady_clock::now();
  std::cout << "\Done!\n" << r << " edges removed.\n" << mesh.number_of_edges() << " final edges.\n";
  std::cout << "Time elapsed: " << std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count() << "ms" << std::endl;
  CGAL::IO::write_polygon_mesh("output.off", mesh, CGAL::parameters::stream_precision(17));
  return EXIT_SUCCESS;
}