import json
import logging
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Configure logging
logger = logging.getLogger(__name__)

# Configure Gemini API
try:
    genai.configure(api_key=settings.GEMINI_API_KEY)
    # Try different models that might work
    model = genai.GenerativeModel('gemini-pro')
    logger.info("Gemini API configured with gemini-pro model")
except Exception as e:
    logger.error(f"Failed to configure Gemini API: {str(e)}")
    model = None

# Project Description for Context
PROJECT_INFO = """
DINEAT RESTAURANT MANAGEMENT SYSTEM - COMPLETE PROJECT OVERVIEW

PROJECT STRUCTURE:
- Django-based web application for restaurant management
- Multi-role system: Admin, Kitchen Staff, Customers
- Real-time order processing and table management
- Complete payment integration with multiple methods
- AI-powered chatbot for customer support
- Mobile-responsive design with modern UI/UX

CORE FEATURES:


1. CUSTOMER-FACING FEATURES:
   - Menu browsing with categories (Vegetarian, Non-vegetarian, Appetizers, Main Course, Desserts, Beverages)
   - Real-time cart management with add/remove/update functionality
   - Table selection and reservation system with availability checking
   - Multiple payment options: COD, Credit/Debit Cards, UPI (GPay, PhonePe, Paytm), Digital Wallets
   - Order tracking with real-time status updates (Pending → Preparing → Ready → Completed)
   - Contact page with social media integration (Instagram, LinkedIn, YouTube)
   - Help and support system with comprehensive documentation
   - User account management with profile updates
   - Order history and repeat ordering capabilities
   - Email notifications for order confirmations and status updates

2. KITCHEN STAFF FEATURES:
   - Real-time order dashboard showing incoming orders with timestamps
   - Order status management (Pending, Preparing, Ready, Completed)
   - Queue management and order prioritization based on preparation time
   - Order details with customer information, table numbers, and special instructions
   - Preparation time tracking with estimated completion times
   - Order filtering by status, time, and table number
   - Bulk order status updates for efficiency
   - Kitchen inventory integration capabilities
   - Staff communication and coordination tools

3. ADMIN FEATURES:
   - Comprehensive dashboard with real-time statistics and charts
   - Order management with advanced filtering and search capabilities
   - Revenue tracking with daily, weekly, and monthly analytics
   - User management with role assignments and permissions
   - Database management (clear orders, backup, restore operations)
   - System configuration and settings management
   - Menu item management with pricing and categories
   - Table management with layout and capacity settings
   - Staff scheduling and performance tracking
   - Customer relationship management tools
   - Export functionality for reports and data analysis

TECHNICAL ARCHITECTURE:

BACKEND STACK:
- Django 5.0 framework with Python 3.11
- MySQL database with optimized ORM queries and indexing
- Role-based authentication system with custom permissions
- RESTful API design patterns for frontend-backend communication
- Secure form handling with comprehensive CSRF protection
- Session management with secure cookie handling
- Database migration system for schema updates
- Background task processing with Celery integration
- API rate limiting and request throttling
- Comprehensive logging and error tracking

FRONTEND STACK:
- HTML5 semantic markup with accessibility features
- CSS3 with modern features (Grid, Flexbox, Custom Properties)
- Vanilla JavaScript with ES6+ features
- Bootstrap 5 framework for responsive design
- Real-time updates using JavaScript Fetch API
- Progressive Web App (PWA) capabilities
- Touch-friendly interface with gesture support
- Lazy loading for optimal performance
- Service worker for offline functionality
- Cross-browser compatibility testing

DATABASE DESIGN:
- User model with role-based permissions (Admin, Kitchen Staff, Customer)
- Order model with comprehensive status tracking and timestamps
- Menu item model with categories, pricing, and availability
- Table model with capacity, location, and availability status
- Cart model for temporary order storage with session management
- Payment model with transaction history and status
- Review and rating system for customer feedback
- Inventory model for stock management
- Notification model for user alerts and updates
- Audit log model for tracking system changes

KEY PAGES AND FUNCTIONALITY:

1. HOME PAGE (main:index):
   - Restaurant overview with hero section and branding
   - Navigation to all major sections with smooth scrolling
   - Featured items and promotional banners
   - Customer testimonials and social proof
   - Real-time order statistics and activity feed
   - Call-to-action buttons for immediate engagement
   - Mobile-optimized layout with hamburger menu

2. MENU PAGE (orders:menu):
   - Categorized food items with filtering and search
   - Add to cart functionality with real-time updates
   - Item details with prices, descriptions, and images
   - Vegetarian/Non-vegetarian indicators with icons
   - Nutritional information and allergen warnings
   - Customer reviews and ratings for each item
   - Availability status and preparation time estimates
   - Recommended items and pairing suggestions

3. CART PAGE (orders:cart):
   - Real-time cart display with comprehensive item management
   - Quantity controls with increment/decrement buttons
   - Item removal with confirmation dialogs
   - Total calculation with tax and service charges
   - Promo code application and discount calculation
   - Special instructions and dietary requirements
   - Estimated preparation and delivery times
   - Proceed to payment with order summary

4. PAYMENT PAGE (main:payment):
   - Two-column layout with order details and payment options
   - Multiple payment method selection with visual indicators
   - QR code generation for UPI payments with dynamic amounts
   - Credit/debit card form with validation and security
   - Digital wallet integration with one-click payments
   - Cash on delivery option with address confirmation
   - Payment processing with loading states and confirmations
   - Invoice generation with order details and breakdown

5. KITCHEN DASHBOARD (dashboard:kitchen):
   - Real-time order queue with color-coded status indicators
   - Order status update interface with drag-and-drop functionality
   - Preparation time tracking with countdown timers
   - Order filtering by status, time, and table number
   - Customer information display with special requirements
   - Bulk operations for multiple order management
   - Kitchen performance metrics and efficiency tracking
   - Staff communication tools and internal messaging

6. ADMIN DASHBOARD (dashboard:admin):
   - Comprehensive statistics with interactive charts and graphs
   - Revenue tracking with multiple time periods and comparisons
   - Order management interface with advanced search capabilities
   - User management system with role assignments and permissions
   - Database operations with backup and restore functionality
   - System configuration with customizable settings
   - Report generation with export to multiple formats
   - Performance monitoring and system health indicators

SECURITY IMPLEMENTATION:
- CSRF protection on all forms with token validation
- Role-based access control with granular permissions
- Input validation and sanitization with comprehensive filtering
- SQL injection prevention with parameterized queries
- XSS protection with content security policy headers
- Secure password handling with bcrypt hashing
- Session security with timeout and regeneration
- API security with authentication and rate limiting
- File upload security with type and size validation
- Data encryption for sensitive information storage

INTEGRATION ECOSYSTEM:
- Google Gemini AI for intelligent chatbot responses
- Payment gateway integration with multiple providers
- Email notification system with HTML templates
- Social media integration with Instagram, LinkedIn, YouTube
- SMS gateway for order status notifications
- Analytics integration with Google Analytics
- Cloud storage for media files and backups
- Third-party delivery service integration APIs
- Accounting software integration for financial tracking
- Customer relationship management (CRM) system integration

MOBILE OPTIMIZATION:
- Fully responsive design with fluid layouts
- Touch-friendly interface with appropriate tap targets
- Optimized navigation with mobile-specific patterns
- Adaptive images with lazy loading and compression
- Mobile-specific features like geolocation services
- Progressive Web App (PWA) with offline capabilities
- Push notifications for order updates
- Mobile payment integration with digital wallets
- Gesture-based interactions and swipe actions
- Performance optimization for mobile networks

PERFORMANCE OPTIMIZATIONS:
- Database query optimization with select_related and prefetch_related
- Static file compression with Gzip and Brotli
- Efficient template rendering with fragment caching
- Minimal JavaScript with tree shaking and minification
- Image optimization with WebP format and responsive images
- CDN integration for static asset delivery
- Database indexing for improved query performance
- Memory caching with Redis for frequently accessed data
- Lazy loading for non-critical components
- Performance monitoring with real-time metrics

DEPLOYMENT ARCHITECTURE:
- Environment configuration with .env file support
- Production-ready Django settings with security optimizations
- Database migration scripts with rollback capabilities
- Comprehensive documentation with API specifications
- Docker containerization for consistent deployments
- CI/CD pipeline with automated testing and deployment
- Load balancing for high availability
- Database replication for data redundancy
- Monitoring and alerting system integration
- Backup and disaster recovery procedures

DEVELOPMENT WORKFLOW:
- Version control with Git and feature branching
- Code review process with pull requests
- Automated testing with unit and integration tests
- Code quality tools with linting and formatting
- Documentation generation with automatic updates
- Development environment with Docker Compose
- Staging environment for testing and validation
- Performance testing with load and stress testing
- Security scanning with vulnerability assessment
- Continuous integration with automated builds

BUSINESS INTELLIGENCE:
- Real-time analytics dashboard with customizable widgets
- Customer behavior tracking and analysis
- Sales trend analysis with predictive modeling
- Inventory optimization with demand forecasting
- Staff performance metrics and productivity analysis
- Customer satisfaction tracking with sentiment analysis
- Market analysis with competitor comparison
- Financial reporting with profit and loss analysis
- Operational efficiency metrics and KPI tracking
- Strategic planning tools with scenario modeling

SCALABILITY FEATURES:
- Horizontal scaling with load balancer support
- Database sharding for large dataset handling
- Microservices architecture for modular growth
- API gateway for service management and routing
- Message queue system for asynchronous processing
- Caching layers for improved response times
- Auto-scaling based on traffic patterns
- Geographic distribution for global reach
- Database connection pooling for efficiency
- Resource monitoring and automatic optimization

The DineAt system represents a complete, enterprise-grade restaurant management solution that combines cutting-edge technology with practical business needs. It provides seamless integration between customers, kitchen operations, and administrative functions while maintaining high standards of security, performance, and user experience. The system is designed for scalability and can handle restaurants of any size, from small cafes to large restaurant chains.
"""

