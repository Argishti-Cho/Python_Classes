# Reverse Lookup

the_dict = {
    'khndzor': 'apple', 
    'azat': 'free', 
    'tandz': 'pear', 
    'anvjar': 'free'
}
key = {v:k for k,v in the_dict.items()}
print(key)