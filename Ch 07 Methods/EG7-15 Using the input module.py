# EG7-15 Using the input module

import BTCInput

text_value = BTCInput.read_text('Enter some text: ')      
print('The text entered is ', text_value)

int_value = BTCInput.read_int('Enter an integer: ')
print('Int value is ', int_value)

float_value = BTCInput.read_float('Enter a float value: ')
print('Float value is ', float_value)                             

ranged_int = BTCInput.read_int_ranged(prompt= 'Int in range 5 to 90: ',
                                      min_value=5,
                                      max_value=90)
print('Ranged int is', ranged_int)

ranged_float = BTCInput.read_float_ranged(prompt= 'Float in range 5 to 90: ',
                                      min_value=5,
                                      max_value=90)
print('Ranged float is', ranged_float)
