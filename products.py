products = []
while True:
	name = input('請輸入產品名稱: ')
	if name == 'q':
		break
	price = input('請輸入產品價格: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '價格為', p[1], '元')
