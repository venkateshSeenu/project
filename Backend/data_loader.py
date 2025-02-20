from database import get_session
from models import Product, Supplier, Batch
from datetime import date

def add_suppliers():
    session = get_session()

    suppliers = [
        Supplier(
            name="ABC Merchandise Co.",
            contact_person="John Doe",
            phone="123-456-7890",
            email="abc_merch@example.com",
            address="123 Market St, Valparaiso, IN",
        ),
        Supplier(
            name="Tee World",
            contact_person="Alice Smith",
            phone="987-654-3210",
            email="tee_world@example.com",
            address="456 Fashion Ave, Chicago, IL",
        ),
        Supplier(
            name="Mug Masters",
            contact_person="Bob Johnson",
            phone="555-234-5678",
            email="mug_masters@example.com",
            address="789 Coffee Rd, Indianapolis, IN",
        ),
        Supplier(
            name="Keychain Kingdom",
            contact_person="Emma Wilson",
            phone="111-222-3333",
            email="keychain_kingdom@example.com",
            address="321 Accessory Ln, Milwaukee, WI",
        ),
    ]

    for supplier in suppliers:
        existing_supplier = session.query(Supplier).filter_by(name=supplier.name).first()
        if not existing_supplier:
            session.add(supplier)

    session.commit()
    session.close()

def add_products():
    session = get_session()
    products = [
        Product(name="Branded T-shirt", category="Clothing", stock_level=10, reorder_threshold=20, price=15.99, supplier_id=1, image_url="/images/tshirt.png"),
        Product(name="Mug", category="Kitchenware", stock_level=200, reorder_threshold=50, price=5.99, supplier_id=2, image_url="/images/mug.jpg"),
        Product(name="Keychain", category="Accessories", stock_level=300, reorder_threshold=75, price=2.99, supplier_id=3, image_url="/images/keychain.jpeg"),
        Product(name="Reusable Ice Cream Container", category="Kitchenware", stock_level=150, reorder_threshold=30, price=10.99, supplier_id=4, image_url="/images/ice_cream_container.jpg"),
    ]

    for product in products:
        existing_product = session.query(Product).filter_by(name=product.name).first()
        if not existing_product:
            session.add(product)

    session.commit()
    session.close()

def add_batches():
    session = get_session()

    batches = [
        Batch(product_id=1, supplier_id=1, quantity_received=100, received_date=date(2025, 2, 10), expiration_date=None, batch_status="Active"),
        Batch(product_id=2, supplier_id=2, quantity_received=50, received_date=date(2025, 2, 5), expiration_date=date(2026, 2, 5), batch_status="Active"),
        Batch(product_id=3, supplier_id=3, quantity_received=200, received_date=date(2025, 1, 15), expiration_date=None, batch_status="Active"),
        Batch(product_id=4, supplier_id=4, quantity_received=75, received_date=date(2025, 2, 1), expiration_date=date(2025, 8, 1), batch_status="Active"),
    ]

    for batch_data in batches:
        try:
            session.add(batch_data)
            session.commit()
        except Exception as e:
            session.rollback()  # Rollback on error
            print(f"Error adding batch {batch_data.id}: {e}")

    session.close()
