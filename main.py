from rdkit.Chem.rdmolfiles import MolFromPDBFile
import MDAnalysis as mda
import matplotlib.pyplot as plt
from mda2rdk import RDK2MDA

rdk_mol_pdb = MolFromPDBFile("101m.pdb", sanitize=True, removeHs=False)
print (rdk_mol_pdb)
uni = mda.Universe("101m.pdb", format="PDB")
print (uni)