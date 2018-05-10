from pycorenlp import StanfordCoreNLP
from pprint import pprint


def GetParser(ip):
	return StanfordCoreNLP(ip)

def Parser(text,nlp):
	return nlp.annotate(text, properties={
		'annotators': 'parse',
		'outputFormat': 'json'
		})


def GetTokens(parsedstr,delimiter=' '):
	tokens = list()
	for sentence in parsedstr['sentences']:
		for token in sentence['tokens']:
			tokens.append(token['word'])
	return delimiter.join(tokens)
if __name__ == "__main__":
	ip = 'http://jaswer.com:8800'
	ss = """“一带一路”（The Belt and Road，缩写B&R）是“丝绸之路经济带”和“21世纪海上丝绸之路”的简称，2013年9月和10月由中国国家主席习近平分别提出建设“新丝绸之路经济带”和“21世纪海上丝绸之路”的合作倡议。 [1]  它将充分依靠中国与有关国家既有的双多边机制，借助既有的、行之有效的区域合作平台，一带一路旨在借用古代丝绸之路的历史符号，高举和平发展的旗帜，积极发展与沿线国家的经济合作伙伴关系，共同打造政治互信、经济融合、文化包容的利益共同体、命运共同体和责任共同体。"""
	nlp = GetParser(ip)
	out = Parser(ss,nlp)
	print(GetTokens(out))