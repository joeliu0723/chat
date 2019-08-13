
def read_file(filename):
	chat = []
	with open(filename, 'r' ,encoding = 'utf-8-sig') as f:  #utf-8後的sig 是去除掉輸出時第一行前端的幾個編碼字母
		for p in f:
			chat.append(p.strip())
	return chat
def convert(lines):
	convert = []
	person = None #預設person值為無,避免第一行不是人名造成當機的狀況
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:   #檢查person是否有值,有的話才跑加入清單的程式碼,避免當掉
			convert.append(person + ': ' + line+'\n')
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