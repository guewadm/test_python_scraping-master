#Exercice : 1

def exercise_one():
    
    for n in range(1,100):
        if n % 15 == 0:
            print("THREEFIVE")
            continue
        elif n % 3 == 0:
            print("THREE")                                        
            continue
        elif n % 5 == 0:        
            print("FIVE")                                    
            continue
        print(n)
        
#Exercice : 2


def colorful(self, n):
        temp = []
        hashlist = {}
        s = str(n)
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp.append(s[i:j + 1])

        for l in range(len(temp)):
            mx = 1
            p = temp[l]
            for k in range(len(p)):
                mx *= int(p[k])
            hashlist[p] = mx

        temp0 = []

        for k, v in hashlist.items():
            if v not in temp0:
                temp0.append(v)
        if len(temp0) == len(temp):
            return 1
        else:
            return 0

        

#Exercice : 3

def calculate(numList):
       if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(calculate([4,3,-2]))

#Exercice : 4

def anagram(list_of_str):
        
    new_list = []
    empty_dict ={}
    
  for item in list_of_str:
        sorted_item = ''.join(sorted(item))
        if sorted_item not in empty_dict:
            empty_dict[sorted_item] = [item]
        else:
            empty_dict[sorted_item].append(item)
    # return empty_dict 
    for k,v in empty_dict.items():
        if len(v)>=2:
            new_list.append(v)
    return new_list

a = ['dog', 'god', 'cat']
print(anagram(a))