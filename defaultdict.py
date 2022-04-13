from collections import defaultdict
dick=defaultdict(set)
dick['a'].add("90")
print(dick)
def notdefined():
    return 9083
ano=defaultdict(notdefined)# bracket should not present here
print(ano[1])
print(ano[1])
print(ano[1])
print(ano[1])
print(ano[1])
print(ano[1])

ano_2=defaultdict(bool)
ano_2['A']=True
print(ano_2['A'])