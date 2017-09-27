# EG8-18 File Input

output_file=open('test.txt','a')
output_file.write('line 1\n')
output_file.write('line 2\n')
output_file.close()

input_file=open('test.txt','r')
total_file=input_file.read()
print(total_file)
input_file.close()

