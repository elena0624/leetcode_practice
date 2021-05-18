# -*- coding: utf-8 -*-
"""
Created on Tue May 18 17:55:02 2021

@author: ppj
"""
import collections
paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

cont_dict=collections.defaultdict(list)
dup_ls=set()
for i in paths:
#    print(i.split())
    file=i.split()
    path=file[0]
    for j in file[1:]:
        content=j[j.find('(')+1:j.find(')')]
        file_name=j[:j.find('(')]
#        print(content)
#        print(file_name)
#        print(path+'/'+file_name)
        if cont_dict[content]:
            dup_ls.add(content)
        cont_dict[content].append(path+'/'+file_name)
print([cont_dict[i] for i in dup_ls])
#%%    
import collections
paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

cont_dict=collections.defaultdict(list)
dup_ls=set()
for i in paths:
#    print(i.split())
    file=i.split()
    path=file[0]
    for j in file[1:]:
        content=j[j.find('(')+1:-1]
        file_name=j[:j.find('(')]
        print(content)
        print(file_name)
#        print(path+'/'+file_name)
        if cont_dict[content]:
            dup_ls.add(content)
        cont_dict[content].append(path+'/'+file_name)
print([cont_dict[i] for i in dup_ls])
            

    