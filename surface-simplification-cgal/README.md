if you just wanna run the algo go to build/release and run the following in the command line

~~~
./edge_collapse.exe
~~~



# How to build & run on Windows

* Install vcgpk through command line:

~~~ 
git clone https://github.com/microsoft/vcpkg
cd vcpkg
./bootstrap-vcpkg.bat 
./vcpkg.exe install yasm-tool:x86-windows
~~~

* Install CGAL and its dependencies:

~~~
./vcpkg install zlib:x64-windows boost:x64-windows eigen3:x64-windows cgal:x64-windows opencv:x64-windows glew:x64-windows glfw3:x64-windows
~~~

* Build and run the simplification algo

Clone the repo and run the following commands

~~~
mkdir build
cd build
cmake-gui ..
~~~

After gui appears press the configure button and make sure to tick "Specify toolchain file for cross-sampling"

In the toolchain file, reference the vcpkg.cmake, which is located under vcpkg/scripts/buildsystems/vcpkg.cmake

In my case 

~~~
C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake
~~~
Press finish and then press generate once the configuration is done.

Then you can open the sln file using visual studio, build and run.

**If running from visual studio doesn't work, you may need to got to Solution properties and select "edge_collapse" as a startup run project.**