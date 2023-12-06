import onnxruntime
import numpy as np

# Load the ONNX model
onnx_model_path = '/root/Workspaces/PyTorch-ONNX-TFLite/modified_model.onnx'
sess = onnxruntime.InferenceSession(onnx_model_path)

# Prepare sample input data
# Replace this with your actual input data
sample_input = np.random.rand(1, 3, 224, 224).astype(np.float32)

# Run inference
input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()[0].name
result = sess.run([output_name], {input_name: sample_input})

# Print the result
print("Model output:", result)
