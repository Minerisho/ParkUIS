// ignore_for_file: prefer_const_constructors

import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:inicio_sesion/clases/vehiculo.dart';

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
  late String token;
  bool isLoading = true;

  List<Vehiculo> result = [];
  @override
  void initState() {
    super.initState();
    processHeredatedData(widget.result);
    obtenerVehiculos();
  }

  Future<void> obtenerVehiculos() async {
    try {
      print('por si acaso este es el token: $token');
      // Enviar los datos al servidor con una solicitud GET

      final response = await http.get(
          Uri.parse(
              'https://parkuis.onrender.com/users/vehiculo/mis-vehiculos'),
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token $token',
          });
      // Actualizar el estado con la respuesta del servidor
      if (response.statusCode == 200) {
        final List<dynamic> jsonData = jsonDecode(response.body);
        final List<Vehiculo> vehiculos =
            jsonData.map((item) => Vehiculo.fromJson(item)).toList();

        setState(() {
          result = vehiculos;
        });
      } else {
        print('Error al obtener los datos: ${response.statusCode}');
      }
      print("status code vehiculo: ${response.statusCode}");
    } catch (e) {
      print('Error: $e');
    }
    ;
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
      appBar: AppBar(
        title: Text('Información de usuario'),
      ),
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
                  SizedBox(height: 20),
                  Divider(
                    thickness: 2.0,
                  ),
                  SizedBox(height: 20),
                  Text(
                    'Vehículos Asociados:',
                    style: TextStyle(fontSize: 20),
                  ),
                  SizedBox(height: 8),
                  result.isEmpty
                      ? Center(child: CircularProgressIndicator())
                      : Expanded(
                          child: ListView.builder(
                            itemCount: result.length,
                            itemBuilder: (context, index) {
                              final vehiculo = result[index];
                              return ListTile(
                                title: Text(vehiculo.placa),
                                subtitle: Text(
                                    'Modelo: ${vehiculo.modelo ?? 'N/A'}\nTipo: ${vehiculo.tipoVehiculo}\nMarca: ${vehiculo.marca}'),
                              );
                            },
                          ),
                        ),
                ],
              ),
            ),
    );
  }
}
