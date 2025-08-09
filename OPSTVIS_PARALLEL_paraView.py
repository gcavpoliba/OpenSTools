# -*- coding: utf-8 -*-
"""
Script modificato per esportare dati compatibili con ParaView
Basato su OPSTVIS_PARALLEL.py - analisi di risultati OpenSees paralleli
Esporta file VTU/PVTU per visualizzazione time-series in ParaView
"""

file = "displacement.part-0.xml"
file2 = "displacement.part-1.xml"
file3 = "displacement.part-2.xml"
file4 = "displacement.part-3.xml"

import xml.etree.ElementTree as xtd
import io
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyvista as pv
import os
from pathlib import Path

#############################################################
# CONFIGURAZIONE ESPORTAZIONE PARAVIEW
#############################################################

# Directory per i file di output ParaView
OUTPUT_DIR = "paraview_output"
# Formato di esportazione: 'vtu' per singoli file, 'pvtu' per parallelo
EXPORT_FORMAT = 'vtu'  
# Esportare serie temporale
EXPORT_TIME_SERIES = True
# Scala di deformazione
DEFORMATION_SCALE = 1000.0

#############################################################
# FUNZIONI ORIGINALI MANTENUTE
#############################################################

def OpenSeesTclRead(tclFile, startswith, n_cols):
    """Legge file TCL di OpenSees e estrae informazioni specifiche"""
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
    """Crea connectivity matrix per elementi quad"""
    nodeiRow = []
    print(f'elem_list: {elemList}')
    print(f'node_list: {nodeList}')
    for i in range(len(elemList[:, 0])):
        nodeiRow.append((4, int(np.argwhere(nodeList == int(elemList[i, 3]))),
                          int(np.argwhere(nodeList == int(elemList[i, 4]))),
                          int(np.argwhere(nodeList == int(elemList[i, 5]))),
                          int(np.argwhere(nodeList == int(elemList[i, 6])))))
    return np.array(nodeiRow)

def cell_type_quad(elemList):
    """Definisce il tipo di cella per elementi quad (VTK type 9)"""
    x = np.repeat(9, (len(elemList[:, 0])))
    return x

def calcola_modulo_spostamenti(t, vec_def, n_points):
    """Calcola gli spostamenti per un dato istante temporale"""
    n = int(t/0.01)
    if n == 0:
        inizio = 0
        fine = int(inizio + n_points)
    else:
        inizio = int(n * n_points)
        fine = int(inizio + n_points)
    spostamenti = vec_def[inizio:fine]
    return spostamenti

