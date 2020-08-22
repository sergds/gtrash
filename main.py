from googletrans import Translator
from random import choice, randint
import json

def swap_string(str):
	return ''.join([ str[x:x+2][::-1] for x in range(0, len(str), 2) ])

def trashgenerate(text, ntimes):
	i = 0
	langs = ['sl', 'ta', 'la', 'cs', 'ja']
	translator = Translator(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36", proxies={'http': '173.82.17.186:5836', 'http': '173.192.128.238:9999', 'http': '118.69.50.154:80', 'http': '150.129.54.111:6666', 'http': '24.222.59.126:3128'})
	desiredlang = choice(langs)
	try:
		texttmp = translator.translate(text, dest=desiredlang)
		print("trashgenerate(): Translated texttmp to " + texttmp.dest)
	except json.decoder.JSONDecodeError:
		print("Reached google translate daily limit on one of proxies.")
		print("Reinitializing translator.")
		translator = Translator(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36", proxies={'http': '173.82.17.186:5836', 'http': '173.192.128.238:9999', 'http': '118.69.50.154:80', 'http': '150.129.54.111:6666', 'http': '24.222.59.126:3128'})


	i = i + 1
	while i != ntimes:
		desiredlang = choice(langs)
		if desiredlang == texttmp.dest:
			print("trashgenerate(): Don't translate to the same language twice.")
			desiredlang = choice(langs)
		try:
			texttmp = translator.translate(texttmp.text, dest=choice(langs))
		except json.decoder.JSONDecodeError:
			print("Reached google translate daily limit on one of proxies.")
			print("Reinitializing translator.")
			translator = Translator(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36", proxies={'http': '173.82.17.186:5836', 'http': '173.192.128.238:9999', 'http': '118.69.50.154:80', 'http': '150.129.54.111:6666', 'http': '24.222.59.126:3128'})
			continue
		print("trashgenerate(): Translated texttmp to " + texttmp.dest)
		if texttmp.dest == 'ja' and randint(1, 2) == 1:
			print("trashgenerate(): Found japanese text, swapping chars ;)")
			print("Original: " + texttmp.text)
			texttmp.text = swap_string(texttmp.text)
			print("Swapped: " + texttmp.text)
		i = i + 1
	texttmp = translator.translate(texttmp.text, dest='ru')
	return texttmp.text

def maketext(wc):
	i = 0
	text = ''
	text = choice(lines)
	i = i + 1
	while wc != i:
		text = text + ' ' + choice(lines)
		i = i + 1
	return text

print("Loading Words...")
with open("words.txt") as file:
    global lines
    lines = []
    for line in file:
            lines.append(line.strip())

nwords = len(lines)
print("Loaded " + str(nwords) + " words")
print("First loaded word: " + lines[0])

print("Making text...")
txt = maketext(randint(10,25))
print("maketext() result: " + txt)
print("Translating it.(!!Cross your fingers!!)")
ttxt = trashgenerate(txt, randint(5, 10))
print("===================================")
print("Result: " + ttxt)
print("===================================")
