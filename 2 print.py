from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_receipt(customer_name, amount_paid, payment_method):
    # Create a PDF document
    c = canvas.Canvas("payment_receipt2.pdf", pagesize=letter)

    # Set up the title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 750, "Payment Receipt")

    # Set up the current date
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.setFont("Helvetica", 12)
    c.drawString(50, 700, f"Date: {date}")

    # Customer details
    c.drawString(50, 670, f"Customer Name: {customer_name}")

    # Payment details
    c.drawString(50, 640, f"Amount Paid: ${amount_paid:.2f}")
    c.drawString(50, 610, f"Payment Method: {payment_method}")

    # Thank you message
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(300, 550, "Thank you for your payment!")

    # Close the PDF document
    c.save()

# Test the function
generate_receipt("Kiran", 900, "Google Pay")