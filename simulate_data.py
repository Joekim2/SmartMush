import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

def generate_data(num_samples=1000):
    data = []
    
    for _ in range(num_samples):
        # We want roughly 50% optimal (1) and 50% suboptimal (0)
        # This ensures the model learns both cases well.
        is_optimal = random.choice([True, False])
        
        if is_optimal:
            # GENERATE GOOD DATA (Force numbers into the ideal range)
            temp = round(random.uniform(18, 24), 1)      # Ideal Temp
            humidity = round(random.uniform(80, 99), 1)  # Ideal Hum
            co2 = round(random.uniform(300, 1000), 1)    # Ideal CO2
            growth_class = 1
        else:
            # GENERATE BAD DATA (Force at least one parameter to be wrong)
            # We pick a random parameter to mess up so the model learns specifically
            mess_up_factor = random.choice(['temp', 'hum', 'co2'])
            
            if mess_up_factor == 'temp':
                # Make temp too hot or too cold
                temp = round(random.choice([random.uniform(10, 17), random.uniform(25, 35)]), 1)
                humidity = round(random.uniform(30, 99), 1)
                co2 = round(random.uniform(300, 2000), 1)
            
            elif mess_up_factor == 'hum':
                # Make humidity too low
                temp = round(random.uniform(10, 35), 1)
                humidity = round(random.uniform(30, 79), 1) # Too dry
                co2 = round(random.uniform(300, 2000), 1)
                
            else: # co2
                # Make CO2 too high
                temp = round(random.uniform(10, 35), 1)
                humidity = round(random.uniform(30, 99), 1)
                co2 = round(random.uniform(1001, 2000), 1) # Too toxic
            
            growth_class = 0
            
        data.append([temp, humidity, co2, growth_class])
        
    df = pd.DataFrame(data, columns=['Temperature', 'Humidity', 'CO2_Level', 'Growth_Class'])
    
    # Shuffle the dataset so 0s and 1s are mixed
    df = df.sample(frac=1).reset_index(drop=True)
    
    df.to_csv('mushroom_data.csv', index=False)
    print(f"✅ Successfully generated {num_samples} balanced samples.")
    print(df['Growth_Class'].value_counts()) # Check the balance

if __name__ == "__main__":
    generate_data()