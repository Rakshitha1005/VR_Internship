import os
import subprocess

# Paths to your input files
receptor_pdb = os.path.abspath("../data/predicted_structure.pdb")
ligand_pdb   = os.path.abspath("../data/Conformer3D_COMPOUND_CID_13243.sdf")  # convert SDF → PDB first if needed

# Output files
receptor_pdbqt = os.path.abspath("../data/receptor.pdbqt")
ligand_pdbqt   = os.path.abspath("../data/ligand.pdbqt")

# Path to MGLTools scripts
# Make sure prepare_receptor4.py and prepare_ligand4.py are in your PATH or specify full paths
prepare_receptor_script = "prepare_receptor4.py"
prepare_ligand_script   = "prepare_ligand4.py"

# Convert receptor
subprocess.run([
    "python", prepare_receptor_script,
    "-r", receptor_pdb,
    "-o", receptor_pdbqt,
    "-A", "hydrogens"
])

# Convert ligand
subprocess.run([
    "python", prepare_ligand_script,
    "-l", ligand_pdb,
    "-o", ligand_pdbqt,
    "-A", "hydrogens"
])

print("Conversion complete!")
print(f"Receptor PDBQT: {receptor_pdbqt}")
print(f"Ligand PDBQT: {ligand_pdbqt}")