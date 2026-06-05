import pymol2

def visualize(protein, ligand):
    with pymol2.PyMOL() as pymol:
        pymol.cmd.load(protein, "enzyme")
        pymol.cmd.load(ligand, "substrate")
        pymol.cmd.show("cartoon", "enzyme")
        pymol.cmd.show("sticks", "substrate")
        pymol.cmd.color("cyan", "enzyme")
        pymol.cmd.color("yellow", "substrate")
        pymol.cmd.png("../results/complex.png", width=800, height=600, dpi=300)

if __name__ == "__main__":
    visualize("../data/predicted_structure_receptor.pdbqt", "../results/docked.pdbqt")