@csrf_exempt
@require_http_methods(["POST"])
def chat_view(request):
    """
    API Endpoint for the Chatbot.
    Accepts JSON: {"message": "user question"}
    Returns JSON: {"status": "success", "response": "bot response"}
    """
    try:
        # Parse Request Body
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()

        if not user_message:
            return JsonResponse({"status": "error", "response": "Message field is required."}, status=400)

        # Fallback responses when API is not available
        bot_reply = get_fallback_response(user_message)
        
        # Try to use Gemini API if available
        if model:
            try:
                prompt = f"""You are a chatbot for a specific software project.

Project details:
{PROJECT_INFO}

Rules:
* Answer only from project details
* Do not use external knowledge
* If unrelated question, reply exactly: "This question is outside the project scope."
* Keep answers concise and helpful.

User question:
{user_message}"""

                response = model.generate_content(prompt)
                bot_reply = response.text.strip()
            except Exception as api_error:
                logger.error(f"Gemini API error: {str(api_error)}")
                # Use fallback response
                bot_reply = get_fallback_response(user_message)

        return JsonResponse({"status": "success", "response": bot_reply})

    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "response": "Invalid JSON format."}, status=400)
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        return JsonResponse({"status": "error", "response": f"An internal error occurred: {str(e)}"}, status=500)

