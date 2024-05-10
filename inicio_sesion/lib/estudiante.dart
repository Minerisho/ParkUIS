// ignore_for_file: prefer_const_constructors

import 'dart:convert';

import 'package:flutter/material.dart';

class EstudiantePage extends StatefulWidget {
  final String result;

  const EstudiantePage({Key? key, required this.result}) : super(key: key);

  @override
  _EstudiantePageState createState() => _EstudiantePageState();
}

class _EstudiantePageState extends State<EstudiantePage> {
  late String email;
  late String nombres;
  late String apellidos;
  late int cc;
  late int numCel;
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    processHeredatedData(widget.result);
  }

  Future<void> processHeredatedData(String result) async {
    Map<String, dynamic> jsonData = jsonDecode(result);
    email = jsonData['usuario']['email'];
    nombres = replaceTildesWithUnicode(jsonData['usuario']['nombres']);
    apellidos = replaceTildesWithUnicode(jsonData['usuario']['apellidos']);
    numCel = jsonData['usuario']['num_cel'];
    cc = jsonData['usuario']['CC'];

    setState(() {
      isLoading = false;
    });
  }

  String replaceTildesWithUnicode(String text) {
    final replacements = {
      'Ã': 'Á',
      'Ã¡': 'á',
      'Ã': 'É',
      'Ã©': 'é',
      'Ã': 'Í',
      'Ã': 'í',
      'ñ': '\u{00F1}',
    };

    for (var char in replacements.keys) {
      text = text.replaceAll(char, replacements[char]!);
    }

    return text;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Información de usuario'),
        ),
        body: isLoading
            ? Center(
                child: CircularProgressIndicator(),
              )
            : Padding(
                padding: const EdgeInsets.all(16.0),
                child: (Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Correo: $email',
                        style: TextStyle(fontSize: 16),
                      ),
                      Text(
                        'Nombre: ${nombres} $apellidos',
                        style: TextStyle(fontSize: 16),
                      ),
                      Text(
                        'Cedula: ${cc}',
                        style: TextStyle(fontSize: 16),
                      ),
                      Text(
                        'Telefono: ${numCel}',
                        style: TextStyle(fontSize: 16),
                      ),
                      SizedBox(height: 20),
                      Divider(
                        thickness: 2.0,
                      ),
                      SizedBox(height: 20),
                      Text(
                        'Vehiculos Asociados:',
                        style: TextStyle(fontSize: 20),
                      ),
                      SizedBox(height: 8),
                    ]))));
  }
}
