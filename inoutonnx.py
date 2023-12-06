import onnx

# Path to your ONNX model file
model_path = "/root/Workspaces/PyTorch-ONNX-TFLite/modified_model.onnx"

# Load the ONNX model
onnx_model = onnx.load(model_path)

# Display input information
print("Input Nodes:")
for input_node in onnx_model.graph.input:
    print(f"  Name: {input_node.name}, Shape: {input_node.type.tensor_type.shape.dim}")

# Display output information
print("\nOutput Nodes:")
for output_node in onnx_model.graph.output:
    print(f"  Name: {output_node.name}, Shape: {output_node.type.tensor_type.shape.dim}")
