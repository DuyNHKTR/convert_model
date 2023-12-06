import tensorflow as tf

# Load the TensorFlow SavedModel
model_path = "/root/Workspaces/PyTorch-ONNX-TFLite/conversion/model_tf"
model = tf.saved_model.load(model_path)

# Get the signature keys
signature_keys = list(model.signatures.keys())

# Assume the first signature is the default one
default_signature = model.signatures[signature_keys[0]]

# Print the output tensor names and shapes
for output_key, output_tensor_info in default_signature.structured_outputs.items():
    print(f"Output Tensor Name: {output_key}")
    print(f"Output Tensor Shape: {output_tensor_info.shape}")
    print()