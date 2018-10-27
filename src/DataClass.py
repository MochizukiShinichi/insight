# - *- coding: utf- 8 - *-
import csv
import re
from os.path import abspath

class Data:
    """
     Data structure to hold and process input *.txt data

     parameters:    
     ----------
     file_path: string, the path of .csv file that holds input data
    
     methods:
        ----------
        statistics methods
        ----------
            generate_tops(self):
                calcuate top occupation/state with top certified applications
                --rtype: None

        ----------
        output methods
        ----------
            generate_output_csv(self):
                generating output *.csv file to output folder
                -- default file name for top occupations: "top_10_occupations.txt"
                -- default file name for top state: "top_10_states.txt"
                --rtype: None
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.top_job = []
        self.top_state = []

    def generate_tops(self):
        """ method to read csv file and generate top_job and top_state
            --rtype: None
        """
        with open(abspath('.') + self.file_path, newline='', encoding='utf_8') as file:
            # find indices correponds to column names
            try:
                names = file.readline().upper().split(';')
                job_name_index = [i for i, name in enumerate(names) if re.search('SOC_NAME',name) != None][0]
                status_index = [i for i, name in enumerate(names) if re.search('STATUS',name) != None][0]
                state_index = [i for i, name in enumerate(names) if re.search('WORKSITE_STATE',name) != None][0]
            except:
                raise NameError('One or more necessary columns cannot be found in the input file')

            top_job = {}
            top_state = {}
          
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[status_index] == 'CERTIFIED':
                    top_job[row[job_name_index]] = 1 + top_job.get(row[job_name_index], 0) 
                    top_state[row[state_index]] = 1 + top_state.get(row[state_index], 0)

            # sort job and state by number and name
            self.top_job = [[job, top_job[job]] for job in sorted(top_job, key=lambda key: (-top_job.get(key), key)) if job != '']
            self.top_state = [[state, top_state[state]] for state in sorted(top_state, key=lambda key: (-top_state.get(key), key)) if state != '']
        
    def generate_output(self):
        """method to output top results to txt files in output folder
            -- rtype: None
        """
        job_cnt = len(self.top_job)
        state_cnt = len(self.top_state)

        if job_cnt == 0:
            raise Exception('zero job categories in the input')
        else:    
            with open(abspath('.') + "/output/top_10_occupations.txt", 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'])

                job_sum = sum([cnt[1] for cnt in self.top_job[:min(10, job_cnt)]])
                for entry in self.top_job[:min(10, job_cnt)]:
                    writer.writerow([entry[0], entry[1], "{:.1%}".format(entry[1]/job_sum)])
          
        if state_cnt == 0:
            raise Exception('zero state categories in the input')         
        else:
            with open(abspath('.') + "/output/top_10_states.txt", 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'])

                state_sum = sum([cnt[1] for cnt in self.top_state[:min(10, state_cnt)]])
                for entry in self.top_state[:min(10, state_cnt)]:
                    writer.writerow([entry[0], entry[1], "{:.1%}".format(entry[1]/state_sum)])