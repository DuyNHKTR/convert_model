import 'dart:io';

class ImageManagement {
  List<String> imagePaths = [];
  List<bool> selectedImages = [];

  Future<void> insertImage() async {
    // Implement the logic for adding images
  }

  Future<void> deleteSelectedImages() async {
    // Implement the logic for deleting selected images
  }

  void toggleSelection(int index) {
    selectedImages[index] = !selectedImages[index];
  }
}
