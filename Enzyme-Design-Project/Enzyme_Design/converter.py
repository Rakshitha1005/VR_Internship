import os
import subprocess
from pathlib import Path

# -----------------------------
# 1. Set folders
# -----------------------------
BASE = Path.cwd()
enzyme_dir = BASE / "enzyme"
substrate_dir = BASE / "substrate"
output_dir = BASE / "output"
output_dir.mkdir(exist_ok=True)

# -----------------------------
# 2. Input enzyme PDB file
# -----------------------------
enzyme_pdb = enzyme_dir / "9J0V.pdb"     # MUST be downloaded from RCSB
receptor_pdbqt = output_dir / "receptor.pdbqt"

# -----------------------------
# 3. MGLTools scripts
# -----------------------------
prepare_receptor = "prepare_receptor4.py"
prepare_ligand = "prepare_ligand4.py"

# -----------------------------
# 4. Convert receptor
# -----------------------------
subprocess.run([
    "python2", prepare_receptor,
    "-r", str(enzyme_pdb),
    "-o", str(receptor_pdbqt),
    "-A", "hydrogens"
])

print("✔ Receptor PDBQT saved to:", receptor_pdbqt)

# -----------------------------
# 5. Process ligands
# -----------------------------
substrate_files = [
    "D-AlanineCID_71080.sdf",
    "R-1-Phenylethylamine_CID_643189.sdf"
]

for sdf_name in substrate_files:
    sdf_path = substrate_dir / sdf_name
    pdb_path = output_dir / (sdf_name.replace(".sdf", ".pdb"))
    pdbqt_path = output_dir / (sdf_name.replace(".sdf", ".pdbqt"))

    # Convert SDF → PDB using OpenBabel
    subprocess.run(["obabel", str(sdf_path), "-O", str(pdb_path), "--gen3d"])

    # Convert PDB → PDBQT
    subprocess.run([
        "python2", prepare_ligand,
        "-l", str(pdb_path),
        "-o", str(pdbqt_path),
        "-A", "hydrogens"
    ])

    print("✔ Ligand prepared:", pdbqt_path)

print("\n🎉 All receptor + ligands prepared successfully!")
