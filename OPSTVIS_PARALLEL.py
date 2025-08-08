# -*- coding: utf-8 -*-
file = "displacement.part-0.xml"
file2 = "displacement.part-1.xml"
file3 = "displacement.part-2.xml"
file4 = "displacement.part-3.xml"

import xml.etree.ElementTree as xtd
import io
import numpy as np
#import respSpectra as rsp
import matplotlib.pyplot as plt
import pandas as pd
import pyvista as pv

#############################################################

#OpenSeesTclRead:
def OpenSeesTclRead(tclFile, startswith, n_cols):
    fileInfo = []
    tclfile = open(tclFile, 'r')
    for line in tclfile:
        if line[:len(startswith)] == startswith:
            args = line.split()
            for i in range(0, n_cols):
                fileInfo.append(args[i])

    tclfile.close()
    return np.array(fileInfo).reshape((-1, n_cols))

def quad_cell(elemList, nodeList):
    nodeiRow = []
    print(f'elem_list: {elemList}')
    print(f'node_list: {nodeList}')
    for i in range(len(elemList[:, 0])):
        nodeiRow.append((4, int(np.argwhere(nodeList == int(elemList[i, 3]))),
                          int(np.argwhere(nodeList == int(elemList[i, 4]))),
                          int(np.argwhere(nodeList == int(elemList[i, 5]))),
                          int(np.argwhere(nodeList == int(elemList[i, 6])))))
    
    #print(f'quad_cell: {np.array(nodeiRow)}')
    return np.array(nodeiRow)

def cell_type_quad(elemList):
    x = np.repeat(9, (len(elemList[:, 0])))
    return x

def calcola_modulo_spostamenti(t,vec_def):
            '''calcola l'intervallo dei valori da prendere nel vettore degli spostamenti'''
            # Esempio: i vettori di spostamento oscillano nel tempo
            inizio = 0
            fine = 0
            n = int(t/0.01)
            if n == 0:
                inizio = 0
                fine = int(inizio+mesh.n_points)
            else:
                inizio = int(n*mesh.n_points)
                fine = int(inizio+mesh.n_points)
            spostamenti = vec_def[inizio:fine]
            return spostamenti

#Funzione di callback per aggiornare il plot in base al valore di t
def update(t):
            sargs= dict(interactive=True)

            state_zero = mesh.points
            #point_labels = [f'{i}' for i in range(mesh.n_points)]
            
            scala = 1000.0
            # Rimuove tutti gli oggetti dal plotter
            p.remove_actor('mesh') 
            p.remove_actor('label') 

            
            # Calcola il nuovo modulo dei vettori
            nuovo_modulo = calcola_modulo_spostamenti(t,deform_x)
    
            # Aggiorna i dati della mesh
            mesh_deformata['modulo_spostamenti'] = nuovo_modulo
            # Rimuovi la mesh precedente e aggiungi la nuova mesh con i valori aggiornati
            #p.add_mesh(mesh, scalars='modulo_spostamenti', cmap='hot', opacity=1.0, name='mesh')
            
            #p.remove_point_label()
            vect_zero = np.repeat(0,len(nuovo_modulo[:]))
            vec_sum = np.column_stack([nuovo_modulo,vect_zero,vect_zero])
            mesh_deformata.points = mesh.points + vec_sum*scala
            
            #label_coords = mesh_deformata.points + [0, 0, 0.02]
            
            #p.add_point_labels(label_coords, point_labels, name='label', font_size=10, point_size=10)
           
            #p.add_mesh(mesh_deformata, scalars='modulo_spostamenti', cmap='jet', opacity=1.0, name='mesh',show_edges = True)
            p.add_mesh(mesh_deformata, scalar_bar_args=sargs, scalars='modulo_spostamenti',  cmap='jet', opacity=1.0, name='mesh', show_edges = True)
            camera = p.camera_position
            print(f'posizione telecamera: {camera}')
            p.show_axes()
