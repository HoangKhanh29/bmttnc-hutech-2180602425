import re

def sum_positive_and_negative_numbers(string):
    # Tìm tất cả các số trong chuỗi
    numbers = re.findall(r'-?\d+', string)
    
    # Khởi tạo tổng số dương và tổng số âm
    positive_sum = 0
    negative_sum = 0
    
    # Tính tổng các số dương và số âm
    for num in numbers:
        num = int(num)
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num
            
    return positive_sum, negative_sum

# Chuỗi ban đầu
input_string = "-100#^sdfkj8902w3ir021@swf-20"

# Tính tổng số dương và số âm
positive_sum, negative_sum = sum_positive_and_negative_numbers(input_string)

# In kết quả
print("Giá trị dương:", positive_sum)
print("Giá trị âm:", negative_sum)