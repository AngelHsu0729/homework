import os #operator system

#讀取檔案
product = []
if os.path.isfile('product.csv'):#檢查檔案在不在
    print('yes, have file')
    with open('product.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'products,prices' in line:
                continue
            name, price = line.strip().split(',')
            product.append([name, price])
    print(product)

else:
    print('no......')

#讓使用者輸入
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    price = int(price)
    product.append([name, price])
print(product)

#印出所有購買紀錄
for p in product:
    print(p[0],'的價格是', p[1])

#寫入檔案
with open('product.csv', 'w', encoding = 'utf-8') as f:
    f.write('products,prices\n')
    for p in product:
        f.write(p[0] + ',' + str(p[1]) + '\n')


