# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:48:03 2020

@author: narul
"""
import numpy as np
import sys
import time
formatted_train_input=sys.argv[1]
formatted_validation_input=sys.argv[2]
formatted_test_input=sys.argv[3]
dict_input=sys.argv[4]
train_out=sys.argv[5]
test_out=sys.argv[6]
metrics=sys.argv[7]
num_epoch=int(sys.argv[8])
train_out=open(train_out, 'w')
test_out=open(test_out, 'w')
metrics=open(metrics, 'w')

#def sparse_dot(x,w):
 #   product=0
  #  a=[]
   # for i,v in w.items():
    #    if (i not in x) or v==0:
     #       continue
        
            
      #  product+=v
       # a.append(i)
    #return product
def sparse_dot(x,w):
    product=0
    #a=[]
    for i in x:
        #if (i not in x) or v==0:
         #   continue
        if w[i]!=0:
            product+=w[i]
           
            
        
        #a.append(i)
    return product


def sigma(x):
    s=1/(1+np.exp(-x))
    return s

#def gradient_i(x,w,y):
 #   grad={}
  #  a=((sigma(sparse_dot(x,w))-y))
   # for j in (w):
    #    if j in x:
     #       grad[j]=a
            
        
      #  else:
            
       #     grad[j]=0
    #return grad

def sgd(x,w,y,gamma):
    
    #grad=gradient_i(x,w,y)
    grad={}
    a=((sigma(sparse_dot(x,w))-y))
    for i in w:
        
        
       if i in x:
            grad[i]=a
            
        
       
       
          
            w[i]=w[i]-gamma*grad[i]
        
    return w
        
        
def predict(x,w,i):
    output=sparse_dot(x[i],w)
    s=sigma(output)
    if s>=0.5:
        return 1
    else:
        return 0
    
    
    
#def SGD(data, weight):
 #   dot=dot_product()
    



starttime=time.time()
dictionary={}
for line in open(dict_input,'r'):
    line2=line.split()
    dictionary[line2[0]]=line2[1]
#print(dictionary)
    
#testdata    
model1=[]


for line in open(formatted_train_input, 'rt'):
        line2=line.split()
        model1.append(line2)
c=[]       
true_values=[]
for i in range(len(model1)):
     j=(model1[i][0].split(":"))
     true_values.append(int(j[0]))
  
#print(true_values)  
for  i in range(len(model1)):

        model1[i].pop(0)
        
#print(model1[0])       
#true_values

for i in range(len(model1)):
    
    dict={}
    
    for j in model1[i]:
        
        d=j.split(":")
        dict[int(d[0])]=1
        
    c.append(dict)
# c  is the feature vector
    # a list of dictionaries

#biasterm

for i in range(len(c)):
    c[i][39176]=1
    
middletime=time.time()

w={}
#initializeweights
for i in range(len(dictionary)+1):
    w[i]=0

epoch=num_epoch
for j in range(epoch):
 print(j)   
 for i in range(len(c)):
       
    w=sgd(c[i],w,true_values[i], 0.1)
   
        

#for i in range(epoch):
 #sgd(c,w,true_values,0.1,i)  

print(w)
a=[]

#train_error
for i in range(len(c)):
   g=predict(c,w,i)
   a.append(g)
   train_out.write(str(g))
   train_out.write("\n")
   
#testdata
   
model1=[]


for line in open(formatted_test_input, 'rt'):
        line2=line.split()
        model1.append(line2)
test=[]       
true_values_test=[]
for i in range(len(model1)):
     j=(model1[i][0].split(":"))
     true_values_test.append(int(j[0]))
  
#print(true_values)  
for  i in range(len(model1)):

        model1[i].pop(0)
        
#print(model1[0])       
#true_values

for i in range(len(model1)):
    
    dict={}
    
    for j in model1[i]:
        
        d=j.split(":")
        dict[int(d[0])]=1
        
    test.append(dict)
# c  is the feature vector
    # a list of dictionaries


#biasterm

for i in range(len(test)):
    test[i][39176]=1


b=[]
for i in range(len(test)):
   g=predict(test,w,i)
   b.append(g)
   test_out.write(str(g))
   test_out.write("\n")
   
           
   
#print(c[0])
#print(a)
#print((sparse_dot(c[50],w)))  
#print(true_values)
#print(a)
test_error, train_error=0,0
for j in range(len(a)):
    if a[j]!=true_values[j]:
        train_error+=1
mean_error_train=train_error/len(c)

for j in range(len(b)):
    if b[j]!=true_values_test[j]:
        test_error+=1
mean_error_test=test_error/len(test)


metrics.write("error(train): ")
metrics.write(str(mean_error_train))
metrics.write("\n")


metrics.write("error(test): ")
metrics.write(str(mean_error_test))
metrics.write("\n")

endtime=time.time()
print(endtime-starttime)
print(middletime-starttime)