tcl=open("cubotto.tcl","w")
tcl.write("model BasicBuilder -ndm 3 -ndf 4\n")
tcl.write("set pid [getPID]\nset np [getNP]\n")
tcl.close()

tcl = open('cubotto.tcl', 'a')
tcl.write('recorder mpco "cubotto_GL-$pid.mpco" -T dt 0.002 -N "displacement" "velocity" "acceleration" "reactionForce" -E "stress" "strain"\n')
tcl.close()


import os
import math as mm
import time as tt
import openseespy.opensees as ops
import gmsh2opensees as g2o
import numpy as nup
import gmsh

gmsh.initialize()
meshfilename = "colOps.msh"
gmsh.open("colOps.msh")

import openSToolsMP as ot

###### START ########
ops.wipe()
ops.model("basicBuilder","-ndm",3,"-ndf",4)



matTag =  1
rho = 1.932 #Mg/m3
G0 = 52630.58283
#E = 210e9 #Pa
nu = 0.2
E = 2*G0*(1+nu) #kPaù

nd = 3 #dimension

#rho = 7300. # kg/m3

friction = 31.0         #friction angle
phaseTransform = 26.0   #phase transformation angle
G1 = 9.e4
B1 = 22.e4
gamma =    0.600     # Newmark integration parameter
dT =   0.002         # time step for analysis, does not have to be the same as accDt.
numSteps= 20001      # number of time steps
rhoS  =1.80          # saturated mass density
rhoF  =1.00          # fluid mass density
Bfluid =2.2e6        # fluid shear modulus
fluid1 =1            # fluid material tag
solid1 =10           # solid material tag
perm   =1.e-5    #permeability (m/s)
accGravity =9.81  #acceleration of gravity
perm1   =[perm/accGravity/rhoF]    # actual value used in computation
accMul = 2                    # acceleration multiplier
pi = 3.1415926535
inclination = 0
massProportionalDamping   =0.0
InitStiffnessProportionalDamping =0.003
gravityX =[accGravity*nup.sin(inclination/180.0*pi)] # gravity acceleration in X direction
gravityY =0.0                                        # gravity acceleration in Y direction
gravityZ =[accGravity*nup.cos(inclination/180.0*pi)]  # gravity acceleration in Z direction
#############################################################################
ops.nDMaterial('PressureDependMultiYield02', 1, 3, rhoS, G1, B1, friction, 2.5, 80, 0.5, phaseTransform, 0.067, 0.23, 0.06, 0.27)

#############################################################################
tcl=open("cubotto.tcl","a")
tcl.write('nDMaterial PressureDependMultiYield02 1 3 2.45 1.3e5 2.6e5 39 0.1 101.0 0.5 26 0.010 0.0 0.35 0.0 20 5.0 3.0 1.0 0.0 0.47 0.9 0.02 0.7 101.0\n')
tcl.close()
#############################################################################
ot.mDefine()
ot.boundNodesPid0()

print('##################################### DIAF ####################################')
ot.mDiaf()

ops.fix(4, 0, 0, 0,1)
#VOLUME
print('############################### vincolo sulle facce di base ###############################')
ot.mFix()
#X
print('############################### vincolo sulle facce a perpendicolare SX ###############################')
ot.mFix()
print('############################### vincolo sulle facce a perpendicolare DX ###############################')
ot.mFix()
#Y
print('############################### vincolo sulle facce a perpendicolare SY ###############################')
ot.mFix()
print('############################### vincolo sulle facce a perpendicolare DY ###############################')
ot.mFix()

ot.mGenFem20()
[colArea,dashpotCoeff,nodo_mesh]=ot.mDash()
ot.mNodeInfoTxt()
nodeList=ot.mRec()

motionDT = 0.005
#recDT = 10*motionDT
recDT = motionDT

tcl = open('cubotto.tcl', 'a')
tcl.write(f'set motionDT {motionDT}\n')
tcl.close()
#############################################################################
motionSteps = 7990
tcl = open('cubotto.tcl', 'a')
tcl.write(f'set motionSteps  {motionSteps}\n')
tcl.close()
#############################################################################
#############################################################################
tcl = open('cubotto.tcl','a')
tcl.write(f'set nSteps {nSteps}\n')
tcl.write(f'set dT {dT}\n')
tcl.close()
##################################################################
gamma = 1.5
gamma1= 0.5

