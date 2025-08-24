import 'package:flutter/material.dart';
import 'core/game.dart';
import 'screens/game_setup_screen.dart';
import 'screens/imagine_screen.dart';
import 'screens/accumulation_screen.dart';
import 'screens/desync_screen.dart';
import 'screens/text_prep_screen.dart';
import 'screens/olaksaonica_screen.dart';
import 'screens/tekstovi_screen.dart';
import 'screens/dynamic_screen.dart';

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
              leading: const Icon(Icons.text_fields),
              title: const Text('Text Prep'),
              onTap: () {
                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const TextPrepScreen(),
                  ),
                );
              },
            ),
            ListTile(
              leading: const Icon(Icons.library_books),
              title: const Text('Tekstovi'),
              onTap: () {
                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const TekstoviScreen(),
                  ),
                );
              },
            ),
            ListTile(
              leading: const Icon(Icons.lightbulb_outline),
              title: const Text('Olaksaonica'),
              onTap: () {
                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const OlaksaonicaScreen(),
                  ),
                );
              },
            ),
            ListTile(
              leading: const Icon(Icons.dynamic_feed),
              title: const Text('Dynamic'),
              onTap: () {
                Navigator.pop(context);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => const DynamicScreen(),
                  ),
                );
              },
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
