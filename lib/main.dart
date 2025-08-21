import 'package:flutter/material.dart';
import 'home_page.dart';

void main() => runApp(const ReadingSpeedster());

class ReadingSpeedster extends StatelessWidget {
  const ReadingSpeedster({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Reading Speedster',
      theme: ThemeData.dark(),
      home: const HomePage(),
    );
  }
}
