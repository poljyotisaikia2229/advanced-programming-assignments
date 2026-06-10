# Import abstract base class tools
from abc import ABC, abstractmethod

# PAYMENT SECTION

# Abstract Payment Interface
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# UPI Payment
class UPIPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Wallet Payment
class WalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")

# NOTIFICATION SECTION

# Abstract Notification Interface
class NotificationService(ABC):

    @abstractmethod
    def send(self, message):
        pass


# Email Notification
class EmailNotification(NotificationService):

    def send(self, message):
        print(f"Email Sent: {message}")


# SMS Notification
class SMSNotification(NotificationService):

    def send(self, message):
        print(f"SMS Sent: {message}")


# Push Notification
class PushNotification(NotificationService):

    def send(self, message):
        print(f"Push Notification Sent: {message}")



# STORAGE SECTION

# Abstract Storage Interface
class Storage(ABC):

    @abstractmethod
    def save(self, order):
        pass


# Database Storage
class DatabaseStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved to Database")


# File Storage
class FileStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved to File")

# ORDER SECTION

# Base Order Class
class Order:

    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    # Method to get total amount
    def get_total(self):
        return self.amount


# Regular Order
class RegularOrder(Order):

    def get_total(self):
        return self.amount


# Discounted Order
class DiscountedOrder(Order):

    def get_total(self):
        return self.amount * 0.9   # 10% discount


# Priority Order
class PriorityOrder(Order):

    def get_total(self):
        return self.amount + 100   # Extra priority fee

# ORDER SERVICE

# High-level Order Service Class
class OrderService:

    def __init__(self, payment_method, notification_service, storage):

        # Dependency Injection
        self.payment_method = payment_method
        self.notification_service = notification_service
        self.storage = storage

    # Method to process complete order
    def place_order(self, order):

        total = order.get_total()

        print("\nProcessing Order...")
        print(f"Customer: {order.customer_name}")
        print(f"Order ID: {order.order_id}")
        print(f"Final Amount: ₹{total}")

        # Payment Processing
        self.payment_method.pay(total)

        # Notification
        self.notification_service.send(
            f"Order {order.order_id} placed successfully!"
        )

        # Save Order
        self.storage.save(order)

# MAIN PROGRAM

if __name__ == "__main__":

    # Take customer details
    customer_name = input("Enter Customer Name: ")

    amount = float(input("Enter Order Amount: "))

    order_id = int(input("Enter Order ID: "))

    # Select Order Type

    print("\nSelect Order Type:")
    print("1. Regular Order")
    print("2. Discounted Order")
    print("3. Priority Order")

    order_choice = int(input("Enter choice: "))

    # Create order based on choice
    if order_choice == 1:
        order = RegularOrder(order_id, customer_name, amount)

    elif order_choice == 2:
        order = DiscountedOrder(order_id, customer_name, amount)

    else:
        order = PriorityOrder(order_id, customer_name, amount)

    # Select Payment Method
    
    print("\nSelect Payment Method:")
    print("1. Credit Card")
    print("2. UPI")
    print("3. Wallet")

    payment_choice = int(input("Enter choice: "))

    if payment_choice == 1:
        payment = CreditCardPayment()

    elif payment_choice == 2:
        payment = UPIPayment()

    else:
        payment = WalletPayment()

    # Select Notification Type

    print("\nSelect Notification Type:")
    print("1. Email")
    print("2. SMS")
    print("3. Push Notification")

    notification_choice = int(input("Enter choice: "))

    if notification_choice == 1:
        notification = EmailNotification()

    elif notification_choice == 2:
        notification = SMSNotification()

    else:
        notification = PushNotification()

    # Select Storage Type
    
    print("\nSelect Storage Type:")
    print("1. Database")
    print("2. File")

    storage_choice = int(input("Enter choice: "))

    if storage_choice == 1:
        storage = DatabaseStorage()

    else:
        storage = FileStorage()

    # Create Order Service

    service = OrderService(
        payment,
        notification,
        storage
    )

    # Process order
    service.place_order(order)