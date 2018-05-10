import codecs
import os  

def GetText(frname,cnt=0):
	text = ''
	with codecs.open(frname,'r',encoding='GB18030') as fr:
		news = dict()
		while 1:
			lines = fr.readlines(1000)
			if not lines:
				print('end')
				break
			for line in lines:
				if line[:14] == '<contenttitle>':
					cnt+=1
					s = line[14:-16].strip()
					text += s
					text += '\n'
					#print(s)
				if line[:9] == '<content>':
					s = line[9:-11].replace('','').replace('　',' ').strip()
					text += s
					text += '\n'
					text += '\n'
					#print(s)
	return text,cnt
def GetFileNames(filedor):
	filenames = list()
	for root,dirs,files in os.walk(filedor):  
		for file in files:
			if file[-3:]=='txt':
			#print(os.path.join(root,file))
				filenames.append(os.path.join(root,file))
	return filenames
if __name__ == "__main__":	
	frname = "/Users/eason/Git/corenlp-cn/news.sohunews.010801.txt"
	filedor = "/Users/eason/Git/corenlp-cn/"
	print(GetText(frname)[0])