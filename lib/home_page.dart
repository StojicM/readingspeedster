import 'package:flutter/material.dart';
import 'core/game.dart';
import 'screens/game_setup_screen.dart';
import 'screens/imagine_screen.dart';
import 'screens/accumulation_screen.dart';
import 'screens/desync_screen.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    final games = <Game>[
      ImagineGame(),
      AccumulationGame(),
      DesyncGame(),
    ];

    return Scaffold(
      appBar: AppBar(title: const Text('Reading Speedster')),
      body: GridView.count(
        crossAxisCount: 2,
        padding: const EdgeInsets.all(16),
        mainAxisSpacing: 16,
        crossAxisSpacing: 16,
        children: games
            .map(
              (game) => ElevatedButton(
                style: ElevatedButton.styleFrom(padding: const EdgeInsets.all(8)),
                onPressed: () => Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => GameSetupScreen(game: game),
                  ),
                ),
                child: Text(game.name, textAlign: TextAlign.center),
              ),
            )
            .toList(),
      ),
      drawer: Drawer(
        child: ListView(
          children: [
            const DrawerHeader(
              decoration: BoxDecoration(color: Colors.deepOrange),
              child: Center(child: Text('Menu')),
            ),
            ListTile(
              leading: const Icon(Icons.info_outline),
              title: const Text('Tutorial'),
              onTap: () {},
            ),
            ListTile(
              leading: const Icon(Icons.settings),
              title: const Text('Settings'),
              onTap: () {},
            ),
          ],
        ),
      ),
    );
  }
}
