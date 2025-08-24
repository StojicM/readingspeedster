import 'package:flutter/material.dart';
import '../core/game.dart';

class _AccumulationConfig extends GameConfig {
  _AccumulationConfig({required super.article});
}

class AccumulationGame extends Game {
  @override
  String get name => 'Accumulation';

  @override
  List<String> get articles => const ['Sample'];

  @override
  GameConfig createConfig() => _AccumulationConfig(article: articles.first);

  @override
  Widget settingsBuilder(GameConfig config, ValueChanged<GameConfig> onChanged) =>
      const SizedBox.shrink();

  @override
  Widget buildPractice(GameConfig config) => const _AccumulationPractice();
}

class _AccumulationPractice extends StatelessWidget {
  const _AccumulationPractice();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Accumulation')),
      body: const Center(child: Text('Accumulation game coming soon')),
    );
  }
}
