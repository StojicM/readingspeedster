import 'package:flutter/widgets.dart';

/// Base class for all game configuration objects.
abstract class GameConfig {
  String article;
  GameConfig({required this.article});
}

/// Base interface for games.
abstract class Game {
  /// Display name for the game.
  String get name;

  /// List of available articles for practice.
  List<String> get articles;

  /// Create a default configuration for this game.
  GameConfig createConfig();

  /// Build widgets to configure game specific settings.
  Widget settingsBuilder(GameConfig config, ValueChanged<GameConfig> onChanged);

  /// Build the practice widget using the provided configuration.
  Widget buildPractice(GameConfig config);
}
