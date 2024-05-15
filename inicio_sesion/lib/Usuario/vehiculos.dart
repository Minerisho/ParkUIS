// ignore_for_file: prefer_const_constructors

import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:inicio_sesion/clases/vehiculo.dart';

class VehiculoPage extends StatefulWidget {
  final String result;

  const VehiculoPage({Key? key, required this.result}) : super(key: key);

  @override
  _VehiculoPageState createState() => _VehiculoPageState();
}

class _VehiculoPageState extends State<VehiculoPage> {
  late String token;
  bool isLoading = true;

  List<Vehiculo> result = [];
  @override
  void initState() {
    super.initState();
    processHeredatedData(widget.result);
    obtenerVehiculos();
  }

  Future<void> processHeredatedData(String result) async {
    Map<String, dynamic> jsonData = jsonDecode(result);
    token = jsonData['token'];

    setState(() {
      isLoading = false;
    });
  }

  Future<void> obtenerVehiculos() async {
    try {
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
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text(
                      'Vehículos Asociados:',
                      style: TextStyle(fontSize: 20),
                      textAlign: TextAlign.center,
                    ),
                    SizedBox(height: 8),
                    result.isEmpty
                        ? Center(child: CircularProgressIndicator())
                        : Expanded(
                            child: ListView.builder(
                              itemCount: result.length,
                              itemBuilder: (context, index) {
                                final vehiculo = result[index];
                                return Column(
                                  children: [
                                    GestureDetector(
                                      onLongPress: () {
                                        showDialog(
                                          context: context,
                                          builder: (BuildContext context) {
                                            return AlertDialog(
                                              title: Text(
                                                  'Opciones de Vehículo \n ${vehiculo.modelo}'),
                                              content: Column(
                                                mainAxisSize: MainAxisSize.min,
                                                children: [
                                                  ElevatedButton(
                                                    onPressed: () {
                                                      // Acción del primer botón
                                                      Navigator.of(context)
                                                          .pop();
                                                    },
                                                    style: ElevatedButton
                                                        .styleFrom(
                                                      primary: Color.fromARGB(
                                                          255, 103, 165, 62),
                                                    ),
                                                    child: Text('Editar'),
                                                  ),
                                                  ElevatedButton(
                                                    onPressed: () {
                                                      // Acción del segundo botón
                                                      Navigator.of(context)
                                                          .pop();
                                                    },
                                                    style: ElevatedButton
                                                        .styleFrom(
                                                      primary: Color.fromARGB(
                                                          255, 103, 165, 62),
                                                    ),
                                                    child: Text('Eliminar'),
                                                  ),
                                                ],
                                              ),
                                            );
                                          },
                                        );
                                      },
                                      child: Container(
                                        decoration: BoxDecoration(
                                          color: Colors.white,
                                          borderRadius:
                                              BorderRadius.circular(10.0),
                                          boxShadow: [
                                            BoxShadow(
                                              color:
                                                  Colors.grey.withOpacity(0.5),
                                              spreadRadius: 2,
                                              blurRadius: 5,
                                              offset: Offset(0, 3),
                                            ),
                                          ],
                                        ),
                                        margin:
                                            EdgeInsets.symmetric(vertical: 4.0),
                                        padding: EdgeInsets.all(8.0),
                                        child: ListTile(
                                          title: Text(
                                            vehiculo.placa,
                                            textAlign: TextAlign.center,
                                          ),
                                          subtitle: Text(
                                            'Modelo: ${vehiculo.modelo ?? 'N/A'}\nTipo: ${vehiculo.tipoVehiculo}\nMarca: ${vehiculo.marca}',
                                            textAlign: TextAlign.center,
                                          ),
                                        ),
                                      ),
                                    ),
                                    if (index < result.length - 1)
                                      SizedBox(height: 8),
                                  ],
                                );
                              },
                            ),
                          ),
                  ],
                ),
              ),
            ),
    );
  }
}
