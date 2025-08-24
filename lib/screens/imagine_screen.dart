import 'dart:async';
import 'package:flutter/material.dart';
import '../core/game.dart';

class ImagineConfig extends GameConfig {
  double displaySeconds;
  ImagineConfig({required super.article, this.displaySeconds = 2.0});
}

class ImagineGame extends Game {
  static const Map<String, List<String>> _articles = {
    'Sample': ['wizardry', 'science', 'flutter'],
    'Tech': ['binary', 'widget', 'state'],
  };

  @override
  String get name => 'Imagine';

  @override
  List<String> get articles => _articles.keys.toList();

  @override
  ImagineConfig createConfig() => ImagineConfig(article: articles.first);

  @override
  Widget settingsBuilder(GameConfig config, ValueChanged<GameConfig> onChanged) {
    final c = config as ImagineConfig;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('Display Seconds: ${c.displaySeconds.toStringAsFixed(1)}'),
        Slider(
          min: 0.5,
          max: 5,
          divisions: 9,
          value: c.displaySeconds,
          label: c.displaySeconds.toStringAsFixed(1),
          onChanged: (v) => onChanged(
            ImagineConfig(article: c.article, displaySeconds: v),
          ),
        ),
      ],
    );
  }

  @override
  Widget buildPractice(GameConfig config) {
    final c = config as ImagineConfig;
    final words = _articles[c.article] ?? [];
    return ImaginePractice(words: words, displaySeconds: c.displaySeconds);
  }
}

class ImaginePractice extends StatefulWidget {
  final List<String> words;
  final double displaySeconds;
  const ImaginePractice({super.key, required this.words, required this.displaySeconds});

  @override
  State<ImaginePractice> createState() => _ImaginePracticeState();
}

class _ImaginePracticeState extends State<ImaginePractice> {
  late Timer _timer;
  int _index = 0;
  bool _showWord = true;

  @override
  void initState() {
    super.initState();
    _timer = Timer.periodic(
      Duration(milliseconds: (widget.displaySeconds * 1000).round()),
      (_) {
        setState(() {
          _showWord = !_showWord;
          if (_showWord) {
            _index = (_index + 1) % widget.words.length;
          }
        });
      },
    );
  }

  @override
  void dispose() {
    _timer.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Imagine')),
      body: Center(
        child: _showWord && widget.words.isNotEmpty
            ? Text(widget.words[_index], style: const TextStyle(fontSize: 40))
            : const SizedBox.shrink(),
      ),
    );
  }
}
