# 🛒 Django E-Commerce Website

A full-featured e-commerce website built using **Django**, **Tailwind CSS**, and **Django REST Framework**. The project includes features like product catalog, cart system, checkout, orders, user authentication, and an admin dashboard.

---

## 🚀 Features

- ✅ User Registration and Login (JWT and Session)
- 🛍️ Product Catalog with multiple images
- 🛒 Add to Cart, Wishlist, and Checkout
- 💳 Order Placement (Cash on Delivery)
- 🧾 My Orders and Order Details with Cancel Option
- 📦 Admin Dashboard (Sales, Profit, Inventory)
- 📈 Analytics by Category and Top Products
- 🎨 Tailwind CSS for responsive frontend
- 🔐 Token-based authentication for API
- ⚙️ Django Admin for backend management

---


---

## ⚙️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: Tailwind CSS, HTML5
- **Authentication**: JWT + Session Auth
- **Database**: SQLite (Dev), PostgreSQL (Recommended)
- **Deployment**: PythonAnywhere, GitHub
- **Package Management**: pip, virtualenv

---

## 🧪 API Endpoints (DRF)

> Example: `api/products/`, `api/cart/`, `api/orders/`, `api/token/`, `api/user/register/`

You can test APIs using **Postman** or **Swagger UI** (if enabled).

---

## 🖥️ Setup Locally

```bash
# 1. Clone the project
git clone https://github.com/niteshsaroj/E-commerce.git
cd E-commerce

# 2. Create and activate virtualenv
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
# OR
.venv\Scripts\activate     # For Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Build Tailwind CSS
npm init -y
npm install tailwindcss @tailwindcss/cli

# 7. After package.json (inside Scripts)
"watch:css": "npx @tailwindcss/cli -i ./static/css/src/input.css -o ./static/css/src/output.css --watch"

# 8. Run Tailwind 
npm run watch:css

# 9. Run server
python manage.py runserver

```

🙋‍♂️ Author
Nitesh Saroj
📫 Email: nitshsaroj517@gmail.com
