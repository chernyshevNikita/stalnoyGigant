from database import Client,Seller,Store, create_session, global_init,Categories, Manufacture


global_init("database/stg.db")
session = create_session()
# создание нового студента
#new_category = Categories(category_name="Телевизор")
#session.add(new_category)
new_manuf = Manufacture(manufacturer_name="Завод 1")
new_seller = Seller(seller_id= 10,seller_name="Favor", rating="3", store_id=1)
session.add(new_manuf)
session.commit()
new_client = Client(client_id = 6, client_name = "Jopa",client_city= "Perm")
# обновить студента
#old_student = session.query(Client).filter(Client.client_id == 1).first()
#print(old_student)
#old_student.client_city = 'водники'
#session.commit()
#print(old_student)
# достать всех студентов
#clients = session.query(Client).all()
#for student in clients:
#    print(student)
print(new_manuf)
print(new_seller)
print(new_client)