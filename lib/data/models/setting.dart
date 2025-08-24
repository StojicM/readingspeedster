class Setting {
  final String igra;
  final String podesavanje;
  final String format;
  final num vrednost;

  Setting({
    required this.igra,
    required this.podesavanje,
    required this.format,
    required this.vrednost,
  });

  factory Setting.fromMap(Map<String, dynamic> map) {
    return Setting(
      igra: map['igra'] as String,
      podesavanje: map['podešavanje'] as String,
      format: map['format'] as String,
      vrednost: map['vrednost'] as num,
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'igra': igra,
      'podešavanje': podesavanje,
      'format': format,
      'vrednost': vrednost,
    };
  }
}
