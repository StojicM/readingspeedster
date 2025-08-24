import 'package:flutter/material.dart';

import '../data/article_service.dart';
import '../data/models/article.dart';

/// Screen displaying available articles loaded from the database.
class TekstoviScreen extends StatefulWidget {
  const TekstoviScreen({super.key});

  @override
  State<TekstoviScreen> createState() => _TekstoviScreenState();
}

class _TekstoviScreenState extends State<TekstoviScreen> {
  final ArticleService _service = ArticleService();
  late Future<List<Article>> _articles;

  @override
  void initState() {
    super.initState();
    _articles = _service.loadArticles();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Tekstovi')),
      body: FutureBuilder<List<Article>>(
        future: _articles,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }
          final data = snapshot.data;
          if (data == null || data.isEmpty) {
            return const Center(child: Text('No articles available'));
          }
          return ListView.separated(
            itemCount: data.length,
            separatorBuilder: (_, __) => const Divider(height: 1),
            itemBuilder: (context, index) {
              final article = data[index];
              return ListTile(
                title: Text(article.naslov),
                onTap: () => _showArticle(context, article),
              );
            },
          );
        },
      ),
    );
  }

  void _showArticle(BuildContext context, Article article) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(article.naslov),
        content: SingleChildScrollView(child: Text(article.text)),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Close'),
          ),
        ],
      ),
    );
  }
}

