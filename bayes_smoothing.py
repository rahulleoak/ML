import pandas as pd


data=pd.read_csv('bayesdata.csv', header=None,delimiter=',')

del data[0]
r,c = data.shape

ones= (data[c]==1).sum()
zeros = (data[c]==0).sum()

prior_prob=list()
prior_prob.append(ones/(ones+zeros))
prior_prob.append(zeros/(ones+zeros))

O=list()
vals=dict()
yes_count=dict()
no_count=dict()
flag=0
for i in range(1,c):
        l=data[i].unique()
#Counting the yes and no in output column
        for j in l:
             temp=data.loc[data[i]==j]
             yes_count[j]=(temp[c] == 1).sum() 
             no_count[j]=(temp[c] == 0).sum()
#Checking for Zero entries
        for k in l:
            if(yes_count[k] == 0):
                flag=1
            if(no_count[k] == 0):
                flag=2
#Updating the yes and no counts
        if(flag!=0):        
            for j in l:
                 if flag==1:
                     yes_count[j]=yes_count[j]+(1/len(l))
                 if flag ==2:
                     no_count[j]=no_count[j]+(1/len(l))
# Updating Probabilites
        for k in l:
            if flag == 1:
                vals[k]=list([yes_count[k]/(ones+1),no_count[k]/zeros])
            elif flag == 2:
                vals[k]=list([yes_count[k]/(ones),no_count[k]/(zeros+1)])
            else:
                vals[k]=list([yes_count[k]/(ones),no_count[k]/zeros])
        O.append(vals)           
        flag=0
        vals={}
        yes_count={}
        no_count={}


# Testing the model
test=['R','HO','N','W']
num1=prior_prob[0]
den1=prior_prob[1]

for i in range(len(test)):
    num1*=O[i][test[i]][0]
    den1*=O[i][test[i]][1]
print("Prediction for ", test)
print('Yes:',num1/(den1+num1))




