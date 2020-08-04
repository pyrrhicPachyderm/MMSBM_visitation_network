#--------------------------------------------------------------------------------------------------
# This script imports output from SA_algorithm.py (which has the best matching of the group labels)
# then reorder the labels of the posteriors of raw mmsbm outputs
#--------------------------------------------------------------------------------------------------

import os
import numpy as np
import sys
import copy
from itertools import combinations
from tqdm import tqdm
import pandas as pd
from collections import OrderedDict

def permute_proba_mat(
	reference = 0,
    	folderin = "../Data/output/raw/proba_mat/",
	folderout = "../Data/output/processed/reordered/proba_mat/",
	rows = 10,
	columns = 10,
	nsamples = 500):

    # read in the best permutations from alignments
    results = np.load('../Data/output/processed/alignments/0proba10gp-10gp.npy')

    for iii in tqdm(range(0, nsamples)):

        # if sampling no == reference, do not permute labels
        if iii==reference:
            continue

        # read in the sample and reshape it in matrix format
        mmat = [x.strip().split() for x in open(folderin+str(iii)+"proba10gp-10gp.dat", "r").readlines()]

        ## select the 1st column and format it
        mmat = np.asarray(mmat)[:,0].reshape((rows,columns)).astype(np.float)

        # extract permuted labels of sample from results
        permuted_labels = results[1:, iii]

        # now reorder sample
        reordered_mat = mmat[permuted_labels[:rows],:] # reorder rows of
        reordered_mat = reordered_mat[:, permuted_labels[rows:]] # reorder columns of proba mat

        # save files as text with each row on a new line
        np.savetxt(folderout+str(iii)+"reordered_proba10gp-10gp.txt", reordered_mat, newline='\r\n')

def permute_user_gp(
    reference = 0,
	folderin = "../Data/output/raw/visitor_gp/",
	folderout = "../Data/output/processed/reordered/visitor_gp/",
	rows = 1000,
	columns = 10,
	nsamples = 500):

    # read in the best permutations from alignments
    results = np.load('../Data/output/processed/alignments/0proba10gp-10gp.npy')

    for iii in tqdm(range(0, nsamples)):
    	#print iii
        if iii==reference:
            continue

        # read in the sample and reshape it in matrix format
        mmat = [x.strip().split() for x in open(folderin+str(iii)+"_visitor_gp10.dat", "r").readlines()]

        # get the user id
        use about the implementation which bits I am missing out.  r_id = np.asarray(mmat)[:,0]
        user_id = list(OrderedDict.fromkeys(user_id))

        ## select the 1st column [contains proba of gp membership]
        mmat = np.asarray(mmat)[:,0].reshape((rows,columns)).astype(np.float)
        
        # extract permuted labels of sample from results
        permuted_labels = results[1:, iii]

        # now reorder sample
        reordered_mat = mmat[:, permuted_labels[:columns]] # reorder columns of proba mat

	np.savetxt(folderout+str(iii)+"reordered_visitorgp10.txt", reordered_mat)

def permute_place_gp(
    reference = 0,
	folderin = "../Data/output/raw/place_gp/",
	folderout = "../Data/output/processed/reordered/place_gp/",
	rows = 10,
	columns = 10,
	nsamples = 500):

    # read in the best permutations from alignments
    results = np.load('../Data/output/processed/alignments/0proba10gp-10gp.npy')

    for iii in tqdm(range(0, nsamples)):

        if iii==reference:
            continue

        # read in the sample and reshape it in matrix format
        mmat = [x.strip().split() for x in open(folderin+str(iii)+"_place_gp10.dat", "r").readlines()]

        # get the place id
        place_id = np.asarray(mmat)[:,0]
        place_id = list(OrderedDict.fromkeys(place_id))

        ## select the 1st column and format it
        mmat = np.asarray(mmat)[:,1].reshape((rows,columns)).astype(np.float)
        print mmat.shape

        # extract permuted labels of sample from results
        permuted_labels = results[1:, iii]
        
        # now reorder sample
        reordered_mat = mmat[:, permuted_labels[-columns:]] # reorder columns of proba mat
        np.savetxt(folderout+str(iii)+"reordered_placegp10.txt", reordered_mat)
