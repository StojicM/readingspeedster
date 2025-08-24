import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:readingspeedster/home_page.dart';

void main() {
  testWidgets('HomePage shows available games', (WidgetTester tester) async {
    await tester.pumpWidget(const MaterialApp(home: HomePage()));

    expect(find.text('Imagine'), findsOneWidget);
    expect(find.text('Accumulation'), findsOneWidget);
    expect(find.text('Desync'), findsOneWidget);
  });
}
