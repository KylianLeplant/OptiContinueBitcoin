def f(x=1,y=1):
    return x+y

def g(y=1, **kwargs):
    return f(y=y, **kwargs)

print(g(x=2))



##test de la fonction LireDonnees
#RawData, RawC = LireDonnees(os.path.join(os.getcwd(), "Data", "Cotations2020.csv"))
#print("DataRaw =", RawData)
#print("\n\n\nRawC =", RawC)
#
##test de la fonction CreerData
#RawData, RawC = LireDonnees(os.path.join(os.getcwd(), "Data", "Cotations2020.csv"))
#D,C = CreerData(RawData,RawC,5)
#print("D =", D)
#print("C =", C)