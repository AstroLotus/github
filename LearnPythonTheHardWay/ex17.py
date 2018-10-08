from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")
#indata = open(from_file).read() #combined one line, org 2

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#print("Alright, all done.")

print(f"Copying from {from_file} to {to_file}", f"The input file is {len(open(from_file).read())} bytes long.")
open(to_file,'w').write(open(from_file).read())
print("Alright, all done!")
#yahoo!you are so smart!
