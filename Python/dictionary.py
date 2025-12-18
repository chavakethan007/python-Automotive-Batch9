capitals={'Telangana':'Hyderabad',
          'Karnataka':'Banglore',
          'Andhra pradesh':'Amaravathi',
          'Madhya Pradesh':'Bombay',
          'Tamilnadu':'chennai'}

print(capitals['Telangana']) #Hyderabad
print(capitals.get('New Delhi')) #None
print(capitals.keys()) #dict_keys(['Telangana', 'Karnataka', 'Andhra pradesh', 'Madhya Pradesh', 'Tamilnadu'])
print(capitals.values()) #dict_values(['Hyderabad', 'Banglore', 'Amaravathi', 'Bombay', 'chennai'])
print(capitals.items()) #dict_items([('Telangana', 'Hyderabad'), ('Karnataka', 'Banglore'), ('Andhra pradesh', 'Amaravathi'), ('Madhya Pradesh', 'Bombay'), ('Tamilnadu', 'chennai')])

print("---------------------------------------------------")

capitals.update({'Delhi': 'New Delhi'})
print(capitals) 
#{'Telangana': 'Hyderabad', 'Karnataka': 'Banglore', 'Andhra pradesh': 'Amaravathi', 'Madhya Pradesh': 'Bombay', 'Tamilnadu': 'chennai', 'Delhi': 'New Delhi'}
capitals.update({'Madhya Pradesh': 'Mumbai'})
print(capitals)
#{'Telangana': 'Hyderabad', 'Karnataka': 'Banglore', 'Andhra pradesh': 'Amaravathi', 'Madhya Pradesh': 'Mumbai', 'Tamilnadu': 'chennai', 'Delhi': 'New Delhi'}
capitals.pop('Tamilnadu')
print(capitals)
#{'Telangana': 'Hyderabad', 'Karnataka': 'Banglore', 'Andhra pradesh': 'Amaravathi', 'Madhya Pradesh': 'Mumbai', 'Delhi': 'New Delhi'}
capitals.clear()

for key,value in capitals:
    print(key,value)

capitals['Andhra pradesh']='Hyderabad'
print(capitals['Andhra pradesh'])