def into_dic(my_list, member):
    list_member = []
    list_member_idx = -1
    new_member = ''
    for obj in my_list:

        if getattr(obj, member) != new_member:
            new_member = getattr(obj, member)
            list_member.append(new_member)

    target_list_member = [[] for x in range(len(list_member))]

    dic_member = dict(zip(list_member, target_list_member))
    #print(dic_member)
    for obj in my_list:
        for member_key in dic_member.keys():
            if getattr(obj, member) == member_key:
                dic_member[member_key].append(obj)
    return dic_member


def obj_into_dic(my_list, *args):
    dic_discipline = into_dic(my_list, args[0])
    #print(dic_discipline)
    try:
        for disc in dic_discipline.keys():
            dic_discipline[disc] = into_dic(dic_discipline[disc], args[1])
            try:
                for exo_nb in dic_discipline[disc].keys():
                    dic_discipline[disc][exo_nb] = into_dic(dic_discipline[disc][exo_nb], args[2])
            except:
                pass
    except:
        pass
    return dic_discipline
