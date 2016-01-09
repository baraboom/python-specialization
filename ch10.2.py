name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = 0
hours = {}
for line in handle:
    if line.startswith('From '):
      count += 1
      nline = line.rstrip()
      nline = nline.split()
      nline = nline[5].split(':')
      # print nline[0]
      nline = nline[0]
      hours[nline] = hours.get(nline,0) + 1

# for h in hours:
# for k, v in hours.items():
  
h = hours.items()
h.sort()

for k, v in h:
  print k, v