#############################################################
def trova_nodo(dicto, dictTag, x, y, z):
    output = 0
    jj = 0
    i = 0
    for node,coord in dicto.items():
        if x == coord['x']: 
            if y == coord['y']:
                if z == coord['z']:
                    output = int(node)
                    break
    #output = nup.unique(nup.array(output, dtype=int))
    print(f'il nodo che cerchi è il numero: {output}')
    for i in dictTag:
        if i == output:
            #print(f'il numero di posizione nella lista {dictTag} è: {jj}')
            return [jj,i]
        else:
            jj = jj+1

    return [jj,i]


def leggi_xml(nome_file):   
    '''legge il file xml e crea una lista in python'''
    #limite dati:
    with io.open(nome_file, 'r') as f:
        # leggi tutte le righe
        lines = f.readlines()
    f.close()
    return lines


def definizione_skip(righe,lines):
    riga_limite = 0

    for i in range(righe):
        if "<Data>"  in lines[i]:
            riga_limite = i
            break
   
    return riga_limite


def ritaglia_xml(lines,righe,n):
    '''ritaglia il file lasciando solo i metadati e crea un file dei metadati
    in termine di coordinate e tag dei nodi'''
    riga_limite = 0

    for i in range(righe):
        if "<Data>"  in lines[i]:
            riga_limite = i
            break
        if riga_limite == 0:
            print("non ho trovato il limite")


    nome_file =str(f'disp_{n}_metadata.xml')
    select = open(nome_file,'w')
    select.close()        
    
    select = open(nome_file,'a')
    for i in range(riga_limite - 1):
        select.write(lines[i])
    
    select.write(" </NodeOutput>")     
    select.write(" </OpenSees>")     
    select.close() 
    return print(nome_file)

def definizione_nodi(select):
    data_disp = xtd.parse(select)
    tag_disp = data_disp.findall(".//NodeOutput")
    nodeTag_disp = []
    node_coord_disp = {}
    for item in tag_disp:
        a = int(item.attrib['nodeTag'])
        x = float(item.attrib['coord1'])
        y = float(item.attrib['coord2'])
        z = float(item.attrib['coord3'])
        nodeTag_disp.append(a)
        node_coord_disp[a] = {'x':x, 'y':y, 'z':z}
    nodeTag_disp = np.array(nodeTag_disp)
    return nodeTag_disp,node_coord_disp

def NodeCoords(TCLFile):
    #global initNodeCoords
    #modelInfo = OpenSeesTclRead(TCLFile, 'model', 6)
    #ndm = ndm_v(TCLFile)
    #ndm imposto = 2
    ndm = 2
    if ndm==3:
        nodeInfo = OpenSeesTclRead(TCLFile, '	node', 5)
        initNodeCoords = nodeInfo[:, 2:5].astype(float)
    elif ndm==2:

        nodeInfo = OpenSeesTclRead(TCLFile, '	node', 4)
        initNodeCoord = nodeInfo[:, 2:4].astype(float)
        initNodeCoords1=[]
        z = np.repeat(0, len(initNodeCoord[:,0]))
        for i in range (len(initNodeCoord[:,0])):

            initNodeCoords1.append((initNodeCoord[i]).tolist())
        initNodeCoords=np.column_stack([initNodeCoords1, z])
    return (initNodeCoords)

def output_disp(imp_disp):
    ndm = 2
    output = np.array(imp_disp)
    n_nodes = (len(output[0])-1)/2
    n_steps = len(output)
    time_frame = output[:,0]
    response_rshp = output[:, 1:].reshape(-1, ndm)
    z_res = np.repeat(0, len(response_rshp[:, 0]))
    response = np.column_stack([response_rshp, z_res])
    return [output, n_nodes, n_steps, time_frame, response_rshp, response]


def spostamenti_x_nodo(nodo,nodeTag_vec,response,numero_nodi):
    index_node=0
    list_tag = list(nodeTag_vec)
    for i in nodeTag_vec:
        if nodo == i:
            index_node = list_tag.index(i)
            print(f'indice: {index_node}')
    #spostamenti = response[:,0][index_node-1::int(numero_nodi)]
    spostamenti = response[:,0][index_node::int(numero_nodi)]

    return spostamenti

