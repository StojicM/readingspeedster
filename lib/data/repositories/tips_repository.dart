import 'package:sqflite/sqflite.dart';

import '../database_service.dart';
import '../models/tip.dart';

class TipsRepository {
  Future<List<Tip>> fetchTips() async {
    final Database db = await DatabaseService.instance.database;
    final List<Map<String, dynamic>> maps = await db.query('Tips');
    return maps.map((e) => Tip.fromMap(e)).toList();
  }
}
