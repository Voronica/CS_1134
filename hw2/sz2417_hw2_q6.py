def two_sum(srt_lst, target):
    tpl = ()
    for item in srt_lst:
        if item < target:
            pair = target - item
            if pair in srt_lst:
                tpl = (srt_lst.index(item), srt_lst.index(pair))
                return tpl
        else:
            return None







