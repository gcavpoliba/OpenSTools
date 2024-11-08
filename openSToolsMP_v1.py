############### PLEASE READ THE DISCLAIMER AND THE DESCRIPTION IN THE GITHUB PAGE ################################################
############### PLEASE READ THE README FILE AND ALL THE GENERAL CONDITION FOR THE USE ARE VALID IN THIS CASE ALSO ################
############### ALSO FOR THIS THE MANUAL WILL BE WRITTEN AS SOON AS POSSIBLE, THERE ARE  STILL BUGS TO RESOLVE ###################

print('SOFTWARE: OpenSTools version. 1.0\n\
RELEASE LICENCE: AGPLv3.0 - Gianluca Cavallo - March 2024\n\
DEVELOPER: Eng. MSC. Gianluca Cavallo\n\
YEAR: Since 2923\n\
EMAIL: g.cavallo@phd.poliba.it\n\
EMAIL: gi.cav.2586@gmail.com\n\
notes: This code was developed during the Phd course: "DRSATE XXXVIII Phd courses cycloe". The aim of the doctorate is the\n\
disaster prevention and protection by the use of HPC systems.\n\
\n\
This software will be used only for sceintific purposes and for noncommercial one and in a way to respect the copyright of the\n\
python application tools used to develop the OpenSTools application.\n\
\n\
The author is not responsable for the use and for the results obtained by the user.\n\
The user takes every duty and responsability derived by the use of OpenSTools on his own in front of the law.\n')

print('\n\n\n\n\n\n\n')

