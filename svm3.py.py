from sklearn import svm
import urllib
import numpy as np
import matplotlib.pyplot as plt
import pandas

filename = 'dataset1.csv'

names = ['WC','WPS','Sizltr','Dic','Numerals','harmvirtue','harmvice','fairnessvirtue','fairnessvice','ingroupvirtue','ingrouvice','authorityvirtue','authorityvice','purityvirtue','purityvice','moralitygeneral','AllPct','depression']  

data_set=pandas.read_csv(filename,names=names)

#print(data_set)

#print("Dataset::", data_set['WC'])

X=pandas.DataFrame(data_set)

#dec=data_set['decision']

d=pandas.Series(data_set['depression'])

y=pandas.DataFrame(d)

#y = column(y, warn=True)

del X[data_set.columns[17]]

X.columns=[data_set.columns[0],data_set.columns[1],data_set.columns[2],data_set.columns[3],data_set.columns[4],data_set.columns[5],data_set.columns[6],data_set.columns[7],data_set.columns[8],data_set.columns[9],data_set.columns[10],data_set.columns[11],data_set.columns[12],data_set.columns[13],data_set.columns[14],data_set.columns[15],data_set.columns[16]]

#print(X)

#print(y)

C=1.0

#svc=svm.SVC(kernel='linear',C=C).fit(X,y.values.ravel())

#lin_svc = svm.LinearSVC(C=C).fit(X, y.values.ravel())

rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y.values.ravel())

h=0.2

  # step size in the mesh



# create a mesh to plot in

x_min, x_max = 0, 17

y_min, y_max = 0, 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, h),

	                     np.arange(y_min, y_max, h))

# title for the plots

titles = ['SVC with linear kernel',

	   'LinearSVC (linear kernel)',

	    'SVC with RBF kernel',

	    'SVC with polynomial (degree 3) kernel']





#for i, clf in enumerate((rbf_svc)):

	 # Plot the decision boundary. For that, we will assign a color to each

	 # point in the mesh [x_min, x_max]x[y_min, y_max].

plt.subplot(2, 2, rbf_svc)

plt.subplots_adjust(wspace=0.4, hspace=0.4)

         

	 #Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])



	 # Put the result into a color plot

	 #Z = Z.reshape(xx.shape)

	 #plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)



	 # Plot also the training points

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)

plt.xlabel('Sepal length')

plt.ylabel('Sepal width')

plt.xlim(xx.min(), xx.max())

plt.ylim(yy.min(), yy.max())

plt.xticks(())

plt.yticks(())

plt.title(titles[i])



plt.show()

