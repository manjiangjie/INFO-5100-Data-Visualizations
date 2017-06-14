import nltk
import json
from collections import defaultdict

function_words = ['PRON', 'ADP', 'CONJ', 'DET', 'PRT']
punct = ['!', '.', ',', ':', '"', '?'];

def get_pos():
	l = []
	d_tag = defaultdict(int)

	with open("../data/wordBank.json", "r", encoding="utf-8") as f:
		words = json.load(f)
		print(len(words))
		for i in range(len(words)):
			word = words[i]['word']
			tag = nltk.pos_tag([word])[0][1]
			simplified_tag = nltk.tag.map_tag('en-ptb', 'universal', tag)
			if simplified_tag == 'VERB':
				words[i]['tag'] = 'Predicates'
			elif simplified_tag == 'NOUN':
				words[i]['tag'] = 'Noun'
			elif simplified_tag in function_words:
				words[i]['tag'] = 'Function Words'
			else:
				words[i]['tag'] = 'Others'
			#print(words[i]['tag'])
			d_tag[words[i]['tag']] += 1
			l.append(words[i])

	with open("../data/wordBank_npf_tag.json", "w", encoding="utf-8") as new_f:
		json.dump(l, new_f)
	print(d_tag)


def story_tag(file_path, write_path):
	tag_dict = {}
	with open(file_path, "r", encoding="utf-8") as f:
		txt = f.read()
	words = nltk.tokenize.word_tokenize(txt)
	tags = nltk.pos_tag(words)

	for t in tags:
		if t[0] not in tag_dict:
			simplified_tag = nltk.tag.map_tag('en-ptb', 'universal', t[1])
			if simplified_tag == 'VERB':
				tag_dict[t[0]] = 'Predicates'
			elif simplified_tag == 'NOUN':
				tag_dict[t[0]] = 'Noun'
			elif simplified_tag in function_words:
				tag_dict[t[0]] = 'Function Words'
			elif simplified_tag not in punct:
				tag_dict[t[0]] = 'Others'

	with open(write_path, "w", encoding="utf-8") as new_f:
		json.dump(tag_dict, new_f)


if __name__ == '__main__':
	get_pos()
	story_tag("../data/story.txt", "../data/story_tag.json")
