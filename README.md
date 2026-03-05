# 🚀 Full Stack Project Generator

This Python script helps developers **quickly bootstrap a full-stack project** by automating the creation of:

* Python **Virtual Environment**
* **React Frontend (Vite)**
* **Django Backend**
* **Frontend folder structure with JSX boilerplate and CSS files**

It reduces repetitive setup tasks and helps you start development faster.

---

# 📦 Features

### 1️⃣ Create Python Virtual Environment

Automatically creates a Python virtual environment using `venv`.

Example:

```
myenv/
```

---

### 2️⃣ Create React Frontend (Vite)

Uses **Vite + React** to generate a frontend project quickly.

Command used internally:

```
npx create-vite@latest frontend --template react
```

---

### 3️⃣ Create Django Backend

Creates a **Django REST backend** and installs required dependencies:

Installed packages:

* Django
* Django REST Framework
* Simple JWT Authentication
* CORS Headers
* Pillow

Backend structure example:

```
backend/
 ├── manage.py
 ├── backend/
 │   ├── settings.py
 │   ├── urls.py
 │   └── asgi.py
```

---

### 4️⃣ Generate Frontend Folder Structure

Automatically generates **organized React folders** with JSX components and CSS files.

Example generated structure:

```
frontend
 ├── home
 │   ├── css
 │   │   └── hero.css
 │   └── jsx
 │       └── Hero.jsx
 │
 ├── about
 │   ├── css
 │   │   └── about.css
 │   └── jsx
 │       └── About.jsx
```

Each JSX file automatically includes **React boilerplate and CSS import**.

Example JSX generated:

```jsx
import React from "react";
import "../css/hero.css";

export const Hero = () => {
  return (
    <div className="hero">
      <h1>Hero Page</h1>
    </div>
  );
};
```

---

# ⚙️ Requirements

Make sure the following are installed:

* **Python 3.8+**
* **Node.js**
* **npm**
* **pip**

Check installations:

```
python --version
node -v
npm -v
pip --version
```

---

# ▶️ How to Run

Run the script:

```
python script.py
```

You will see a menu:

```
Select what you want to create ?

1. Frontend
2. Backend
3. Folders in frontend
4. Create Environment
```

---

# 🧩 Menu Options

### Option 1 — Create Frontend

Creates a React project using **Vite**.

Example input:

```
Enter the frontend folder name
frontend
```

---

### Option 2 — Create Backend

Creates Django project and installs dependencies.

Example input:

```
Enter the Backend Folder name
backend
```

---

### Option 3 — Create Frontend Structure

Creates pages and components interactively.

Example:

```
Enter name of the page: home
Enter file name: hero
Enter file name: testimonial
done
```

Generated files:

```
home/jsx/Hero.jsx
home/jsx/Testimonial.jsx
home/css/hero.css
home/css/testimonial.css
```

---

### Option 4 — Create Virtual Environment

Example:

```
Enter ENV name
env
```

Generated:

```
env/
```

---

# 🧠 Example Workflow

Recommended workflow:

```
1️⃣ Create Environment
2️⃣ Create Backend
3️⃣ Create Frontend
4️⃣ Generate Frontend Structure
```

---

# 🛠 Future Improvements

Possible enhancements:

* Automatic **React Router setup**
* Automatic **Redux / Zustand store setup**
* TailwindCSS installation
* Django app auto creation
* Auto start frontend and backend servers
* API service folder generation

---

# 👨‍💻 Author

Project Automation Script for **Fast Full Stack Development**.

---

⭐ If this project saves you time, consider improving or extending it!
