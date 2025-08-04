import os
import django
import shutil
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

def copy_image_to_media(image_name):
    source = os.path.join(settings.STATIC_ROOT, 'images', image_name)
    dest_dir = os.path.join(settings.MEDIA_ROOT, 'products')
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, image_name)
    shutil.copy2(source, dest)
    return f'products/{image_name}'

def populate_db():
    # Create categories
    categories = {
        'sofa': Category.objects.create(name='Sofa'),
        'chair': Category.objects.create(name='Chair'),
        'mobile': Category.objects.create(name='Mobile'),
        'watch': Category.objects.create(name='Watch'),
        'wireless': Category.objects.create(name='Wireless'),
    }

    # Create products
    products_data = [
        # Furniture Products (Big Discount)
        {
            'id': '01',
            'name': 'Stone and Beam Westview',
            'description': 'Comfortable and stylish double sofa',
            'price': 193.99,
            'category': 'sofa',
            'rating': 5,
            'image': 'double-sofa-01.png'
        },
        {
            'id': '02',
            'name': 'Rivet Bigelow Modern',
            'description': 'Modern sofa for your living room',
            'price': 253.99,
            'category': 'sofa',
            'rating': 5,
            'image': 'double-sofa-02.png'
        },
        {
            'id': '03',
            'name': 'Amazon Brand Modern Sofa',
            'description': 'Contemporary sofa with premium comfort',
            'price': 173.99,
            'category': 'sofa',
            'rating': 5,
            'image': 'double-sofa-03.png'
        },
        # New Arrivals Products (First 3 Mobile)
        {
            'id': '07',
            'name': 'iPhone 15 Pro',
            'description': 'Latest iPhone with advanced features',
            'price': 799.99,
            'category': 'mobile',
            'rating': 5,
            'image': 'phone-03.png'
        },
        {
            'id': '08',
            'name': 'iPhone 15 Max',
            'description': 'Premium iPhone with large display',
            'price': 799.99,
            'category': 'mobile',
            'rating': 5,
            'image': 'phone-02.jpg'
        },
        {
            'id': '09',
            'name': 'Realme 8',
            'description': 'Feature-rich Android smartphone',
            'price': 599.99,
            'category': 'mobile',
            'rating': 5,
            'image': 'phone-03.png'
        },
        # New Arrivals Products (Last 3 Watches)
        {
            'id': '10',
            'name': 'Apple Watch Series 8',
            'description': 'Premium smartwatch with health features',
            'price': 399.99,
            'category': 'watch',
            'rating': 5,
            'image': 'watch-01.jpg'
        },
        {
            'id': '11',
            'name': 'Samsung Galaxy Watch 6',
            'description': 'Advanced Android smartwatch',
            'price': 299.99,
            'category': 'watch',
            'rating': 5,
            'image': 'watch-02.jpg'
        },
        {
            'id': '12',
            'name': 'Rolex Submariner',
            'description': 'Luxury analog watch',
            'price': 899.99,
            'category': 'watch',
            'rating': 5,
            'image': 'watch-03.jpg'
        },
        # Best Sales Products
        {
            'id': '13',
            'name': 'Beat Studio Wireless',
            'description': 'Premium wireless headphones',
            'price': 199.99,
            'category': 'wireless',
            'rating': 5,
            'image': 'wireless-01.png'
        },
        {
            'id': '14',
            'name': 'Sony BT Headphones',
            'description': 'High-quality wireless headphones',
            'price': 199.99,
            'category': 'wireless',
            'rating': 5,
            'image': 'wireless-03.png'
        },
        {
            'id': '15',
            'name': 'Black Headphones',
            'description': 'Stylish black headphones',
            'price': 169.99,
            'category': 'wireless',
            'rating': 5,
            'image': 'wireless-02.png'
        },
        {
            'id': '16',
            'name': 'Premium HeadAirpods',
            'description': 'Premium wireless earbuds',
            'price': 139.99,
            'category': 'wireless',
            'rating': 5,
            'image': 'wireless-04.png'
        },
        {
            'id': '17',
            'name': 'Google Pixel 8 Pro',
            'description': 'Latest Google flagship smartphone',
            'price': 899.99,
            'category': 'mobile',
            'rating': 5,
            'image': 'phone-02.jpg'
        },
        {
            'id': '18',
            'name': 'Samsung Galaxy Z Fold 5',
            'description': 'Premium foldable smartphone',
            'price': 1799.99,
            'category': 'mobile',
            'rating': 5,
            'image': 'phone-03.png'
        }
    ]

    # Create products
    for product_data in products_data:
        product_id = product_data.pop('id')
        category_name = product_data.pop('category')
        image_name = product_data.pop('image')
        image_path = copy_image_to_media(image_name)
        Product.objects.create(
            id=product_id,
            category=categories[category_name],
            image=image_path,
            name=product_data.pop('name'),
            description=product_data.pop('description'),
            price=product_data.pop('price'),
            rating=product_data.pop('rating')
        )

    print("Database populated successfully!")

if __name__ == '__main__':
    # Clear existing data
    Product.objects.all().delete()
    Category.objects.all().delete()
    
    # Populate with new data
    populate_db() 