import 'dart:io';

import 'package:flutter/services.dart';
import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqflite.dart';

class DatabaseService {
  DatabaseService._();

  static final DatabaseService instance = DatabaseService._();
  static const String _dbName = 'rs.db';

  Database? _database;

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDatabase();
    return _database!;
  }

  Future<Database> _initDatabase() async {
    final directory = await getApplicationDocumentsDirectory();
    final path = '${directory.path}/$_dbName';

    if (!await File(path).exists()) {
      await _copyDatabase(path);
    }

    return openDatabase(path);
  }

  Future<void> _copyDatabase(String path) async {
    final data = await rootBundle.load('assets/db/$_dbName');
    final bytes =
        data.buffer.asUint8List(data.offsetInBytes, data.lengthInBytes);
    await File(path).writeAsBytes(bytes, flush: true);
  }
}
