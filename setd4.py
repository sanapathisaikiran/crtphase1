janasena={"og","sai","kalki","pushpa"}
janasena.add("devara")
#add value
print(janasena)
janasena.update(["saripodha","senivaram","kanguva"])
print(janasena)
janasena.discard("sai")
print(janasena)
janasena.remove("pushpa")
print(janasena)
tdp={"familystar","gaami"}
bjp=janasena.union(tdp)
print(bjp)