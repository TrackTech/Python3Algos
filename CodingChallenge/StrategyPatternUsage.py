"""
The Scenario: "The Dynamic Shipping Engine"

The Context:
You are building the backend for a global logistics company. The system needs to calculate the shipping cost for a package based on the carrier the customer chooses.

The Problem:
Initially, the company only used FedEx and UPS. But now, they are adding DHL, USPS, and a local Biking Courier. Each carrier has a completely different way of calculating costs:

FedEx: Charges based on weight (weight×2.5).

UPS: Charges based on weight AND a flat fuel surcharge (weight×2.0+10).

Biking Courier: Flat rate of $5 regardless of weight.

The Constraint:
Your ShippingOrder class must be able to switch carriers at any time (e.g., if a user changes their mind at checkout) without you having to write a massive if-else block inside the calculate_total() method.
"""

# you dont want to have a lot of IF - ELSE in code

# use stragey patter, so that shipping stragegy can be set during ruuning of order
# use factor in that patter

# factory class should be seperate to have a seperate of concerns

from enum import Enum, auto
from abc import ABC, abstractmethod

# 1. Type Safety with Enum
class Carrier(Enum):
    FEDEX = auto()
    UPS = auto()
    BIKING = auto()

# 2. Strategy Interface
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, weight: float) -> float:
        pass

# 3. Concrete Strategies
class FedExStrategy(ShippingStrategy):
    def calculate(self, weight):
        return weight * 2.5

class UPSStrategy(ShippingStrategy):
    def calculate(self, weight):
        return (weight * 2.0) + 10

class BikingStrategy(ShippingStrategy):
    def calculate(self, weight):
        return 5.0  # Flat rate

# 4. Simple Factory
class ShippingFactory:
    @staticmethod
    def get_strategy(carrier_type: Carrier) -> ShippingStrategy:
        # Dictionary mapping is the most Pythonic "Factory"
        strategies = {
            Carrier.FEDEX: FedExStrategy(),
            Carrier.UPS: UPSStrategy(),
            Carrier.BIKING: BikingStrategy()
        }
        return strategies.get(carrier_type)

# 5. The Context
class ShippingOrder:
    def __init__(self, weight: float):
        self.weight = weight
        self._strategy = None  # Dependency

    def set_carrier(self, carrier_type: Carrier):
        # Using the factory to inject the strategy
        self._strategy = ShippingFactory.get_strategy(carrier_type)

    def calculate_total(self) -> float:
        if not self._strategy:
            raise ValueError("Carrier not set!")
        return self._strategy.calculate(self.weight)

# --- EXECUTION ---
order = ShippingOrder(weight=10)

order.set_carrier(Carrier.FEDEX)
print(f"FedEx Cost: {order.calculate_total()}") # 25.0

order.set_carrier(Carrier.UPS)
print(f"UPS Cost: {order.calculate_total()}")   # 30.0
