import 'package:flutter/material.dart';
import 'package:flutterzin/main.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'register.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final emailController = TextEditingController();
    final passwordController = TextEditingController();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextField(
              controller: emailController,
              decoration: const InputDecoration(
                labelText: 'Email',
                border: OutlineInputBorder(),
              ),
              keyboardType: TextInputType.emailAddress,
            ),
            const SizedBox(height: 16.0),
            TextField(
              controller: passwordController,
              decoration: const InputDecoration(
                labelText: 'Senha',
                border: OutlineInputBorder(),
              ),
              obscureText: true,
            ),
            const SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: () async {
                final email = emailController.text;
                final password = passwordController.text;
                try {
                  final response = await http.post(
                    Uri.parse('http://10.128.0.78:5000/login'),
                    headers: <String, String>{
                      'Content-Type': 'application/json',
                    },
                    body: jsonEncode(<String, String>{
                      'email': email,
                      'password': password,
                    }),
                  );

                  if (response.statusCode == 200) {
                    Navigator.pushReplacement(
                      context,
                      MaterialPageRoute(builder: (context) => const MinhaPrimeiraTela()),
                    );
                  } else {
                    showDialog(
                      context: context,
                      builder: (context) => AlertDialog(
                        title: const Text('Erro de Login'),
                        content: Text('Falha ao autenticar: ${response.body}'),
                        actions: <Widget>[
                          TextButton(
                            onPressed: () => Navigator.of(context).pop(),
                            child: const Text('OK'),
                          ),
                        ],
                      ),
                    );
                  }
                } catch (e) {
                  showDialog(
                    context: context,
                    builder: (context) => AlertDialog(
                      title: const Text('Erro'),
                      content: Text('Erro ao conectar ao servidor: $e'),
                      actions: <Widget>[
                        TextButton(
                          onPressed: () => Navigator.of(context).pop(),
                          child: const Text('OK'),
                        ),
                      ],
                    ),
                  );
                }
              },
              child: const Text('Login'),
            ),
            TextButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const RegisterScreen()),
                );
              },
              child: const Text('Não tem uma conta? Cadastre-se aqui'),
            ),
          ],
        ),
      ),
    );
  }
}
