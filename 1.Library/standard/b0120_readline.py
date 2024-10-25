
with open('example.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    line = infile.readline()

    while line:
        outfile.write(line)
        line = infile.readline()

print("File content has been copied from 'example.txt' to 'output.txt'.")
