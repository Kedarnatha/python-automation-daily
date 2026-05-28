# 📧 Email Automation using Python

## 🚀 Project Overview
This project sends emails automatically using Python.

Features:
- Send single email
- Send bulk emails
- Read emails from CSV file
- Read message from text file
- Personalized email support

---

## 🧠 Technologies Used
- Python
- smtplib
- pandas
- email.message

---

## 📂 Project Structure

Day04_Email_Automation/

├── send_email.py  
├── emails.csv  
├── message.txt  
└── README.md  

---

## 📄 emails.csv Format

```csv
name,email
Kedar,kedar@gmail.com
Ravi,ravi@gmail.com
```

---

## 📝 message.txt Format

```text
Hello {name},

This is an automated email sent using Python.

Thank you!
```

---

## ▶️ How to Run

### 1️⃣ Install pandas

```bash
pip install pandas
```

### 2️⃣ Add your Gmail and App Password

Inside `send_email.py`

```python
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
```

### 3️⃣ Run the script

```bash
python send_email.py
```

---

## ✅ Output

The script sends personalized emails automatically to all users in the CSV file.

---

## 🔥 Future Improvements

- Add file attachments
- Add HTML emails
- Add GUI
- AI-generated email content
