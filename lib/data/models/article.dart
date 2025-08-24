class Article {
  final String naslov;
  final String text;

  Article({required this.naslov, required this.text});

  factory Article.fromMap(Map<String, dynamic> map) {
    return Article(
      naslov: map['naslov'] as String,
      text: map['text'] as String,
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'naslov': naslov,
      'text': text,
    };
  }
}
