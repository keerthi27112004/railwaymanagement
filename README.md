# Railway Management System

A web-based **Railway Management System** that allows users to check train availability, book seats, and manage railway data with **role-based access control (RBAC)**.

---

## **Features**
- **User Authentication**
  - Register a user
  - Login with JWT authentication
- **Train Management** (Admin only)
  - Add new trains
  - View available trains between stations
- **Booking System** (Authenticated Users)
  - Check seat availability
  - Book seats with race condition handling (transactions)
  - View booking details

---

## **Tech Stack**
- **Backend:** Django + Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Token)
- **Race Condition Handling:** PostgreSQL Transactions (`select_for_update`)
- **Security:** Role-based access control (RBAC)

---

## **Installation**
### **1️⃣ Go to the Project Folder**
```sh
cd railway_management
```

### **2️⃣ Create and Activate Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configure Database (PostgreSQL)**
Edit `settings.py` and update:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### **5️⃣ Run Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **6️⃣ Create Superuser (Admin)**
```sh
python manage.py createsuperuser
```

### **7️⃣ Start the Server**
```sh
python manage.py runserver
```

---
