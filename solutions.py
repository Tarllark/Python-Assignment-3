###############################################
#
# Title:	solutions.py
#
# Descr:	Solutions to assignment 3 problems
#
# Author:	Tarllark
#
# Team:		Successful Story
#
###############################################



import numpy as np

#Solution for problem 2:
def getArrayFromCSV(file):
	data = np.genfromtxt(file, delimiter=',', dtype=np.uint, skip_header=1)
	
	return data

#Solution for problem 3:
def getEnglishSpeakers(file):
    dataset = getArrayFromCSV(file)
    english = [5390, 5514, 5314, 5352, 5309, 5502, 5303, 5305, 5526, 5345, 5339, 5308, 5142, 5625, 5347, 5311, 5374, 5170]
    nonEnglish = np.unique(dataset[:,3])
    for code in english:
        exist = np.where(nonEnglish[nonEnglish == code])
        if(nonEnglish[exist] == code):
            np.delete(nonEnglish, exist)
    dMask = (dataset[:,0] == 2015)
    EnglishSpeakers = np.array([np.sum(dataset[dMask & (dataset[:,3] == c_code)][:,4]) for c_code in english]).sum()
    Others = np.array([np.sum(dataset[dMask & (dataset[:,3] == c_code)][:,4]) for c_code in nonEnglish]).sum()
    res = (EnglishSpeakers, Others)
    return res

#Solution for problem 4:
def getFilteredDataset(originDataset, mask):
    dataset = originDataset[(mask)]
    return dataset

#Solution for problem 5:
def getSpecificData(originDataset, data, value):
    switcher = {
         0: (originDataset[:,0] == value), # Year
         1: (originDataset[:,1] == value), # Area
         2: (originDataset[:,2] == value), # Age
         3: (originDataset[:,3] == value), # Nationality
    }
    return np.sum(originDataset[switcher.get(data)][:,4])