beta  = (1/4)*(gamma+0.5)**2
beta1 = 0.25

###################### ANALISI STAGE 0 ###########################
tcl = open("cubotto.tcl", "a")
tcl.write("puts 'ANALISI STATICA START'\n")
tcl.write("model BasicBuilder -ndm 3 -ndf 4\n")
tcl.close()

startT = tt.time()
ot.mStage0(gamma1,beta1,a0,a1)
#################################################################
ops.model("basicBuilder", "-ndm", 3, "-ndf", 4)
tcl = open("cubotto.tcl", "a")
tcl.write("model BasicBuilder -ndm 3 -ndf 4\n")
tcl.close()

ops.updateMaterialStage('-material', 1, '-stage', 1)
ops.updateMaterialStage('-material', 2, '-stage', 1)

tcl = open('cubotto.tcl', 'a')
tcl.write('updateMaterialStage -material 1 -stage 1\n')
tcl.write('updateMaterialStage -material 2 -stage 1\n')
tcl.write('domainChange\n')
tcl.close()

print('############################################# REMOVE SX ################################à')
ot.App.mRemoveX(ot.Model)
print('############################################# REMOVE DX ################################à')
ot.App.mRemoveX(ot.Model)
print('############################################## tie nodes facce a perpendicolare x')
ot.mTieNodes()
#############################################################
cFactor = colArea * dashpotCoeff*2
#############################################################
ops.model('basic', '-ndm', 3, '-ndf', 4)
##################### reset time and analysis ####################
ops.setTime(0.0)
ops.wipeAnalysis()
ops.remove('recorders')

tcl = open('cubotto.tcl', 'a')
tcl.write('setTime 0.0\n\
wipeAnalysis\n\
remove recorders\n')
tcl.write('set recDT $motionDT\n')
tcl.close()

######################## define velocity time history file
velocityFile = 'yerbaNSvelocity';
data_gm = nup.loadtxt('yerbaNSvelocity.out')
ops.timeSeries('Path', 2, '-dt', motionDT, '-filePath', velocityFile +'.out', '-factor', cFactor)
ops.pattern('Plain', 10, 2)
ops.load(nodo_mesh, 0.5,0.0, 0.0, 0.0)


################################## modificare per associare accelerazione #######################
tcl = open('cubotto.tcl', 'a')
tcl.write('set velocityFile veloma2000.out\n')
tcl.write(f'set timeSeries "Path 2 -dt {motionDT} -filePath $velocityFile -factor {cFactor}"\n')
tcl.write('pattern Plain 10 $timeSeries'+' {\n')
tcl.close()
################################################################################

m = ot.Model()
proc_dict = m.mDict()
procId = ot.trova_nodo(proc_dict,int(nodo_mesh))
for proc in procId:
    
    tcl = open('cubotto.tcl','a')
    tcl.write("if {"+f' $pid == {proc}'+'}'+' {\n')
    tcl.write(f'    load {nodo_mesh} 0.5 0.0 0.0 0.0\n')
    tcl.write("}}\n")
    tcl.close()
    
    
print("Dynamic loading created...")

ops.constraints('Penalty', 1.0E16, 1.0E16)
ops.test('NormDispIncr', 1e-3, 100, 1)
ops.algorithm('ModifiedNewton')
ops.numberer('RCM')
ops.system('UmfPack')
ops.integrator('Newmark', gamma1, beta1)
ops.rayleigh(a0, a1, 0.0, 0.0)
ops.analysis('Transient')
#############################################################################
#############################################################################
tcl = open('cubotto.tcl', 'a')
tcl.write('puts "ANALISI DINAMICA START"\n')
tcl.write(f'constraints Penalty 1.0E16 1.0E16\n\
test NormDispIncr 1e-3 100 1\n\
algorithm ModifiedNewton\n\
numberer ParallelPlain\n\
system Mumps -ICNTL14 200\n\
integrator Newmark {gamma1} {beta1}\n\
rayleigh {a0} {a1} 0.0 0.0\n\
analysis Transient\n\
analyze 7990 0.005\n')
tcl.close()

tcl = open('cubotto.tcl','a')
tcl.write('puts "Finished with dynamic analysis..."\n\
    wipe')
tcl.close()

print("Finished with dynamic analysis...")
ops.wipe()
