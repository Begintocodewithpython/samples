# EG8-18 File Input

output_file=open('test.txt','w')
output_file.write('line 1\n')
output_file.write('line 2\n')
output_file.close()

input_file=open('test.txt','r')
for line in input_file:
    line=line.strip()
    print(line)
input_file.close()
