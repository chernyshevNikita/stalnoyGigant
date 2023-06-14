from database import Client,Seller,Store, create_session, global_init,Categories, Manufacture, Order, Product,SellerProduct
from faker import Faker
import random

global_init("database/stgg.db")
session = create_session()
fk = Faker("ru")
fk_eng = Faker()
#Faker.seed(200)

new = SellerProduct(product_id=45,seller_id=12)
session.add(new)
session.commit()
print(new.products.product_name)








