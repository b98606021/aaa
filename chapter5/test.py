with open('james.txt') as jaf:
	data = jaf.readline()
# strip()->刪除字串中不需要的空白符號,
# split()->()內的符號來分隔赴值
james = data.strip().split(',')

with open('julie.txt') as juf:
	date = juf.readline()
julie = data.strip().split(',')

with open('sarah.txt') as saf:
	date = saf.readline()
sarah = data.strip().split(',')

with open('mikey.txt') as mif:
	date = mif.readline()
mikey = data.strip().split(',')


print(james)
print(julie)
print(sarah)
print(mikey)