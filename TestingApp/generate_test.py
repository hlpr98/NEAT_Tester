import subprocess

subprocess.run(['cp', './TestingApp/TriangleApp.py', './Test_Generator/TriangleApp.py'])
subprocess.run(['python', './Test_Generator/pmt.py', '-n', str(5), '-s', str(2), 'TriangleApp', '-o', './tmp/testing'])
subprocess.run(['rm', './Test_Generator/TriangleApp.py'])
