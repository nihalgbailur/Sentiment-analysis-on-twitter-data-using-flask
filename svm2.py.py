from sklearn import svmimport urllibimport numpy as npimport matplotlib.pyplot as pltimport urllibimport pandasfilename='dataset1.csv'names = ['WC','WPS','Sizltr','Dic','Numerals','harmvirtue','harmvice','fairnessvirtue','fairnessvice','ingroupvirtue','ingrouvice','authorityvirtue','authorityvice','purityvirtue','purityvice','moralitygeneral','AllPct','depression']  data_set=pandas.read_csv(filename,names=names)#print(data_set)#print("Dataset::", data_set['WC'])X=pandas.DataFrame(data_set)#dec=data_set['decision']d=pandas.Series(data_set['depression'])y=pandas.DataFrame(d)#y = column(y, warn=True)del X[data_set.columns[17]]X.columns=[data_set.columns[0],data_set.columns[1],data_set.columns[2],data_set.columns[3],data_set.columns[4],data_set.columns[5],data_set.columns[6],data_set.columns[7],data_set.columns[8],data_set.columns[9],data_set.columns[10],data_set.columns[11],data_set.columns[12],data_set.columns[13],data_set.columns[14],data_set.columns[15],data_set.columns[16]]#print(X)#print(y)C=1.0#svc=svm.SVC(kernel='linear',C=C).fit(X,y.values.ravel())rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y.values.ravel())