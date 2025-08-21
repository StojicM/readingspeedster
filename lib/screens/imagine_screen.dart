import 'dart:async';
import 'package:flutter/material.dart';

class ImagineScreen extends StatefulWidget {
  const ImagineScreen({super.key});

  @override
  State<ImagineScreen> createState() => _ImagineScreenState();
}

class _ImagineScreenState extends State<ImagineScreen> {
  final _words = ['wizardry', 'science', 'flutter'];
  late Timer _timer;
  int _index = 0;
  bool _showWord = true;
  double displaySeconds = 2.0;
  TextStyle style = const TextStyle(fontSize: 40);

  @override
  void initState() {
    super.initState();
    _timer = Timer.periodic(
      Duration(milliseconds: (displaySeconds * 1000).round()),
      (_) {
        setState(() {
          _showWord = !_showWord;
          if (_showWord) {
            _index = (_index + 1) % _words.length;
          }
        });
      },
    );
  }

  @override
  void dispose() {
    _timer.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Imagine')),
      body: Center(
        child:
            _showWord ? Text(_words[_index], style: style) : const SizedBox.shrink(),
      ),
    );
  }
}