print('Copyright @ 1999-2020 The Regents of the University of California [The Regents]. All Rights Reserved.\n)
print('\n')
print('The Regents grants permission, without fee and without a written license agreement, for [a] use\n') 
print('reproduction, modification, and distribution of this software and its documentation by educational,\n') 
print("research, and non-profit entities for noncommercial purposes only; and [b] use, reproduction and \n")
print('modification of this software by other entities for internal purposes only. The above copyright\n\
notice, this paragraph and the following three paragraphs must appear in all copies and modifications\n\
of the software and/or documentation.\n') 
print('\n\
\n\
Permission to incorporate this software into products for commercial distribution may be obtained \n\
by contacting the University of California \n\
Office of Technology Licensing \n\
2150 Shattuck Avenue n 510, \n\
Berkeley, CA 94720-1620, \n\
[510] 643-7201.\n\
\n\
This software program and documentation are copyrighted by The Regents of the University of California. \n\
The Regents does not warrant that the operation of the program will be uninterrupted or error-free. The \n\
end-user understands that the program was developed for research purposes and is advised not to rely \n\
exclusively on the program for any reason.\n')

print('IN NO EVENT SHALL REGENTS BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL \n\
DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF REGENTS\n') 
print('HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  REGENTS GRANTS NO EXPRESS OR IMPLIED LICENSE IN ANY PATENT \n\
RIGHTS OF REGENTS BUT HAS IMPLEMENTED AN INDIVIDUAL CONTRIBUTOR LICENSE AGREEMENT FOR THE OPENSEES PROJECT AT \n\
THE UNIVERISTY OF CALIFORNIA, BERKELEY TO BENEFIT THE END USER.\n\
\n\
REGENTS SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY \n\
AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, PROVIDED HEREUNDER IS PROVIDED \n\
*AS IS*. REGENTS HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.\n')

print('MPCO post-processing tool\n\
ASDEA Software Technology: https://asdeasoft.net STKO [Scientific ToolKit for OpenSees]: \n\
https://asdeasoft.net/stko/\n\
Petracca, M., Candeloro, F., & Camata, G. [2017]. "STKO user manual". ASDEA Software Technology, Pescara Italy.\n')

print('Gmsh is copyright (C) 1997-2024 by C. Geuzaine and J.-F. Remacle')

py = open("cubotto_exe.py","w")
py.write('import os\n\
import openseespy.opensees as ops\n\
import numpy as nup\n\
ops.wipe()\n\
import math as mm\n\
import time as tt\n')
py.close()


import os
import openseespy.opensees as ops
import gmsh2opensees as g2o
import numpy as nup
import gmsh
import math as mm
import time as tt


def trova_nodo(dicto,value):
    print('loading....')
    output = []
    for nproc, subdict in dicto.items():
        if subdict == {}:
            break
        else:
            for el_num,nod_list in subdict.items():
                if value in nod_list:
                    output.append(nproc)
    output = nup.unique(nup.array(output,dtype = int))
    return output



def trova_elemento(dicto,value):
    print('loading....')
    for nproc, subdict in dicto.items():
        for el_num,nod_list in subdict.items():
            if value == el_num:
                return nproc

nop = int(input('inserire il numero dei processori; '))

class Model(object):
    global nodo_mesh
    global PhysGr
    global nop
    PhysGr = g2o.get_physical_groups_map(gmsh.model)
    print(g2o.get_physical_groups_map(gmsh.model))
    
    def __init__(self,uniqueVector = [],nomeEl=str()):
        self.uniqueVector = uniqueVector
        self.nomeEl = nomeEl
        self.PhysGr = PhysGr
        print('Model activated')

    def setGeoElement(self,nomeEl):
        self.nomeEl = nomeEl
        print('setGeoElement: geometry element inserted')

    def getElementsVectors(self):
        elementTag=[]
        nodeTag=[]
        entities=[]
        entTag = []
        elementName=[]
        elementNnode=[]
        Tags = []
        LNT = 0
        TagPh = PhysGr[self.nomeEl][1]
        DimPh = PhysGr[self.nomeEl][0]
        if DimPh ==3:
            elementTag, nodeTag, elementName, elementNnode = g2o.get_elements_and_nodes_in_physical_group(self.nomeEl,gmsh.model)
            LNT = len(nodeTag)
            return (elementTag, nodeTag, elementName, elementNnode,LNT)
        else:
            entities = gmsh.model.getEntitiesForPhysicalGroup(DimPh, TagPh)
            Tags = gmsh.model.mesh.getElements(DimPh, entities[0])
            elementTag = Tags[1][0]
            nodeTag = Tags[2][0]
            entTag, elementTag, nodeTag = gmsh.model.mesh.getElements(DimPh, entities[0])
            return (elementTag, nodeTag)
    
    def mDict(self):
        '''vale solo per volumi = 'Solids' '''
        global proc_dict
        print('funzione mDict')
        print(f'nop = {nop}')
        m = Model()
        m.setGeoElement('Solid')
        elementTag, nodeTag, elementName, elementNnode, LNT = m.getElementsVectors()
        eleNode = {}
        eleNode = dict(zip(elementTag, nodeTag))

        numero_nodi = len(nodeTag)
        print(f'numero dei nodi:  {numero_nodi}')

        numero_el = len(elementTag)
        print(f'numero di elementi: {numero_el}')
        
        
        numero_el_np = 0
        if numero_el%(nop-1)==0:
            numero_el_np = int(numero_el/(nop-1))
        else:
            numero_el_np = int(numero_el/(nop-1)) + 1
        
        print(f'il numero di el per np è: {numero_el_np}')
        
        proc_dict = {}
        for i in range(1,nop):
            proc_dict[i] = 0
        
    
        i = 1
        j = 0 
        k = 0 
        jj = 0
        proc_list = {}
        while i < nop:
            proc_dict[i] = {}
            while j < numero_el:
                jj = elementTag[j]
                if k < numero_el_np:
                    proc_dict[i][jj] = eleNode[jj]
                    k = k + 1
                    j = j + 1
                else:  
                    k = 0
                    break
            i = i + 1
        return proc_dict    
    
    def setUniqueVector(self,uniqueVector):
        self.uniqueVector = uniqueVector

    def getUniqueVector(self):
        return self.uniqueVector

    def nodeNumCoordVector(self):
        opsVector = []
        collect = []
        coord_l=[]
        num = 0
        x=0
        y=0
        z=0
        j=0
        for j in self.uniqueVector:
            x = gmsh.model.mesh.getNode(int(j))[0][0]
            y = gmsh.model.mesh.getNode(int(j))[0][1]
            z = gmsh.model.mesh.getNode(int(j))[0][2]
            coord_l=[x,y,z]
            num = int(j)
            collect = [num,coord_l]
            opsVector.append(collect)
        return opsVector

    def listOfTagsij(self,l,ll):
        nodeTot = []
        nodeTotU = []
        self.l = l 
        self.ll = ll 
        for i in range(0, l):
            for j in range(0, ll):
                nodeTot.append(self.uniqueVector[i][j])
        nodeTotU=nup.unique(nup.array(nodeTot, dtype=int).reshape(-1))
        return nodeTotU

    def makeUnique(self):
        getUnique= nup.unique(nup.array(self.uniqueVector, dtype=int).reshape(-1))
        print('make Unique ok')
        return getUnique

    def nodeCornEdge(self,type):
        print('insert type = 8-nodi o 20-nodi')
        self.type = type
        j=0
        i=0
        k=0
        n = 0
        nodeNum = []
        nodeVecCorn = []
        nodeVecEdge = []
        mem = []
        elemento = str(type) 
        if elemento == '20-nodi':
            p = 1 
            l = int(len(self.uniqueVector[p]))
            for i in range(0, l):
                for j in range(0, 20):
                    nodeNum = self.uniqueVector[p][i][j]
                    mem.append(nodeNum)
                    if j == 7:
                        nodeVecCorn.append(mem)
                        mem = []
                    elif j == 19:
                        nodeVecEdge.append(mem)
                        mem = []
        else:
            len1 = len(self.uniqueVector[1][0])
            for i in range(0, len1):
                n = self.uniqueVector[1][0][i]
                mem.append(n)
                j = j + 1
                if j == 4:
                    nodeVecCorn.append(mem)
                    mem = []
                elif j == 8:
                    nodeVecEdge.append(mem)
                    j = 0
                    mem = []
        return (nodeVecCorn,nodeVecEdge)

    def sendOpsNodes(self,dim,ndf):
        print('funzione sendOpsNodes')
        self.dim = dim 
        self.ndf = ndf 
        m = Model()
        proc_dict = m.mDict()
        ops.model("basicBuilder", "-ndm", dim, "-ndf", ndf)
        ###################################
        
        py = open("cubotto_exe.py","a")
        py.write(f'ops.model("basicBuilder","-ndm",{dim},"-ndf",{ndf})\n')
        py.close()
        ###################################
        
        tcl=open("cubotto.tcl","a")
        tcl.write(f'model BasicBuilder -ndm {dim} -ndf {ndf}\n')
        tcl.close()
        ###################################
        l = len(self.uniqueVector)
        for i in range(0,l):
            coord = [self.uniqueVector[i][1][0],self.uniqueVector[i][1][1],self.uniqueVector[i][1][2]]
            ops.node(int(self.uniqueVector[i][0]),*coord)
            ###################################
            procId = trova_nodo(proc_dict,self.uniqueVector[i][0])
            for proc in procId:
                py = open("cubotto_exe.py","a")
                py.write(f'if pid == {proc}:\n')
                py.close()
                ###################################
                tcl=open("cubotto.tcl","a")
                tcl.write("if {"+f' $pid == {proc}'+' }'+' {\n')
                tcl.close()
                ###################################
                py = open("cubotto_exe.py","a")
                py.write(f"    ops.node({int(self.uniqueVector[i][0])}, {coord[0]}, {coord[1]}, {coord[2]})\n")
                py.close()
                ###################################
                tcl=open("cubotto.tcl","a")
                tcl.write(f'    node {int(self.uniqueVector[i][0])} {coord[0]} {coord[1]} {coord[2]}\n')
                tcl.write('}\n')
                tcl.close()
                
                
            ###################################


    def sendOpsFixes(self,dim,ndf,x,y,z,p):
        print('funzione sendOpsFixes')
        self.dim = int(dim)
        self.ndf = int(ndf)
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.p = int(p)
        m = Model()
        proc_dict = m.mDict()
        if ndf == 4:
            ops.model("basicBuilder", "-ndm", dim, "-ndf", ndf)
            ################################### 
            
            py = open("cubotto_exe.py","a")
            py.write(f'ops.model("basicBuilder","-ndm",{dim},"-ndf",{ndf})\n')
            py.close()
            ###################################
            
            tcl=open("cubotto.tcl","a")
            tcl.write(f'model BasicBuilder -ndm {dim} -ndf {ndf}\n')
            tcl.close()
            
            ###################################
            l = len(self.uniqueVector)
            for i in range(0, l):
                ###################################
                ops.remove('sp', int(self.uniqueVector[i][0]),1)
                ops.remove('sp', int(self.uniqueVector[i][0]),2)
                ops.remove('sp', int(self.uniqueVector[i][0]),3)
                ops.remove('sp', int(self.uniqueVector[i][0]),4)
                ops.fix(int(self.uniqueVector[i][0]), x, y, z, p)
                print(f' ndf = 4, nodo: {int(self.uniqueVector[i][0])}, {x}, {y}, {z}, {p}')
                            
                coord = [self.uniqueVector[i][1][0],self.uniqueVector[i][1][1],self.uniqueVector[i][1][2]]
                procId = trova_nodo(proc_dict,self.uniqueVector[i][0])
                               
                j = 0
                for proc in procId:
               
                    py = open("cubotto_exe.py","a")
                    py.write(f'if pid == {proc}:\n')
                    py.write(f'    ops.remove("sp", {int(self.uniqueVector[i][0])},1)\n\
    ops.remove("sp", {int(self.uniqueVector[i][0])},2)\n\
    ops.remove("sp", {int(self.uniqueVector[i][0])},3)\n\
    ops.remove("sp", {int(self.uniqueVector[i][0])},4)\n\
    ops.fix({int(self.uniqueVector[i][0])}, {x}, {y}, {z},{p})\n')
                    py.close()
                    ###################################
                    
                    tcl=open("cubotto.tcl","a")
                    tcl.write("if {"+f' $pid == {proc}'+' }'+' {\n')
                    tcl.write(f'    remove sp {int(self.uniqueVector[i][0])} 1\n    remove sp {int(self.uniqueVector[i][0])} 2\n    remove sp {int(self.uniqueVector[i][0])} 3\n')
                    tcl.write(f'    fix {int(self.uniqueVector[i][0])} {x} {y} {z} {p}\n')
                    tcl.write('}\n')
                    tcl.close()
                    
                    ###################################
                    if j == 0:
                        py = open("cubotto_exe.py","a")
                        py.write('if pid == 0:\n')
                        py.write(f'    ops.remove("sp", {int(self.uniqueVector[i][0])},1)\n\
    ops.remove("sp", {int(self.uniqueVector[i][0])},2)\n\
    ops.remove("sp", {int(self.uniqueVector[i][0])},3)\n\
    ops.fix({int(self.uniqueVector[i][0])}, {x}, {y}, {z},{p})\n')
                        py.close()
                        
                        tcl=open("cubotto.tcl","a")
                        tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
                        tcl.write(f'    remove sp {int(self.uniqueVector[i][0])} 1\n    remove sp {int(self.uniqueVector[i][0])} 2\n    remove sp {int(self.uniqueVector[i][0])} 3\n    remove sp {int(self.uniqueVector[i][0])} 4\n')
                        tcl.write(f'    fix {int(self.uniqueVector[i][0])} {x} {y} {z} {p}\n')
                        tcl.write('}\n')
                        tcl.close()
                        
                        j = j + 1
                ###################################             
                
        else:
            ops.model("basicBuilder", "-ndm", dim, "-ndf", ndf)
            ################################### 
            
            py = open("cubotto_exe.py","a")
            py.write(f'ops.model("basicBuilder","-ndm",{dim},"-ndf",{ndf})\n')
            py.close()
            
            
            tcl=open("cubotto.tcl","a")
            tcl.write(f'model BasicBuilder -ndm {dim} -ndf {ndf}\n')
            tcl.close()
            
            
            ###################################
            l = len(self.uniqueVector)
            for i in range(0, l):
                ops.remove('sp', int(self.uniqueVector[i][0]),1)
                ops.remove('sp', int(self.uniqueVector[i][0]),2)
                ops.remove('sp', int(self.uniqueVector[i][0]),3)
                ops.fix(int(self.uniqueVector[i][0]), x, y, z, p)
                print(f' ndf = 3, nodo: {int(self.uniqueVector[i][0])}, {x}, {y}, {z}, {p}')

                ###################################
                procId = trova_nodo(proc_dict,self.uniqueVector[i][0])
                coord = [self.uniqueVector[i][1][0],self.uniqueVector[i][1][1],self.uniqueVector[i][1][2]]
                j = 0
                for proc in procId:
                    
                    py = open("cubotto_exe.py","a")
                    py.write(f'if pid == {proc}:\n')
                    py.write(f'    ops.remove("sp", {int(self.uniqueVector[i][0])},1)\n\
    ops.remove("sp", {int(self.uniqueVector[i][0])},2)\n\
    ops.remove("sp", {int(self.uniqueVector[i][0])},3)\n\
    ops.fix({int(self.uniqueVector[i][0])}, {x}, {y}, {z})\n')
                    py.close()
                    
                    tcl=open("cubotto.tcl","a")
                    tcl.write("if {"+f' $pid == {proc}'+' }'+' {\n')
                    tcl.write(f'    remove sp {int(self.uniqueVector[i][0])} 1\n    remove sp {int(self.uniqueVector[i][0])} 2\n    remove sp {int(self.uniqueVector[i][0])} 3\n')
                    tcl.write(f'    fix {int(self.uniqueVector[i][0])} {x} {y} {z}\n')
                    tcl.write('}\n')
                    tcl.close()
                    
                    if j == 0:
                        py = open("cubotto_exe.py","a")
                        py.write('if pid == 0:\n')
                        py.write(f'    ops.remove("sp", {int(self.uniqueVector[i][0])},1)\n\
    ops.remove("sp", {int(self.uniqueVector[i][0])},2)\n\
    ops.remove("sp", {int(self.uniqueVector[i][0])},3)\n\
    ops.fix({int(self.uniqueVector[i][0])}, {x}, {y}, {z})\n')
                        py.close()
                        
                        tcl=open("cubotto.tcl","a")
                        tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
                        tcl.write(f'    remove sp {int(self.uniqueVector[i][0])} 1\n    remove sp {int(self.uniqueVector[i][0])} 2\n    remove sp {int(self.uniqueVector[i][0])} 3\n')
                        tcl.write(f'    fix {int(self.uniqueVector[i][0])} {x} {y} {z}\n')
                        tcl.write('}\n')
                        tcl.close()
                        j = j+1
                    
                    
                

class App(Model):
    ops.reactions()
    def __init__(self):
        Model.__init__(self)
        

    def subReacForce(self):
        print('funzione subReacForce')
        print(g2o.get_physical_groups_map(gmsh.model))
        m = Model()
        proc_dict = m.mDict()
        type_el = str(input('what geoElement do you want to fix substituting'))
        b = m.setGeoElement(type_el)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[0])
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()
        m.setUniqueVector(f)
        dim = 3
        ndf = 4
        reacV1={}
        mem = 0
        ops.model("basicBuilder", "-ndm", 3, "-ndf", 4)


        n = 0
        while n < 2:
            for i in f:
                mem = ops.nodeReaction(int(i[0]), -1)
                reacV1[int(i[0])] = mem
                ops.load(int(i[0]), mem[0],mem[1],mem[2],0.0)

                procId = trova_nodo(proc_dict,int(i[0]))
                for proc in procId:

                    py = open("cubotto_exe.py", "a")
                    py.write(f'if pid == {proc}:\n')
                    py.write(f"    ops.load({int(i[0])}, {mem[0]},{mem[1]},{mem[2]},0.0)\n")

                    tcl=open("cubotto.tcl","a")
                    tcl.write("if {"+f' $pid == {proc}'+' }'+' {\n')
                    tcl.write(f'    load {int(i[0])} {mem[0]} {mem[1]} {mem[2]} 0.0\n')

                    tcl.write('}\n')
                    tcl.close()

                    py.write(f'if pid == 0:\n')
                    py.write(f"    ops.load({int(i[0])}, {mem[0]},{mem[1]},{mem[2]},0.0)\n")

                    py.close()

                    tcl=open("cubotto.tcl","a")
                    tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
                    tcl.write(f'    load {int(i[0])} {mem[0]} {mem[1]} {mem[2]} 0.0\n')
                    tcl.write('}\n')
                    tcl.close()

            #########################

            print('\nEdge\n')
            m.setUniqueVector(c[1])
            print(len(c[1]))
            print(len(c[1][0]))
            l=len(c[1])
            ll=len(c[1][0])
            d = m.listOfTagsij(l,ll)
            m.setUniqueVector(d)
            e = m.makeUnique()
            f = m.nodeNumCoordVector()
            m.setUniqueVector(f)
            dim = 3
            ndf = 3
            reacV2={}
            mem = 0

            

            for i in f:
                mem = ops.nodeReaction(int(i[0]), -1)

                reacV2[int(i[0])] = mem
                ops.load(int(i[0]), mem[0],mem[1],mem[2])


                procId = trova_nodo(proc_dict,int(i[0]))
                for proc in procId:

                    py = open("cubotto_exe.py", "a")
                    py.write(f'if pid == {proc}:\n')
                    py.write(f"    ops.load({int(i[0])}, {mem[0]},{mem[1]},{mem[2]})\n")

                    tcl=open("cubotto.tcl","a")
                    tcl.write("if {"+f' $pid == {proc}'+' }'+' {\n')
                    tcl.write(f'    load {int(i[0])} {mem[0]} {mem[1]} {mem[2]}\n')
                    tcl.write('}\n')
                    tcl.close()

                    py.write('if pid == 0:\n')

                    py.write(f"    ops.load({int(i[0])}, {mem[0]},{mem[1]},{mem[2]})\n")
                    py.close()

                    tcl=open("cubotto.tcl","a")
                    tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
                    tcl.write(f'    load {int(i[0])} {mem[0]} {mem[1]} {mem[2]}\n')
                    tcl.write('}\n')
                    tcl.close()
            n = n + 1

