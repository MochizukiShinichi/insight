import DataClass
from os.path import abspath


import argparse
parser = argparse.ArgumentParser(description='specifiy input file names')
parser.add_argument('--InputFile', help='name of input data file', required=True)
args = parser.parse_args()

input_file_name = args.InputFile
dt = DataClass.Data(input_file_name)

dt.generate_tops()
dt.generate_output()