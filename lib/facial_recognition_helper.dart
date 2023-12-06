import 'package:tflite_flutter/tflite_flutter.dart';

class FacialRecognitionHelper {
  static Interpreter? _interpreter;

  static Future<void> loadModel() async {
    try {
      _interpreter = await Interpreter.fromAsset(
          'assets/your_facial_recognition_model.tflite');
    } catch (e) {
      print('Error loading the model: $e');
    }
  }

  static Future<bool> detectFace(String imagePath) async {
    try {
      if (_interpreter == null) {
        print(
            'Model not loaded. Call loadModel() before performing facial recognition.');
        return false;
      }

      var recognitions = await _interpreter.(
        path: imagePath,
        model: 'SSDMobileNet',
        imageMean: 127.5,
        imageStd: 127.5,
        threshold: 0.4,
        numResultsPerClass: 1,
      );

      return recognitions.isNotEmpty;
    } catch (e) {
      print('Error during facial recognition: $e');
      return false;
    }
  }

  static void closeModel() {
    if (_interpreter != null) {
      _interpreter!.close();
      _interpreter = null;
    }
  }
}
