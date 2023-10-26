def getChar(x):
    return chr(x + ord('a'))

s = input()
t = input()

need_tree = array = automaton = False

for i in range(26):
    t_count = t.count(getChar(i))
    s_count = s.count(getChar(i))

    if t_count > s_count:
        need_tree = True
    elif t_count < s_count:
        automaton = True

index_found, match = 0, -1

for i in range(len(t)):
    index_found = s.find(t[i], match + 1)
    if index_found > match:
        match = index_found
    else:
        array = True
        break

if need_tree:
    print("need tree")
elif automaton and array:
    print("both")
elif automaton:
    print("automaton")
else:
    print("array")

# Trước tiên ta có nhận xét như sau:
# 1. Nếu có 1 ký tự nào có trong t mà không có trong s => không thể biến đổi s thành t => "need tree"
# 2. Nếu có 1 ký tự nào có trong s mà không có trong t => để có thể biển s thành t thì ta phải bỏ ký tự đó => "automaton"
# 3. Phép biến đổi "array" hoán đổi vị trí của 2 ký tự chỉ cần thiết nếu thứ tự xuất hiện của các ký tự trong chuỗi t không trùng
#     khớp với thứ tự  của các ký tự  đó trong chuỗi s
# Để giair quyết 1 và 2 ta dùng một mảng đếm tần suất xuất hiện của từng ký tự trong chuỗi s và chuỗi t. Sau đó duyệt từng ký tự 
#     trong bảng chữ cái gồm 26 chữ cái:
# - Nếu  tần suất xuất hiện của ký tự đó trong chuỗi t lớn hơn chuỗi s, nghĩa là chuỗi s không đủ ký tự để biến đỗi thành chuỗi t => "need tree"
# - Nếu  tần suất xuất hiện của ký tự đó trong chuỗi t nhỏ hơn chuỗi s, nghĩa là sẽ có 1 số ký tự thừa => "automaton"
# Ta cần giải quyết trường hợp 3 để có thể đưa ra kết luận là “array” hay “both”. Bằng cách duyệt qua từng ký tự trong chuỗi
#     t, ta tìm vị trí của ký tự tương ứng trong chuỗi s. Nếu các vị trí này tăng dần nghĩa là các ký tự này đã đúng vị trí, ta không cần đổi chỗ.
#     Ngược lại thì ta kết luận "array"
# Xem xét liệu “automaton” và “array” có cùng thỏa hay không để đưa ra kết luận là “both”.