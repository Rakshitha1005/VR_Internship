import pymol2

with pymol2.PyMOL() as pymol:
    cmd = pymol.cmd
    # Load a PDB file (use your predicted_structure.pdb)
    cmd.load('../data/predicted_structure_receptor.pdbqt', 'enzyme')
    cmd.show('cartoon', 'enzyme')
    cmd.color('cyan', 'enzyme')
    # Save an image to check output
    cmd.png('../results/EstB_binding.png', width=800, height=600)

print("PyMOL test complete! Check results/test_output.png")