def get_fallback_response(message):
    """Fallback responses for when API is unavailable"""
    message_lower = message.lower()
    
    # Special greeting for hi/hello
    if any(keyword in message_lower for keyword in ['hi', 'hello', 'hey', 'hii', 'hiii']):
        return "🎉 Welcome to DineAt! I'm your personal restaurant assistant!"
    
    # Menu and food categories
    if any(keyword in message_lower for keyword in ['menu', 'food', 'order', 'eat', 'dish', 'vegetarian', 'non-vegetarian', 'appetizer', 'dessert', 'beverage']):
        return "🍽️ Our comprehensive menu with prices:\n\n🥗 **VEGETARIAN**\n• Veg Biryani - ₹180\n• Paneer Butter Masala - ₹220\n• Veg Pulao - ₹160\n• Dal Makhani - ₹200\n• Mixed Veg - ₹180\n\n🍖 **NON-VEGETARIAN**\n• Chicken Biryani - ₹220\n• Butter Chicken - ₹250\n• Mutton Curry - ₹280\n• Fish Fry - ₹200\n• Egg Curry - ₹180\n\n🥗 **APPETIZERS**\n• Samosa - ₹30\n• Spring Roll - ₹80\n• Paneer Tikka - ₹150\n• Chicken Wings - ₹180\n\n🍛 **MAIN COURSE**\n• Naan - ₹20\n• Roti - ₹15\n• Rice - ₹60\n• Raita - ₹40\n\n🍰 **DESSERTS**\n• Gulab Jamun - ₹60\n• Ice Cream - ₹80\n• Ras Malai - ₹70\n\n🥤 **BEVERAGES**\n• Lemon Juice - ₹40\n• Mango Lassi - ₹60\n• Soda - ₹30\n\nEach item includes detailed descriptions, nutritional info, allergen warnings, and preparation time estimates. Browse with filtering and search, add to cart with real-time updates!"
    
    # Specific menu item prices
    if any(keyword in message_lower for keyword in ['price', 'cost', 'rate', 'how much', 'menu item', 'item price']):
        return "💰 **DineAt Menu Prices:**\n\n🥗 **VEGETARIAN:** Veg Biryani ₹180 | Paneer Butter Masala ₹220 | Veg Pulao ₹160 | Dal Makhani ₹200 | Mixed Veg ₹180\n\n🍖 **NON-VEGETARIAN:** Chicken Biryani ₹220 | Butter Chicken ₹250 | Mutton Curry ₹280 | Fish Fry ₹200 | Egg Curry ₹180\n\n🥗 **APPETIZERS:** Samosa ₹30 | Spring Roll ₹80 | Paneer Tikka ₹150 | Chicken Wings ₹180\n\n🍛 **MAIN COURSE:** Naan ₹20 | Roti ₹15 | Rice ₹60 | Raita ₹40\n\n🍰 **DESSERTS:** Gulab Jamun ₹60 | Ice Cream ₹80 | Ras Malai ₹70\n\n🥤 **BEVERAGES:** Lemon Juice ₹40 | Mango Lassi ₹60 | Soda ₹30\n\nAll prices include tax. Add items to cart for real-time total calculation!"
    
    # Specific menu items - Vegetarian
    if any(keyword in message_lower for keyword in ['veg biryani', 'vegetable biryani']):
        return "🍛 **Veg Biryani** - ₹180\n\n📝 **Description:** Fragrant basmati rice cooked with mixed vegetables, aromatic spices, and herbs.\n⏱️ **Preparation Time:** 15 minutes\n🌱 **Category:** Vegetarian\n🥗 **Nutritional Info:** 320 calories, Protein 8g, Carbs 45g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['paneer butter masala', 'paneer']):
        return "🧈 **Paneer Butter Masala** - ₹220\n\n📝 **Description:** Soft cottage cheese cubes in rich, creamy tomato-based gravy with butter and aromatic spices.\n⏱️ **Preparation Time:** 20 minutes\n🌱 **Category:** Vegetarian\n🥗 **Nutritional Info:** 380 calories, Protein 18g, Carbs 22g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['veg pulao', 'vegetable pulao']):
        return "🍚 **Veg Pulao** - ₹160\n\n📝 **Description:** Fluffy basmati rice cooked with seasonal vegetables and mild spices.\n⏱️ **Preparation Time:** 12 minutes\n🌱 **Category:** Vegetarian\n🥗 **Nutritional Info:** 280 calories, Protein 6g, Carbs 42g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['dal makhani']):
        return "🍲 **Dal Makhani** - ₹200\n\n📝 **Description:** Creamy black lentils cooked overnight with butter, cream, and aromatic spices.\n⏱️ **Preparation Time:** 25 minutes\n🌱 **Category:** Vegetarian\n🥗 **Nutritional Info:** 290 calories, Protein 12g, Carbs 35g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    # Specific menu items - Non-Vegetarian
    if any(keyword in message_lower for keyword in ['chicken biryani']):
        return "🍗 **Chicken Biryani** - ₹220\n\n📝 **Description:** Aromatic basmati rice with tender chicken pieces, exotic spices, and herbs.\n⏱️ **Preparation Time:** 20 minutes\n🍖 **Category:** Non-Vegetarian\n🥗 **Nutritional Info:** 420 calories, Protein 28g, Carbs 38g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['butter chicken']):
        return "🍗 **Butter Chicken** - ₹250\n\n📝 **Description:** Tender chicken pieces in rich, creamy tomato-based gravy with butter and aromatic spices.\n⏱️ **Preparation Time:** 25 minutes\n🍖 **Category:** Non-Vegetarian\n🥗 **Nutritional Info:** 450 calories, Protein 32g, Carbs 28g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['mutton curry']):
        return "🥩 **Mutton Curry** - ₹280\n\n📝 **Description:** Tender mutton pieces cooked in spicy, aromatic gravy with traditional spices.\n⏱️ **Preparation Time:** 30 minutes\n🍖 **Category:** Non-Vegetarian\n🥗 **Nutritional Info:** 480 calories, Protein 35g, Carbs 25g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['fish fry']):
        return "🐟 **Fish Fry** - ₹200\n\n📝 **Description:** Fresh fish fillets marinated in spices and pan-fried to golden perfection.\n⏱️ **Preparation Time:** 18 minutes\n🍖 **Category:** Non-Vegetarian\n🥗 **Nutritional Info:** 320 calories, Protein 24g, Carbs 12g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    # Specific menu items - Appetizers
    if any(keyword in message_lower for keyword in ['samosa']):
        return "🥟 **Samosa** - ₹30\n\n📝 **Description:** Crispy triangular pastry filled with spiced potatoes and peas.\n⏱️ **Preparation Time:** 8 minutes\n🌱 **Category:** Vegetarian Appetizer\n🥗 **Nutritional Info:** 120 calories, Protein 3g, Carbs 18g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['spring roll']):
        return "🥢 **Spring Roll** - ₹80\n\n📝 **Description:** Crispy rolls filled with mixed vegetables and served with sweet chili sauce.\n⏱️ **Preparation Time:** 10 minutes\n🌱 **Category:** Vegetarian Appetizer\n🥗 **Nutritional Info:** 180 calories, Protein 4g, Carbs 22g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['paneer tikka']):
        return "🍢 **Paneer Tikka** - ₹150\n\n📝 **Description:** Marinated cottage cheese cubes grilled in tandoor with vegetables and spices.\n⏱️ **Preparation Time:** 15 minutes\n🌱 **Category:** Vegetarian Appetizer\n🥗 **Nutritional Info:** 240 calories, Protein 14g, Carbs 16g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    # Specific menu items - Main Course
    if any(keyword in message_lower for keyword in ['naan']):
        return "🍞 **Naan** - ₹20\n\n📝 **Description:** Soft, fluffy leavened flatbread baked in tandoor.\n⏱️ **Preparation Time:** 5 minutes\n🌱 **Category:** Main Course Bread\n🥗 **Nutritional Info:** 90 calories, Protein 3g, Carbs 18g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['roti']):
        return "🫓 **Roti** - ₹15\n\n📝 **Description:** Whole wheat unleavened flatbread cooked on griddle.\n⏱️ **Preparation Time:** 3 minutes\n🌱 **Category:** Main Course Bread\n🥗 **Nutritional Info:** 70 calories, Protein 2g, Carbs 15g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    # Specific menu items - Desserts
    if any(keyword in message_lower for keyword in ['gulab jamun']):
        return "🍮 **Gulab Jamun** - ₹60\n\n📝 **Description:** Soft milk solids dumplings soaked in rose-flavored sugar syrup.\n⏱️ **Preparation Time:** 5 minutes\n🌱 **Category:** Vegetarian Dessert\n🥗 **Nutritional Info:** 180 calories, Protein 4g, Carbs 28g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['ice cream']):
        return "🍨 **Ice Cream** - ₹80\n\n📝 **Description:** Creamy frozen dessert available in vanilla, chocolate, and strawberry flavors.\n⏱️ **Preparation Time:** 2 minutes\n🌱 **Category:** Vegetarian Dessert\n🥗 **Nutritional Info:** 220 calories, Protein 4g, Carbs 26g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    # Specific menu items - Beverages
    if any(keyword in message_lower for keyword in ['lemon juice', 'lime juice']):
        return "🍋 **Lemon Juice** - ₹40\n\n📝 **Description:** Fresh lemon juice with water, sugar, and mint leaves.\n⏱️ **Preparation Time:** 3 minutes\n🌱 **Category:** Vegetarian Beverage\n🥗 **Nutritional Info:** 60 calories, Protein 0g, Carbs 15g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    if any(keyword in message_lower for keyword in ['mango lassi']):
        return "🥭 **Mango Lassi** - ₹60\n\n📝 **Description:** Creamy yogurt drink with sweet mango pulp and cardamom.\n⏱️ **Preparation Time:** 5 minutes\n🌱 **Category:** Vegetarian Beverage\n🥗 **Nutritional Info:** 140 calories, Protein 4g, Carbs 24g\n✅ **Available:** Yes\n\nAdd to cart for real-time ordering!"
    
    # Cart and ordering system
    if any(keyword in message_lower for keyword in ['cart', 'add', 'remove', 'quantity', 'update', 'promo', 'discount']):
        return "🛒 Advanced cart management with real-time updates! Add/remove items, update quantities with increment/decrement buttons, apply promo codes for discounts, calculate totals with tax and service charges, add special instructions and dietary requirements, see estimated preparation times, and proceed to payment with detailed order summary!"
    
    # Order tracking and status
    if any(keyword in message_lower for keyword in ['track', 'status', 'where', 'delivery', 'pending', 'preparing', 'ready', 'completed', 'notification']):
        return "📋 Complete order tracking system: Real-time status updates (Pending → Preparing → Ready → Completed), email notifications for confirmations and status changes, SMS gateway notifications, preparation time tracking with countdown timers, estimated delivery times, and comprehensive order history with repeat ordering capabilities!"
    
    # Payment methods detailed
    if any(keyword in message_lower for keyword in ['payment', 'pay', 'card', 'upi', 'wallet', 'cash', 'gpay', 'phonepe', 'paytm', 'transaction', 'invoice']):
        return "💳 Comprehensive payment system: • Cash on Delivery with address confirmation • Credit/Debit Cards with secure validation • UPI (GPay, PhonePe, Paytm) with dynamic QR code generation • Digital Wallets with one-click payments • Payment processing with loading states • Invoice generation with detailed breakdown • Transaction history and status tracking!"
    
    # Table reservation system
    if any(keyword in message_lower for keyword in ['table', 'booking', 'reservation', 'seat', 'availability', 'capacity', 'layout']):
        return "🍽️ Smart table management: Visual table selection with availability checking, capacity and location settings, automatic reservation when ordering, special requirements and dietary accommodations, table layout management for restaurant configuration, and real-time availability updates across all devices!"
    
    # Kitchen operations
    if any(keyword in message_lower for keyword in ['kitchen', 'chef', 'staff', 'preparation', 'queue', 'cooking', 'inventory']):
        return "🍳 Advanced kitchen operations: Real-time order dashboard with color-coded status, drag-and-drop order management, preparation time tracking with countdown timers, bulk order status updates, kitchen inventory integration, staff communication tools, performance metrics tracking, and order filtering by status, time, and table number!"
    
    # Admin dashboard and management
    if any(keyword in message_lower for keyword in ['admin', 'dashboard', 'analytics', 'revenue', 'statistics', 'management', 'reports', 'export']):
        return "📊 Powerful admin dashboard: Comprehensive real-time statistics with interactive charts, revenue tracking with multiple time periods, advanced order management with search capabilities, user management with role assignments, database operations (backup/restore), report generation with export to multiple formats, staff scheduling and performance tracking, CRM tools, and system health monitoring!"
    
    # Technical architecture
    if any(keyword in message_lower for keyword in ['technology', 'tech', 'backend', 'frontend', 'database', 'django', 'architecture', 'stack']):
        return "🛠️ Enterprise-grade tech stack: Backend - Django 5.0 with Python 3.11, MySQL with optimized queries, RESTful APIs, Celery for background tasks. Frontend - HTML5, CSS3, ES6+ JavaScript, Bootstrap 5, PWA capabilities. Database - User/Order/Menu/Table/Payment models with relationships. Security - CSRF, XSS protection, bcrypt hashing, rate limiting!"
    
    # Security features
    if any(keyword in message_lower for keyword in ['security', 'csrf', 'authentication', 'protection', 'safe', 'encryption', 'sql injection']):
        return "🔒 Comprehensive security implementation: CSRF protection with token validation, role-based access control with granular permissions, input validation and sanitization, SQL injection prevention with parameterized queries, XSS protection with CSP headers, secure password handling with bcrypt, session security with timeout regeneration, API authentication and rate limiting, file upload security, and data encryption!"
    
    # Mobile and performance
    if any(keyword in message_lower for keyword in ['mobile', 'responsive', 'phone', 'tablet', 'touch', 'performance', 'speed', 'optimization', 'pwa']):
        return "📱 Mobile-optimized with PWA: Fully responsive design with fluid layouts, touch-friendly interface with gesture support, Progressive Web App capabilities with offline functionality, push notifications for order updates, lazy loading for performance, image optimization with WebP format, CDN integration, mobile payment integration, and performance monitoring for mobile networks!"
    
    # Integrations and APIs
    if any(keyword in message_lower for keyword in ['integration', 'api', 'gemini', 'ai', 'email', 'sms', 'social media', 'analytics']):
        return "🔗 Rich integration ecosystem: Google Gemini AI for intelligent chatbot, multiple payment gateway providers, email notification system with HTML templates, SMS gateway for status updates, social media integration (Instagram, LinkedIn, YouTube), Google Analytics integration, cloud storage for media, third-party delivery service APIs, accounting software integration, and CRM system connectivity!"
    
    # Deployment and scalability
    if any(keyword in message_lower for keyword in ['deploy', 'production', 'hosting', 'environment', 'migration', 'docker', 'scalability', 'load balancing']):
        return "🚀 Production-ready deployment: Environment configuration with .env support, Django production settings with security optimizations, database migration scripts with rollback, Docker containerization, CI/CD pipeline with automated testing, load balancing for high availability, database replication for redundancy, monitoring and alerting, backup procedures, and horizontal scaling capabilities!"
    
    # Development workflow
    if any(keyword in message_lower for keyword in ['development', 'workflow', 'git', 'testing', 'code review', 'documentation', 'ci/cd']):
        return "💻 Professional development workflow: Version control with Git and feature branching, code review process with pull requests, automated testing with unit and integration tests, code quality tools with linting, automatic documentation generation, Docker Compose development environment, staging for testing, performance and security testing, and continuous integration with automated builds!"
    
    # Business intelligence
    if any(keyword in message_lower for keyword in ['business', 'intelligence', 'analytics', 'metrics', 'kpi', 'forecasting', 'customer behavior']):
        return "📈 Advanced business intelligence: Real-time analytics with customizable widgets, customer behavior tracking and analysis, sales trend analysis with predictive modeling, inventory optimization with demand forecasting, staff performance metrics, customer satisfaction tracking with sentiment analysis, market analysis with competitor comparison, financial reporting, and strategic planning tools!"
    
    # User roles and permissions
    if any(keyword in message_lower for keyword in ['roles', 'permissions', 'admin', 'staff', 'customer', 'access', 'authentication']):
        return "👥 Three-tier role system: Admin (full system access, analytics, user management, database operations), Kitchen Staff (order management, status updates, preparation tracking, inventory), Customer (ordering, tracking, payments, profile management). Role-based permissions ensure secure access control with granular permissions for each user type!"
    
    # Database and data management
    if any(keyword in message_lower for keyword in ['database', 'data', 'models', 'orm', 'query', 'backup', 'restore']):
        return "🗄️ Robust database architecture: MySQL with optimized ORM queries, comprehensive models (User, Order, MenuItem, Table, Cart, Payment, Review, Inventory, Notification, AuditLog), database indexing for performance, query optimization with select_related/prefetch_related, backup and restore operations, migration system with rollback capabilities, and audit logging for data changes!"
    
    # Contact and support
    if any(keyword in message_lower for keyword in ['help', 'support', 'contact', 'phone', 'email', 'whatsapp', 'documentation']):
        return "📞 Comprehensive support system: Contact page with social media integration, real-time AI chatbot support (that's me! 😊), detailed help documentation, email notifications, customer relationship management tools, feedback and review system, and multi-channel support including phone, email, WhatsApp, and live chat for complete customer assistance!"
    
    # Project overview and capabilities
    if any(keyword in message_lower for keyword in ['project', 'about', 'dineat', 'restaurant', 'system', 'overview', 'capabilities', 'features']):
        return "🏢 DineAt is an enterprise-grade restaurant management solution! Complete features: 📱 Customer ordering with 6 menu categories 🛒 Real-time cart management 🍳 Kitchen operations dashboard 📊 Admin analytics 💳 Multiple payment methods 🤖 AI chatbot support 📱 Mobile PWA 🛠️ Modern tech stack 🔒 Enterprise security 📈 Business intelligence 🚀 Production deployment. Handles restaurants of any size!"
    
    # Default comprehensive response
    return "🤖 I'm your complete DineAt expert! Ask me about: 🍽️ Menu & Food Categories 🛒 Cart & Ordering 📋 Order Tracking 💳 Payment Systems 🍽️ Table Reservations 🍳 Kitchen Operations 📊 Admin Analytics 🛠️ Technical Architecture 🔒 Security Features 📱 Mobile Performance 🔗 Integrations 🚀 Deployment 💻 Development Workflow 📈 Business Intelligence 🗄️ Database Design 👥 User Roles 📞 Support System! Type any detailed question!"

@csrf_exempt
@require_http_methods(["GET"])
def chatbot_status(request):
    """Check chatbot status"""
    if model:
        return JsonResponse({
            "status": "available",
            "message": "Chatbot is online with AI capabilities"
        })
    else:
        return JsonResponse({
            "status": "unavailable", 
            "message": "AI is unavailable, using fallback responses"
        })
