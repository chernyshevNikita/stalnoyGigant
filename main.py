from database import Client,Seller,Store, create_session, global_init,Categories, Manufacture, Product


global_init("database/stgg.db")
session = create_session()
# создание нового студента
#new_category = Categories(category_name="Телевизор")
#session.add(new_category)
#new_manuf = Seller(seller_name="mark",rating=4,store_id=2)
#session.add(new_manuf)
#session.commit()
# обновить студента
#old_student = session.query(Client).filter(Client.client_id == 1).first()
#print(old_student)
#old_student.client_city = 'водники'
#session.commit()
#print(old_student)
# достать всех студентов
sellers = session.query(Seller).all()
for student in sellers:
    print(student)
#print(new_manuf)

