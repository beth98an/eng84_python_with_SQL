# a runner- main- imports - create object -execute

from nw_products import NwProducts

prod = NwProducts()
print(prod.retrieve_all_data_from_products())
print(prod.create_table())
print(prod.stock())