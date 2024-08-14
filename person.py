class Person():
    def __init__(self, beliefs={}, income=0, costs=0):   # preliminary: income and costs instead of all the detailed parameters
        self.beliefs = beliefs
        self.in = income
        self.out = costs

p = []
n = 2
for i in range(n):
    p.append(Person())

# now for some kind of interaction.
