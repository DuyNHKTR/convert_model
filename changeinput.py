import onnx

# Load the ONNX model
onnx_model = onnx.load('/root/Workspaces/PyTorch-ONNX-TFLite/scrfd_s.onnx')

# Set the new input name and shape
new_input_name = 'input'
new_input_shape = [1, 3, None, None]  # Replace 'None' with the appropriate dimensions

# Get the original input name
original_input_name = onnx_model.graph.input[0].name

# Change the input name
onnx_model.graph.input[0].name = new_input_name

# Update the input name and shape in subsequent nodes
for node in onnx_model.graph.node:
    for i, input_name in enumerate(node.input):
        if input_name == original_input_name:
            node.input[i] = new_input_name

# Update the input shape in the model
onnx_model.graph.input[0].type.tensor_type.shape.ClearField("dim")
onnx_model.graph.input[0].type.tensor_type.shape.dim.extend(
    [onnx.TensorShapeProto.Dimension(dim_value=d) for d in new_input_shape]
)

# Save the modified ONNX model
onnx.save_model(onnx_model, 'modified_model.onnx')
