All 4 Rest 

This project is a system designed for managing products, brands,
and their associated managers in the context of "All 4 Rest." 
It includes features for handling product types, brand information, 
and positions within the organization.

Database Structure Overview

![Screenshot 2024-12-01 at 20.19.36.png](../../Desktop/Screenshot%202024-12-01%20at%2020.19.36.png)

The project is built around the following key models:

1. Position
Represents the roles in the system (e.g., furniture seller, grill seller, camping seller).
Fields:
    name (Choice Field: furniture seller, grill seller, camping seller)

2. Manager (AbstractUser)
Extends Django's AbstractUser to represent users who manage products and brands.
Fields:
    position (Foreign Key to Position)
    username, password, email, first_name, last_name (inherited from AbstractUser)

3. Brand
Stores details about brands associated with products.
Fields:
    name
    country

4. Product
Represents individual products under specific brands.
Fields:
    name
    price
    brand (Foreign Key to Brand)
    description
    type (Foreign Key to ProductType)
    photo

5. ProductType
Categorizes products into types (e.g., garden furniture, grill products, camping products).
Fields:
    name (Choice Field: garden furniture, grill products, camping products)
    managers (Foreign Key to Manager)


Installation Steps

1. Clone the Repository:
git clone <repository_url>

2. Create a Virtual Environment:
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate     # For Windows

3. Install Dependencies:
pip install -r requirements.txt

4. Run Migrations:
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser:
python manage.py createsuperuser

6. Run the Development Server:
python manage.py runserver

7. Optional: Load Initial Data
You can load predefined positions, product types, or brands using fixtures:
python manage.py loaddata initial_data.json
