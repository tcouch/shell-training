#!/usr/bin/python

import sys, csv

filea = sys.argv[1]
fileb = sys.argv[2]

def get_data(filename):
	with open(filename,'rb') as f:
		reader = csv.reader(f)
		data = list(reader)[0]
		data = [float(x) for x in data]
	return data

def scale_a():
	a_data[:]=[x/100 for x in a_data]
	return

def scale_b():
	b_data[:]=[(x+5)/10 for x in b_data]
	return

a_data = get_data(filea)
scale_a()
b_data = get_data(fileb)
scale_b()

a_avg = sum(a_data)/len(a_data)
b_avg = sum(b_data)/len(b_data)

score = a_avg - 0.8*b_avg

print score, " ", filea, " ", fileb
