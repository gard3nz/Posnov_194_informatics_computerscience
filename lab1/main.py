from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import setup_database, create_session, Customer  # Подключаем модели из ORM

# Инициализация базы данных
engine = setup_database("sqlite:///customer.sqlite")
session = create_session(engine)


# CREATE (Создание)
def add_customer(Id, fname, lname, db, cty, stte, zp):
    try:
        new_customer = Customer(
            id=Id,
            first_name=fname,
            last_name=lname,
            dob=db,
            city=cty,
            state=stte,
            zip=zp
        )
        session.add(new_customer)
        session.commit()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    print(f"Customer '{fname}' added with ID: {new_customer.id}")
    return new_customer.id


# READ (Чтение)
def get_customer_by_id(customer_id):
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        print(f"Founded customer with name: {customer.first_name}")
        return customer
    else:
        print(f"Customer with ID {customer_id} not found.")
        return None


def get_customers_by_state(customer_state):
    customers = session.query(Customer).filter_by(state=customer_state).all()
    for customer in customers:
        print(f"Customer ID: {customer.id}, Name: {customer.first_name}")
    return customers


def get_all_customers():
    customers = session.query(Customer).all()
    for custom in customers:
        print(f"Customer ID: {custom.id}, Name: {custom.first_name}")
    return customers


def delete_customer(customer_id):
    custom = session.query(Customer).filter_by(id=customer_id).first()
    if custom:
        session.delete(custom)
        session.commit()
        print(f"Customer ID {customer_id} deleted.")
    else:
        print(f"Customer with ID {customer_id} not found.")


def update_customer_name(customer_id, new_name):
    custom = session.query(Customer).filter_by(id=customer_id).first()
    if custom:
        custom.first_name = new_name
        session.commit()
        print(f"Customer ID {customer_id} updated to '{new_name}'")
        return custom
    else:
        print(f"Customer with ID {customer_id} not found.")
        return None

dct_person={
    "person1":{
        "id": 99999,
        "name": "vladislav", 
        "last_name": "drr", 
        "year": "1999-10-12", 
        "city":"Moscow", 
        "US": "1995251"
}
    2: '99998, "maxim", "drr", "2000-10-12", "Moscow", "MN", "1995234"',
    3: '99997, "alexei", "drr", "1997-10-12", "Tomsk", "US", "1995892"'
}
first=dict[1]
second=dict[2]
third=dict[3]
print(first)
# Примеры использования
if __name__ == "__main__":
    try:
        # Создание
        customer_id = add_customer(99999, "vladislav", "drr", "1999-10-12", "Moscow", "US", "1995251")
        # Измененеие имени пользователя по айди
        update_customer_name(99999, "Murat")
        # Поиск по айди
        print(get_customer_by_id(99999))
        # Вывод всех пользователей со штатом "MN"
        print(get_customers_by_state("MN"))
        # Удаление пользователя
        delete_customer(99999)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