def leggi_xml(nome_file):   
    """Legge il file XML e crea una lista in Python"""
    with io.open(nome_file, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines

def definizione_skip(righe, lines):
    """Trova la riga dove iniziano i dati"""
    riga_limite = 0
    for i in range(righe):
        if "<Data>" in lines[i]:
            riga_limite = i
            break
    return riga_limite

def ritaglia_xml(lines, righe, n):
    """Estrae i metadati dal file XML"""
    riga_limite = 0
    for i in range(righe):
        if "<Data>" in lines[i]:
            riga_limite = i
            break
        if riga_limite == 0:
            print("non ho trovato il limite")

    nome_file = str(f'disp_{n}_metadata.xml')
    select = open(nome_file, 'w')
    select.close()        
    
    select = open(nome_file, 'a')
    for i in range(riga_limite - 1):
        select.write(lines[i])
    
    select.write(" </NodeOutput>")     
    select.write(" </OpenSees>")     
    select.close() 
    return print(nome_file)

def definizione_nodi(select):
    """Estrae tag e coordinate dei nodi dal file XML"""
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
        node_coord_disp[a] = {'x': x, 'y': y, 'z': z}
    nodeTag_disp = np.array(nodeTag_disp)
    return nodeTag_disp, node_coord_disp

def output_disp(imp_disp):
    """Processa i dati di spostamento"""
    ndm = 2
    output = np.array(imp_disp)
    n_nodes = (len(output[0])-1)/2
    n_steps = len(output)
    time_frame = output[:, 0]
    response_rshp = output[:, 1:].reshape(-1, ndm)
    z_res = np.repeat(0, len(response_rshp[:, 0]))
    response = np.column_stack([response_rshp, z_res])
    return [output, n_nodes, n_steps, time_frame, response_rshp, response]

def spostamenti_x_nodo(nodo, nodeTag_vec, response, numero_nodi):
    """Estrae gli spostamenti X per un nodo specifico"""
    index_node = 0
    list_tag = list(nodeTag_vec)
    for i in nodeTag_vec:
        if nodo == i:
            index_node = list_tag.index(i)
            print(f'indice: {index_node}')
    spostamenti = response[:, 0][index_node::int(numero_nodi)]
    return spostamenti

def spostamenti_y_nodo(nodo, nodeTag_vec, response, numero_nodi):
    """Estrae gli spostamenti Y per un nodo specifico"""
    index_node = 0
    list_tag = list(nodeTag_vec)
    for i in nodeTag_vec:
        if nodo == i:
            index_node = list_tag.index(i)
            print(f'indice: {index_node}')
    spostamenti = response[:, 1][index_node::int(numero_nodi)]
    return spostamenti

def extract_nodeCoord(dictCord):
    """Estrae coordinate e lista nodi dal dizionario"""
    listCoord = []
    listNodes = []
    for i in dictCord:
        x = dictCord[i]['x']
        y = dictCord[i]['y']
        z = dictCord[i]['z']
        cord = [x, y, z]
        listCoord.append(cord)
        listNodes.append(i)
    return np.array(listCoord), np.array(listNodes)

def analisi_len(vettore, lunghezza):
    """Verifica e corregge la lunghezza dei vettori"""
    k = 0
    for i in vettore:
        if len(i) > lunghezza:
            print(f'non omogeneo in {k}')
        if len(i) < lunghezza:
            print(f'non omogeneo in {k}')
            print('correggo con zeri....')
            vettore[k] = np.repeat(0.0, lunghezza)
        k = k + 1

#############################################################
# NUOVE FUNZIONI PER ESPORTAZIONE PARAVIEW
#############################################################

def create_output_directory(directory):
    """Crea la directory di output se non esiste"""
    Path(directory).mkdir(parents=True, exist_ok=True)
    print(f"Directory di output creata/verificata: {directory}")

def export_to_vtu(mesh, filename, time_value=None):
    """
    Esporta mesh PyVista in formato VTU (XML UnstructuredGrid)
    
    Args:
        mesh: PyVista UnstructuredGrid
        filename: nome del file di output
        time_value: valore temporale per serie temporali
    """
    # Aggiungi informazioni temporali se necessario
    if time_value is not None:
        mesh.field_data['TimeValue'] = np.array([time_value])
    
    # Salva in formato VTU
    mesh.save(filename, binary=True)
    print(f"Esportato: {filename}")

def export_to_legacy_vtk(mesh, filename):
    """
    Esporta mesh in formato VTK legacy (compatibile con versioni older di ParaView)
    
    Args:
        mesh: PyVista UnstructuredGrid
        filename: nome del file di output
    """
    #mesh.save(filename, binary=False, file_format='vtk')
    mesh.save(filename, binary=False)
    print(f"Esportato VTK legacy: {filename}")

def create_pvd_file(base_name, time_steps, file_list, output_dir):
    """
    Crea un file PVD (ParaView Data) per serie temporali
    
    Args:
        base_name: nome base per il file PVD
        time_steps: array dei valori temporali
        file_list: lista dei file VTU corrispondenti
        output_dir: directory di output
    """
    pvd_filename = os.path.join(output_dir, f"{base_name}.pvd")
    
    with open(pvd_filename, 'w') as pvd:
        pvd.write('<?xml version="1.0"?>\n')
        pvd.write('<VTKFile type="Collection" version="0.1" byte_order="LittleEndian">\n')
        pvd.write('  <Collection>\n')
        
        for time, filename in zip(time_steps, file_list):
            relative_path = os.path.basename(filename)
            pvd.write(f'    <DataSet timestep="{time}" file="{relative_path}"/>\n')
        
        pvd.write('  </Collection>\n')
        pvd.write('</VTKFile>\n')
    
    print(f"File PVD creato: {pvd_filename}")
    return pvd_filename

def export_time_series(mesh_base, deform_x, time_frame, output_dir, 
                      deformation_scale=1000.0, sample_rate=1):
    """
    Esporta serie temporale completa per ParaView
    
    Args:
        mesh_base: mesh di base non deformata
        deform_x: vettore deformazioni
        time_frame: array dei tempi
        output_dir: directory output
        deformation_scale: scala di amplificazione deformazioni
        sample_rate: frequenza di campionamento (1 = tutti i frame)
    
    Returns:
        lista dei file creati
    """
    file_list = []
    n_points = mesh_base.n_points
    
    # Copia iniziale della mesh
    spostamenti_zero = mesh_base.points.copy()
    
    # Campiona i time steps secondo sample_rate
    sampled_indices = range(0, len(time_frame), sample_rate)
    sampled_times = [time_frame[i] for i in sampled_indices]
    
    print(f"Esportazione di {len(sampled_times)} time steps...")
    
    for idx, t_idx in enumerate(sampled_indices):
        t = time_frame[t_idx]
        
        # Crea copia della mesh per questo timestep
        mesh_t = mesh_base.copy()
        
        # Calcola spostamenti per questo istante
        nuovo_modulo = calcola_modulo_spostamenti(t, deform_x, n_points)
        
        # Aggiungi campo scalare degli spostamenti
        mesh_t['displacement_magnitude'] = nuovo_modulo
        
        # Crea vettore spostamenti 3D
        vect_zero = np.repeat(0, len(nuovo_modulo[:]))
        vec_displacement = np.column_stack([nuovo_modulo, vect_zero, vect_zero])
        
        # Aggiungi campo vettoriale degli spostamenti
        mesh_t['displacement_vector'] = vec_displacement
        
        # Applica deformazione alla mesh
        mesh_t.points = spostamenti_zero + vec_displacement * deformation_scale
        
        # Nome file con padding per ordinamento corretto
        filename = os.path.join(output_dir, f"displacement_{idx:04d}.vtu")
        
        # Esporta in formato VTU con informazioni temporali
        export_to_vtu(mesh_t, filename, time_value=t)
        file_list.append(filename)
        
        # Progress indicator
        if idx % 10 == 0:
            print(f"  Processato frame {idx}/{len(sampled_times)}")
    
    # Crea file PVD per la serie temporale
    pvd_file = create_pvd_file("displacement_series", sampled_times, file_list, output_dir)
    
    print(f"\nSerie temporale esportata con successo!")
    print(f"Per visualizzare in ParaView: File -> Open -> {pvd_file}")
    
    return file_list

def export_static_deformed_states(mesh_base, deform_x, time_points, output_dir, 
                                 deformation_scale=1000.0):
    """
    Esporta stati deformati specifici (es. max deformazione, stati caratteristici)
    
    Args:
        mesh_base: mesh di base
        deform_x: vettore deformazioni
        time_points: lista di tempi specifici da esportare
        output_dir: directory output
        deformation_scale: scala deformazioni
    """
    n_points = mesh_base.n_points
    spostamenti_zero = mesh_base.points.copy()
    
    for t in time_points:
        # Crea mesh per questo stato
        mesh_state = mesh_base.copy()
        
        # Calcola spostamenti
        nuovo_modulo = calcola_modulo_spostamenti(t, deform_x, n_points)
        mesh_state['displacement_magnitude'] = nuovo_modulo
        
        # Applica deformazione
        vect_zero = np.repeat(0, len(nuovo_modulo[:]))
        vec_displacement = np.column_stack([nuovo_modulo, vect_zero, vect_zero])
        mesh_state['displacement_vector'] = vec_displacement
        mesh_state.points = spostamenti_zero + vec_displacement * deformation_scale
        
        # Esporta
        filename = os.path.join(output_dir, f"state_t_{t:.2f}.vtu")
        export_to_vtu(mesh_state, filename)

def export_xdmf_format(mesh, deform_x, time_frame, output_dir):
    """
    Esporta in formato XDMF/HDF5 per dataset molto grandi
    Richiede h5py installato
    
    Args:
        mesh: mesh PyVista
        deform_x: vettore deformazioni
        time_frame: array temporale
        output_dir: directory output
    """
    try:
        import h5py
        
        h5_file = os.path.join(output_dir, "displacement_data.h5")
        xdmf_file = os.path.join(output_dir, "displacement_data.xdmf")
        
        n_points = mesh.n_points
        n_cells = mesh.n_cells
        n_times = len(time_frame)
        
        # Crea file HDF5
        with h5py.File(h5_file, 'w') as hf:
            # Geometria (costante nel tempo)
            hf.create_dataset('geometry', data=mesh.points)
            
            # Topologia (connectivity)
            cells_array = mesh.cells.reshape(-1, 5)[:, 1:]  # Rimuovi il conteggio nodi
            hf.create_dataset('topology', data=cells_array)
            
            # Serie temporale degli spostamenti
            disp_group = hf.create_group('displacements')
            for i, t in enumerate(time_frame[::10]):  # Campiona ogni 10 frame
                step_data = calcola_modulo_spostamenti(t, deform_x, n_points)
                disp_group.create_dataset(f'step_{i:04d}', data=step_data)
            
            # Tempi
            hf.create_dataset('time', data=time_frame[::10])
        
        # Crea file XDMF
        with open(xdmf_file, 'w') as xf:
            xf.write('<?xml version="1.0" ?>\n')
            xf.write('<!DOCTYPE Xdmf SYSTEM "Xdmf.dtd" []>\n')
            xf.write('<Xdmf Version="3.0">\n')
            xf.write('  <Domain>\n')
            xf.write('    <Grid Name="TimeSeries" GridType="Collection" CollectionType="Temporal">\n')
            
            for i, t in enumerate(time_frame[::10]):
                xf.write(f'      <Grid Name="mesh" GridType="Uniform">\n')
                xf.write(f'        <Time Value="{t}"/>\n')
                xf.write(f'        <Topology TopologyType="Quadrilateral" NumberOfElements="{n_cells}">\n')
                xf.write(f'          <DataItem Format="HDF" DataType="Int" Dimensions="{n_cells} 4">\n')
                xf.write(f'            displacement_data.h5:/topology\n')
                xf.write(f'          </DataItem>\n')
                xf.write(f'        </Topology>\n')
                xf.write(f'        <Geometry GeometryType="XYZ">\n')
                xf.write(f'          <DataItem Format="HDF" DataType="Float" Dimensions="{n_points} 3">\n')
                xf.write(f'            displacement_data.h5:/geometry\n')
                xf.write(f'          </DataItem>\n')
                xf.write(f'        </Geometry>\n')
                xf.write(f'        <Attribute Name="displacement" AttributeType="Scalar" Center="Node">\n')
                xf.write(f'          <DataItem Format="HDF" DataType="Float" Dimensions="{n_points}">\n')
                xf.write(f'            displacement_data.h5:/displacements/step_{i:04d}\n')
                xf.write(f'          </DataItem>\n')
                xf.write(f'        </Attribute>\n')
                xf.write(f'      </Grid>\n')
            
            xf.write('    </Grid>\n')
            xf.write('  </Domain>\n')
            xf.write('</Xdmf>\n')
        
        print(f"File XDMF/HDF5 creati: {xdmf_file}, {h5_file}")
        return True
        
    except ImportError:
        print("h5py non installato. Saltando esportazione XDMF/HDF5")
        print("Per abilitare: pip install h5py")
        return False

def validate_export(output_dir):
    """
    Verifica che i file esportati siano validi e leggibili
    
    Args:
        output_dir: directory contenente i file esportati
    
    Returns:
        dict con risultati della validazione
    """
    validation_results = {
        'pvd_file': False,
        'vtu_files': 0,
        'total_size_mb': 0,
        'errors': []
    }
    
    # Verifica file PVD
    pvd_file = os.path.join(output_dir, "displacement_series.pvd")
    if os.path.exists(pvd_file):
        validation_results['pvd_file'] = True
        try:
            # Verifica che sia XML valido
            import xml.etree.ElementTree as ET
            ET.parse(pvd_file)
        except Exception as e:
            validation_results['errors'].append(f"PVD file non valido: {e}")
    
    # Conta e verifica file VTU
    vtu_files = [f for f in os.listdir(output_dir) if f.endswith('.vtu')]
    validation_results['vtu_files'] = len(vtu_files)
    
    # Calcola dimensione totale
    total_size = 0
    for filename in os.listdir(output_dir):
        filepath = os.path.join(output_dir, filename)
        if os.path.isfile(filepath):
            total_size += os.path.getsize(filepath)
    
    validation_results['total_size_mb'] = total_size / (1024 * 1024)
    
    # Test di lettura con PyVista
    if vtu_files:
        test_file = os.path.join(output_dir, vtu_files[0])
        try:
            test_mesh = pv.read(test_file)
            if test_mesh.n_points == 0:
                validation_results['errors'].append("Mesh vuota nel file di test")
        except Exception as e:
            validation_results['errors'].append(f"Errore lettura VTU: {e}")
    
    return validation_results

#############################################################
# MAIN PROCESSING - PARTE ORIGINALE CON MODIFICHE
#############################################################

# Lettura file XML
lines = leggi_xml(file)
lines2 = leggi_xml(file2)
lines3 = leggi_xml(file3)
lines4 = leggi_xml(file4)

righe = len(lines)
righe2 = len(lines2)
righe3 = len(lines3)
righe4 = len(lines4)

skip0 = definizione_skip(righe, lines) + 1
skip1 = definizione_skip(righe2, lines2) + 1
skip2 = definizione_skip(righe3, lines3) + 1
skip3 = definizione_skip(righe4, lines4) + 1

ritaglia_xml(lines, righe, 0)
ritaglia_xml(lines2, righe2, 1)
ritaglia_xml(lines3, righe3, 2)
ritaglia_xml(lines4, righe4, 3)

# Lettura dati pandas
imp_disp = pd.read_csv(file, delim_whitespace=True, header=None, comment='<', skiprows=skip0)
imp_disp2 = pd.read_csv(file2, delim_whitespace=True, header=None, comment='<', skiprows=skip1)
imp_disp3 = pd.read_csv(file3, delim_whitespace=True, header=None, comment='<', skiprows=skip2)
imp_disp4 = pd.read_csv(file4, delim_whitespace=True, header=None, comment='<', skiprows=skip3)

# Definizione nodi
select = "disp_0_metadata.xml"
nodeTag, node_coord = definizione_nodi(select)

select = "disp_1_metadata.xml"
nodeTag2, node_coord2 = definizione_nodi(select)

select = "disp_2_metadata.xml"
nodeTag3, node_coord3 = definizione_nodi(select)

select = "disp_3_metadata.xml"
nodeTag4, node_coord4 = definizione_nodi(select)

# Output processing
[output, n_nodes, n_steps, time_frame, response_rshp, response] = output_disp(imp_disp)
[output2, n_nodes2, n_steps2, time_frame, response_rshp2, response2] = output_disp(imp_disp2)
[output3, n_nodes3, n_steps3, time_frame, response_rshp3, response3] = output_disp(imp_disp3)
[output4, n_nodes4, n_steps4, time_frame, response_rshp4, response4] = output_disp(imp_disp4)

# Costruzione dizionari globali
dict_global_disp = {}
for i in nodeTag:
    dict_global_disp[i] = {
        'x_disp': spostamenti_x_nodo(i, nodeTag, response_rshp, int(n_nodes)),
        'y_disp': spostamenti_y_nodo(i, nodeTag, response_rshp, int(n_nodes))
    }
for i in nodeTag2:
    dict_global_disp[i] = {
        'x_disp': spostamenti_x_nodo(i, nodeTag2, response_rshp2, int(n_nodes2)),
        'y_disp': spostamenti_y_nodo(i, nodeTag2, response_rshp2, int(n_nodes2))
    }
for i in nodeTag3:
    dict_global_disp[i] = {
        'x_disp': spostamenti_x_nodo(i, nodeTag3, response_rshp3, int(n_nodes3)),
        'y_disp': spostamenti_y_nodo(i, nodeTag3, response_rshp3, int(n_nodes3))
    }
for i in nodeTag4:
    dict_global_disp[i] = {
        'x_disp': spostamenti_x_nodo(i, nodeTag4, response_rshp4, int(n_nodes4)),
        'y_disp': spostamenti_y_nodo(i, nodeTag4, response_rshp4, int(n_nodes4))
    }

dict_coord_global = {}
for i in node_coord:
    dict_coord_global[i] = node_coord[i]
for i in node_coord2:
    dict_coord_global[i] = node_coord2[i]
for i in node_coord3:
    dict_coord_global[i] = node_coord3[i]
for i in node_coord4:
    dict_coord_global[i] = node_coord4[i]

# Connectivity e mesh setup
connectivity = OpenSeesTclRead("elements.tcl", "element SSPquadUP", 7)
elemList = connectivity[:, 2]
nodeCoord, nodeList = extract_nodeCoord(dict_coord_global)

# Pulizia memoria
del lines, lines2, lines3, lines4
del imp_disp, imp_disp2, imp_disp3, imp_disp4
del node_coord, node_coord2, node_coord3, node_coord4
del nodeTag, nodeTag2, nodeTag3, nodeTag4
del output, output2, output3, output4
del response, response2, response3, response4
del response_rshp, response_rshp2, response_rshp3, response_rshp4

# Preparazione vettore spostamenti
conv = [i for i in [dict_global_disp[key]['x_disp'] for key in dict_global_disp]]
analisi_len(conv, n_steps)
conv = np.array(conv).reshape(-1, n_steps).T

# Azzera spostamenti fase precedente
first_array = conv[0, :]
conv = conv - first_array

deform_x = np.array(conv).reshape((-1, 1))

#############################################################
# CREAZIONE MESH E ESPORTAZIONE PER PARAVIEW
#############################################################

print("\n" + "="*60)
print("INIZIO ESPORTAZIONE PER PARAVIEW")
print("="*60)

# Crea directory output
create_output_directory(OUTPUT_DIR)

# Crea mesh PyVista
cells = quad_cell(connectivity, nodeList)
cell_type = cell_type_quad(connectivity)
mesh = pv.UnstructuredGrid(cells, cell_type, nodeCoord)
n_points = mesh.n_points

print(f"\nMesh creata:")
print(f"  - Numero di nodi: {n_points}")
print(f"  - Numero di celle: {mesh.n_cells}")
print(f"  - Tipo celle: Quadrilaterali (VTK type 9)")

# 1. ESPORTA MESH NON DEFORMATA (riferimento)
print("\n1. Esportazione mesh non deformata...")
reference_file = os.path.join(OUTPUT_DIR, "mesh_reference.vtu")
mesh_ref = mesh.copy()
mesh_ref['displacement_magnitude'] = np.zeros(n_points)
export_to_vtu(mesh_ref, reference_file)

# Esporta anche in formato legacy VTK per compatibilità
legacy_file = os.path.join(OUTPUT_DIR, "mesh_reference_legacy.vtk")
export_to_legacy_vtk(mesh_ref, legacy_file)

# 2. ESPORTA SERIE TEMPORALE COMPLETA
if EXPORT_TIME_SERIES:
    print("\n2. Esportazione serie temporale...")
    
    # Definisci intervallo temporale da esportare
    # Puoi modificare questi parametri secondo necessità
    t_start = 0.0
    t_end = min(50.0, len(time_frame) * 0.01)  # Limita a 50 secondi o durata max
    sample_rate = 10  # Esporta ogni 10 frame per ridurre dimensione
    
    # Crea subset di time_frame
    time_indices = range(0, min(int(t_end/0.01), len(time_frame)), sample_rate)
    time_subset = [time_frame[i] if i < len(time_frame) else time_frame[-1] 
                   for i in time_indices]
    
    # Esporta serie temporale
    files = export_time_series(
        mesh_base=mesh,
        deform_x=deform_x,
        time_frame=time_frame[:len(time_subset)*sample_rate],
        output_dir=OUTPUT_DIR,
        deformation_scale=DEFORMATION_SCALE,
        sample_rate=sample_rate
    )

# 3. ESPORTA STATI CARATTERISTICI
print("\n3. Esportazione stati caratteristici...")

# Trova tempo di massima deformazione
max_disp_idx = np.argmax(np.abs(deform_x))
max_disp_time = (max_disp_idx // n_points) * 0.01

print(f"  - Tempo di massima deformazione: t = {max_disp_time:.2f} s")

# Esporta stati specifici
characteristic_times = [
    0.0,           # Stato iniziale
    max_disp_time, # Massima deformazione
    25.0,          # Tempo intermedio
    50.0           # Tempo finale
]

# Filtra tempi validi
characteristic_times = [t for t in characteristic_times if t <= len(time_frame)*0.01]

export_static_deformed_states(
    mesh_base=mesh,
    deform_x=deform_x,
    time_points=characteristic_times,
    output_dir=OUTPUT_DIR,
    deformation_scale=DEFORMATION_SCALE
)

# 4. ESPORTA INFORMAZIONI AGGIUNTIVE
print("\n4. Creazione file di informazioni...")

# Crea file info con parametri di visualizzazione
info_file = os.path.join(OUTPUT_DIR, "visualization_info.txt")
with open(info_file, 'w') as f:
    f.write("PARAMETRI DI VISUALIZZAZIONE PARAVIEW\n")
    f.write("="*50 + "\n\n")
    f.write(f"Scala di deformazione applicata: {DEFORMATION_SCALE}\n")
    f.write(f"Numero totale di time steps: {n_steps}\n")
    f.write(f"Passo temporale: 0.01 s\n")
    f.write(f"Durata totale simulazione: {n_steps * 0.01:.2f} s\n")
    f.write(f"Numero di nodi: {n_points}\n")
    f.write(f"Numero di elementi: {mesh.n_cells}\n")
    f.write("\nCAMPI DISPONIBILI:\n")
    f.write("  - displacement_magnitude: modulo dello spostamento (scalare)\n")
    f.write("  - displacement_vector: vettore spostamento 3D\n")
    f.write("\nISTRUZIONI PARAVIEW:\n")
    f.write("1. Aprire il file 'displacement_series.pvd' per la serie temporale\n")
    f.write("2. Usare il filtro 'Warp By Vector' sul campo 'displacement_vector'\n")
    f.write("3. Colorare per 'displacement_magnitude'\n")
    f.write("4. Usare Animation View per controllare l'animazione\n")

print(f"\nFile di informazioni creato: {info_file}")

# 5. CREAZIONE SCRIPT PYTHON PER PARAVIEW
print("\n5. Creazione script Python per ParaView...")

paraview_script = os.path.join(OUTPUT_DIR, "paraview_visualization.py")
with open(paraview_script, 'w') as f:
    f.write("""# Script Python per ParaView
# Eseguire in ParaView: Tools -> Python Shell -> Run Script

from paraview.simple import *

# Carica il file PVD
displacement_series = PVDReader(FileName='displacement_series.pvd')

# Crea vista di rendering
renderView = GetActiveViewOrCreate('RenderView')

# Display dei dati
display = Show(displacement_series, renderView)

# Applica colormap
ColorBy(display, ('POINTS', 'displacement_magnitude'))
display.RescaleTransferFunctionToDataRange(True)

# Seleziona colormap 'jet'
colorMap = GetColorTransferFunction('displacement_magnitude')
colorMap.ApplyPreset('jet', True)

# Mostra color bar
display.SetScalarBarVisibility(renderView, True)

# Aggiungi filtro Warp By Vector (opzionale)
# warpByVector = WarpByVector(Input=displacement_series)
# warpByVector.Vectors = ['POINTS', 'displacement_vector']
# warpByVector.ScaleFactor = 1.0  # Già scalato nell'esportazione

# Display con deformazione
# Show(warpByVector, renderView)
# Hide(displacement_series, renderView)

# Reset camera
renderView.ResetCamera()

# Setup animazione
animationScene = GetAnimationScene()
animationScene.UpdateAnimationUsingDataTimeSteps()

print("Visualizzazione caricata con successo!")
print("Usa i controlli di animazione per navigare nella serie temporale")
""")

print(f"Script ParaView creato: {paraview_script}")

#############################################################
# REPORT FINALE
#############################################################

print("\n" + "="*60)
print("ESPORTAZIONE COMPLETATA CON SUCCESSO!")
print("="*60)
print(f"\nFile creati in: {os.path.abspath(OUTPUT_DIR)}/")
print("\nPer visualizzare in ParaView:")
print("  1. Aprire ParaView")
print("  2. File -> Open -> selezionare 'displacement_series.pvd'")
print("  3. Cliccare Apply")
print("  4. Usare i controlli di animazione per visualizzare la serie temporale")
print("\nFile principali creati:")
print(f"  - displacement_series.pvd: Serie temporale completa")
print(f"  - mesh_reference.vtu: Mesh non deformata di riferimento")
print(f"  - state_t_*.vtu: Stati caratteristici")
print(f"  - paraview_visualization.py: Script di setup automatico")
print("="*60)

#############################################################
# SEZIONE OPZIONALE: VISUALIZZAZIONE INTERATTIVA PYVISTA
#############################################################

# Chiedi all'utente se vuole anche la visualizzazione PyVista
user_choice = input("\nVuoi anche visualizzare con PyVista interattivo? (s/n): ")

if user_choice.lower() == 's':
    print("\n" + "="*60)
    print("VISUALIZZAZIONE INTERATTIVA PYVISTA")
    print("="*60)
    
    # Funzione di callback per aggiornare il plot
    def update(t):
        sargs = dict(interactive=True)
        scala = DEFORMATION_SCALE
        
        # Rimuove tutti gli oggetti dal plotter
        p.remove_actor('mesh') 
        p.remove_actor('label') 
        
        # Calcola il nuovo modulo dei vettori
        nuovo_modulo = calcola_modulo_spostamenti(t, deform_x, n_points)
        
        # Aggiorna i dati della mesh
        mesh_deformata['modulo_spostamenti'] = nuovo_modulo
        
        # Applica deformazione
        vect_zero = np.repeat(0, len(nuovo_modulo[:]))
        vec_sum = np.column_stack([nuovo_modulo, vect_zero, vect_zero])
        mesh_deformata.points = mesh.points + vec_sum * scala
        
        # Aggiungi mesh aggiornata
        p.add_mesh(mesh_deformata, scalar_bar_args=sargs, scalars='modulo_spostamenti',  
                   cmap='jet', opacity=1.0, name='mesh', show_edges=True)
        
        # Mostra assi
        p.show_axes()
        
        # Debug: stampa posizione camera
        camera = p.camera_position
        print(f'Posizione telecamera: {camera}')
    
    # Setup visualizzazione interattiva
    sargs = dict(interactive=False)
    
    # Ricrea mesh per visualizzazione (nel caso sia stata modificata)
    cells_vis = quad_cell(connectivity, nodeList)
    cell_type_vis = cell_type_quad(connectivity)
    mesh_vis = pv.UnstructuredGrid(cells_vis, cell_type_vis, nodeCoord)
    
    # Creare un plotter
    p = pv.Plotter()
    
    # Aggiungere la mesh iniziale con t = 0
    t_init = 0.0
    modulo_spostamenti = calcola_modulo_spostamenti(t_init, deform_x, n_points)
    mesh_vis['modulo_spostamenti'] = modulo_spostamenti
    
    p.add_mesh(mesh_vis, scalar_bar_args=sargs, scalars='modulo_spostamenti', 
               cmap='jet', opacity=1.0, clim=[0.0, 0.03], name='mesh', show_edges=True)
    
    # Creare una copia della mesh per la versione deformata
    mesh_deformata = mesh_vis.copy()
    
    # Aggiungere la mesh deformata iniziale
    p.add_mesh(mesh_deformata, scalar_bar_args=sargs, scalars='modulo_spostamenti', 
               cmap='jet', opacity=1.0, clim=[0.0, 0.03], name='mesh', show_edges=True)
    
    # Durata animazione
    durata = min(50, len(time_frame) * 0.01)
    
    # Aggiungere uno slider per controllare il tempo t
    p.add_slider_widget(
        update,
        rng=[0, durata],
        title="Time (sec)",
        fmt="%.2f",
        style='modern',
        color='black'
    )
    
    # Mostra il plotter
    p.show(cpos='xy')
    
    print("\nVisualizzazione PyVista chiusa.")

print("\n")