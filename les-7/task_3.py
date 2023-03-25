# 1:40
# enumerate
my_string = '12345453452423'
my_string = list(my_string)
print(my_string)
for i, item in enumerate(my_string, 1):
    print(f'{i}. {item}')
