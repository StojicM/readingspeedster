import 'package:flutter/material.dart';

/// Screen allowing users to paste or type a text and prepare it for practice.
class TextPrepScreen extends StatelessWidget {
  const TextPrepScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = TextEditingController();
    return Scaffold(
      appBar: AppBar(title: const Text('Text Prep')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Paste or type your text below:'),
            const SizedBox(height: 8),
            Expanded(
              child: TextField(
                controller: controller,
                expands: true,
                maxLines: null,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  alignLabelWithHint: true,
                ),
              ),
            ),
            const SizedBox(height: 16),
            Align(
              alignment: Alignment.centerRight,
              child: ElevatedButton(
                onPressed: () {
                  // Placeholder for text preparation logic.
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text('Text prepared')),
                  );
                },
                child: const Text('Prepare'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

