from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def generate_receipt(customer_name, amount_paid, items_purchased,payment_method):
    # Create a PDF document
    doc = SimpleDocTemplate("payment_receipt1.pdf", pagesize=letter)

    # Content for the receipt
    receipt_content = [
        ["Customer Name:", customer_name],
        ["Items Purchased:", ", ".join(items_purchased)],
        ["Amount Paid:", "Rs. " + str(amount_paid)],
        ["payment_method:",payment_method]

    ]

    # Create a table from the content
    receipt_table = Table(receipt_content)

    # Add style to the table
    receipt_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                       ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                       ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    # Add the table to the document
    doc.build([receipt_table])


# Example usage
customer_name = "Nani"
items_purchased = ["Biryani", "kabab", "pizza"]
amount_paid = 500.00
payment_method="Google Pay"


generate_receipt(customer_name, amount_paid, items_purchased, payment_method)

