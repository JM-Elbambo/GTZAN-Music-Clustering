import os
import re
import pandas as pd
import numpy as np

class DatasetCleaner():

	def clean_csv(input_filepath: str, output_filepath: str):
		"""Outputs a cleaned version of the input file

		Args:
			input_filepath (str): path to the input csv file
			output_filepath (str): path to the output csv file
		"""
		# Load csv file
		df = pd.read_csv(input_filepath)

		# Remove rows with empty values
		df.replace('', np.nan, inplace=True)
		df.dropna(axis=0, inplace=True)

		# Export to csv
		pd.DataFrame.to_csv(df, output_filepath, index=False)
