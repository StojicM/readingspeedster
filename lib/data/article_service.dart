import 'models/article.dart';
import 'repositories/article_repository.dart';

/// Simple service wrapper around [ArticleRepository].
class ArticleService {
  final ArticleRepository _repository = ArticleRepository();

  Future<List<Article>> loadArticles() => _repository.fetchArticles();
}