##############################################################################################################################
    def mRemove(self):

        print('funzione remove')
        print(g2o.get_physical_groups_map(gmsh.model))
        m = Model()
        ########################### ATTENZIONE ############################
        proc_dict = m.mDict()
        ###################################################################
        type_el = str(input('what geoElement do you want to remove fixes'))
        b = m.setGeoElement(type_el)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[0])
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l, ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()
        m.setUniqueVector(f)
        dim = 3
        ndf = 4
        reacV1 = {}
        mem = 0
        ops.model("basicBuilder", "-ndm", 3, "-ndf", 4)

        tcl = open("cubotto.tcl", "a")
        tcl.write("model BasicBuilder -ndm 3 -ndf 4\n")
        tcl.close()

        py = open("cubotto_exe.py", "a")
        py.write('ops.model(" basicBuilder", " - ndm", 3, " - ndf ", 4)\n')
        py.close()
        for i in f:
            mem = ops.nodeReaction(int(i[0]), -1)
            reacV1[int(i[0])] = mem

            ops.remove('sp',int(i[0]))

            procId = trova_nodo(proc_dict,int(i[0]))
            for proc in procId:

                py = open("cubotto_exe.py", "a")
                py.write(f'if pid == {proc}:\n')
                py.write(f"    ops.remove('sp',{int(i[0])},1)\n\
        ops.remove('sp',{int(i[0])},2)\n\
        ops.remove('sp',{int(i[0])},3)\n")

                tcl=open("cubotto.tcl","a")
                tcl.write("if {"+f' $pid == {proc}'+' }'+' {\n')

                tcl.write(f'    remove sp {int(i[0])} 1\n    remove sp {int(i[0])} 2\n    remove sp {int(i[0])} 3\n')
                tcl.write('}\n')
                tcl.close()

                py.write(f'if pid == 0:\n')

                py.write(f'    ops.remove("sp",{int(i[0])},1)\n\
        ops.remove("sp",{int(i[0])},2)\n\
        ops.remove("sp",{int(i[0])},3)\n')
                py.close()

                tcl=open("cubotto.tcl","a")
                tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
                tcl.write(f'    remove sp {int(i[0])} 1\n    remove sp {int(i[0])} 2\n    remove sp {int(i[0])} 3\n')
                tcl.write('}\n')
                tcl.close()

        #########################

        print('\nEdge\n')
        m.setUniqueVector(c[1])
        print(len(c[1]))
        print(len(c[1][0]))
        l=len(c[1])
        ll=len(c[1][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()
        m.setUniqueVector(f)
        dim = 3
        ndf = 3
        reacV2={}
        mem = 0

        ops.model("basicBuilder", "-ndm", 3, "-ndf", 3)
        py = open("cubotto_exe.py", "a")
        py.write('ops.model(" basicBuilder", " - ndm", 3, " - ndf ", 3)\n')
        py.close()

        tcl = open("cubotto.tcl", "a")
        tcl.write("model BasicBuilder -ndm 3 -ndf 3\n")
        tcl.close()

        for i in f:
            mem = ops.nodeReaction(int(i[0]), -1)

            reacV2[int(i[0])] = mem

            ops.remove('sp',int(i[0]))

            procId = trova_nodo(proc_dict,int(i[0]))
            for proc in procId:


                py = open("cubotto_exe.py", "a")
                py.write(f'if pid == {proc}:\n')
                py.write(f"    ops.remove('sp',{int(i[0])},1)\n\
            ops.remove('sp',{int(i[0])},2)\n\
            ops.remove('sp',{int(i[0])},3)\n")



                tcl=open("cubotto.tcl","a")
                tcl.write("if {"+f' $pid == {proc}'+' }'+' {\n')

                tcl.write(f'    remove sp {int(i[0])} 1\n    remove sp {int(i[0])} 2\n    remove sp {int(i[0])} 3\n')
                tcl.write('}\n')
                tcl.close()

                py.write('if pid == 0:\n')
                py.write(f'    ops.remove("sp",{int(i[0])},1)\n\
            ops.remove("sp",{int(i[0])},2)\n\
            ops.remove("sp",{int(i[0])},3)\n')

                py.close()

                tcl=open("cubotto.tcl","a")
                tcl.write("if {"+f' $pid == 0'+' }'+' {\n')

                tcl.write(f'    remove sp {int(i[0])} 1\n    remove sp {int(i[0])} 2\n    remove sp {int(i[0])} 3\n')
                tcl.write('}\n')
                tcl.close()
    
    
def mDefine():
        print('funzione mDefine')
        m = Model()
        proc_dict = m.mDict()
        b = m.setGeoElement('Solid')
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('20-nodi')
        m.setUniqueVector(c[0])
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()
        m.setUniqueVector(f)
        dim = 3
        ndf = 4
        m.sendOpsNodes(dim,ndf)
        ##
        m.setUniqueVector(c[1])
        print(len(c[1]))
        print(len(c[1][0]))
        l=len(c[1])
        ll=len(c[1][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()
        m.setUniqueVector(f)
        dim = 3
        ndf = 3
        m.sendOpsNodes(dim,ndf)




def boundNodesPid0():
    print('funzione boundNodesPid0')
    print('attenzione al nome dei geoGruppi, dal gruppo si sono elminati i solidi e le linee, attenzione ai nomi, rieditare boundNodesPid0')
    m = Model()
    boundNodesCornTag = []
    boundNodesEdgeTag = []

    for i in m.PhysGr:
        type_el = str(i)
        if type_el == 'Solid':
            continue
        elif type_el == 'Edges':
            continue
        elif (type_el == "SX" or type_el == "DX" or type_el == "SY" or type_el == "DY" or type_el == "DOWN" or type_el == "TOP"):
            b = m.setGeoElement(type_el)
            bb = m.getElementsVectors()
            m.setUniqueVector(bb)
            c = m.nodeCornEdge('8-nodi')
            m.setUniqueVector(c[0])
            print(len(c[0]))
            print(len(c[0][0]))
            l = len(c[0])
            ll = len(c[0][0])
            d = m.listOfTagsij(l,ll)
            m.setUniqueVector(d)
            e = m.makeUnique()
            for i in e:
                    boundNodesCornTag.append(i)
            
    for i in m.PhysGr:
        type_el = str(i)
        if type_el == 'Solid':
            continue
        elif type_el == 'Edges':
            continue
        elif (type_el == "SX" or type_el == "DX" or type_el == "SY" or type_el == "DY" or type_el == "DOWN" or type_el == "TOP"):

            b = m.setGeoElement(type_el)
            bb = m.getElementsVectors()
            m.setUniqueVector(bb)
            c = m.nodeCornEdge('8-nodi')
            
            m.setUniqueVector(c[1])
            print(len(c[1]))
            print(len(c[1][0]))
            l=len(c[1])
            ll=len(c[1][0])
            d = m.listOfTagsij(l,ll)
            m.setUniqueVector(d)
            e = m.makeUnique()
            for i in e:
                boundNodesEdgeTag.append(i)
                
    boundNodeCorner = nup.unique(nup.array(boundNodesCornTag))
    boundNodeEdge = nup.unique(nup.array(boundNodesEdgeTag))
   
    
    dim = 3
    ndf = 4
    
    py = open("cubotto_exe.py","a")
    py.write(f'ops.model("basicBuilder","-ndm",{dim},"-ndf",{ndf})\n')
    py.write('if pid == 0:\n')
    py.close()
    
    tcl=open("cubotto.tcl","a")
    tcl.write(f'model BasicBuilder -ndm {dim} -ndf {ndf}\n')
    tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
    tcl.close()
    
    for j in boundNodeCorner:
        x = gmsh.model.mesh.getNode(int(j))[0][0]
        y = gmsh.model.mesh.getNode(int(j))[0][1]
        z = gmsh.model.mesh.getNode(int(j))[0][2]
        num = int(j)
        py = open("cubotto_exe.py","a")
        py.write(f'    ops.node({num},{x},{y},{z})\n')
        py.close()
        
        tcl=open("cubotto.tcl","a")
        tcl.write(f'    node {num} {x} {y} {z}\n')
        tcl.close()
    
    tcl=open("cubotto.tcl","a")
    tcl.write('}\n')
    tcl.close()
                
        

    dim = 3
    ndf = 3
    
    py = open("cubotto_exe.py","a")
    py.write(f'ops.model("basicBuilder","-ndm",{dim},"-ndf",{ndf})\n')
    py.write('if pid == 0:\n')
    py.close()
    
    tcl=open("cubotto.tcl","a")
    tcl.write(f'model BasicBuilder -ndm {dim} -ndf {ndf}\n')
    tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
    tcl.close()
    
    for j in boundNodeEdge:
        x = gmsh.model.mesh.getNode(int(j))[0][0]
        y = gmsh.model.mesh.getNode(int(j))[0][1]
        z = gmsh.model.mesh.getNode(int(j))[0][2]
        num = int(j)
        py = open("cubotto_exe.py","a")
        py.write(f'    ops.node({num},{x},{y},{z})\n')
        py.close()
        
        tcl=open("cubotto.tcl","a")
        tcl.write(f'    node {num} {x} {y} {z}\n')
        tcl.close()
        
    tcl=open("cubotto.tcl","a")
    tcl.write('}\n')
    tcl.close()
        
        
    print(boundNodeCorner,boundNodeEdge)
    return [boundNodeCorner,boundNodeEdge]      

def mgetFixedCoord():
        f = ops.getFixedNodes()
        coordTag=[]
        fixedCoord=[]
        Dofs=[]
        for i in f:
            coordTag.append(i)
            coordFixNode = ops.nodeCoord(i)
            fixedCoord.append(coordFixNode)
            g = ops.getFixedDOFs(i)
            Dofs.append(g)
        return [coordTag,fixedCoord,Dofs]

def mFix():
    print('funzione mFix')
    print(g2o.get_physical_groups_map(gmsh.model))
    m = Model()
    fixed = mgetFixedCoord()
    type_el = str(input('inserisci l elemento geo da vincolare: '))
    print('inserire 1 per vincolo on 0 per vincolo off')

    DofL = []
    x = int(input('x: 1 0n - 0 off: '))
    f_x = 0
    if x == 1:
        f_x = 1
        DofL.append(f_x)
    else:
        f_x = 0

    y = int(input('y: 1 0n - 0 off: '))
    f_y = 0
    if y == 1:
        f_y = 2
        DofL.append(f_y)
    else:
        f_y = 0

    z = int(input('z: 1 0n - 0 off: '))
    f_z = 0
    if z == 1:
        f_z = 3
        DofL.append(f_z)
    else:
        f_z = 0

    p = int(input('p: 1 0n - 0 off: '))
    f_p = 0
    if p == 1:
        f_p = 4
        DofL.append(f_p)
    else:
        f_p = 0
    fix_mem = [x, y, z, p]
    b = m.setGeoElement(type_el)
    bb = m.getElementsVectors()
    m.setUniqueVector(bb)
    c = m.nodeCornEdge('8-nodi')
    m.setUniqueVector(c[0])
    print(len(c[0]))
    print(len(c[0][0]))
    l = len(c[0])
    ll = len(c[0][0])
    d = m.listOfTagsij(l, ll)
    m.setUniqueVector(d)
    e = m.makeUnique()
    f = m.nodeNumCoordVector()
    ff = []
    num = 0
    for i in f:
        flag = 0
        num = 0
        mem = []
        if fixed == [[], [], []]:
            ff.append(i)
            m.setUniqueVector(ff)
            dim = 3
            ndf = 4
            m.sendOpsFixes(dim, ndf, x, y, z, p)
            continue
        ff = []
        x = fix_mem[0]
        y = fix_mem[1]
        z = fix_mem[2]
        p = fix_mem[3]
        for j in fixed[1]:

            if (flag == 1 or flag == 2):
                break
            if i[1] == j:

                k = fixed[2][num]
                if (flag == 1 or flag == 2):
                    break

                for kk in k:
                    if flag == 1:
                        break
                    for l in DofL:
                        if kk == l:
                            flag = 1
                            break
                        else:
                            if kk == 1:
                                x = 1
                                flag = 2
                                break
                            elif kk == 2:
                                y = 1
                                flag = 2
                                break
                            elif kk == 3:
                                z = 1
                                flag = 2
                                break
                            elif kk == 4:
                                p = 1
                                flag = 2
                                break
            else:
                num = num + 1

        if (flag == 0 or flag == 2):
            ff.append(i)
            m.setUniqueVector(ff)
            dim = 3
            ndf = 4
            m.sendOpsFixes(dim, ndf, x, y, z, p)
            ff = []
            x = fix_mem[0]
            y = fix_mem[1]
            z = fix_mem[2]
            p = fix_mem[3]
    

    print('\nEdge\n')
    m.setUniqueVector(c[1])
    print(len(c[1]))
    print(len(c[1][0]))
    l = len(c[1])
    ll = len(c[1][0])
    d = m.listOfTagsij(l, ll)
    m.setUniqueVector(d)
    e = m.makeUnique()
    f = m.nodeNumCoordVector()
    ff = []

    for i in f:
        num = 0
        flag = 0
        mem = []
        if fixed == [[], [], []]:
            ff.append(i)
            m.setUniqueVector(ff)
            dim = 3
            ndf = 3
            m.sendOpsFixes(dim, ndf, x, y, z, p)
            continue
        ff = []
        x = fix_mem[0]
        y = fix_mem[1]
        z = fix_mem[2]
        p = fix_mem[3]
        for j in fixed[1]:
            if (flag == 1 or flag == 2):
                break
            if i[1] == j:
                k = fixed[2][num]
                if (flag == 1 or flag == 2):
                    break
                for kk in k:
                    if flag == 1:
                        break
                    for l in DofL:
                        if kk == l:
                            flag = 1
                            break
                        else:
                            if kk == 1:
                                flag = 2
                                x = 1
                                break
                            elif kk == 2:
                                flag = 2
                                y = 1
                                break
                            elif kk == 3:
                                flag = 2
                                z = 1
                                break
            else:
                num = num + 1
        if (flag == 0 or flag == 2):
            ff.append(i)
            m.setUniqueVector(ff)
            dim = 3
            ndf = 3
            m.sendOpsFixes(dim, ndf, x, y, z, p)
            ff = []
            x = fix_mem[0]
            y = fix_mem[1]
            z = fix_mem[2]
            p = fix_mem[3]


def mRec():
    print('funzione mRec')
    print('The code is under developement, please remeber to change the 3d recorder element range in mRec functions')
    global nodeList

    m = Model()
    proc_dict = m.mDict()
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    eleNodes = bb[1]
    eleTag = bb[0]
    m.setUniqueVector(eleNodes)
    l = len(eleNodes)
    ll = len(eleNodes[0])
    d = m.listOfTagsij(l, ll)
    m.setUniqueVector(d)
    e = m.makeUnique()
    nup.savetxt('nodeInfo.txt', e)
    #############################################
    load_nodeList = nup.loadtxt('nodeInfo.txt')
    nodeList = []

    for i in range(len(load_nodeList)):
        nodeList.append(int(load_nodeList[i]))

    m.setUniqueVector(eleTag)
    max_value = nup.max(eleTag)
    min_value = nup.min(eleTag)
    print(f'min_value = {min_value}, max_value = {max_value}')
    ops.recorder('Node', '-xml', 'Gdisplacement.out', '-time', '-node', *nodeList, '-dof', 1, 2, 3, 'disp')
    ops.recorder('Node', '-xml', 'Gacceleration.out', '-time', '-node', *nodeList, '-dof', 1, 2, 3, 'accel')
    ops.recorder('Node', '-xml', 'GporePressure.out', '-time', '-node', *nodeList, '-dof', 4, 'vel')
    #################################################
    for nproc, subdict in proc_dict.items():
        if subdict == {}:
            break
        else:
            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == {nproc}:\n')
            py.close()
            
            tcl=open("cubotto.tcl","a")
            tcl.write("if {"+f' $pid == {nproc}'+' }'+' {\n')
            tcl.close()
            
            for el_num,nod_list in subdict.items():
                max_val = int(nup.max(nod_list))
                min_val = int(nup.min(nod_list))
            py = open("cubotto_exe.py", "a")
            py.write(f"    ops.recorder('Node','-xml','Gdisplacement.out','-time','-nodeRange',{min_val}, {max_val},'-dof', 1, 2, 3, 'disp')\n\
    ops.recorder('Node','-xml','Gacceleration.out','-time','-nodeRange',{min_val}, {max_val},'-dof', 1, 2, 3, 'accel')\n\
    ops.recorder('Node','-xml','GporePressure.out','-time','-nodeRange',{min_val}, {max_val},'-dof', 4, 'vel')\n")
            py.close()
                
            tcl = open('cubotto.tcl', 'a')
            tcl.write(f'    recorder Node -xml Gdisplacement.out -time -nodeRange {min_val} {max_val} -dof 1 2 3 disp \n\
    recorder Node -xml Gvelocity.out -time -time -nodeRange {min_val} {max_val} -dof 1 2 3 vel \n\
    recorder Node -xml Gacceleration.out -time -nodeRange {min_val} {max_val} -dof 1 2 3 accel \n\
    recorder Node -xml Gporepressure.out -time -nodeRange {min_val} {max_val} -dof 4 vel \n')
            tcl.write('}\n')
            tcl.close()
                
    #################################################
    ops.recorder('Element', '-xml', 'Gstress.out', '-time', '-eleRange', 1, 50000, 'material', '1', 'stress')
    ops.recorder('Element', '-xml', 'Ggauss.out', '-time', '-eleRange', 1, 50000, 'material', '1', 'gausspoint')
    ops.recorder('Element', '-xml', 'Gstrain.out', '-time', '-eleRange', 1, 50000, 'material', '1', 'strain')
    #################################################
    
    for nproc, subdict in proc_dict.items():
        if subdict == {}:
            break
        else:
            el_n_list=[]
            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == {nproc}:\n')
            py.close()
            
            tcl=open("cubotto.tcl","a")
            tcl.write("if {"+f' $pid == {nproc}'+' }'+' {\n')
            tcl.close()
            
            for el_num,nod_list in subdict.items():
                el_n_list.append(el_num)
            max_val = int(nup.max(el_n_list))
            min_val = int(nup.min(el_n_list))
        py = open("cubotto_exe.py", "a")
        py.write(f"    ops.recorder('Element','-file','Gstress.out','-time','-eleRange', {min_val},{max_val},'material','1','stress')\n\
    ops.recorder('Element','-file','Ggauss.out','-time','-eleRange', {min_val},{max_val},'material','1','gausspoint')\n\
    ops.recorder('Element','-file','Gstrain.out','-time','-eleRange', {min_val},{max_val},'material','1','strain')\n")
        py.close()
            
        tcl = open('cubotto.tcl', 'a')
        tcl.write(f'    recorder Element -file Gstress.out -time -eleRange {min_val} {max_val} -material 1 stress\n\
    recorder Element -file Gstrain.out -time -eleRange {min_val} {max_val} -material 1 strain\n')
        tcl.write('}\n')
        tcl.close()

    print("OK RECORDERS")
        #################################################
    return nodeList

def mGenFem20():
    ops.model("basicBuilder", "-ndm", 3, "-ndf", 4)
    py = open("cubotto_exe.py", "a")
    py.write('ops.model("basicBuilder", "-ndm", 3, "-ndf", 4)\n')
    py.close()

    tcl = open("cubotto.tcl", "a")
    tcl.write("model BasicBuilder -ndm 3 -ndf 4\n")
    tcl.close()

    print('funzione mGenFem20')
    m = Model()
    proc_dict = m.mDict()
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    eleNodes = bb[1]
    eleTag = bb[0]
    LET = len(bb[0])
    for i in range(0,LET):
        elem = int(eleTag[i])
        nodo1 = int(eleNodes[i][5])
        nodo2 = int(eleNodes[i][1])
        nodo3 = int(eleNodes[i][2])
        nodo4 = int(eleNodes[i][6])
        nodo5 = int(eleNodes[i][4])
        nodo6 = int(eleNodes[i][0])
        nodo7 = int(eleNodes[i][3])
        nodo8 = int(eleNodes[i][7])
        nodo9 = int(eleNodes[i][12])
        nodo10 = int(eleNodes[i][11])
        nodo11 = int(eleNodes[i][14])
        nodo12 = int(eleNodes[i][18])
        nodo13 = int(eleNodes[i][10])
        nodo14 = int(eleNodes[i][9])
        nodo15 = int(eleNodes[i][15])
        nodo16 = int(eleNodes[i][17])
        nodo17 = int(eleNodes[i][16])
        nodo18 = int(eleNodes[i][8])
        nodo19 = int(eleNodes[i][13])
        nodo20 = int(eleNodes[i][19])
        nodes_l = [nodo1,nodo2,nodo3,nodo4,nodo5,nodo6,nodo7,nodo8,nodo9, nodo10, nodo11,nodo12, nodo13, nodo14,nodo15,nodo16, nodo17,nodo18, nodo19, nodo20]
        ops.element('20_8_BrickUP',elem,*nodes_l, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
        #################################################
        procId = trova_elemento(proc_dict,elem)
        if elem == []:
            continue
        else:
            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == {procId}:\n')
            py.write(f"    ops.element('20_8_BrickUP',{elem},{nodo1}, {nodo2}, {nodo3}, {nodo4}, {nodo5}, {nodo6}, {nodo7}, {nodo8}, {nodo9},{nodo10}, {nodo11}, {nodo12}, {nodo13}, {nodo14}, {nodo15}, {nodo16}, {nodo17}, {nodo18},{nodo19}, {nodo20}, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)\n")
            py.close()
            
            tcl = open("cubotto.tcl","a")
            tcl.write("if {"+f' $pid == {procId}'+' }'+' {\n')
            tcl.write(f'    element 20_8_BrickUP {elem} {nodo1} {nodo2} {nodo3} {nodo4} {nodo5} {nodo6} {nodo7} {nodo8} {nodo9} {nodo10} {nodo11} {nodo12} {nodo13} {nodo14} {nodo15} {nodo16} {nodo17} {nodo18} {nodo19} {nodo20} 1  2.2e6 1 1.0 1.0 1.0 0.0 0.0 -20.0\n')
            tcl.write ('}\n')
            tcl.close()




def mDiaf():
    
    m = Model()

    ops.model("basicBuilder", "-ndm", 3, "-ndf", 3)
    nodo_mesh = int(input('inserisci il nodo selezionato per il dashpot: '))
    el = str(input('inserisci la superficie da irrigidire: '))
    b = m.setGeoElement(el)
    bb = m.getElementsVectors()
    m.setUniqueVector(bb)
    d = bb[1]
    m.setUniqueVector(d)
    e = m.makeUnique()
    for i in e:
        if i == nodo_mesh:
            continue
        else:
            ops.equalDOF(int(nodo_mesh), int(i), 1)
            ops.equalDOF(int(nodo_mesh), int(i), 2)
            ops.equalDOF(int(nodo_mesh), int(i), 3)

            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == 0:\n')
            py.write(f'    ops.equalDOF({int(nodo_mesh)}, {int(i)}, 1)\n')
            py.write(f'    ops.equalDOF({int(nodo_mesh)}, {int(i)}, 2)\n')
            py.write(f'    ops.equalDOF({int(nodo_mesh)}, {int(i)}, 3)\n')
            py.close()        
    
            tcl = open("cubotto.tcl", "a")
            tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
            tcl.write("model BasicBuilder -ndm 3 -ndf 3\n")
            tcl.write(f'equalDOF {int(nodo_mesh)} {int(i)} 1\n')
            tcl.write(f'equalDOF {int(nodo_mesh)} {int(i)} 2\n')
            tcl.write(f'equalDOF {int(nodo_mesh)} {int(i)} 3\n')
            tcl.write('}\n')
            tcl.close()


def mDash():
        ops.model("basicBuilder", "-ndm", 3, "-ndf", 3)
        py = open("cubotto_exe.py", "a")
        py.write('ops.model(" basicBuilder", " - ndm", 3, " - ndf ", 3)\n')
        py.close()

        tcl = open("cubotto.tcl", "a")
        tcl.write("model BasicBuilder -ndm 3 -ndf 3\n")
        tcl.close()


        print('funzione mDash')
        m = Model()
        proc_dict = m.mDict()
        b = m.setGeoElement('Solid')
        bb = m.getElementsVectors()
        eleNodes = bb[1]
        eleTag = bb[0]
        m.setUniqueVector(eleNodes)
        l = len(bb[1])
        ll=len(bb[1][0])
        c = m.listOfTagsij(l,ll)
        m.setUniqueVector(c)
        cc = m.makeUnique()
        max_value = nup.max(cc)
        min_value = nup.min(cc)
        dashFree = int(max_value + 1)
        
        print(f'dashFree = {dashFree}')
        
        dashFix = int(max_value + 2)
        print(f'dashFix = {dashFix}')
        
        x = float(input('insert x coord of dashpot in format 0.0'))
        y = float(input('insert y coord of dashpot in format 0.0')) 
        z = float(input('insert z coord of dashpot in format 0.0'))
        ops.node(dashFree,x,y,z)
        #################################################
        #################################################
        ops.node(dashFix,x,y,z)
        #################################################
        #################################################
        
        ops.fix(dashFix,1,1,1)
        
        #################################################
        #################################################
        
        f_x = int(input('Free node - insert 1 to constrain on - 0 to constrain off on dir x'))
        f_y = int(input('Free node - insert 1 to constrain on - 0 to constrain off on dir y'))
        f_z = int(input('Free node - insert 1 to constrain on - 0 to constrain off on dir z'))
        
        ops.fix(int(dashFree),f_x,f_y,f_z)
        
        #################################################
        #################################################
        
        nodo_mesh = int(input('write the mesh node tag who want to assigned dashpot'))
        
        ops.equalDOF(int(nodo_mesh), int(dashFree),1)
        
        colArea =   float(input('conn. area of dashpot'))
        rockVS =    float(input('Bedrock VS'))
        rockDen  =  float(input('Bedrock density'))
        dashpotCoeff = rockVS*rockDen*colArea
        tag = int(input('insert uniaxialMaterial tag (> n. geo-material)'))
        alpha = 1 
        ops.uniaxialMaterial('Viscous',tag,dashpotCoeff, alpha)
        
        m.setUniqueVector(eleTag)
        max_tag = nup.max(eleTag)
        print('ATTENZIONE PER IL MOMENTO POSSIBILE SOLO LUNGO X QUINDI PREMERE 1')
        var_dir = int(input('dof of dashpot -dir: 1 along x, 2 along xy, 3 along y'))
        if var_dir == 1:
            dir = [1]
        elif var_dir == 2:
            dir = [1,2]
        elif var_dir == 3:
            dir = [2]
        ops.element('zeroLength', int(max_tag+1), int(dashFix), int(dashFree), '-mat', tag, '-dir', *dir)
        
        #################################################
        procId = trova_nodo(proc_dict,int(nodo_mesh))
        for proc in procId:
            
            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == {proc}:\n')
            
            tcl=open("cubotto.tcl","a")
            tcl.write("if {"+f' $pid == {proc}'+' }'+' {\n')
            tcl.close()
            
            py = open("cubotto_exe.py", "a")
            py.write(f'    ops.node({dashFree},{x},{y},{z})\n')
            py.close()
            
            tcl=open("cubotto.tcl","a")
            tcl.write(f'    node {dashFree} {x} {y} {z}\n')
            tcl.close()
            
            py = open("cubotto_exe.py", "a")
            py.write(f'    ops.node({dashFix},{x},{y},{z})\n')
            py.close()
            
            tcl=open("cubotto.tcl","a")
            tcl.write(f'    node {dashFix} {x} {y} {z}\n')
            tcl.close()
            
            py = open("cubotto_exe.py", "a")
            py.write(f'    ops.fix({dashFix},1,1,1)\n')
            py.close()
            
            tcl=open("cubotto.tcl","a")
            tcl.write(f'    fix {dashFix} 1 1 1\n')
            tcl.close()
            
            py = open("cubotto_exe.py", "a")
            py.write(f'    ops.fix({dashFree},{f_x},{f_y},{f_z})\n')
            py.close()
            
            tcl=open("cubotto.tcl","a")
            tcl.write(f'    fix {dashFree} {f_x} {f_y} {f_z}\n')
            tcl.close()
            
            py = open("cubotto_exe.py", "a")
            py.write(f'    ops.equalDOF(int({nodo_mesh}), int({dashFree}),1)\n')
            py.close()
            
            tcl=open("cubotto.tcl","a")
            tcl.write(f'    equalDOF {int(nodo_mesh)} {int(dashFree)} 1\n')
            tcl.close()
            
        #################################################
        
        
        #################################################
            py = open("cubotto_exe.py", "a")
            py.write(f"    ops.uniaxialMaterial('Viscous',{tag},{dashpotCoeff}, {alpha})\n")
            py.close()
        #################################################
            tcl=open("cubotto.tcl","a")
            tcl.write(f'    uniaxialMaterial Viscous {tag} {dashpotCoeff} {alpha}\n')
            tcl.close()
            
        #################################################
            py = open("cubotto_exe.py", "a")
            py.write(f'    dir = {dir}\n')
            py.write(f"    ops.element('zeroLength', {int(max_tag+1)}, {int(dashFix)}, {int(dashFree)}, '-mat', {tag}, '-dir', *dir)\n")
            py.close()
        ################################################# ATTENZIONE SI è IMPOSTO DIREZIONE 1
            tcl=open("cubotto.tcl","a")
            #tcl.write(f'    set dir {dir}\n')
            tcl.write(f'    set dir 1\n')
            tcl.write(f'    element zeroLength  {int(max_tag+1)} {int(dashFix)} {int(dashFree)} -mat {tag} -dir $dir\n')
            tcl.write("}\n")
        
        return [colArea,dashpotCoeff,nodo_mesh]
    
        
        

def floatingNodes():
    connectedNodes = []
    for ele in ops.getEleTags():
        for nd in ops.eleNodes(ele):
            connectedNodes.append(nd)

    definedNodes = ops.getNodeTags()

    return list(set(connectedNodes) ^ set(definedNodes))


def chPerm():
    print('funzione chPerm')
    m = Model()
    proc_dict = m.mDict()
    permh = float(input('insert h permeability'))
    permv = float(input('insert v permeability'))
    eleTags = []
    getParamTags = []

    for i in ops.getParamTags():
        getParamTags.append(i)

    LT = len(getParamTags)
    if getParamTags == []:
        tag = 1
    else:
        tag = int(getParamTags[LT - 1]) + 1

    for i in ops.getEleTags():
        eleTags.append(int(i))

    LT2 = len(eleTags)
    for j in range(0, LT2 - 1):
        i = eleTags[j]
        ops.parameter(int(tag), 'element', i, 'hPerm')
        ops.parameter(int(tag + 1), 'element', i, 'vPerm')
        #################################################
        procId = trova_elemento(proc_dict,i)    
        py = open("cubotto_exe.py", "a")
        py.write(f'if pid == {procId}:\n')
        py.write(f"    ops.parameter({int(tag)}, 'element', {i},'hPerm')\n")
        py.close()
        
        tcl = open('cubotto.tcl', 'a')
        tcl.write("if {"+f' $pid == {procId}'+' }'+' {\n')
        tcl.write(f'    parameter {int(tag)} element {i} hPerm\n')
        tcl.close()
        
        py = open("cubotto_exe.py", "a")
        py.write(f"    ops.parameter({int(tag + 1)}, 'element', {i},'vPerm')\n")
        py.close()
        
        tcl = open('cubotto.tcl', 'a')
        tcl.write(f'    parameter {int(tag + 1)} element {i} vPerm\n')
        tcl.close()
        
        
        #################################################
        ops.updateParameter(int(tag), permh)
        ops.updateParameter(int(tag + 1), permv)
        #################################################
        py = open("cubotto_exe.py", "a")
        py.write(f"    ops.updateParameter({int(tag)},{permh})\n")
        py.close()
        
        tcl = open('cubotto.tcl', 'a')
        tcl.write(f'    updateParameter {int(tag)} {permh}\n')
        tcl.close()
        
        py = open("cubotto_exe.py", "a")
        py.write(f"    ops.updateParameter({int(tag + 1)},{permv})\n")
        py.close()
        
        tcl = open('cubotto.tcl', 'a')
        tcl.write(f'    updateParameter {int(tag+1)} {permv}\n')
        tcl.write('}\n')
        tcl.close()
        
        
        #################################################
        tag = tag + 2
        
def mTieNodes():
        print('funzione mTieNodes')
        m = Model()
        proc_dict = m.mDict()
        type_el_master1 = str(input('insert master plane geoElement'))
        b = m.setGeoElement(type_el_master1)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[0]) 
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()

        type_el_slave1 = str(input('insert slave plane geoElement'))
        b = m.setGeoElement(type_el_slave1)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[0])
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        g = m.nodeNumCoordVector()
        i = 0
        j = 0
        k = 0
        DOF = [1, 2]
        eqDofDic = {}
        for i in f:
            for j in g:
                z_master = i[1][2]
                z_slave = j[1][2]
                if z_master == z_slave:
                    eqDofDic[i[0]] = j[0]
                    ops.equalDOF(int(i[0]), int(j[0]), *DOF)
                    #################################################
                   
                    py = open("cubotto_exe.py", "a")
                    py.write(f'if pid == 0:\n')
                    py.write(f'    DOF = {DOF}\n')
                    py.write(f'    ops.equalDOF({int(i[0])}, {int(j[0])}, *DOF)\n')
                    py.close()
                          
                    tcl = open('cubotto.tcl', 'a')
                    tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
                    tcl.write(f'    equalDOF {int(i[0])} {int(j[0])} {DOF[0]} {DOF[1]}\n')
                    tcl.write('}\n')
                    tcl.close()           
           
        b = m.setGeoElement(type_el_master1)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[1]) 
        print(len(c[1])) 
        print(len(c[1][0]))
        l=len(c[1])
        ll=len(c[1][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()

        b = m.setGeoElement(type_el_slave1)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[1])
        print(len(c[1]))
        print(len(c[1][0]))
        l = len(c[1])
        ll = len(c[1][0])
        d = m.listOfTagsij(l, ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        g = m.nodeNumCoordVector()
        i = 0
        j = 0
        k = 0
        DOF = [1, 2]
        eqDofDic = {}
        for i in f:
            for j in g:
                z_master = i[1][2]
                z_slave = j[1][2]
                if z_master == z_slave:
                    eqDofDic[i[0]] = j[0]
                    ops.equalDOF(int(i[0]), int(j[0]), *DOF)
                    #################################################
                    
                    py = open("cubotto_exe.py", "a")
                    py.write(f'if pid == 0:\n')
                    py.write(f'    DOF = {DOF}\n')
                    py.write(f'    ops.equalDOF({int(i[0])}, {int(j[0])}, *DOF)\n')
                    py.close()
                    
                    tcl = open('cubotto.tcl', 'a')
                    tcl.write("if {"+f' $pid == 0'+' }'+' {\n')
                    #tcl.write(f'    set DOF {DOF}\n')
                    tcl.write(f'    equalDOF {int(i[0])} {int(j[0])} {DOF[0]} {DOF[1]}\n')
                    tcl.write('}\n')
                    tcl.close()                    
                    #################################################



def mStage0(gamma1,beta1,a0,a1):
    print('funzione mStage0')
    
    
    ops.model("basicBuilder", "-ndm", 3, "-ndf", 4)
    
    

    ops.updateMaterialStage('-material', 1, '-stage', 0)
    ops.updateMaterialStage('-material', 2, '-stage', 0)

    py = open("cubotto_exe.py", "a")
    py.write('ops.model("basicBuilder","-ndm",3,"-ndf",4)\n')
    py.close()
    
    tcl = open('cubotto.tcl', 'a')
    tcl.write('model BasicBuilder -ndm 3 -ndf 4\n')
    tcl.close()
    
    py = open("cubotto_exe.py", "a")
    py.write("ops.updateMaterialStage('-material', 1, '-stage', 0)\n")
    py.write("ops.updateMaterialStage('-material', 2, '-stage', 0)\n")
    py.close()
    
    tcl = open('cubotto.tcl', 'a')
    tcl.write('updateMaterialStage -material 1 -stage 0\n')
    tcl.write('updateMaterialStage -material 2 -stage 0\n')
    tcl.close()

    ops.constraints('Penalty', 1.e18, 1.e18)
    ops.test('NormDispIncr', 1.0e-6, 500, 1)
    ops.algorithm('KrylovNewton')
    ops.numberer('Plain')
    ops.system('ProfileSPD')
    ops.integrator('Newmark', gamma1, beta1)
    ops.analysis('Transient')

    
    py = open("cubotto_exe.py", "a")
    py.write(f"ops.constraints('Penalty', 1.e18, 1.e18)\n\
ops.test('NormDispIncr', 1.0e-6, 500, 1)\n\
ops.algorithm('KrylovNewton')\n\
ops.numberer('ParallelRCM')\n\
ops.system('Mumps')\n\
ops.integrator('Newmark', {gamma1}, {beta1})\n\
ops.analysis('Transient')\n\
startT = tt.time()\n\
ops.analyze(1,1)\n")
    py.close()
    
    tcl = open('cubotto.tcl', 'a')
    tcl.write(f'constraints Penalty 1.0E16 1.0E16\n\
test NormDispIncr 1e-3 100 1\n\
algorithm ModifiedNewton\n\
numberer ParallelRCM\n\
system Mumps -ICNTL14 200\n\
integrator Newmark {gamma1} {beta1}\n\
analysis Transient\n\
set ok [analyze $nSteps $dT]\n\
analyze 10 500\n')
    tcl.close()
    
    ops.analyze(1, 1)




def mRecDyn(recDT):
    print('funzione mRecDyn')
    m = Model()
    proc_dict = m.mDict()
    print('The code is under developement, please remeber to change the 3d recorder element range in mRec functions')
    ops.recorder('Node', '-xml', 'displacement.out', '-time', '-dT', recDT, '-node', *nodeList, '-dof', 1, 2, 3,'disp')
    ops.recorder('Node', '-xml', 'acceleration.out', '-time', '-dT', recDT, '-node', *nodeList, '-dof', 1, 2, 3,'accel')
    ops.recorder('Node', '-xml', 'porePressure.out', '-time', '-dT', recDT, '-node', *nodeList, '-dof', 4, 'vel')

    ops.recorder('Element', '-xml', 'stress.txt', '-time', '-dT', recDT, '-eleRange', 1, 50000, 'material', '1','stress')
    ops.recorder('Element', '-xml', 'strain.txt', '-time', '-dT', recDT, '-eleRange', 1, 50000, 'material', '1','strain')
    ops.recorder('Element', '-xml', 'strain.txt', '-time', '-dT', recDT, '-eleRange', 1, 50000, 'material', '1','plastic')

    ops.recorder('Element', '-xml', 'stress.out', '-time', '-dT', recDT, '-eleRange', 1, 50000, 'material', '1','stress')
    ops.recorder('Element', '-xml', 'strain.out', '-time', '-dT', recDT, '-eleRange', 1, 50000, 'material', '1','strain')
    ops.recorder('Element', '-xml', 'plastic.out', '-time', '-dT', recDT, '-eleRange', 1, 50000, 'material', '1','plastic')
   

    for nproc, subdict in proc_dict.items():
        if subdict == {}:
            break
        else:
            el_n_list=[]
            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == {nproc}:\n')
            py.close()
            
            tcl = open('cubotto.tcl', 'a')
            tcl.write("if {"+f' $pid == {nproc}'+' }'+' {\n')
            tcl.close()
            
            for el_num,nod_list in subdict.items():
                el_n_list.append(el_num)
                max_val = int(nup.max(nod_list))
                min_val = int(nup.min(nod_list))
            ### NODI #######
            py = open("cubotto_exe.py", "a")
            py.write(f"    ops.recorder('Node','-xml','displacement.out','-time', '-dT',recDT,'-nodeRange',{min_val},{max_val},'-dof', 1, 2,3, 'disp')\n\
    ops.recorder('Node','-xml','acceleration.out','-time', '-dT',recDT,'-nodeRange',{min_val},{max_val},'-dof', 1, 2,3, 'accel')\n\
    ops.recorder('Node','-xml','porePressure.out','-time', '-dT',recDT,'-nodeRange',{min_val},{max_val},'-dof', 4, 'vel')\n")
            py.close()
            
            tcl = open('cubotto.tcl', 'a')
            tcl.write(f'    eval "recorder Node -xml displacement.out -time -dT {recDT} -nodeRange {min_val} {max_val} -dof 1 2 3 disp" \n\
    eval "recorder Node -xml velocity_{min_val}_{max_val}.out -time -dT {recDT} -nodeRange {min_val} {max_val} -dof 1 2 3 vel" \n\
    eval "recorder Node -xml acceleration_{min_val}_{max_val}.out -time -dT {recDT} -nodeRange {min_val} {max_val} -dof 1 2 3 accel" \n\
    eval "recorder Node -xml porepressure_{min_val}_{max_val}.out -time -dT {recDT} -nodeRange {min_val} {max_val} -dof 4 vel" \n')
            tcl.close()
            
            max_val = int(nup.max(el_n_list))
            min_val = int(nup.min(el_n_list))
            py = open("cubotto_exe.py", "a")
            py.write(f"    ops.recorder('Element','-xml','stress.out','-time','-eleRange', {min_val},{max_val},'material','1','stress')\n\
    ops.recorder('Element','-xml','gauss.out','-time','-eleRange', {min_val},{max_val},'material','1','gausspoint')\n\
    ops.recorder('Element','-xml','strain.out','-time','-eleRange', {min_val},{max_val},'material','1','strain')\n")
            py.close()
        
            tcl = open('cubotto.tcl', 'a')
            tcl.write(f'    eval "recorder Element -xml stress_{min_val}_{max_val}.out -time -dT {recDT} -eleRange {min_val} {max_val} -material 1 stress"\n\
    eval "recorder Element -xml strain_{min_val}_{max_val}.out -time -dT {recDT} -eleRange {min_val} {max_val} -material 1 strain"\n')
            tcl.write('}\n')
            tcl.close()


def mExportPVD():
    m = Model()
    filename = 'exportPVDfile'
    if not os.path.exists(filename):
        os.makedirs(filename)
    ops.recorder('PVD', filename, 'disp', 'gausspoint', 'stress')


def mNodeInfoTxt():
    global nodeList
   
    m = Model()
    print('Attenzione chiamare con Solid l elemento di volume')
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    eleNodes = bb[1]
    eleTag = bb[0]
    m.setUniqueVector(eleNodes)
    l = len(eleNodes)
    ll = len(eleNodes[0])
    d = m.listOfTagsij(l, ll)
    m.setUniqueVector(d)
    e = m.makeUnique()
    nup.savetxt('nodeInfo.txt', e)

def mNodeInfoCornerDat():
    m = Model()
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    m.setUniqueVector(bb)
    c = m.nodeCornEdge('20-nodi')
    m.setUniqueVector(c[0])
    print(len(c[0]))
    print(len(c[0][0]))
    l = len(c[0])
    ll = len(c[0][0])
    d = m.listOfTagsij(l,ll)
    m.setUniqueVector(d)
    e = m.makeUnique()
    f = m.nodeNumCoordVector()
    n = open("nodeInfoCorner.dat","w")
    for i in f:
        xCoord =  i[1][0]
        yCoord =  i[1][1]
        zCoord =  i[1][2]
        n.write(f"{i[0]} {xCoord}    {yCoord}    {zCoord}\n")
    n.close()
    

def mNodeInfoDat():
    m = Model()
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    m.setUniqueVector(bb[1])
    c = m.makeUnique()
    m.setUniqueVector(c)
    d=m.nodeNumCoordVector()
    n=open("nodeInfo.dat","w")
    for i in d:
     xCoord =  i[1][0]
     yCoord =  i[1][1]
     zCoord =  i[1][2]
     n.write(f"{i[0]} {xCoord}    {yCoord}    {zCoord}\n")
    n.close()


def mGIDfile():
    m = Model()
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    eleNodes = bb[1]
    eleTag = bb[0]
    LET = len(bb[0])
    print(LET)
    
    mesh=open("mesh4GID.msh","w")
    element=open("element4GID.dat","w")
    mesh.write("MESH dimension 3 ElemType Hexahedra Nnode 20\n") 
    mesh.write("Coordinates\n")
    mesh.write("#node_number   coord_x   coord_y   coord_z\n")
    m.setUniqueVector(bb[1])
    c = m.makeUnique()
    m.setUniqueVector(c)
    d=m.nodeNumCoordVector()
    for i in d:
         xCoord =  i[1][0]
         yCoord =  i[1][1]
         zCoord =  i[1][2]
    mesh.write(f"{i[0]} {xCoord}    {yCoord}    {zCoord}\n")
    mesh.write("end coordinates\n")
    mesh.write("Elements\n")
        
    mesh.write("# element   nodo1  nodo2   nodo3   nodo4   nodo5   nodo6   nodo7   nodo8   nodo9   nodo10   nodo11   nodo12   nodo13   nodo14   nodo15   nodo16   nodo17   nodo18   nodo19   nodo20\n")
    
    for i in range(0,LET):
            elem = int(eleTag[i])
            nodo1 = int(eleNodes[i][4])
            nodo2 = int(eleNodes[i][5])
            nodo3 = int(eleNodes[i][1])
            nodo4 = int(eleNodes[i][0])
            nodo5 = int(eleNodes[i][7])
            nodo6 = int(eleNodes[i][6])
            nodo7 = int(eleNodes[i][2])
            nodo8 = int(eleNodes[i][3])
            nodo9 = int(eleNodes[i][16])
            nodo10 = int(eleNodes[i][12])
            nodo11 = int(eleNodes[i][8])
            nodo12 = int(eleNodes[i][10])
            nodo13 = int(eleNodes[i][19])
            nodo14 = int(eleNodes[i][14])
            nodo15 = int(eleNodes[i][13])
            nodo16 = int(eleNodes[i][15])
            nodo17 = int(eleNodes[i][17])
            nodo18 = int(eleNodes[i][18])
            nodo19 = int(eleNodes[i][11])
            nodo20 = int(eleNodes[i][9])
            nodes_l = [nodo1,nodo2,nodo3,nodo4,nodo5,nodo6,nodo7,nodo8,nodo9, nodo10, nodo11,nodo12, nodo13, nodo14,nodo15,nodo16, nodo17,nodo18, nodo19, nodo20]
            mesh.write(f"{elem} {nodo1} {nodo2} {nodo3} {nodo4} {nodo5} {nodo6} {nodo7} {nodo8} {nodo9} {nodo10} {nodo11} {nodo12} {nodo17} {nodo18} {nodo19} {nodo20} {nodo13} {nodo14} {nodo15} {nodo16} \n")
            element.write(f"{elem} {nodo1} {nodo2} {nodo3} {nodo4} {nodo5} {nodo6} {nodo7} {nodo8} {nodo9} {nodo10} {nodo11} {nodo12} {nodo17} {nodo18} {nodo19} {nodo20} {nodo13} {nodo14} {nodo15} {nodo16}\n")
    mesh.write("end elements")
    
    element.close()
    mesh.close()


