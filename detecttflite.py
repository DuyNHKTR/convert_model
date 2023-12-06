import cv2
import numpy as np
import tensorflow as tf

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path='/root/Workspaces/PyTorch-ONNX-TFLite/conversion/model.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Load an image for testing
image_path = '/root/Workspaces/PyTorch-ONNX-TFLite/tough-crowd.png'
image = cv2.imread(image_path)

# Preprocess the input image to match the expected input shape of the TFLite model
input_tensor = interpreter.tensor(input_details[0]['index'])

# Resize the image to match the expected input shape (assuming 3, 1, 1)
input_image = cv2.resize(image, (1, 1))

# Normalize pixel values if needed
input_image = input_image.astype(np.float32) / 255.0

# Transpose dimensions to match the expected shape (3, 1, 1)
input_image = np.transpose(input_image, (2, 0, 1))

# Assign the preprocessed image to the input tensor
input_tensor()[0] = input_image

# Run inference
interpreter.invoke()

# Get the output
output_tensor = interpreter.tensor(output_details[0]['index'])
output = output_tensor()

# Process the output for object detection
# (Assuming the output format is similar to the SCRFD model)
det_boxes = output[:, :4]
det_scores = output[:, 4]

# Filter detections based on confidence threshold
thresh = 0.3
keep_indices = np.where(det_scores >= thresh)[0]
det_boxes = det_boxes[keep_indices]

# Draw bounding boxes on the image
for box in det_boxes:
    cv2.rectangle(image, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)

# Save the image with drawn bounding boxes
output_image_path = 'img_with_boxes_tflite.png'
cv2.imwrite(output_image_path, image)

print(f"Result saved to {output_image_path}")
