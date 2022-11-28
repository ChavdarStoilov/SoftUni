class Gym:

    def __init__(self) -> None:
        self.customers = []
        self.trainers  = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []


    def add_customer(self, customer):
        
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):

        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        
        customers = [customer for customer in self.customers if customer.id == subscription_id]
        trainers = [trainer for trainer in self.trainers if trainer.id == subscription_id]
        equipment = [equipment for equipment in self.equipment if equipment.id == subscription_id]
        plans = [plan for plan in self.plans if plan.id == subscription_id]
        subscriptions = [subscription for subscription in self.subscriptions if subscription.id == subscription_id]

        result = f'{subscriptions[0]}\n{customers[0]}\n{trainers[0]}\n{equipment[0]}\n{plans[0]}'

        return result

