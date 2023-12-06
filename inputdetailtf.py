import tensorflow as tf

# Load the TensorFlow model
model_path = '/root/Workspaces/PyTorch-ONNX-TFLite/conversion/model_tf'
model = tf.saved_model.load(model_path)

# Print the model signatures
print("Model Signatures:", model.signatures)

# Assuming the default serving signature
serving_signature = model.signatures['serving_default']

# Inspect the input and output tensor information
input_tensor_info = serving_signature.structured_input_signature
output_tensor_info = serving_signature.structured_outputs

print("Input Tensor Info:", input_tensor_info)
print("Output Tensor Info:", output_tensor_info)