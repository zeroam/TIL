from layer_naive import *

apple = 100
apple_num = 2
tax = 1.1

# 계층들
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# 순전파
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

# 역전파
dprice = 1
dapple_price, dtax = mul_tax_layer.backword(dprice)
dapple, dapple_num = mul_apple_layer.backword(dapple_price)

print(f'price: {int(price)}')    # 220
print(f'dApple: {dapple}')  # 2.2
print(f'dApple_num: {int(dapple_num)}') # 110
print(f'dTax: {dtax}')  # 200