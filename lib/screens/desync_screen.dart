import 'package:flutter/material.dart';
import '../core/game.dart';

class _DesyncConfig extends GameConfig {
  _DesyncConfig({required super.article});
}

class DesyncGame extends Game {
  @override
  String get name => 'DeSync';

  @override
  List<String> get articles => const ['Sample'];

  @override
  GameConfig createConfig() => _DesyncConfig(article: articles.first);

  @override
  Widget settingsBuilder(GameConfig config, ValueChanged<GameConfig> onChanged) =>
      const SizedBox.shrink();

  @override
  Widget buildPractice(GameConfig config) => const _DesyncPractice();
}

class _DesyncPractice extends StatelessWidget {
  const _DesyncPractice();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('DeSync')),
      body: const Center(child: Text('DeSync game coming soon')),
    );
  }
}
