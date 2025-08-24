class Tip {
  final String tip;
  final num weigth;

  Tip({required this.tip, required this.weigth});

  factory Tip.fromMap(Map<String, dynamic> map) {
    return Tip(
      tip: map['tip'] as String,
      weigth: map['weigth'] as num,
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'tip': tip,
      'weigth': weigth,
    };
  }
}
