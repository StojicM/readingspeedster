import 'package:sqflite/sqflite.dart';

import '../database_service.dart';
import '../models/setting.dart';

class SettingsRepository {
  Future<List<Setting>> fetchSettings({String? game}) async {
    final Database db = await DatabaseService.instance.database;
    final List<Map<String, dynamic>> maps = await db.query(
      'Podesavanja',
      where: game != null ? 'igra = ?' : null,
      whereArgs: game != null ? [game] : null,
    );
    return maps.map((e) => Setting.fromMap(e)).toList();
  }
}
