// ignore_for_file: prefer_const_constructors, library_private_types_in_public_api

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
    // de ser necesario decodificar esto deberia servir, tomar con pinzas
    //final String decodedResult = utf8.decode(result);
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
              child: Center(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    SizedBox(height: 8),
                    Container(
                      padding: EdgeInsets.all(16.0),
                      margin: EdgeInsets.only(bottom: 16.0),
                      decoration: BoxDecoration(
                        color: const Color.fromARGB(255, 45, 49, 51),
                        borderRadius:
                            BorderRadius.circular(10.0), // Bordes redondeados
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Text(
                            email,
                            style: TextStyle(
                                fontSize: 16,
                                color: Colors.white), // Texto blanco
                          ),
                          SizedBox(height: 8), // Espacio entre los textos
                          Text(
                            '$nombres $apellidos',
                            style: TextStyle(
                                fontSize: 16,
                                color: Colors.white), // Texto blanco
                          ),
                          SizedBox(height: 8), // Espacio entre los textos
                          Text(
                            'Cédula: $cc',
                            style: TextStyle(
                                fontSize: 16,
                                color: Colors.white), // Texto blanco
                          ),
                          SizedBox(height: 8), // Espacio entre los textos
                          Text(
                            'Teléfono: $numCel',
                            style: TextStyle(
                                fontSize: 16,
                                color: Colors.white), // Texto blanco
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
    );
  }
}
