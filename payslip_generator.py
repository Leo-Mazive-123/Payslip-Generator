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
    df = pd.read_excel(r"C:\Users\Leo-T-Mazive\Documents\Payslip Project\employee.xlsx")
except Exception as e:
    raise FileNotFoundError("Error reading 'employees.xlsx': " + str(e))

# Function to create a PDF payslip (updated and styled)
def create_payslip(emp_id, name, basic, allow, deduct, net_salary):
    pdf = FPDF()
    pdf.add_page()
    
    # Colors
    header_color = (70, 130, 180)  # Steel blue
    border_color = (169, 169, 169)  # Dark gray

    # Header
    pdf.set_fill_color(*header_color)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 15, "Dear Valued Employee - Monthly Payslip", ln=True, align='C', fill=True)

    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)

    # Employee Info
    pdf.set_fill_color(245, 245, 245)
    pdf.set_draw_color(*border_color)
    pdf.cell(50, 10, "Employee Name:", border=1, fill=True)
    pdf.cell(0, 10, name, border=1, ln=True)
    
    pdf.cell(50, 10, "Employee ID:", border=1, fill=True)
    pdf.cell(0, 10, str(emp_id), border=1, ln=True)

    pdf.ln(5)
    
    # Salary Breakdown Header
    pdf.set_font("Arial", "B", 14)
    pdf.set_fill_color(*header_color)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, "Salary Breakdown", ln=True, fill=True)
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    
    # Breakdown Table
    def salary_row(label, amount):
        pdf.cell(80, 10, label, border=1, fill=True)
        pdf.cell(0, 10, f"${amount:.2f}", border=1, ln=True)
    
    pdf.set_fill_color(255, 255, 255)
    salary_row("Basic Salary", basic)
    salary_row("Allowances", allow)
    salary_row("Deductions", deduct)

    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(230, 230, 250)
    salary_row("Net Salary", net_salary)

    # Footer
    pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, "This is a system-generated payslip. Please contact HR for any queries.", ln=True, align='C')

    # Save file
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

print("✅ All done! Mr.Mazive")
