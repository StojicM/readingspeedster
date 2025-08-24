import 'package:sqflite/sqflite.dart';

import '../database_service.dart';
import '../models/article.dart';

class ArticleRepository {
  Future<List<Article>> fetchArticles() async {
    final Database db = await DatabaseService.instance.database;
    final List<Map<String, dynamic>> maps = await db.query('Artikli');
    return maps.map((e) => Article.fromMap(e)).toList();
  }
}
