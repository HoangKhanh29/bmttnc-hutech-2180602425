import itertools

def print_permutations(lst):
    # Lấy tất cả các hoán vị
    permutations = itertools.permutations(lst)
    
    # In tất cả các hoán vị
    for perm in permutations:
        print(perm)

# Danh sách ban đầu
lst = [1, 2, 3]

# Gọi hàm để in các hoán vị
print_permutations(lst)