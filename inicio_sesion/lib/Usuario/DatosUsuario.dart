// ignore_for_file: prefer_const_constructors

import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:inicio_sesion/clases/vehiculo.dart';

class DatosUsuarioPage extends StatefulWidget {
  final String result;

  const DatosUsuarioPage({Key? key, required this.result}) : super(key: key);

  @override
  _DatosUsuarioPageState createState() => _DatosUsuarioPageState();
}

class _DatosUsuarioPageState extends State<DatosUsuarioPage> {
  late String email;
  late String nombres;
  late String apellidos;
  late int cc;
  late int numCel;
  late String token;
  bool isLoading = true;

  List<Vehiculo> result = [];
  @override
  void initState() {
    super.initState();
    processHeredatedData(widget.result);
  }

  Future<void> processHeredatedData(String result) async {
    Map<String, dynamic> jsonData = jsonDecode(result);
    token = jsonData['token'];
    email = jsonData['usuario']['email'];
    nombres = jsonData['usuario']['nombres'];
    apellidos = jsonData['usuario']['apellidos'];
    numCel = jsonData['usuario']['num_cel'];
    cc = jsonData['usuario']['CC'];

    setState(() {
      isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: isLoading
          ? Center(
              child: CircularProgressIndicator(),
            )
          : Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
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
                      'Cédula: ${cc}',
                      style: TextStyle(fontSize: 16),
                    ),
                    Text(
                      'Teléfono: ${numCel}',
                      style: TextStyle(fontSize: 16),
                    ),
                  ]),
            ),
    );
  }
}
