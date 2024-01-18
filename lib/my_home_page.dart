import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import '../database/database_helper.dart';
import '../object_detection/object_detection.dart';

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final ImagePicker _imagePicker = ImagePicker();
  final DatabaseHelper _databaseHelper = DatabaseHelper();
  final ObjectDetection _objectDetection = ObjectDetection();

  List<String> imagePaths = [];
  List<bool> selectedImages = [];

  // ... (rest of the class content)
}