def spostamenti_y_nodo(nodo,nodeTag_vec,response,numero_nodi):
    index_node=0
    list_tag = list(nodeTag_vec)
    for i in nodeTag_vec:
        if nodo == i:
            index_node = list_tag.index(i)
            print(f'indice: {index_node}')
    #spostamenti = response[:,1][index_node-1::int(numero_nodi)]
    spostamenti = response[:,1][index_node::int(numero_nodi)]
    return spostamenti

def extract_nodeCoord(dictCord):
    listCoord=[]
    listNodes = []
    for i in dictCord:
        x = dictCord[i]['x']
        y = dictCord[i]['y']
        z = dictCord[i]['z']
        cord = [x,y,z]
        listCoord.append(cord)
        listNodes.append(i)
    return np.array(listCoord),np.array(listNodes)

def convertFromParallel_x(time_frame,dict_global_disp):
    '''riscrive il file output come se fosse stato eseguito in seriale il risultato è un file .out'''
    otp = open('outptu_disp.out','w')
    otp.close()
    for j in range(len(time_frame)):
        print(f'time_frame: {time_frame[j]}')
        otp = open('outptu_disp.out','a')
        #print(f'time_frame: {time_frame[j]}')
        otp.write(f'{time_frame[j]} ')
        #otp.close()
        for i in dict_global_disp:
            #if j > 0:
                if len(dict_global_disp[i]['x_disp']) == 1: 
                    #extract.append([time_frame[j],i,np.nan])
                    otp = open('outptu_disp.out','a')
                    otp.write(f'0.0 ')
                    #otp.close()                 
                else:
                    valore = dict_global_disp[i]['x_disp'][j]
                    #extract.append([time_frame[j],i,valori])
                    otp = open('outptu_disp.out','a')
                    otp.write(f'{valore} ')
                    #otp.close()
        otp = open('outptu_disp.out','a')
        otp.write(f'\n')
        otp.close()
        
def analisi_len(vettore,lunghezza):
    k = 0
    for i in vettore:
        if len(i) > lunghezza:
            print(f'non omogeneo in {k}')
        if len(i) < lunghezza:
            print(f'non omogeneo in {k}')
            print('correggo con zeri....')
            vettore[k] = np.repeat(0.0,lunghezza)
        k = k + 1
           

riga_limite = 0

lines = leggi_xml(file)
lines2 = leggi_xml(file2)
lines3 = leggi_xml(file3)
lines4 = leggi_xml(file4)


righe = len(lines)
righe2 = len(lines2)
righe3 = len(lines3)
righe4 = len(lines4)

skip0 = definizione_skip(righe,lines)+1
skip1 = definizione_skip(righe2,lines2)+1
skip2 = definizione_skip(righe3,lines3)+1
skip3 = definizione_skip(righe4,lines4)+1

ritaglia_xml(lines,righe,0)
ritaglia_xml(lines2,righe2,1)
ritaglia_xml(lines3,righe3,2)
ritaglia_xml(lines4,righe4,3)


#############################################################
###### CREZIONE TABELLA PANDAS RISULTATI NODALI #############
#############################################################

imp_disp =   pd.read_csv(file, delim_whitespace=True, header=None, comment='<', skiprows=skip0)

imp_disp2 =   pd.read_csv(file2, delim_whitespace=True, header=None, comment='<', skiprows=skip1)

imp_disp3 =   pd.read_csv(file3, delim_whitespace=True, header=None, comment='<', skiprows=skip2)

imp_disp4 =   pd.read_csv(file4, delim_whitespace=True, header=None, comment='<', skiprows=skip3)

#############################################################

select = "disp_0_metadata.xml"
nodeTag,node_coord = definizione_nodi(select)

select = "disp_1_metadata.xml"
nodeTag2,node_coord2 = definizione_nodi(select)

select = "disp_2_metadata.xml"
nodeTag3,node_coord3 = definizione_nodi(select)

select = "disp_3_metadata.xml"
nodeTag4,node_coord4 = definizione_nodi(select)
############################################## Nodi e coordinate

