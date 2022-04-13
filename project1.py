import numpy as np
input_data = (63,1,3,145,233,1,0,150,0,2.3,0,0,1)
clean_input = np.array(input_data)
final_input = clean_input.reshape(1,-1)
print(input_data)
print(clean_input)
print(final_input)