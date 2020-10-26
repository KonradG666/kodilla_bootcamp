# Example 1
print('L {:<20} R'.format('x'))
# Example 2
print('L {:^20} R'.format('x'))
# Example 3
print('L {:>20} R'.format('x'))

base_unit = "kg"
product_type = "Ser"
currency = "zł"
product_1 = "Roquefort"
product_1_price_per_weight = 12.50
product_1_weight = 1.00 + 2.00   # second number is additional buy
final_price_1 = product_1_price_per_weight * product_1_weight
product_2 = "Stilton"
product_2_price_per_weight = 11.24
product_2_weight = 1.00
final_price_2 = product_2_price_per_weight * product_2_weight
product_3 = "Brie"
product_3_price_per_weight = 9.30
product_3_weight = 1.00
final_price_3 = product_3_price_per_weight * product_3_weight
product_4 = "Gouda"
product_4_price_per_weight = 8.55
product_4_weight = 1.00
final_price_4 = product_1_price_per_weight * product_4_weight
product_5 = "Edam"
product_5_price_per_weight = 11.00
product_5_weight = 1.00
final_price_5 = product_5_price_per_weight * product_5_weight
product_6 = "Parmezan"
product_6_price_per_weight = 16.50
product_6_weight = 1.00 + 3.50   # second number is additional buy
final_price_6 = product_6_price_per_weight * product_6_weight
product_7 = "Mozzarella"
product_7_price_per_weight = 14.00 + 0.13
product_7_weight = 1.00
final_price_7 = product_7_price_per_weight * product_7_weight
product_8 = "Czechosłowacki z owczego mleka"
product_8_price_per_weight = 122.32
product_8_weight = 1.00 + 0.22  # second number is additional buy
final_price_8 = product_8_price_per_weight * product_8_weight
product_9 = "Listek Mięty"
product_9_price_per_weight = 20.00
product_9_weight = 0.2
final_price_9 = product_9_price_per_weight * product_9_weight

shopping_report = f"Lista serów: \n{product_type}  {product_1}, {product_1_weight} {base_unit}  cena {product_1_price_per_weight * product_1_weight} {currency} \n{product_type} {product_2}, {product_2_weight} {base_unit}  cena {product_2_price_per_weight*product_2_weight} {currency} \n{product_type} {product_3}, {product_3_weight} {base_unit}  cena {product_3_price_per_weight*product_3_weight} {currency} \n{product_type} {product_4}, {product_4_weight} {base_unit}  cena {product_4_price_per_weight*product_4_weight} {currency} \n{product_type} {product_5}, {product_5_weight} {base_unit}  cena {product_5_price_per_weight*product_5_weight} {currency} \n{product_type} {product_6}, {product_6_weight} {base_unit}  cena {product_6_price_per_weight*product_6_weight} {currency} \n{product_type} {product_7}, {product_7_weight} {base_unit}  cena {product_7_price_per_weight*product_7_weight} {currency} \n{product_type} {product_8}, {product_8_weight} {base_unit}  cena {product_8_price_per_weight*product_8_weight} {currency} \n{product_type} {product_9}, {product_9_weight} {base_unit}  cena {product_9_price_per_weight*product_9_weight} {currency}. "
total_sum = f" Kwata całkowita: {final_price_1+final_price_2+final_price_3+final_price_4+final_price_5+final_price_6+final_price_7+final_price_8+final_price_9} {currency}"

print(shopping_report)
print(total_sum)

