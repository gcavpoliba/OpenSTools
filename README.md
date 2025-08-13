

![logo](logo.png)\




___![OpenSTools](InitialStaticAnalysis.png)\
__![OpenSTools](animation.gif)\
__![OpenSTools](animation%20(2).gif)
==========
08/08/2025 - OPSTVIS Parallel Version - The python code for OPSTVIS able to plot the OpenSees parallel code with pyVista/paraView, Enjoy \
__![OpenSTools](PARAVIEW.png) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16835626.svg)](https://doi.org/10.5281/zenodo.16835626) PARALLEL \
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15025232.svg)](https://doi.org/10.5281/zenodo.15025232) SINGLE ELEMENT
==========
***UPDATED!!! v2 available!!!***
OPENSTOOLS (v2)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14056127.svg)](https://doi.org/10.5281/zenodo.14056127) \
[DOWNLOAD HERE](https://doi.org/10.5281/zenodo.14056127)
==========
***LAST UPDATE***:
14/03/2025 (pi greek day) - opstvis: a rough node results visualizing tool with pyvista and FeView [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15025232.svg)](https://doi.org/10.5281/zenodo.15025232)
\
[DOWNLOAD HERE](https://zenodo.org/records/15025232)
==========

**A python code to pre-process the finite element models in the OpenSees and OpenSeesSP software**

**POLITECNICO DI BARI** - **DRSATE XXXVIII PhD cycle**\
**author:** GIANLUCA CAVALLO 
[![ORCID](https://img.shields.io/badge/ORCID-ID-green?logo=orcid)](https://orcid.org/0000-0002-1825-0097)\
**year: 2023**\
**email:** gi.cav.2586@gmail.com\
**email:** g.cavallo@phd.poliba.it\
**note:** Please, cite the author if use any part of this code\
**note:** This code is part of the phd study course with the Supervisor: Prof. G Elia and Scientific Director: Prof.ssa Federica Cotecchia.\
**note:** This code will be used only for scientific purposes. no commercial objectives will be sought\
**note:** The user accept in use this code in all of its part for noncommercial purposes only\
**note:** The user has to respect every copyright request and limitation on his own responsability

All rights reserved to:
- University of California - Office of technology licensing.
- Gmsh is copyright (C) 1997-2024 by C. Geuzaine and J.-F. Remacle (see the CREDITS file for more information) and is distributed under the terms of the GNU General Public License (GPL) (version 2 
  or later, with an exception to allow for easier linking with external libraries). 
- ASDEA Software Technology: https://asdeasoft.net 
STKO (Scientific ToolKit for OpenSees): https://asdeasoft.net/stko/ 
Petracca, M., Candeloro, F., & Camata, G. (2017). "STKO user manual". ASDEA Software Technology, Pescara Italy.

CODE DEPENDENCIES
-----------------

openseespy  

opensees 

gmsh 

gmsh2opensees 

numpy 

scipy 

time 

math 

os


REMARKS AND TIPS
----------------

The milestone codes followed are those in the opensees and openseespy documentation on 2d and 3d shaked columns\
The file MASTER.py is only a rough example to test the code functionality and it will not lead to a result\
The file MASTER is connected to the tool module "openSTools.py"\
You have to execute the mfix function any times the number of the fixed surfaces, pay attention to the edges\
The same if you want remove the fixies\
Please contact me for some code bugs to correct\

Gmsh2Opensees is available from  here: https://github.com/jaabell/gmsh2opensees/archive/refs/heads/main.zip,\
follow the github.com/jaabell/gmsh2opensees instruction to install in your python interpreter.\
Before to install remember to change the g2o_elements_functions.py.\
In gmsh you HAVE TO call Solid the geo-element of dimension 3 or you will get an "invalid 'Solid'" error.\
Whit this code you could perform easily the analysis with every mesh you build with gmsh and 20-8 node up \
element you should take care in the geo_material choice\
At last, remember to add the 20 hex node element in the gmsh2opensees package before to add it in python

\***Have fun***
=============================




VIDEO RESULT EXAMPLES
---------------------
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14174620.svg)](https://doi.org/10.5281/zenodo.14174620) ***code available***


![DRM_Prototype](GIF_pendio.gif)\

___________![DRM_Prototype2](2DPrototype.gif)\

<div align="center">
<img src="output.gif" alt="Description" width="800" height="600" />
</div>


Copyright @ 1999-2020 The Regents of the University of California (The Regents). All Rights Reserved.\
\
The Regents grants permission, without fee and without a written license agreement, for (a) use, \
reproduction, modification, and distribution of this software and its documentation by educational, \
research, and non-profit entities for noncommercial purposes only; and (b) use, reproduction and \
modification of this software by other entities for internal purposes only. The above copyright \
notice, this paragraph and the following three paragraphs must appear in all copies and modifications \
of the software and/or documentation.\
\

OPSTOOLS - Anti-Plagiarism Notice
==================================
This software is licensed under the GNU Affero General Public License (AGPL). We encourage collaboration and sharing of knowledge within the open-source community. However, we strongly condemn any form of plagiarism.

Plagiarism undermines the integrity of our work and the trust within the community. If you use or modify this software, please ensure that you give appropriate credit to the original authors and respect the terms of the AGPL.

By contributing to this project, you agree to uphold these principles and promote a culture of honesty and respect in software development. Let’s work together to create a transparent and collaborative environment!


