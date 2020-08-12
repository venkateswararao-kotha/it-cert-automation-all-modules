orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

from collections import defaultdict

sales_by_model = defaultdict(int)
sales_by_model[key] += 1
sort_sales_by_model = sorted(sales_by_model.items(), key=lambda x: x[1], reverse=True)

total_sales_for_car_year = defaultdict(int)
total_sales_for_car_year[key] += 1


dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
for dic in dataList:
    for key in dic:
        print(dic[key])

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
first_key = next(iter(sort_orders))

for i in sort_orders:
	print(i[0], i[1])

my_dict = {'foo': 'bar', 'spam': 'eggs'}
first_key = next(iter(sort_orders)) # outputs 'foo'

list(my_dict.keys())[0]


#  Page Layout and Typography Using Scripts (PLATYPUS)

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

styles = getSampleStyleSheet()

report = SimpleDocTemplate("/tmp/cars.pdf")
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

report.build([report_title])

{
        "id": 47,
        "car": {
                "car_make": "Lamborghini",
                "car_model": "Murciélago",
                "car_year": 2002
        },
        "price": "$13724.05",
        "total_sales": 149
}

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])


table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table])

# TODO: also handle max sales
item_sales = 0
item_sales = item["total_sales"]
if item_sales > max_sales["sales"]:
    item["sales"] = item_sales
    max_sales["sales"] = item_sales
    max_sales = item

# TODO: also handle most popular car_year
sales_by_model = defaultdict(int)

for item in data:
    sales_by_model[item["car"]["car_year"]] += item["total_sales"]

sort_sales_by_model = sorted(sales_by_model.items(), key=lambda x: x[1], reverse=True)
first_key = next(iter(sort_sales_by_model))  # return key, value as tuple
# print(sort_sales_by_model)
print(type(first_key), first_key)

summary = [
    "The {} generated the most revenue: ${}\n".format(
        format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}\n".format(
        format_car(max_sales["car"]), max_sales["sales"]),
    "The most popular year was {} with {} sales\n".format(
        first_key[0], first_key[1]),
]

roomno = "Room" + room
w_text = []
w_text.append(Paragraph("To use the wireless broadband…:",stylesheet["BodyText"]))
w_text.append(Paragraph("User id: <b>" + roomno + "</b>", stylesheet["BodyText"]))
w_text.append(Paragraph("Password: <b>" + password + "</b>", stylesheet["BodyText"]))
