
def read_file(filename):
	chat = []
	with open(filename, 'r' ,encoding = 'utf-8-sig') as f:  #utf-8後的sig 是去除掉輸出時第一行前端的幾個編碼字母
		for p in f:
			chat.append(p.strip())
	return chat
def convert(lines):
	convert = []
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		convert.append(person + ':' + line+'\n')
	print(convert)
	return convert

def write_file(filename,ret):
	new = []
	with open(filename, 'w' ,encoding = 'utf-8') as f:
		for i in ret:
			new =f.write(i)
		return new

def main():
	lines = read_file('input.txt')
	w = convert(lines)
	write_file('output.txt',w)

main()

#write_file()