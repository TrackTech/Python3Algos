"""
The Context:
Our e-commerce platform currently uses a StripePayment class. We’ve been using it for years, and it is integrated into our checkout, refund, and subscription services.

The Problem:
Management just signed a deal with a new provider called SuperPay. However, SuperPay’s code looks totally different from Stripe’s.

The Constraints:

Our Checkout system expects a method called make_payment(amount).

Stripe (Existing) uses: charge(dollars).

SuperPay (New) uses: send_transaction(cents). (Note: SuperPay uses cents, so $10.00 must be sent as 1000).
"""

"""
Proble snippet
# --- EXISTING CODE (DO NOT MODIFY THESE) ---

class StripePayment:
    def charge(self, dollars):
        print(f"Stripe: Charging ${dollars}")

class SuperPay:
    def send_transaction(self, cents):
        print(f"SuperPay: Sending transaction of {cents} cents")

# --- THE CLIENT (DO NOT MODIFY THIS) ---

def run_checkout(processor, amount):
    # The client ONLY knows how to call 'make_payment'
    processor.make_payment(amount)
"""

from abc import ABC, abstractmethod

# 1. The Interface (The "Contract")
class IPaymentProcessor(ABC):
    @abstractmethod
    def make_payment(self, dollars: int):
        pass

# --- EXTERNAL CLASSES (ADAPTEES) ---
class StripePayment:
    def charge(self, dollars):
        print(f"Stripe: Charging ${dollars}")

class SuperPay:
    def send_transaction(self, cents):
        print(f"SuperPay: Sending transaction of {cents} cents")

# --- YOUR ADAPTERS ---

class StripePaymentAdapter(IPaymentProcessor):
    def __init__(self, stripe_obj: StripePayment):
        self.adaptee = stripe_obj
    
    def make_payment(self, dollars):
        # Translate make_payment -> charge
        self.adaptee.charge(dollars)

class SuperPayPaymentAdapter(IPaymentProcessor):
    def __init__(self, superpay_obj: SuperPay):
        self.adaptee = superpay_obj
    
    def make_payment(self, dollars):
        # 1. Translation: make_payment -> send_transaction
        # 2. Transformation: dollars -> cents
        cents = dollars * 100
        self.adaptee.send_transaction(cents)

# --- THE CLIENT ---

def run_checkout(processor: IPaymentProcessor, amount: int):
    processor.make_payment(amount)

# --- EXECUTION ---
if __name__ == "__main__":
    # Create the third-party objects
    stripe = StripePayment()
    super_pay = SuperPay()

    # Wrap them in your adapters
    adapter1 = StripePaymentAdapter(stripe)
    adapter2 = SuperPayPaymentAdapter(super_pay)

    # Use them interchangeably!
    run_checkout(adapter1, 50)   # Output: Stripe: Charging $50
    run_checkout(adapter2, 50)   # Output: SuperPay: Sending 5000 cents
