# Welcome to the Grocery Store App

![Grocery Store App](grocery-store.png)

The **Grocery Store App** is a user-friendly and efficient web application designed to streamline your grocery shopping experience. Whether you're a customer looking to easily browse and purchase products or an admin wanting to manage categories and products effortlessly, this app has you covered. With a powerful tech stack comprising **Python Flask**, **SQLAlchemy**, **SQLite**, and **Bootstrap**, we've created a seamless and visually appealing solution for all your grocery store needs.
## Quick Guide: Running Your Flask Application

1. **Virtual Environment:**
   - Create: `python -m venv venv`
   - Activate:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`

2. **Install Modules:**
   - In venv: `pip install -r requirements.txt`

3. **Database Setup:**
   - Ensure `instance/store.sqlite3` or schema is ready.

4. **Admin Config:**
   - Update `config.json` with admin info.

5. **Initialize Database:**
   - Activate venv and run:
     ```python
     python
     from app import db
     db.create_all()
     exit()
     ```

6. **Run Flask App:**
   - Terminal: `python app.py`

7. **Access App:**
   - Browser: `http://127.0.0.1:5000/`

8. **Interact:**
   - Explore the app.

Adjust steps as needed for your project's setup.

## Features

- **User-Friendly Interface:** The app boasts an intuitive and visually pleasing design, making it easy for both new and returning customers to navigate and shop.
  
- **User Authentication:** New users can register by providing a unique username and secure password. Returning users can easily sign in to their accounts for a personalized shopping experience.
  
- **Admin Panel:** Administrators have access to a robust admin panel that offers complete control over the app's inventory. CRUD (Create, Read, Update, Delete) operations are available for both categories and products.
  
- **Effortless Category Management:** Admins can seamlessly add, edit, and delete product categories through the admin panel, ensuring a well-organized inventory.
  
- **Comprehensive Product Management:** Admins have the ability to manage products with ease. They change order status.
- **Comprehensive Product Management:** Admins have the ability to manage products with ease. They change order status.
- **Comprehensive Inventory Management:** After order is confirmed, Inventory will be managed accordingly.

## Tech Stack

- **Python Flask:** A powerful and flexible web framework that enables rapid development of web applications.
  
- **SQLAlchemy:** A widely-used SQL toolkit and Object-Relational Mapping (ORM) library that simplifies database management and interactions.
  
- **SQLite:** A lightweight and efficient database engine, perfect for small to medium-sized applications.
  
- **Bootstrap:** A popular front-end framework that ensures a responsive and visually appealing user interface.
