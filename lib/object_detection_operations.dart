import 'dart:typed_data';
import 'package:image_picker/image_picker.dart';
import 'package:demo/object_detection.dart';

class ObjectDetectionOperations {
  final ObjectDetection _objectDetection = ObjectDetection();
  final ImagePicker _imagePicker = ImagePicker();

  Future<Uint8List> analyzeImage() async {
    final XFile? pickedFile =
        await _imagePicker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      String imagePath = pickedFile.path;
      return _objectDetection.analyseImage(imagePath);
    }
    return Uint8List(0);
  }
}
