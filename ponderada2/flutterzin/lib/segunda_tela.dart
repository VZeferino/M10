import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class MinhaSegundaTela extends StatefulWidget {
  const MinhaSegundaTela({super.key});

  @override
  State<MinhaSegundaTela> createState() => _MinhaSegundaTelaState();
}

class _MinhaSegundaTelaState extends State<MinhaSegundaTela> {
  final TextEditingController _controller = TextEditingController();
  String _saida = '';

  void _makeRequest() async {
    final uri = Uri.parse('http://172.24.0.2:5000/tasks');
    String username = 'user1';
    String password = 'senha1';
    String basicAuth = 'Basic ${base64Encode(utf8.encode('$username:$password'))}';

    try {
      final response = await http.post(
        uri,
        headers: <String, String>{
          'Authorization': basicAuth,
        },
      );

      if (mounted) {
        setState(() {
        _saida = response.body;
      });
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _saida = "Erro ao fazer a requisição: $e";
      });
    }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Minha segunda tela'),
      ),
      body: Column(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              controller: _controller,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Digite seu nome',
              ),
            ),
          ),
          ElevatedButton(
            onPressed: _makeRequest,
            child: const Text("Consultar"),
          ),
          Text(_saida),
        ],
      ),
    );
  }
}