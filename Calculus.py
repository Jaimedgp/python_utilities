import sys
sys.path.insert(0, '/home/jaimedgp/J_Graphics_P/')
import OpenScript as op
from math import sqrt, sin, cos

def gratingParameter():

	table, index = op.Open_file_CSV('/home/jaimedgp/Dropbox/VerbTeX/Exp_Optics/Diffraction/dParameter.csv')

	MedR = sum(table[index[3]])/6 # Media del angulo en radianes
	MedG = sum(table[index[2]])/6 # Media del angulo en grados
	MedD = sum(table[index[4]])/6  # Media del parametro de malla

	xxxxx = 0
	for i in table[index[3]]:
		xxxxx += (i-MedR)**2
	varTtaR = xxxxx/5

	varMedTtaR = varTtaR/6

	MedDTta = 480/(2*sin(MedR))
	varDMed = sqrt(((480*cos(MedR)/(2*sin(MedR)**2))**2)*varMedTtaR)

	return MedDTta, varDMed

#######################################################################################################

def unknowWaveLength(MedD, varD):

	table, index = op.Open_file_CSV('/home/jaimedgp/Dropbox/VerbTeX/Exp_Optics/Diffraction/unKnowWL.csv')

	MedR = sum(table[index[3]])/6 # Media del angulo en radianes
	MedG = sum(table[index[2]])/6 # Media del angulo en grados


	xxxxx = 0
	for i in table[index[3]]:
		xxxxx += (i-MedR)**2
	varTtaR = xxxxx/5

	varMedTtaR = varTtaR/6

	MedWL = 2*MedD*sin(MedR)
	varMedWL = sqrt(( 2*sin(MedR)*varD )**2+( ((2*MedD*cos(MedR))**2)*varMedTtaR))

	return MedWL, varMedWL


MedDTta, varDMed = gratingParameter()

print (MedDTta, varDMed)

print unknowWaveLength(MedDTta, varDMed)
