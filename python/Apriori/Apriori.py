#可以计算k项集的支持度和置信度；如果不能排序，是字符的话可以转化成字符
def load_data_set():#给出dataset
    """
    Load a sample data set (From Data Mining: Concepts and Techniques, 3th Edition)
    Returns: 
        A data set: A list of transactions. Each transaction contains several items.
    """
    data_set = [['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'],
            ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'],
            ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]
    return data_set


def create_C1(data_set):#把c1每个元素，得到1——项集
    """
    Create frequent candidate 1-itemset C1 by scaning data set.
    Args:
        data_set: A list of transactions. Each transaction contains several items.
    Returns:
        C1: A set which contains all frequent candidate 1-itemsets
    """
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])#frozenset('')和frozenset（[]）效果是一样的
            C1.add(item_set)#set有set.add()和remove()方法,set可以对其中的frozedset去重
    return C1


def is_apriori(Ck_item, Lksub1):#对k候选项进行筛选
    """
    Judge whether a frequent candidate k-itemset satisfy Apriori property.
    Args:
        Ck_item: a frequent candidate k-itemset in Ck which contains all frequent
                 candidate k-itemsets.Ck中的一个频繁候选k项集，其中包含所有频繁候选k项集。，只有一个
        Lksub1: Lk-1, a set which contains all frequent candidate (k-1)-itemsets.
        一个包含所有频繁候选（k-1） - 集合的集合。
    Returns:
        True: satisfying Apriori property.
        False: Not satisfying Apriori property.
    """
    for item in Ck_item:#Ck_item是候选k频繁项集中的一个，例如['l1','l2']
        sub_Ck = Ck_item - frozenset([item])#判断候选集中的每个子项都是k-1项的子集
        if sub_Ck not in Lksub1:
            return False
    return True


def create_Ck(Lksub1, k):#如果前k-2项元素相同，那么考虑set的并集，
    """
    Create Ck, a set which contains all all frequent candidate k-itemsets
    by Lk-1's own connection operation.
    Args:
        Lksub1: Lk-1, a set which contains all frequent candidate (k-1)-itemsets.
        k: the item number of a frequent itemset.
    Return:
        Ck: a set which contains all all frequent candidate k-itemsets.
    """
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:#如果前k-2项元素相同，那么考虑set的并集
                Ck_item = list_Lksub1[i] | list_Lksub1[j]#frozedset也可以这种方式取并集
                # pruning
                if is_apriori(Ck_item, Lksub1):#如果子项都是频繁项集，那么该项可以作为k频繁项集
                    Ck.add(Ck_item)
    return Ck


def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):#计算筛选候选集的支持度并筛选
    """
    Generate Lk by executing a delete policy from Ck.
    Args:
        data_set: A list of transactions. Each transaction contains several items.
        Ck: A set which contains all all frequent candidate k-itemsets.
        min_support: The minimum support.
        support_data: A dictionary. The key is frequent itemset and the value is support.
    Returns:
        Lk: A set which contains all all frequent k-itemsets.
    """
    Lk = set()
    item_count = {}#dict
    for t in data_set:
        for item in Ck:
            if item.issubset(t):#s.issubset( x ) 判断 集合s 是否是 集合x 子集
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk


def generate_L(data_set, k, min_support):#
    """
    Generate all frequent itemsets.
    Args:
        data_set: A list of transactions. Each transaction contains several items.
        k: Maximum number of items for all frequent itemsets.
        min_support: The minimum support.
    Returns:
        L: The list of Lk.
        support_data: A dictionary. The key is frequent itemset and the value is support.
    """
    support_data = {}
    C1 = create_C1(data_set)
    L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)#set变成list
    for i in range(2, k+1):
        Ci = create_Ck(Lksub1, i)
        Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data


def generate_big_rules(L, support_data, min_conf):#求置信度
    """
    Generate big rules from frequent itemsets.
    Args:
        L: The list of Lk.
        support_data: A dictionary. The key is frequent itemset and the value is support.
        min_conf: Minimal confidence.
    Returns:
        big_rule_list: A list which contains all big rules. Each big rule is represented
                       as a 3-tuple.
    """
    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = support_data[freq_set] / support_data[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and big_rule not in big_rule_list:
                        # print freq_set-sub_set, " => ", sub_set, "conf: ", conf
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    return big_rule_list


if __name__ == "__main__":
    """
    Test
    """
    data_set = load_data_set()
    L, support_data = generate_L(data_set, k=3, min_support=0.2)
    big_rules_list = generate_big_rules(L, support_data, min_conf=0.7)
    for Lk in L:
        print("="*50)#横线虚线
        print("frequent " + str(len(list(Lk)[0])) + "-itemsets\t\tsupport")
        print("="*50)
        for freq_set in Lk:
            print(freq_set, support_data[freq_set])
    print()
    print("Big Rules")
    for item in big_rules_list:
        print(item[0], "=>", item[1], "conf: ", item[2])
        
        
#c1,计算支持度，然后筛选
#根据ck求ck+1,,前k-1项相同的合并，然后判断子集是否属于ck；计算支持度度筛选，计算置信度，判断是否具有关系，
#依次进行以上过程，直到没有k-1项相同的