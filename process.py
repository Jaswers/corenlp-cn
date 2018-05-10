from corenlp import *
from data import *
from tqdm import tqdm

filedor = "/Users/eason/Git/corenlp-cn/"
target = "/Users/eason/Git/corenlp-cn/processed.txt"
finText = ''
cnt = 0
names = GetFileNames(filedor)
for name in tqdm(names):
	text,cnt = GetText(name,cnt)
	finText += text
	print(name,cnt)
print("total",cnt)
with open(target,'w') as fw:
	fw.write(finText)
	
