products = []
while True:
	name = input('請輸入產品名稱: ')
	if name == 'q':
		break
	products.append(name)
print(products)
