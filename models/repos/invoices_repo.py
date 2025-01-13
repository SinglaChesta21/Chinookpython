import sqlite3
from models.invoices import Invoice
from models.repos.a_invoices import AInvoice

class InvoiceRepo(AInvoice):
    def create_invoice(self, model: Invoice) -> None:
        pass
    def update_invoice(self, invoice_id: int, model: Invoice) -> None:
        pass

    def delete_invoice(self, invoice_id: int) -> None:
        pass

    def get_invoice(self, invoice_id: int) -> Invoice:
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM invoices WHERE InvoiceId = ?", (invoice_id,))
                row = cursor.fetchone()
                if row:
                    return Invoice(*row)
                else:
                    print(f"No invoice found for InvoiceId {invoice_id}")
                    return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def get_all_invoices(self) -> list[Invoice]:
        invoices = []
        try:
            with sqlite3.connect("chinook.db") as conn:
                cursor = conn.execute("SELECT * FROM invoices")
                for row in cursor:
                    invoices.append(Invoice(*row))
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return invoices
