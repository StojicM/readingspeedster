import 'package:flutter/material.dart';

class DesyncScreen extends StatelessWidget {
  const DesyncScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('DeSync')),
      body: const Center(child: Text('DeSync game coming soon')),
    );
  }
}
