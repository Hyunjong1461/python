def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    if start_index > end_index:
        return None

    mid = (end_index + start_index) // 2

    if element == some_list[mid]:
        # print(element, "same", some_list[mid], "mid ", mid)
        return mid
    elif element > some_list[mid]:
        return binary_search(element, some_list, mid + 1)
    elif element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)
    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))