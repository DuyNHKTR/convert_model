import tensorflow as tf

# Path to your TensorFlow SavedModel directory
saved_model_path = "/root/Workspaces/PyTorch-ONNX-TFLite/conversion/model_tf"

# Load the TensorFlow SavedModel
model = tf.saved_model.load(saved_model_path)

# Display input information
print("Input Signature:")
for signature_key in model.signatures.keys():
    signature = model.signatures[signature_key]
    print(f"  Signature: {signature_key}")
    
    if isinstance(signature.inputs, dict):
        for input_name, tensor_info in signature.inputs.items():
            print(f"    Input Name: {input_name}, Shape: {tensor_info.shape}")
    elif isinstance(signature.inputs, list):
        for input_tensor in signature.inputs:
            print(f"    Input Name: {input_tensor.name}, Shape: {input_tensor.shape}")

# Display output information
print("\nOutput Signature:")
for signature_key in model.signatures.keys():
    signature = model.signatures[signature_key]
    print(f"  Signature: {signature_key}")
    
    if isinstance(signature.outputs, dict):
        for output_name, tensor_info in signature.outputs.items():
            print(f"    Output Name: {output_name}, Shape: {tensor_info.shape}")
    elif isinstance(signature.outputs, list):
        for output_tensor in signature.outputs:
            print(f"    Output Name: {output_tensor.name}, Shape: {output_tensor.shape}")
