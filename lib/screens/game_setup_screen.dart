import 'package:flutter/material.dart';
import '../core/game.dart';

/// Screen allowing the user to choose article and configure settings
/// before starting the practice for a [Game].
class GameSetupScreen extends StatefulWidget {
  final Game game;
  const GameSetupScreen({super.key, required this.game});

  @override
  State<GameSetupScreen> createState() => _GameSetupScreenState();
}

class _GameSetupScreenState extends State<GameSetupScreen> {
  late GameConfig _config;

  @override
  void initState() {
    super.initState();
    _config = widget.game.createConfig();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Setup ${widget.game.name}')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Article'),
            DropdownButton<String>(
              value: _config.article,
              items: widget.game.articles
                  .map((a) => DropdownMenuItem(value: a, child: Text(a)))
                  .toList(),
              onChanged: (value) {
                if (value == null) return;
                setState(() => _config.article = value);
              },
            ),
            const SizedBox(height: 16),
            widget.game.settingsBuilder(_config, (newConfig) {
              setState(() => _config = newConfig);
            }),
            const Spacer(),
            Center(
              child: ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (_) => widget.game.buildPractice(_config),
                    ),
                  );
                },
                child: const Text('Start Practice'),
              ),
            )
          ],
        ),
      ),
    );
  }
}
