import 'package:flutter/material.dart';
import 'package:flutterzin/segunda_tela.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MinhaPrimeiraTela(),
    );
  }
}


class MinhaPrimeiraTela extends StatelessWidget {
  const MinhaPrimeiraTela({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title: const Text('Ponderada do Zeferino'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.asset('assets/murilo.jpeg',
            width: 300,
            height: 300,
            fit:BoxFit.cover,
            ),
          ),
          const Text(
            'Bem vindo! Clique no botão abaixo para acessar suas tarefas!',
            textAlign: TextAlign.center,
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.push(context, MaterialPageRoute(builder: (context) => const MinhaSegundaTela()));
            },
            child: const Text('Acesse aqui'),
          ),
        ]
      ),
    );
  }
}