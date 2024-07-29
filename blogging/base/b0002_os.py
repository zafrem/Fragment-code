import os

# get os environ
print(os.environ['PATH'])

# get current path
print(os.getcwd())

# get upper path
os.chdir('..//')
print(os.getcwd())

# get current folder list
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.listdir())

# Create and Delete file folder
if not os.path.isdir('temp'):
    os.mkdir('temp')
print(os.listdir())
os.chdir('./temp')
print(os.getcwd())
os.chdir('..//')
print(os.getcwd())
os.removedirs('temp')
print(os.listdir())

# Only current fold name without path
curr_path = os.path.dirname(os.path.abspath(__file__))
print(os.path.basename(curr_path))

# Current fold path
print(os.path.dirname(curr_path))

# Split Path + Current Fold
print(os.path.split(curr_path))

# Check exist path
print(os.path.exists(curr_path))