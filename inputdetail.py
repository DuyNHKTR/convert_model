import tensorflow as tf

# Load the TFLite model
model_path = '/root/Workspaces/PyTorch-ONNX-TFLite/conversion/model.tflite'
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input details
input_details = interpreter.get_input_details()

# Print input details
print("Input details:")
print(input_details)
