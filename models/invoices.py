class Invoice:
    def __init__(self, invoice_id: int, customer_id: int, invoice_date: str, billing_address: str, billing_city: str, billing_state: str, billing_country: str, billing_postal_code: str, total: float):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.invoice_date = invoice_date
        self.billing_address = billing_address
        self.billing_city = billing_city
        self.billing_state = billing_state
        self.billing_country = billing_country
        self.billing_postal_code = billing_postal_code
        self.total = total

    def __repr__(self):
        return (
            f"Invoice(invoice_id={self.invoice_id}, customer_id={self.customer_id}, "
            f"invoice_date='{self.invoice_date}', billing_address='{self.billing_address}', "
            f"billing_city='{self.billing_city}', billing_state='{self.billing_state}', "
            f"billing_country='{self.billing_country}', billing_postal_code='{self.billing_postal_code}', "
            f"total={self.total})"
        )
