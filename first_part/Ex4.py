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