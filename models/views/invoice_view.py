from models.repos.invoices_repo import InvoiceRepo

def view_all_invoices():
    try:
        ir = InvoiceRepo()
        invoices = ir.get_all_invoices()
        if not invoices:
            print("No invoices found.")
        else:
            print("Invoices Table Data\n------------------")
            for invoice in invoices:
                print(invoice)
    except Exception as e:
        print(f"An error occurred: {e}")

def view_invoice_by_id(invoice_id: int):
    try:
        ir = InvoiceRepo()
        invoice = ir.get_invoice(invoice_id)
        if invoice:
            print(f"Invoice Details for Invoice ID {invoice_id}:")
            print(invoice)
        else:
            print(f"No invoice found for Invoice ID {invoice_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all invoices")
    print("2. View invoice by ID")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_all_invoices()
    elif choice == "2":
        try:
            invoice_id = int(input("Enter invoice ID: "))
            view_invoice_by_id(invoice_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    else:
        print("Invalid choice. Please choose 1 or 2.")
