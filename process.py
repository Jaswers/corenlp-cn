from corenlp import *
from data import *
from tqdm import tqdm


def getLines(frname):
    cnt = 0
    with open(frname, 'r') as fr:
        while 1:
            try:
                lines = fr.readlines(100000)
                if not lines:
                    break
                for line in lines:
                    cnt+=1
            except Exception as e:
                print(e)
    return cnt


def parserText(frname, parser):
    text = ''
    with open(frname, 'r') as fr:
        while 1:
            try:
                lines = fr.readlines(1000000000)
                if not lines:
                    break
                for line in tqdm(lines):
                    if line[0] != '\n':
                        #print('123')
                        out = Parser(line,parser)
                        out = GetTokens(out)
                        #print(out)
                        text += out
            except Exception as e:
                print('opps',e)
                print(line)
                print('opps',e)
    return text




if __name__ == "__main__":
    ip = 'http://mesos-gpu-online008-bjdxt9.cloud.qiyi.domain:31015'
    frname = "/Users/eason/Git/data.txt"
    target = "/Users/eason/Git/extracted_data.txt"
    totalLine = getLines(frname)
    print(totalLine)
    parser = GetParser(ip)
    t = parserText(frname, parser)
    with open(target,'w') as fw:
        fw.write(t)





