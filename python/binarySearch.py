def bSearch(li, el):
    end = len(li)
    beg = 0
    count = 0
    if not el in li:
        print("{} 원소가 리스트에 존재하지 않습니다.".format(el))
        return -1
    else:
        while beg <= end:
            count += 1
            mid = (beg + end) // 2

            if li[mid] == el:
                return mid, count
            elif li[mid] < el:
                beg = mid + 1
             
            elif li[mid] > el:
                end = mid - 1