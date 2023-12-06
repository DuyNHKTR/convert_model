import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt  # for visualization (optional)

# Load the TFLite model
model_path = '/root/Workspaces/PyTorch-ONNX-TFLite/conversion/model.tflite'
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input details
input_details = interpreter.get_input_details()
input_shape = input_details[0]['shape']
input_dtype = input_details[0]['dtype']

# Generate a random tensor resembling an image with shape (1, 3, 640, 640)
random_image = np.random.randint(0, 256, size=input_shape, dtype=np.uint8)



# Convert the random image tensor to FLOAT32
random_image_float32 = random_image.astype(np.float32) / 255.0  # Normalize pixel values to [0, 1]

# Set the converted tensor as the input to the interpreter
interpreter.set_tensor(input_details[0]['index'], random_image_float32)

# Run inference
interpreter.invoke()

# Get the output tensor(s)
output_details = interpreter.get_output_details()
output_tensor = interpreter.get_tensor(output_details[0]['index'])

# Process the output as needed
# ...

# Print the results
print("Random Image Tensor:")
print(random_image_float32)
print("\nModel Output:")
print(output_tensor)
