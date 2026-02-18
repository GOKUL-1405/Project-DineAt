# DineAt - Restaurant Management System

A comprehensive Django-based restaurant management system with MySQL database, supporting role-based access for customers, kitchen staff, and administrators.

## 🚀 Features

- **Role-Based Authentication**: Separate login portals for customers, kitchen staff, and administrators
- **Menu Management**: Browse menu items by category with search functionality
- **Order System**: Complete ordering workflow with cart, table selection, and confirmation
- **Kitchen Dashboard**: Real-time order management with kanban-style board
- **Admin Dashboard**: Statistics, order management, and system oversight
- **Responsive Design**: Modern, mobile-friendly interface

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL 5.7 or higher
- pip (Python package manager)

## 🛠️ Installation

### 1. Clone or Navigate to Project Directory

```bash
cd c:\Users\Gokul Kumar\Desktop\pro\backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up MySQL Database

**Create Database:**
```sql
CREATE DATABASE dineat_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Create MySQL User (Optional but recommended):**
```sql
CREATE USER 'dineat_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON dineat_db.* TO 'dineat_user'@'localhost';
FLUSH PRIVILEGES;
```

### 6. Configure Environment Variables

Copy the example environment file:
```bash
copy .env.example .env
```

Edit `.env` file with your database credentials:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=dineat_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

**Generate a secure secret key:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 7. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 9. Create Sample Data (Optional)

Access Django admin at `http://localhost:8000/admin` and create:
- Menu items
- Tables
- Additional users (kitchen staff, customers)

### 10. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## 📁 Project Structure

```
backend/
├── DineAt/                 # Project configuration
│   ├── settings.py        # Django settings with MySQL config
│   ├── urls.py           # Root URL configuration
│   ├── wsgi.py           # WSGI entry point
│   └── asgi.py           # ASGI entry point
├── apps/
│   ├── accounts/         # User authentication & roles
│   ├── orders/           # Menu & ordering system
│   ├── dashboard/        # Admin & kitchen dashboards
│   └── main/             # Public pages
├── templates/            # HTML templates
├── static/              # CSS, JavaScript, images
├── media/               # User uploads
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## 👥 User Roles

### Customer
- Browse menu
- Add items to cart
- Select table
- Place orders
- View order status

### Kitchen Staff
- View incoming orders
- Update order status (Preparing, Ready, Served)
- Manage order workflow

### Administrator
- Full system access
- View statistics and analytics
- Manage menu items
- Manage users
- Oversee all orders

## 🔗 Key URLs

- **Homepage**: `/`
- **Menu**: `/orders/menu/`
- **Cart**: `/orders/cart/`
- **Customer Login**: `/accounts/login/customer/`
- **Kitchen Login**: `/accounts/login/kitchen/`
- **Admin Login**: `/accounts/login/admin/`
- **Admin Dashboard**: `/dashboard/admin/`
- **Kitchen Dashboard**: `/dashboard/kitchen/`
- **Django Admin**: `/admin/`

## 🎨 Customization

### Adding Menu Items
1. Log in to Django admin (`/admin/`)
2. Navigate to "Menu Items"
3. Click "Add Menu Item"
4. Fill in details and upload image
5. Save

### Creating Users
1. Access Django admin
2. Go to "Users"
3. Create user and assign role (ADMIN, KITCHEN, or CUSTOMER)

## 🐛 Troubleshooting

### Database Connection Error
- Verify MySQL is running
- Check credentials in `.env` file
- Ensure database exists

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Migration Issues
```bash
python manage.py makemigrations --empty appname
python manage.py migrate --fake
```

## 📝 License

This project is created for educational purposes.

## 🤝 Support

For issues or questions, please contact the development team.

---

**Built with Django 5.0 & MySQL** 🚀
