import sys
import shutil
args = sys.argv
file_name = args[1]
sim_file = args[2]
with open(sim_file, 'r') as sim:
    sim_text = sim.read()
with open(file_name[:-4] + '.sh', 'w') as new_sim:
    new_sim.write(sim_text.replace('the_file_name', file_name[:-4]))
