import tensorflow as tf
import cv2
import numpy as np

def distance2bbox(points, distance, max_shape=None):
    """Decode distance prediction to bounding box."""
    x1 = points[:, 0] - distance[:, 0]
    y1 = points[:, 1] - distance[:, 1]
    x2 = points[:, 0] + distance[:, 2]
    y2 = points[:, 1] + distance[:, 3]
    if max_shape is not None:
        x1 = np.clip(x1, 0, max_shape[1])
        y1 = np.clip(y1, 0, max_shape[0])
        x2 = np.clip(x2, 0, max_shape[1])
        y2 = np.clip(y2, 0, max_shape[0])
    return np.stack([x1, y1, x2, y2], axis=-1)

def process_tf_output(outputs, anchor_scales):
    fmc = len(anchor_scales)
    scores_list, bboxes_list = [], []
    for idx in range(fmc):
        scores = tf.nn.softmax(outputs[idx][:, 1:])
        bbox_preds = outputs[idx + fmc]
        bbox_preds = bbox_preds * anchor_scales[idx]
        height, width = bbox_preds.shape[1], bbox_preds.shape[2]
        anchor_centers = np.stack(np.mgrid[:height, :width][::-1], axis=-1).astype(np.float32)
        anchor_centers = (anchor_centers * anchor_scales[idx]).reshape((-1, 2))
        bboxes = distance2bbox(anchor_centers, bbox_preds)
        scores_list.append(scores.numpy().ravel())
        bboxes_list.append(bboxes)
    return scores_list, bboxes_list

def main():
    # Load TensorFlow SavedModel
    saved_model_path = "/root/Workspaces/PyTorch-ONNX-TFLite/conversion/model_tf"
    model = tf.saved_model.load(saved_model_path)

    # Input image
    img_path = "/root/Workspaces/PyTorch-ONNX-TFLite/tough-crowd.png"
    img = cv2.imread(img_path)

    # Preprocess the image (you may need to adapt this based on the model requirements)
    input_size = (640, 640)  # Adjust the input size based on the model
    img = cv2.resize(img, input_size)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Prepare the input data
    img = np.transpose(img, (2, 0, 1))  # Change HWC to CHW
    img = np.expand_dims(img, axis=0).astype(np.float32) / 255.0

    # Run inference
    outputs = model(input=tf.constant(img), unknown=tf.constant(0))  # Pass appropriate values for unknown inputs

    # Process the TensorFlow model outputs
    anchor_scales = [8, 16, 32, 64, 128]  # Adjust based on your model
    scores_list, bboxes_list = process_tf_output(outputs, anchor_scales)

    # Display or use the bounding boxes as needed
    for scores, bboxes in zip(scores_list, bboxes_list):
        # Perform further processing or visualization based on your requirements
        print("Scores:", scores)
        print("Bounding Boxes:", bboxes)

if __name__ == "__main__":
    main()