[output, n_nodes, n_steps, time_frame, response_rshp, response] = output_disp(imp_disp)
[output2, n_nodes2, n_steps2, time_frame, response_rshp2, response2] = output_disp(imp_disp2)
[output3, n_nodes3, n_steps3, time_frame, response_rshp3, response3] = output_disp(imp_disp3)
[output4, n_nodes4, n_steps4, time_frame, response_rshp4, response4] = output_disp(imp_disp4)


# dict_global_disp_0 = {}
# for i in nodeTag:
#     dict_global_disp_0[i] = {'x_disp':spostamenti_x_nodo(i,nodeTag,response_rshp,int(n_nodes)),'y_disp':spostamenti_y_nodo(i,nodeTag,response_rshp,int(n_nodes))}

# dict_coord_global_0 = {}
# for i in node_coord:
#     dict_coord_global_0[i] = node_coord[i]  

dict_global_disp={}
for i in nodeTag:
    dict_global_disp[i] = {'x_disp':spostamenti_x_nodo(i,nodeTag,response_rshp,int(n_nodes)),'y_disp':spostamenti_y_nodo(i,nodeTag,response_rshp,int(n_nodes))}
for i in nodeTag2:
    dict_global_disp[i] = {'x_disp':spostamenti_x_nodo(i,nodeTag2,response_rshp2,int(n_nodes2)),'y_disp':spostamenti_y_nodo(i,nodeTag2,response_rshp2,int(n_nodes2))}
for i in nodeTag3:
    dict_global_disp[i] = {'x_disp':spostamenti_x_nodo(i,nodeTag3,response_rshp3,int(n_nodes3)),'y_disp':spostamenti_y_nodo(i,nodeTag3,response_rshp3,int(n_nodes3))}
for i in nodeTag4:
    dict_global_disp[i] = {'x_disp':spostamenti_x_nodo(i,nodeTag4,response_rshp4,int(n_nodes4)),'y_disp':spostamenti_y_nodo(i,nodeTag4,response_rshp4,int(n_nodes4))}
               
dict_coord_global={}
for i in node_coord:
    dict_coord_global[i] = node_coord[i]   
for i in node_coord2:
    dict_coord_global[i] = node_coord2[i]    
for i in node_coord3:
    dict_coord_global[i] = node_coord3[i]
for i in node_coord4:
    dict_coord_global[i] = node_coord4[i]          
           

#connectivity = OpenSeesTclRead("feView_tcl_0.tcl", "element quadUP", 7)
connectivity = OpenSeesTclRead("elements.tcl", "element SSPquadUP", 7)
elemList = connectivity[:,2]
nodeCoord, nodeList = extract_nodeCoord(dict_coord_global)

#nodeInfo = OpenSeesTclRead("feView_tcl_0.tcl", '	node', 4)
#nodeCoord = NodeCoords("feView_tcl_0.tcl")
#nodeList = nodeInfo[:,1]
#nodeiRow = quad_cell(connectivity,nodeList)


#################################################################
######### SPAZIO MEMORIA
#################################################################

del lines
del lines2
del lines3
del lines4

del imp_disp
del imp_disp2
del imp_disp3
del imp_disp4

del node_coord
del node_coord2
del node_coord3
del node_coord4

del nodeTag
del nodeTag2
del nodeTag3
del nodeTag4

del output
del output2
del output3
del output4

del response
del response2
del response3
del response4

del response_rshp
del response_rshp2
del response_rshp3
del response_rshp4

################################################################
##### VETTORE DEGLI SCALARI X
################################################################
conv = [i for i in [dict_global_disp[key]['x_disp'] for key in dict_global_disp]]
analisi_len(conv,n_steps)
conv = np.array(conv).reshape(-1,n_steps).T

#### AZZERO SPOSTAMENTI FASE PRECEDENTE ########

first_array = conv[0,:]
conv = conv-first_array
#conv_mod = conv[:,1:]
#conv_export = np.column_stack([time_frame,conv])

