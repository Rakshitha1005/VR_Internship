# import pymol
# from pymol import cmd

# # Start PyMOL in script mode
# pymol.finish_launching()

# # Load predicted enzyme structure and docked substrate
# cmd.load('../data/predicted_structure.pdb', 'enzyme')
# # cmd.load('../results/docking_output.pdbqt', 'substrate')
# cmd.load('../data/Conformer3D_COMPOUND_CID_13243.sdf', 'substrate')


# # Simple visualization commands
# cmd.show('cartoon', 'enzyme')
# cmd.show('sticks', 'substrate')
# cmd.color('cyan', 'enzyme')
# cmd.color('yellow', 'substrate')

# # Save a figure
# cmd.png('../results/enzyme_docking.png', width=1200, height=800)
# print("Visualization saved as enzyme_docking.png")



import pymol
from pymol import cmd

# Launch PyMOL in script mode
pymol.finish_launching()

# --- Load structures ---
# Load EstB enzyme structure (PDB format)
cmd.load('../data/predicted_structure.pdbqt', 'EstB')

# Load docked ligand from AutoDock Vina output
cmd.load('../results/docked.pdbqt', 'Ligand')

# --- Visualization setup ---
cmd.hide('everything')
cmd.show('cartoon', 'EstB')
cmd.color('cyan', 'EstB')

cmd.show('sticks', 'Ligand')
cmd.color('yellow', 'Ligand')

# --- Highlight binding pocket (within 4 Å of ligand) ---
cmd.select('Pocket', 'br. Ligand around 4.0')
cmd.show('sticks', 'Pocket')
cmd.color('salmon', 'Pocket')

# --- Optional: highlight catalytic residues (e.g., Ser105, His207, Asp236) ---
# cmd.select('Catalytic', 'resi 105+207+236')
# cmd.show('sticks', 'Catalytic')
# cmd.color('red', 'Catalytic')

# --- Zoom and render ---
cmd.zoom('Ligand')
cmd.png('../results/EstB_binding.png', width=1600, height=1200, dpi=300, ray=1)
print("✅ Render saved as ../results/EstB.png")

# --- Clean exit ---
cmd.quit()
