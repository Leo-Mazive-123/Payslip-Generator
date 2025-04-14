# 🧾 Payslip Generator & Email Sender

A Python-based automation tool that reads employee data from Excel, generates personalized PDF payslips, and emails them directly to employees.

## 🚀 Features

- ✅ Reads employee salary data from an Excel spreadsheet
- ✅ Generates detailed, formatted PDF payslips
- ✅ Sends payslips via email to each employee
- ✅ Error handling and logging built-in
- ✅ Clean, reusable code structure

---

## 📂 Folder Structure

project/ │ ├── data/ │ └── employees.xlsx # Employee salary data │ ├── output/ │ └── *.pdf # Generated payslips │ ├── logs/ │ └── email_log.txt # Sent/failed email logs │ ├── payslip_generator.py # Main script ├── email_sender.py # Handles email sending └── requirements.txt # Required packages

yaml
Copy
Edit

---

## ⚙️ Tech Stack

- `pandas` – Excel data handling  
- `reportlab` – PDF generation  
- `smtplib` + `email` – Email sending  
- `openpyxl` – Excel support for `.xlsx`  
- `dotenv` – Load sensitive info securely (optional)

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/payslip-generator.git
   cd payslip-generator
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Prepare your Excel file

Make sure your employees.xlsx file includes columns like:

Name	Email	Basic Salary	Allowance	Deductions
Roshly Musonza	musonzaroshly@gmail.com	1000	200	50
Update SMTP/email credentials

Either use a .env file or update credentials directly in email_sender.py (not recommended for production).

▶️ How to Run
bash
Copy
Edit
python payslip_generator.py
You’ll see a success message for each payslip sent, and any errors will be logged.

📬 Sample Output
PDF payslips are named using the employee’s name

Example email:

Subject: Your Monthly Payslip
Body: Dear Roshly, please find your attached payslip for this month.
Attachment: Roshly_Musonza_Payslip.pdf

💡 Future Improvements
Add company branding/logo to PDFs

Password-protect PDF files

Web interface (Flask or Streamlit)

Upload to Google Drive or Dropbox

Send via WhatsApp (Twilio API)

🧠 Credits
Developed by Leo Mazive as part of a Python crash course project.

Feel free to connect on LinkedIn or check out more on GitHub.

