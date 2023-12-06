import 'dart:io';
import 'package:path/path.dart';
import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqflite.dart';

class DatabaseHelper {
  static final _databaseName = 'image_database.db';
  static final _databaseVersion = 1;

  static final table = 'images';

  static final columnId = 'id';
  static final columnImagePath = 'imagePath';

  // make this a singleton class
  DatabaseHelper._privateConstructor();
  static final DatabaseHelper instance = DatabaseHelper._privateConstructor();

  static Database? _database;

  Future<Database> get database async {
    if (_database != null) return _database!;

    _database = await _initDatabase();
    return _database!;
  }

  _initDatabase() async {
    Directory documentsDirectory = await getApplicationDocumentsDirectory();
    String path = join(documentsDirectory.path, _databaseName);
    return await openDatabase(path,
        version: _databaseVersion, onCreate: _onCreate);
  }

  Future _onCreate(Database db, int version) async {
    await db.execute('''
      CREATE TABLE $table (
        $columnId INTEGER PRIMARY KEY,
        $columnImagePath TEXT NOT NULL
      )
    ''');
  }

  Future<int> insert(Map<String, dynamic> row) async {
    Database db = await instance.database;
    return await db.insert(table, row);
  }

  Future<List<Map<String, dynamic>>> queryAll() async {
    Database db = await instance.database;
    return await db.query(table);
  }

  Future<void> deleteItemsWithEmptyPath() async {
    final db = await instance.database;
    await db.delete(table,
        where: '$columnImagePath IS NULL OR $columnImagePath = ""');
  }

  Future<void> delete(String imagePath) async {
    final db = await instance.database;
    await db
        .delete(table, where: '$columnImagePath = ?', whereArgs: [imagePath]);
  }
}
