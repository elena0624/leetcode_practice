class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        cont_dict=collections.defaultdict(list)
        dup_ls=set()
        for i in paths:
            file=i.split()
            path=file[0]
            for j in file[1:]:
                #content=j[j.find('(')+1:j.find(')')]
                content=j[j.find('(')+1:-1]
                file_name=j[:j.find('(')]
                if cont_dict[content]:
                    dup_ls.add(content)
                cont_dict[content].append(path+'/'+file_name)
        return([cont_dict[i] for i in dup_ls])