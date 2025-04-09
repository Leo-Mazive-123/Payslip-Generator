import os
import pandas as pd
from fpdf import FPDF
import yagmail
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# 🔍 TEMPORARY: Show what’s being loaded
print("EMAIL_USER =", EMAIL_USER)
print("EMAIL_PASS =", EMAIL_PASS)


# Create payslip folder if it doesn't exist
os.makedirs("payslips", exist_ok=True)

# Read the Excel file
try:
    df = pd.read_excel(r"C:\Users\Leo-T-Mazive\Documents\New folder1\employee.xlsx")
except Exception as e:
    raise FileNotFoundError("Error reading 'employees.xlsx': " + str(e))

# Function to create a PDF payslip
def create_payslip(emp_id, name, basic, allow, deduct, net_salary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Payslip", ln=True, align='C')

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Employee Name: {name}", ln=True)
    pdf.cell(200, 10, f"Employee ID: {emp_id}", ln=True)
    pdf.cell(200, 10, f"Basic Salary: ${basic:.2f}", ln=True)
    pdf.cell(200, 10, f"Allowances: ${allow:.2f}", ln=True)
    pdf.cell(200, 10, f"Deductions: ${deduct:.2f}", ln=True)
    pdf.cell(200, 10, f"Net Salary: ${net_salary:.2f}", ln=True)
    
    filename = f"payslips/{emp_id}.pdf"
    pdf.output(filename)
    return filename

# Function to send email with payslip
def send_email(to_email, pdf_path, name):
    subject = "Your Payslip for This Month"
    body = f"Hello {name},\n\nPlease find attached your payslip for this month.\n\nBest regards,\nHR Department"
    yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASS)
    yag.send(to=to_email, subject=subject, contents=body, attachments=pdf_path)

# Process each employee
for index, row in df.iterrows():
    try:
        emp_id = row['Employee ID']
        name = row['Name']
        email = row['Email']
        basic = float(row['Basic Salary'])
        allow = float(row['Allowances'])
        deduct = float(row['Deductions'])
        net_salary = basic + allow - deduct

        print(f"Generating payslip for {name}...")

        pdf_path = create_payslip(emp_id, name, basic, allow, deduct, net_salary)
        send_email(email, pdf_path, name)

        print(f"Payslip sent to {email}.\n")
    except Exception as e:
        print(f"Error processing row {index + 2}: {e}")

print("✅ All done!")
