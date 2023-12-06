import cv2

# Import the SCRFD class
from scrfd import SCRFD

# Define the path to the SCRFD ONNX model file
model_file_path = '/root/Workspaces/PyTorch-ONNX-TFLite/modified_model.onnx'

# Create an instance of the SCRFD model
scrfd_model = SCRFD(model_file=model_file_path)

# Load an image for testing
image_path = '/root/Workspaces/PyTorch-ONNX-TFLite/tough-crowd.png'
image = cv2.imread(image_path)

# Specify the input size for detection
input_size = (640, 640)

# Perform object detection using SCRFD
det_boxes, kpss = scrfd_model.detect(image, input_size=input_size, thresh=0.3, max_num=100, metric='default')

# Draw bounding boxes on the image
for box in det_boxes:
    cv2.rectangle(image, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)

# Draw key points if available
if kpss is not None:
    for kps in kpss:
        for kp in kps:
            cv2.circle(image, (int(kp[0]), int(kp[1])), 3, (0, 0, 255), -1)

# Save the image with bounding boxes and key points
output_image_path = 'img_with_boxes_1.png'
cv2.imwrite(output_image_path, image)

print(f"Result saved to {output_image_path}")
