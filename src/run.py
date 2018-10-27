import DataClass

# argument parser for command-line input, currently specifying only input file name
import argparse
parser = argparse.ArgumentParser(description='specifiy input file names')
parser.add_argument('--InputFile', help='name of input data file', required=True)
args = parser.parse_args()
input_file_name = args.InputFile

# input_file_name = '/input/H1B_FY_2016.csv'
# run data class to generate output
dt = DataClass.Data(input_file_name)
dt.generate_tops()
dt.generate_output()