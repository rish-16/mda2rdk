# mda2rdk
Python library for molecule interchangeability between RDKit Mol and MDAnalysis Universe

## Why?
RDKit and MDAnalysis are two popular libraries to manipulate molecular objects. However, there is no support for interoperability between the two libraries and their data representations, `Mol` and `Universe` respectively. `mda2rdk` is a library to convert molecules between these representations easily.

## Installation

You can install `mda2rdk` via `pip`:

```bash
pip install mda2rdk
```

Or, you can install it from source:

```bash
git clone https://github.com/rish-16/mda2rdk.git
cd mda2rdk

```

## Usage

```python
from mda2rdk import MDA2RDK, RDK2MDA
import MDAnalysis as mda
from rdkit.Chem.rdmolfiles import MolFromPDBFile

rdk2mad_converter = RDK2MDA() # initialise converter

rdk_mol_pdb = MolFromPDBFile("101m.pdb", sanitize=True, removeHs=False)
print (rdk_mol_pdb)

'''
<rdkit.Chem.rdchem.Mol object at 0x7fc79015c0f0>
'''

mda_pdb_uni = rdk2mad_converter.convert(rdk_mol_pdb)
print (mda_pdb_uni)

'''
<Universe with 1413 atoms>
'''
```