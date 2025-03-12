# Telegram Chat Deletion Script (Educational Purpose Only)

🚨 **Disclaimer:** This script is for **educational purposes only**. Use it responsibly and only with accounts that you own. The author is not responsible for any misuse of this tool.

---

## 📌 About

This Python script automates the deletion of all chats (excluding channels) from a Telegram account using the **Telethon** library. It iterates through all dialogs and removes conversations while ensuring channels remain unaffected.

---

## ⚙️ Requirements

Ensure you have the following installed:

- **Python 3.x**
- **Telethon** library
- A Telegram **API ID** and **API Hash** (from [my.telegram.org](https://my.telegram.org/))

---

## 🚀 Installation & Setup

### **1️⃣ Install Dependencies**

```sh
pip install telethon
```

### **2️⃣ Get API Credentials**

1. Visit [my.telegram.org](https://my.telegram.org/)
2. Log in with your Telegram account
3. Go to "API Development Tools"
4. Note down your **API ID** and **API Hash**

### **3️⃣ Configure the Script**

- Open `delete_chats.py` in a text editor.
- Replace the placeholders with your **API ID** and **API Hash**:

```python
api_id =  0  # Your API ID (integer)
api_hash = ''  # Your API Hash
```

---

## 📌 Running the Script

Run the following command to execute the script:

```sh
python delete_chats.py
```

The script will delete **all private chats** while keeping channels untouched.

---

## ⚠️ Warning
- This action **CANNOT be undone**.
- The script does **not delete channels or groups**.
- Use at your **own risk** and **only on accounts you own**.

---

## 🛠️ Contribution & Issues

If you want to contribute or report any issues, feel free to create a **Pull Request** or **Issue** in the repository.

🚀 **Happy Coding!**
