""" Handling Household Problems """

class ElectricalError(Exception):
    
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
        
    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)


class PlumbingError(Exception):
    
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem
        
    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)


def cause_error(error_type):

    if error_type == 'electrical':
        raise ElectricalError('circuit breaker', 'overloaded')
    
    elif error_type == 'plumbing':
        raise PlumbingError('dishwasher', 'spraying water')
    else:
        raise Exception('a generic household problem')

try:
    cause_error('garden')
except ElectricalError as e:
    print(e)
    print('Fix it myself.')
except PlumbingError as e:
    print(e)
    print('Call a plumber!')
except:
    print('Call the landlord')
