# 🛒 Django E-Commerce Website

A full-featured e-commerce website built using **Django**, **Tailwind CSS**, and **Django REST Framework**. The project includes features like product catalog, cart system, checkout, orders, user authentication, and an admin dashboard.

---

## 🚀 Features

- ✅ User Registration and Login (JWT and Session)
- 🛍️ Product Catalog with multiple images
- 🛒 Add to Cart, Wishlist, and Checkout
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

## 🛠️ View :
<img width="1920" height="1080" alt="Screenshot 2025-08-01 132717" src="https://github.com/user-attachments/assets/16a5a55b-49fa-4768-8160-d772b0f55824" />
<img width="1390" height="794" alt="Screenshot 2025-08-01 132813" src="https://github.com/user-attachments/assets/85665af6-7bf9-4d65-b9a0-481981faef61" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 133306" src="https://github.com/user-attachments/assets/1a32650f-58d6-4a2c-ad11-e43542a614d6" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 133228" src="https://github.com/user-attachments/assets/f4a62167-7e63-4a54-bab3-a8a1ef531d61" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 133148" src="https://github.com/user-attachments/assets/c597d13f-9620-4c67-a6da-228c79bfaa1f" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 133057" src="https://github.com/user-attachments/assets/098f1680-fc7f-4cf8-9270-d3598ec135aa" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 133024" src="https://github.com/user-attachments/assets/b892fa31-f289-4b6e-9a59-73d475635962" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 133003" src="https://github.com/user-attachments/assets/27cb7868-c8cd-4c2a-b617-1ff747bf1db5" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 132929" src="https://github.com/user-attachments/assets/4273f5df-05b8-45d8-8d2a-0ecd3d0c082d" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 132909" src="https://github.com/user-attachments/assets/d02260a6-9932-4dfb-b288-009773357bdd" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 132843" src="https://github.com/user-attachments/assets/c9ef93a4-de8f-44da-b845-079558fc6299" />

🙋‍♂️ Author
Nitesh Saroj
📫 Email: nitshsaroj517@gmail.com
