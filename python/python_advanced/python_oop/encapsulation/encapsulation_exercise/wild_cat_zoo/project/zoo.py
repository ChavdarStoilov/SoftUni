class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []



    def add_animal(self, animal, price):
        
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price

            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

        elif self.__budget < price:
            return 'Not enough budget'
        
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'

        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                
                return f'{worker_name} fired successfully'
                
        return f'There is no {worker_name} in the zoo'
    
    def pay_workers(self):
        all_worker_salary = 0
        
        for worker in self.workers:
            all_worker_salary +=  worker.salary

        if self.__budget >= all_worker_salary:
            self.__budget -= all_worker_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        

        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        cost_care = 0

        for animal in self.animals:
            cost_care += animal.money_for_care

        if self.__budget >= cost_care:
            self.__budget -= cost_care
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount
        

    def animals_status(self):
        output = f'You have {len(self.animals)} animals'
        tigers = [an.__repr__() for an in self.animals if an.__class__.__name__ == 'Tiger']
        lions = [an.__repr__() for an in self.animals if an.__class__.__name__ == 'Lion']
        cheetahs = [an.__repr__() for an in self.animals if an.__class__.__name__ == 'Cheetah']  
        animals = {'Lions': lions, 'Tigers': tigers, 'Cheetahs': cheetahs}
        
        for name, animal in animals.items():

            output += f'\n----- {len(animal)} {name}:\n'
            output += '\n'.join(animal)

        return output

    def workers_status(self):
        output = f'You have {len(self.workers)} workers'
        keepers = [wo.__repr__() for wo in self.workers if wo.__class__.__name__ == 'Keeper']
        caretakers = [wo.__repr__() for wo in self.workers if wo.__class__.__name__ == 'Caretaker']
        vets = [wo.__repr__() for wo in self.workers if wo.__class__.__name__ == 'Vet']  
        workers = {'Keepers': keepers, 'Caretakers': caretakers, 'Vets': vets}
        
        for name, worker in workers.items():

            output += f'\n----- {len(worker)} {name}:\n'
            output += '\n'.join(worker)

        return output
