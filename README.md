# DineAt Restaurant Management System

A comprehensive frontend solution for restaurant management with customer ordering, kitchen management, and admin controls.

## 🚀 Getting Started

1. Open `index.html` in your web browser to start the application
2. Navigate through different sections based on your user role

## 📱 Pages & Navigation

### Public Pages (No Login Required)
- **index.html** - Home page with overview and navigation
- **login.html** - Login type selection (Customer/Kitchen/Admin)
- **customer-login.html** - Customer authentication
- **kitchen-login.html** - Kitchen staff authentication  
- **admin-login.html** - Administrator authentication
- **about.html** - About the restaurant
- **contact.html** - Contact information and form
- **help.html** - Help documentation and FAQs

### Customer Pages (Login Required)
- **table-selection.html** - Select dining table
- **menu.html** - Browse menu and add items to cart
- **cart.html** - View cart and process payment
- **order-confirmation.html** - Order success confirmation

### Kitchen Pages (Kitchen Login Required)
- **kitchen-dashboard.html** - Order management for kitchen staff

### Admin Pages (Admin Login Required)
- **admin-dashboard.html** - Complete system administration

## 🔐 User Flow

### Customer Flow
1. Login → Select Table → Browse Menu → Add to Cart → Payment → Order Confirmation

### Kitchen Staff Flow
1. Login → View Orders → Confirm Orders → Mark Ready → Complete Orders

### Admin Flow
1. Login → Dashboard → Manage Orders/Menu/Tables/Payments

## 🎯 Key Features

### Customer Features
- Table selection with real-time availability
- Menu categorized by type (Veg, Non-Veg, Desserts, Beverages)
- Shopping cart with add/remove functionality
- Multiple payment options (Cash, Card, UPI, Wallet)
- Order tracking and confirmation
- Star ratings and reviews for dishes

### Kitchen Features
- Real-time order viewing
- Order status management (Pending → Confirmed → Ready → Served)
- Table-specific order tracking
- Order cancellation capabilities

### Admin Features
- Complete order management (view, edit, cancel, add)
- Menu item management (add, edit, delete)
- Table status monitoring
- Payment history tracking
- Revenue and statistics dashboard

## 🔧 Technical Features

- **Responsive Design** - Works on all devices
- **Local Storage** - Cart and session persistence
- **Role-based Access** - Secure page navigation
- **Modern UI** - Clean, professional interface
- **Form Validation** - Input validation and error handling
- **Notifications** - User-friendly feedback system

## 📂 File Structure

```
DineAt Project/
├── index.html                 # Home page
├── login.html                 # Login selection
├── customer-login.html        # Customer login
├── kitchen-login.html         # Kitchen login
├── admin-login.html           # Admin login
├── table-selection.html       # Table booking
├── menu.html                  # Menu browsing
├── cart.html                  # Shopping cart
├── order-confirmation.html    # Order success
├── kitchen-dashboard.html     # Kitchen management
├── admin-dashboard.html       # Admin panel
├── about.html                 # About page
├── contact.html               # Contact page
├── help.html                  # Help documentation
├── styles.css                 # Main stylesheet
├── script.js                  # JavaScript functionality
└── README.md                  # This file
```

## 🎨 Navigation System

All pages are interconnected through:
- **Navigation Bar** - Consistent across all pages
- **Role-based Redirects** - Automatic navigation based on user type
- **Protected Routes** - Login required for certain pages
- **Smart Navigation** - Context-aware page transitions

## 🔗 Page Connections

### From Home Page
- → Login Page
- → About Page
- → Contact Page  
- → Help Page
- → Menu Page (if logged in)

### From Login Page
- → Customer Login
- → Kitchen Login
- → Admin Login

### After Login
- Customer → Table Selection
- Kitchen → Kitchen Dashboard
- Admin → Admin Dashboard

### Cross-Page Features
- Cart persists across menu and cart pages
- User session maintained across all pages
- Logout returns to home page
- Smart redirects based on user role

## 🚀 Quick Start

1. Open `index.html`
2. Click "Get Started" to go to login
3. Select your user type
4. Enter credentials (any credentials work for demo)
5. Navigate through your role-specific workflow

## 📞 Support

For any issues or questions:
- Check the Help page (`help.html`)
- Contact information available on Contact page
- Built-in notifications guide users through the process

---

**Note**: This is a frontend demonstration. Backend integration would be required for production use with real data persistence and user authentication.
