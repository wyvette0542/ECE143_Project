import numpy as np
import pandas as pd 



def searchByWord(searchFileName = "languages.npy", searchWord = "internship", beginning = 0, end = 12282, saveFileName = "internshipPopularity.npy" ):
	""" this function searches the scraped npy files and builds a database with only the files that contain the given searchWord

	Arguments: 
		searchFileName: str
		searchWord: str
		beginning: int
		end: int
		saveFileName: int

	Returns:
		Does not return, just saves the files as a database

	Raises:
		AssertionError"""

	assert isinstance(searchFileName, str)
	assert isinstance(searchWord, str)
	assert isinstance(beginning, int)
	assert isinstance(end, int)
	assert isinstance(saveFileName, int)

	languages = np.load(searchFileName)

	languagesDict = {lang : 0 for lang in languages}
	for i in range(beginning, end):
		print(i) ## prints location to show progress
		try:
			file = np.load("job_description" + str(i) + ".npy")
			if searchWord in file: 
				for lang in languages:
					if lang in file:
						languagesDict[lang] +=1
		except:
			print("failed to work on file" + str(i))

	# print(languagesDict)
	np.save(saveFileName, languagesDict)
