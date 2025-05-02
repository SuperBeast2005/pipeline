import datetime
import random
from faker import Faker

fake = Faker()

def generate_random_data():
        return {
            'id': random.randint(1, 10000000),
            'name': fake.first_name(),
            'surname': fake. last_name(),
            'birthdate': fake.date_of_birth(minimum_age=1, maximum_age=90).isoformat(),
            'ip_address': str(fake.ipv4()),
            'port': fake.port_number(),
            'timestamp': str(datetime.datetime.now())
        }
    
if __name__=="__main__":
    print(generate_random_data()['ip_address'])
    