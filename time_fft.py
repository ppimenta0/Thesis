import vtk
from vtk.util.numpy_support import vtk_to_numpy

# Path to your VTK file
file_path = 'your_file.vtk'

# Create a reader for the VTK file
reader = vtk.vtkStructuredPointsReader()
reader.SetFileName(r"C:\Users\pneve\Desktop\Thesis\DataAnalysis\volume_structured_115.vtk")
reader.Update()  # Necessary to read the file data

# Get the structured grid from the reader
structured_grid = reader.GetOutput()

# Extract point coordinates (spatial data)
points = structured_grid.GetPoint()
point_coordinates = vtk_to_numpy(points.GetData())
print(points)
# Extract velocity components
# Note: Adjust 'u.x', 'u.y', 'u.z' to the actual names in your VTK file
velocity_x = vtk_to_numpy(points.GetArray('u.x'))
velocity_y = vtk_to_numpy(points.GetCellData().GetArray('u.y'))
velocity_z = vtk_to_numpy(points.GetCellData().GetArray('u.z'))

print(velocity_x, velocity_y, velocity_z)

# Now you have the spatial coordinates in `point_coordinates`
# and the velocity components in `velocity_x`, `velocity_y`, `velocity_z`
