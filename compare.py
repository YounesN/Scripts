import os
cpu_lines = []
gpu_lines = []

with open('cpu.debug') as file:
  lines = file.readlines()
  for line in lines:
    cols = line.split(',')
    cpu_lines.append(cols)

with open('gpu.debug') as file:
  lines = file.readlines()
  for line in lines:
    cols = line.split(',')
    gpu_lines.append(cols)

def compare(n1, n2):
  m1 = len(n1)
  m2 = len(n2)
  length = min(m1, m2, 11)
  for i in range(length):
    if n1[i] != n2[i]:
      return False
  return True

def compare_vector(cpu, gpu):
  total_length = len(cpu)
  array_length = total_length-4
  for i in range(array_length):
    if not compare(cpu[i+4], gpu[i+4]):
      print(cpu[i+4], gpu[i+4], i)
      return False
  return True

for i in range(len(cpu_lines)):
  cpu = cpu_lines[i]
  gpu = gpu_lines[i]
  if cpu[0] == 'double':
    cols = cpu[1].split('/')
    filename = cols[-1]
    if not compare(cpu[3], gpu[3]):
      print(cpu[3], gpu[3])
      print('LINE: ', i, filename, cpu[2])
      quit()
  elif cpu[0] == 'vector|double':
    cols = cpu[2].split('/')
    filename = cols[-1]
    if not compare_vector(cpu, gpu):
      print('LINE: ', i, filename, cpu[3])
      quit()
