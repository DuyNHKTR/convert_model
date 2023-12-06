import cv2
import numpy as np
import tensorflow as tf

# Load the TensorFlow model
model_path = '/root/Workspaces/PyTorch-ONNX-TFLite/conversion/model_tf'
model = tf.saved_model.load(model_path)

# Load an image for testing
image_path = '/root/Workspaces/PyTorch-ONNX-TFLite/tough-crowd.png'
image = cv2.imread(image_path)

# Resize the image
input_width, input_height = 640, 640  # Adjust these dimensions based on the model's requirements
resized_image = cv2.resize(image, (input_width, input_height))

# Normalize pixel values
normalized_image = resized_image.astype(np.float32) / 255.0

# Add batch dimension
# Add batch and channel dimensions
input_image = np.expand_dims(normalized_image, axis=0)  # Add batch dimension
input_image = np.transpose(input_image, (0, 3, 1, 2))  # Transpose to (batch, channels, height, width)

# Create a dictionary for the input tensor using the correct name
input_tensor_name = 'input'  # Use the actual name of your input tensor
input_dict = {input_tensor_name: tf.constant(input_image)}

# Perform inference
detection_result = model(**input_dict)
print("Keys in detection_result:", detection_result.shape)

# Save detection_result to log.txt
# log_path = 'log.txt'
# with open(log_path, 'w') as log_file:
#     log_file.write("Keys in detection_result:\n")
#     for key, value in detection_result.items():
#         log_file.write(f"{key}: {value}\n")

# print(f"Detection result saved to {log_path}")
exit()

# Process the output for object detection
# (Assuming the output format is similar to the SCRFD model)
det_boxes = detection_result['detection_boxes'].numpy()
det_scores = detection_result['detection_scores'].numpy()

# Filter detections based on confidence threshold
thresh = 0.3
keep_indices = np.where(det_scores >= thresh)[0]
det_boxes = det_boxes[keep_indices]

# Draw bounding boxes on the image
for box in det_boxes:
    ymin, xmin, ymax, xmax = box
    xmin = int(xmin * image.shape[1])
    xmax = int(xmax * image.shape[1])
    ymin = int(ymin * image.shape[0])
    ymax = int(ymax * image.shape[0])
    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

# Save the image with drawn bounding boxes
output_image_path = 'img_with_boxes_tf.png'
cv2.imwrite(output_image_path, image)

print(f"Result saved to {output_image_path}")
