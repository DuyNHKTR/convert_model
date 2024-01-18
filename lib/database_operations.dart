import 'package:demo/database_helper.dart';

class DatabaseOperations {
  static final String columnId = 'id';
  static final String columnImagePath = 'imagePath';

  DatabaseHelper _databaseHelper = DatabaseHelper();

  Future<int> insertImage(String imagePath) async {
    Map<String, dynamic> row = {columnImagePath: imagePath};
    return await _databaseHelper.insert(row);
  }

  Future<List<Map<String, dynamic>>> queryAllImages() async {
    return await _databaseHelper.queryAll();
  }

  Future<void> deleteImage(String imagePath) async {
    await _databaseHelper.delete(imagePath);
  }
}
