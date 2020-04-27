import sys
import numpy as np
import argparse

def Inferring_Peptide_from_Full_Spectrum(lens):
	mass = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259,
	"F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406,
	"K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
	"P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,
	"T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}
	diff = np.diff(sorted(lens[1:]))
	print(diff)
	l = int((len(lens[1:])-2)/2)
	ans = []
	i = 0
	m = 0
	while i != len(diff):
		m += diff[i]
		if round(m,2) in list(map(lambda x: round(x,2), list(mass.values()))):
			for k, v in mass.items():
				if  round(m,2) == round(v,2):
					ans.append(k)
					break
			i += 1
			m = 0
		else:
			i += 1

	return(''.join(ans)[:l])

def main(args):
	
		with open(args.input, 'r') as r:
			lens = list(map(lambda x: float(x.rstrip('\n')), r.readlines()))
		print(Inferring_Peptide_from_Full_Spectrum(lens))
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(
	formatter_class=argparse.ArgumentDefaultsHelpFormatter)    
	parser.add_argument('-input', type=str,help='path to input file')
	args = parser.parse_args()
	main(args)

