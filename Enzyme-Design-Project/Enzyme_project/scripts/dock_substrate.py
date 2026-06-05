#from vina import Vina

# # Initialize Vina
#v = Vina(sf_name='vina')

# # Load enzyme and substrate
#v.set_receptor('../data/predicted_structure.pdb')
#v.set_ligand_from_file('../data/Conformer3D_COMPOUND_CID_13243.sdf')

# # Define docking box (center + size)
#v.compute_vina_maps(center=[10, 10, 10], box_size=[20, 20, 20])
#v.dock(exhaustiveness=8, n_poses=5)

# # Save results
#v.write_poses('../results/docking_output.pdbqt', n_poses=5)
#print("Docking completed. Results saved in ../results/docking_output.pdbqt")


import subprocess
import os

# Paths to receptor and ligand
receptor = os.path.abspath("../data/predicted_structure_receptor.pdbqt")
ligand = os.path.abspath("../data/ligand.pdbqt")
output = os.path.abspath("../results/docked.pdbqt")

# Docking box parameters (replace with your pocket coordinates)
center_x, center_y, center_z = 12.3, 25.7, 8.5
size_x, size_y, size_z = 20, 20, 20

# Run AutoDock Vina via subprocess
subprocess.run([
    "vina",
    "--receptor", receptor,
    "--ligand", ligand,
    "--center_x", str(center_x),
    "--center_y", str(center_y),
    "--center_z", str(center_z),
    "--size_x", str(size_x),
    "--size_y", str(size_y),
 "--size_z", str(size_z),
    "--out", output,
    "--exhaustiveness", "8",  # optional, default 8
    "--num_modes", "9"         # optional, default 9
])

print(f"Docking complete! Results saved at {output}")
