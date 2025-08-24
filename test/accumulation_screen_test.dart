import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:readingspeedster/screens/accumulation_screen.dart';

void main() {
  testWidgets('Accumulation screen shows placeholder text', (WidgetTester tester) async {
    final game = AccumulationGame();
    final config = game.createConfig();

    await tester.pumpWidget(MaterialApp(home: game.buildPractice(config)));

    expect(find.text('Accumulation game coming soon'), findsOneWidget);
  });
}
