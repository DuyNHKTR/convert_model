import cv2
import onnxruntime
import numpy as np

# Load the ONNX model
onnx_model_path = '/root/Workspaces/PyTorch-ONNX-TFLite/modified_model.onnx'
ort_session = onnxruntime.InferenceSession(onnx_model_path)

# Read an input image
image_path = '/root/Workspaces/PyTorch-ONNX-TFLite/tough-crowd.png'
img = cv2.imread(image_path)

# Preprocess the input image (adjust according to your model's input requirements)
input_name = ort_session.get_inputs()[0].name
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB if needed
input_tensor = np.expand_dims(img, axis=0).astype(np.float32)

# Run the ONNX model
outputs = ort_session.run(None, {input_name: input_tensor})

# Access bounding box predictions from the output tensors
# Modify according to the actual output tensors of your model
# This is just a placeholder; replace it with the actual way your model outputs bounding boxes
boxes = outputs[0]

# Draw bounding boxes on the image
for box in boxes:
    x1, y1, x2, y2 = map(int, box[:4])
    score = box[4]
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(img, f"{score:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Save the image with bounding boxes
output_image_path = 'path/to/your/output_image.jpg'
cv2.imwrite(output_image_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

# Print the output shapes (adjust based on your actual output tensors)
for i, box in enumerate(boxes):
    print(f"Output Tensor Name: {i}")
    print(f"Output Tensor Shape: {box.shape}")

# Further processing or visualization based on your needs
