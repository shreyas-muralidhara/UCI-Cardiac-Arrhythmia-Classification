import xlrd
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

location = ("./Data.xlsx")
wb = xlrd.open_workbook(location) 
sheet = wb.sheet_by_index(0)

nrows = sheet.nrows
ncols = sheet.ncols

datadictionary = {}
for i in range(ncols):
	countnull = 0
	for j in range(nrows):
		if j==0:
			datadictionary[sheet.cell_value(j,i)]=[]
		else:
			if sheet.cell_value(j,i) != "":
				datadictionary[sheet.cell_value(0,i)].append(sheet.cell_value(j,i))
			else:
				countnull+=1
				if countnull>136:
					del datadictionary[sheet.cell_value(0,i)]
					break
				else:
					datadictionary[sheet.cell_value(0,i)].append("Alpha")

classval = datadictionary["class"]
del datadictionary["class"]

for i in datadictionary:
	summ=0
	denom=0
	for j in datadictionary[i]:
		if j != "Alpha":
			summ+=j
			denom+=1

	for j in range(len(datadictionary[i])):
		if datadictionary[i][j]=="Alpha":
			datadictionary[i][j]=summ/denom
count = 0 
b = []
for i in datadictionary:
	a = []
	for j in datadictionary[i]:
		if j not in a:
			a.append(j)

	if len(a)<4:
		b.append(i)
		
for i in b:
	del datadictionary[i]

newdictionary = {}

df = pd.DataFrame(datadictionary)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(df)

y_train = np.array(classval)
print(y_train)
x_trainf, x_test, y_trainf, y_test = train_test_split(x_scaled ,y_train,test_size = 0.2, shuffle = True, stratify = y_train)

x_trainf, x_val, y_trainf, y_val = train_test_split(x_trainf,y_trainf, test_size = 0.2,shuffle = True, stratify = y_trainf)

ncols = x_trainf.shape
print(type(ncols))
pca = PCA(n_components=ncols[1])
x_train_pca = pd.DataFrame(pca.fit_transform(x_trainf))

x_train_pca.to_csv("New.csv")