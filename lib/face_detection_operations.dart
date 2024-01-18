import 'dart:io';
import 'dart:typed_data';
import 'dart:ui';
import 'package:image/image.dart' as img;
import 'package:google_ml_kit/google_ml_kit.dart';

class FaceDetectionOperations {
  Future<Uint8List> performFaceDetection(String imagePath) async {
    final inputImage = InputImage.fromFilePath(imagePath);
    final options = FaceDetectorOptions(
      enableContours: true,
      enableLandmarks: true,
    );
    final faceDetector = GoogleMlKit.vision.faceDetector(options);

    try {
      final List<Face> faces = await faceDetector.processImage(inputImage);

      // Draw bounding boxes on the image
      final img.Image originalImage =
          img.decodeImage(File(imagePath).readAsBytesSync())!;
      for (Face face in faces) {
        final Rect boundingBox = face.boundingBox!;
        img.drawRect(originalImage,
            x1: boundingBox.left.toInt(),
            y1: boundingBox.top.toInt(),
            x2: boundingBox.right.toInt(),
            y2: boundingBox.bottom.toInt(),
            color: img.ColorFloat16.rgb(255, 0, 0));
      }

      return Uint8List.fromList(img.encodeJpg(originalImage));
    } finally {
      faceDetector.close();
    }
  }
}
