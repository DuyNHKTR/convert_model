import onnx

# Load the ONNX model
onnx_model = onnx.load('/root/Workspaces/PyTorch-ONNX-TFLite/modified_model.onnx')

# Print the ONNX model graph
print(onnx.helper.printable_graph(onnx_model.graph))
