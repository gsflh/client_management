# **Client Management System**

This is a simple Client Management System built using **Flask**, **SQLite**, **HTML**, **CSS**, and **JavaScript**. The system allows users to:

- Log in to the system (simple validation).
- Add new clients.
- View a list of all clients.
- Update client details.
- Delete clients from the system.

## **Table of Contents**
- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [License](#license)

---

## **Features**
1. **Login System**: Simple form-based login.
2. **Add Client**: Form to add a new client with fields like name, date of birth, address, email, phone, and service availed.
3. **View Clients**: Display all clients with options to update or delete them.
4. **Update Client**: Modify an existing client's details.
5. **Delete Client**: Remove a client from the system.
6. **Responsive Design**: Basic responsive layout using HTML and CSS.

---

## **Technologies**
- **Flask** (Backend framework)
- **SQLite** (Database)
- **HTML/CSS** (Frontend)
- **JavaScript** (Frontend interactivity)
- **Python** (Primary language)

---

## **Setup Instructions**

### Prerequisites:
- Python 3.12
- pip (Python package manager)

### Step-by-Step Setup:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gsflh/client_management.git
   cd client-management
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **Access the web app:**
   Open your browser and go to `http://127.0.0.1:5000/`.

### Database Initialization:
The database (`clients.db`) will be created automatically when you first run the app. The `clients` table will be initialized with fields for client information such as name, date of birth, address, email, phone, and service availed.

---

## **Project Structure**

```
client_management/
├── app.py                   # Main Flask application
├── templates/                # HTML templates for different pages
│   ├── base.html             # Base HTML layout
│   ├── login.html            # Login page template
│   ├── add_client.html       # Add client page template
│   ├── view_clients.html     # View clients page template
│   └── update_client.html    # Update client page template
├── static/                   # Static assets (CSS, JS)
│   ├── css/
│   │   └── styles.css        # CSS file for styling
│   └── js/
│       └── scripts.js        # JavaScript file for interactivity (if needed)
├── clients.db                # SQLite database
├── requirements.txt          # List of Python dependencies
└── README.md                 # Project documentation (this file)
```

---

## **Usage**

### **Login Page:**
- URL: `/`
- Enter the username and password. For testing purposes, use:
  - **Username**: `admin`
  - **Password**: `password`

### **Add Client:**
- URL: `/add_client`
- Fill in client details (name, date of birth, address, email, phone, service availed) and click "Add Client".

### **View Clients:**
- URL: `/view_clients`
- Displays all clients in a table. You can update or delete a client by clicking on the respective links in the table.

### **Update Client:**
- URL: `/update_client/<id>`
- Modify the client's details and save the changes.

### **Delete Client:**
- Clicking "Delete" on the client row in the **View Clients** page will delete that client from the system.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to fork this repository, open issues, or contribute!
