'''
Приклад роботи с datawiz API
'''

import datetime
from dwapi import datawiz
from pprint import pprint

date_from = datetime.date(2015, 8, 9)
date_to = datetime.date(2015, 9, 12)

# Створення классу для вибору данних:
# datawiz.DW(API_KEY, API_SECRET) 
# якщо де API_KEY, API_SECRET - ключ і підпис користувача, якщо вони не задані то запускаємо для тестового користувача.
dw = datawiz.DW()

# print (dw.get_products_sale(products = [2855561, 2861880],by='turnover',
# 				shops = [601,641,595],
# 				date_from = date_from,
# 				date_to = date_to,
# 				interval = datawiz.WEEKS))

# pprint(dw.get_category())
# pprint(dw.get_client_info())
# pprint(dw.get_product(products=[2921857, 2876683]))
# pprint(dw.get_categories_sale(categories=[50599, 50600, "sum"],
#                               by='turnover',
#                               shops=[305, 306, 318, 321],
#                               date_from=datetime.date(2015, 8, 9),
#                               date_to=datetime.date(2015, 9, 9),
#                               interval=datawiz.WEEKS))

# pprint(dw.get_receipt(19623631))
# pprint(dw.get_receipts(categories=[50599, 50600],
#                        shops=[305, 306, 318, 321],
#                        date_from=datetime.date(2015, 8, 9),
#                        date_to=datetime.date(2015, 9, 9),
#                        type="short"))

# pprint(dw.get_products_stock(categories=[68805, 69607], by='stock_qty',
#                       shops=[601, 641],
#                       date_from=datetime.date(2015, 8, 9),
#                       date_to=datetime.date(2015, 9, 9),
#                       ))
# print(dw.get_categories_stock(categories=[68805, 69607], by='stock_value',
#                         shops=[601, 641],
#                         date_from=datetime.date(2015, 8, 9),
#                         date_to=datetime.date(2015, 9, 9),
#                         ))
# pprint(dw.get_lost_sales(category=68805,
#                          shops=[601, 641],
#                          date_from=datetime.date(2015, 8, 9),
#                          date_to=datetime.date(2015, 9, 9),
#                          ))
# pprint(dw.get_sales_plan(category=68805,
#                          shops=[601, 641],
#                          date=datetime.date(2015, 8, 1),
#                          ))
# pprint(dw.get_sales(
#     date_from=datetime.date(2015, 8, 9),
#     date_to=datetime.date(2015, 9, 9),
# ))

# pprint(dw.get_sale_info(40))

# pprint(dw.get_sales_dynamics(
#     date_from='2015-5-1',
#     date_to='2015-11-1',
#     by='receipts_qty',
#     show='both'
# ))

# pprint(dw.get_loyalty_sales(
#     shops=[601, 641],
#     date_from=datetime.date(2015, 8, 9),
#     date_to=datetime.date(2015, 9, 9),
# ))
