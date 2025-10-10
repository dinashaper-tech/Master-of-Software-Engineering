from abc import ABC, abstractmethod

#abstract base class

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal."
    
class StripePayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe."
    
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card."
    

class PaymentProcessorFactory:
    _processors = {
        'paypal': PayPalPayment,
        'stripe': StripePayment,
        'credit_card': CreditCardPayment
    }

    @classmethod
    def create_processor(cls, payment_method):
        processor_class = cls._processors.get(payment_method.lower())
        if not processor_class:
            raise ValueError(f"Unknown payment method: {payment_method}")
        return processor_class()
    
#Clean client code

def checkout(payment_method, amount):
    processor = PaymentProcessorFactory.create_processor(payment_method)
    return processor.process_payment(amount)

print(checkout('paypal', 100))
print(checkout('stripe', 200))