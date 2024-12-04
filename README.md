# All 4 Rest

Welcome to **All 4 Rest** — a robust system for managing products, brands, and their managers, tailored to support diverse organizational roles. This platform streamlines handling product types, brand information, and hierarchical positions within the organization.  
Link on live page: https://all-for-rest.onrender.com/  
**User for testing:** login - oleh, password - oleh1234  
**Note:** This user is grill seller, so he can change only grill products, but no delete. Delete product can only superuser.  



---

## 📖 Overview

"All 4 Rest" simplifies the management of:
- Product types
- Brand details
- Organizational roles and positions

The system is designed with scalability and clarity in mind, ensuring efficient management of business operations.

---

## 🗂️ Database Structure

Here's an overview of the project's database design:

<img width="1184" alt="Screenshot 2024-12-01 at 20 19 36" src="https://github.com/user-attachments/assets/49758279-c84f-4e25-baaf-6bf693a793ff">
---

## Models

### 1. **Position**
Defines roles within the system, such as:
- Furniture Seller
- Grill Seller
- Camping Seller

**Fields:**
- `name` (Choice Field)

---

### 2. **Manager (AbstractUser)**
Extends Django's `AbstractUser` to represent individuals managing products and brands.

**Fields:**
- `position` (Foreign Key to `Position`)
- Inherited: `username`, `password`, `email`, `first_name`, `last_name`

---

### 3. **Brand**
Stores brand details related to products.

**Fields:**
- `name`
- `country`

---

### 4. **Product**
Represents individual products under specific brands.

**Fields:**
- `name`
- `price`
- `brand` (Foreign Key to `Brand`)
- `description`
- `type` (Foreign Key to `ProductType`)
- `photo`

---

### 5. **ProductType**
Categorizes products into types, such as:
- Garden Furniture
- Grill Products
- Camping Products

**Fields:**
- `name` (Choice Field)
- `managers` (Foreign Key to `Manager`)

---

## 🚀 Installation

Follow these steps to set up the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/dmytrik/all_for_rest.git

2. **Create a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate       # Linux/Mac
   env\Scripts\activate          # Windows 

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser

6. **Start the Development Server:**
   ```bash
   python manage.py runserver

7. **Initial Data Load:**
   ```bash
   python manage.py loaddata initial_data.json
