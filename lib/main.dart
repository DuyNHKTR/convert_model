import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'database_helper.dart';
import 'dart:typed_data';
import 'package:demo/object_detection.dart'; // Replace with the correct import

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Image Database App',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final ImagePicker _picker = ImagePicker();
  TextEditingController _imagePathController = TextEditingController();
  List<String> imagePaths = [];
  List<bool> selectedImages = List<bool>.generate(0, (index) => false);
  ObjectDetection objectDetection = ObjectDetection();
  _insertImage() async {
    final XFile? pickedFile =
        await _picker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      String imagePath = pickedFile.path;
      Map<String, dynamic> row = {
        DatabaseHelper.columnImagePath: imagePath,
      };
      final id = await DatabaseHelper.instance.insert(row);
      print('Image inserted with id: $id');
      _showImageAddedDialog();
      _loadImages(); // Refresh the list of images
    }
  }

  _loadImages() async {
    List<Map<String, dynamic>> allRows =
        await DatabaseHelper.instance.queryAll();
    setState(() {
      imagePaths = allRows
          .map((row) => row[DatabaseHelper.columnImagePath] as String)
          .toList();
      // Initialize the list of selected images
      selectedImages = List<bool>.generate(imagePaths.length, (index) => false);
    });
  }

  _showImageAddedDialog() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Image Added'),
          content: Text('The image has been added successfully.'),
          actions: [
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }

  _deleteSelectedImages() async {
    // Delete selected images from the database
    for (int i = selectedImages.length - 1; i >= 0; i--) {
      if (selectedImages[i]) {
        await DatabaseHelper.instance.delete(imagePaths[i]);
        selectedImages.removeAt(i);
        imagePaths.removeAt(i);
      }
    }
    _loadImages(); // Refresh the list of images after deletion
  }

  _objectDetect() async {
    final XFile? pickedFile =
        await _picker.pickImage(source: ImageSource.gallery);
    if (pickedFile != null) {
      String imagePath = pickedFile.path;
      Uint8List detectedImage = objectDetection.analyseImage(imagePath);
      _showDetectedImage(detectedImage);
    }
  }

  _showDetectedImage(Uint8List detectedImage) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Object Detection Result'),
          content: Image.memory(detectedImage),
          actions: [
            ElevatedButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('OK'),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Image Database App'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            ElevatedButton(
              onPressed: _insertImage,
              child: Text('Add Image'),
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: _deleteSelectedImages,
              child: Text('Delete Selected Images'),
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: _objectDetect,
              child: Text('Object Detect'),
            ),
            Expanded(
              child: GridView.builder(
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 4,
                  crossAxisSpacing: 8.0,
                  mainAxisSpacing: 8.0,
                ),
                itemCount: imagePaths.length,
                itemBuilder: (context, index) {
                  return GestureDetector(
                    onTap: () {
                      setState(() {
                        // Toggle the selection status when tapped
                        selectedImages[index] = !selectedImages[index];
                      });
                    },
                    child: Stack(
                      children: [
                        Image.file(File(imagePaths[index])),
                        if (selectedImages[index])
                          Positioned(
                            top: 8.0,
                            right: 8.0,
                            child: Icon(
                              Icons.check_circle,
                              color: Colors.green,
                              size: 24.0,
                            ),
                          ),
                      ],
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
