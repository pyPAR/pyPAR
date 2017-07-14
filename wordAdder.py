import re
import words
#working with words
#TEST
lugat=words.lugat
idsa=words.idsa
def set(arg, ida):
	if len(arg)==0:
		word=raw_input("Yangi so'zni kiriting !!!    ")
	else:
		word=arg.lower()
	ids=ida+1
	typ=raw_input("So'z tipini kiriting !!!   ")
	cr=int(raw_input("So'zga kayfiyat jihatdan baho bering.         "))
	lg=lugat
	lg[word[0]][word]=[word, ids, typ, cr]
	fil=open("words.py", "w")
	fil.write("lugat="+str(lg))
	fil.write("\nidsa="+str(ids))
	fil.close()
	print "words bazaga qushildi !!!"
	get(ids)

def que(arg, idsss):
	ans=raw_input("y/n ?")
	if ans=="y":
		set(arg, idsss)
	else:
		get(idsss)

def getall(arg, idssj):
	arg.lower()
	wor=re.split("\W", arg)
	for j in wor:
		try:
			print words.lugat[j[0]][j][0]
			print words.lugat[j[0]][j][1]
			print words.lugat[j[0]][j][2]
		except KeyError:
			print "Kechirasiz "+j+" so'zini tushunmayman !!!\nXohlasanggiz urgatishinggiz mumkin!!!\nXohlaysizmi !?"
			que(j, idssj)
		except IndexError:
			print "Kechirasiz lekin men son va simvollarni tushinmayman hozircha !!!\nUzr !!\n"
			get(idssj)
	
def get(idss):
	word=raw_input("suz kiriting !!!     ")
	if idss>0:
		getall(word, idss)
		get(idss)
	else:
		getall(word, idsa)
		get(idsa)

get(0)
