# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:20:22 2020

@author: narul
"""

import numpy as np
import sys
train_file=sys.argv[1]
validation_file=sys.argv[2]
dict_input=sys.argv[4]
test_file=sys.argv[3]
formatted_train_out=sys.argv[5]
formatted_validation_out=sys.argv[6]
formatted_test_out=sys.argv[7]
feature_flag=int(sys.argv[8])

dictionary={}


    


train_file=open(train_file, 'r')
validation_file=open(validation_file, 'r')
test_file=open(test_file,'r')
formatted_train_out=open(formatted_train_out, 'w')
formatted_validation_out=open(formatted_validation_out, 'w')
formatted_test_out=open(formatted_test_out, 'w')
for line in open(dict_input,'r'):
    line2=line.split()
    dictionary[line2[0]]=line2[1]
    


if feature_flag==1:

#trainfile
    redict=[]




          
    reviews=[]
    for line in train_file:
        line2=line.split()
        reviews.append(line2)

    k=0
    while k<len(reviews):
        red={}
        j=0
        while j<len(reviews[k]):
        
           red[reviews[k][j]]=0
           j+=1
        redict.append(red)
        k+=1

    k=0    
    while k<len(redict):
       for i in redict[k]:
          if i in dictionary:
            redict[k][i]=int(dictionary[i])+1
           
       k+=1        

         

   
#model1
    for t in range(len(redict)):
    
        formatted_train_out.write(list(redict[t])[0])
        formatted_train_out.write('\t')
        for j in (redict[t]):
            if redict[t][j]!=0:
                formatted_train_out.write(str(redict[t][j]-1))
                formatted_train_out.write(":1")
                formatted_train_out.write("\t")
        formatted_train_out.write("\n")        
                
#validationfile
    redict=[]




          
    reviews=[]
    for line in validation_file:
        line2=line.split()
        reviews.append(line2)

    k=0
    while k<len(reviews):
        red={}
        j=0
        while j<len(reviews[k]):
        
           red[reviews[k][j]]=0
           j+=1
        redict.append(red)
        k+=1

    k=0    
    while k<len(redict):
       for i in redict[k]:
          if i in dictionary:
            redict[k][i]=int(dictionary[i])+1
           
       k+=1        

         


#model1
    for t in range(len(redict)):
    
        formatted_validation_out.write(list(redict[t])[0])
        formatted_validation_out.write('\t')
        for j in (redict[t]):
            if redict[t][j]!=0:
                formatted_validation_out.write(str(redict[t][j]-1))
                formatted_validation_out.write(":1")
                formatted_validation_out.write("\t")
        formatted_validation_out.write("\n")            
        
        
#testfile
    redict=[]




          
    reviews=[]
    for line in test_file:
        line2=line.split()
        reviews.append(line2)

    k=0
    while k<len(reviews):
        red={}
        j=0
        while j<len(reviews[k]):
        
           red[reviews[k][j]]=0
           j+=1
        redict.append(red)
        k+=1

    k=0    
    while k<len(redict):
       for i in redict[k]:
          if i in dictionary:
            redict[k][i]=int(dictionary[i])+1
           
       k+=1        

         


#model1
    for t in range(len(redict)):
    
        formatted_test_out.write(list(redict[t])[0])
        formatted_test_out.write('\t')
        for j in (redict[t]):
            if redict[t][j]!=0:
                formatted_test_out.write(str(redict[t][j]-1))
                formatted_test_out.write(":1")
                formatted_test_out.write("\t")
        formatted_test_out.write("\n")            
            

        
        
#model2
else:
        
#trainfile
     b=[]
     reviews=[]
     for line in train_file:
        line2=line.split()
        reviews.append(line2)

     for k in range(len(reviews)):
       a=[]
       for j in range(len(reviews[k])):
        
         if reviews[k][j] in dictionary:
            a.append(reviews[k][j])
       if a!=[]:        
         b.append(a)
    
     

     trim=4

     c=[]
     for k in range(len(b)):
       m=[]
       for j in range(len(b[k])):
       
          if b[k].count(b[k][j])<trim:
             m.append(b[k][j])
      
       c.append((m))



     for i in range(len(c)):
    
        c[i]=list( dict.fromkeys(c[i]) )
     

     model2=[]
     for k in range(len(((c)))):
         ar={}
         for i in range(len(set(c[k]))):
            ar[c[k][i]]=1
         model2.append(ar)


   
     redict2=[]
     for i in range(len(model2)):
         die={}
         for j in (model2[i]):
            if j in dictionary:
               die[dictionary[j]]=1
         redict2.append(die)
     


#model2print

     for t in range(len(redict2)):
    
        formatted_train_out.write(reviews[t][0])
        formatted_train_out.write('\t')
        for u,v in (redict2[t].items()):
            
                formatted_train_out.write(str(u))
                formatted_train_out.write(":")
                formatted_train_out.write(str(v))
                formatted_train_out.write("\t")
        formatted_train_out.write("\n")        
                
#validationfile
     
     b=[]
     reviews=[]
     for line in validation_file:
        line2=line.split()
        reviews.append(line2)

     for k in range(len(reviews)):
       a=[]
       for j in range(len(reviews[k])):
        
         if reviews[k][j] in dictionary:
            a.append(reviews[k][j])
       if a!=[]:        
           b.append(a)
    
     

     trim=4

     c=[]
     for k in range(len(b)):
       m=[]
       for j in range(len(b[k])):
       
          if b[k].count(b[k][j])<trim:
             m.append(b[k][j])
      
       c.append((m))



     for i in range(len(c)):
    
        c[i]=list( dict.fromkeys(c[i]) )
     

     model2=[]
     for k in range(len(((c)))):
         ar={}
         for i in range(len(set(c[k]))):
            ar[c[k][i]]=1
         model2.append(ar)


   
     redict2=[]
     for i in range(len(model2)):
         die={}
         for j in (model2[i]):
            if j in dictionary:
               die[dictionary[j]]=1
         redict2.append(die)
     


#model2print

     for t in range(len(redict2)):
    
        formatted_validation_out.write(reviews[t][0])
        formatted_validation_out.write('\t')
        for u,v in (redict2[t].items()):
            
                formatted_validation_out.write(str(u))
                formatted_validation_out.write(":")
                formatted_validation_out.write(str(v))
                formatted_validation_out.write("\t")
        formatted_validation_out.write("\n")        
                
#testfile
     b=[]
     reviews=[]
     for line in test_file:
        line2=line.split()
        reviews.append(line2)

     for k in range(len(reviews)):
       a=[]
       for j in range(len(reviews[k])):
        
         if reviews[k][j] in dictionary:
            a.append(reviews[k][j])
       if a!=[]:        
            b.append(a)
    
     

     trim=4

     c=[]
     for k in range(len(b)):
       m=[]
       for j in range(len(b[k])):
       
          if b[k].count(b[k][j])<trim:
             m.append(b[k][j])
      
       c.append((m))



     for i in range(len(c)):
    
        c[i]=list( dict.fromkeys(c[i]) )
     

     model2=[]
     for k in range(len(((c)))):
         ar={}
         for i in range(len(set(c[k]))):
            ar[c[k][i]]=1
         model2.append(ar)


   
     redict2=[]
     for i in range(len(model2)):
         die={}
         for j in (model2[i]):
            if j in dictionary:
               die[dictionary[j]]=1
         redict2.append(die)
     


#model2print

     for t in range(len(redict2)):
    
        formatted_test_out.write(reviews[t][0])
        formatted_test_out.write('\t')
        for u,v in (redict2[t].items()):
            
                formatted_test_out.write(str(u))
                formatted_test_out.write(":")
                formatted_test_out.write(str(v))
                formatted_test_out.write("\t")
        formatted_test_out.write("\n")        
                   