#np.savetxt('output_mp.out',conv_export)

deform_x = np.array(conv).reshape((-1,1))
#deform_x = deform_xy[:,0]

#################################################################
# convertFromParallel_x(time_frame,dict_global_disp)
# file_spost = "outptu_disp.out"
# deformation = out_response(file_spost,n_steps,2,'all')
# disp_x = deformation[:,0]
#################################################################

################################################################
##### PYVISTA SPOSTAMENTI
################################################################
cells = quad_cell(connectivity,nodeList)
cell_type = (cell_type_quad(connectivity))
print(f'celltype: {cell_type}')
mesh = pv.UnstructuredGrid( cells, cell_type, nodeCoord)
n_points = mesh.n_points

   
# Aggiungere la mesh iniziale con t = 0
t_init = 0.0
modulo_spostamenti = calcola_modulo_spostamenti(t_init,deform_x)
mesh['modulo_spostamenti'] = modulo_spostamenti
spostamenti_zero = mesh.points.copy()
##########################################################
############################ CREAZIONE VIDEO
#Creare un plotter
# p = pv.Plotter()

# p.add_mesh(mesh, scalars='modulo_spostamenti', cmap='jet', opacity=1.0, name='mesh', show_edges = True)
# p.show_axes
# p.camera_position = 'xy'

# p.open_gif('animation.gif')
# nframe = 5000
# dT_nframe = 0.01
# t_durata = nframe*dT_nframe
# time_frame = np.arange(0.0,t_durata,dT_nframe)

# for t in time_frame:
    # scala = 500.0
    #label_coords = mesh.points + [0, 0, 0.02]
   # point_labels = [f'{i}' for i in range(mesh.n_points)]
   # p.add_point_labels(label_coords, point_labels, name='label', font_size=10, point_size=10)
    
    # nuovo_modulo = calcola_modulo_spostamenti(t,deform_x)
    # mesh['modulo_spostamenti'] = nuovo_modulo
    # vect_zero = np.repeat(0,len(nuovo_modulo[:]))
    # vec_sum = np.column_stack([nuovo_modulo,vect_zero,vect_zero])
    # mesh.points = spostamenti_zero + vec_sum*scala
    #mesh.points =  vec_sum*scala
    # p.add_mesh(mesh, scalars='modulo_spostamenti', cmap='jet', opacity=1.0, clim = [-0.08,0.05],  name='mesh', show_edges = True)
    #p.camera.zoom(2)
    
    # p.camera_position = [(1033.0888501834386, 18.893062403961615, 796.7726439626823),
     # (1036.9287631858638, 71.04047286922118, -126.29949604983189),
     # (0.010157813813937206, 0.9983541715885984, 0.05644259818757917)]
    
    # p.write_frame()
# p.close()
# p.clear()
###########################################################
###########################################################

sargs= dict(interactive=False)
cells = quad_cell(connectivity,nodeList)
cell_type = (cell_type_quad(connectivity))
mesh = pv.UnstructuredGrid( cells, cell_type, nodeCoord)
n_points = mesh.n_points

# Creare un plotter
p = pv.Plotter()


# Aggiungere la mesh iniziale con t = 0
t_init = 0.0
modulo_spostamenti = calcola_modulo_spostamenti(t_init,deform_x)
mesh['modulo_spostamenti'] = modulo_spostamenti

p.add_mesh(mesh, scalar_bar_args=sargs, scalars='modulo_spostamenti', cmap='jet', opacity=1.0, clim=[0.0,0.03], name='mesh', show_edges = True)

# Creare una copia della mesh per la versione deformata
mesh_deformata = mesh.copy()

# Aggiungere la mesh deformata iniziale
p.add_mesh(mesh_deformata, scalar_bar_args=sargs, scalars='modulo_spostamenti', cmap='jet', opacity=1.0, clim=[0.0,0.03], name='mesh', show_edges = True)


###################################################################

durata = 50

# Aggiungere uno slider per controllare il tempo t
p.add_slider_widget(update,rng=[0,durata],title="time (sec)")


p.show(cpos='xy')
