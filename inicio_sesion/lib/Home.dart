// ignore_for_file: prefer_const_constructors, use_build_context_synchronously

import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:inicio_sesion/Usuario/Principal.dart';
import 'package:inicio_sesion/registro.dart';
import 'package:http/http.dart' as http;

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final TextEditingController usuarioController = TextEditingController();
  final TextEditingController contrasenaController = TextEditingController();

  String result = '';
  bool _isObscure = true;

  Future<void> enviarDatosAlServidor() async {
    final String usuario = usuarioController.text.trim();
    final String contrasena = contrasenaController.text.trim();

    // Construir el mapa con los datos del usuario
    final Map<String, String> datosUsuario = {
      'email': usuario,
      'password': contrasena,
    };

    try {
      // Convertir el mapa a JSON
      final datosJson = jsonEncode(datosUsuario);

      // Enviar los datos al servidor
      final http.Response response = await http.post(
        Uri.parse('https://parkuis.onrender.com/users/login'),
        headers: <String, String>{
          'Content-Type': 'application/json',
        },
        body: datosJson,
      );

      print('respuesta: $response');

      // Actualizar el estado con la respuesta del servidor
      setState(() {
        result = response.body;
      });

      print('result = $result');
      print('statuscode: ${response.statusCode}');

      if (response.statusCode != 404) {
        //En caso de que si pase
        Navigator.push(
          context,
          MaterialPageRoute(
              builder: (context) => PrincipalUser(
                    result: result,
                  )),
        );
      }
    } catch (e) {
      setState(() {
        result = 'Error al enviar los datos: $e';
      });
      print('no se pudo porque: $e');
      showDialog(
        context: context,
        barrierDismissible: true,
        builder: (BuildContext context) {
          return const AlertDialog(
            title: Text('Advertencia'),
            content: Text('Usuario o contraseña incorrecto'),
          );
        },
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Center(
                child: Image.asset(
                  'images/logoCompleto.png',
                  width: 200, // Ancho de la imagen
                  height: 200, // Alto de la imagen
                ),
              ),
              TextField(
                controller: usuarioController,
                decoration: InputDecoration(
                  labelText: 'Usuario',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                ),
                onChanged: (_) {
                  setState(() {
                    result = ''; // Limpiar el resultado al cambiar el texto
                  });
                },
              ),
              SizedBox(height: 16),
              TextField(
                controller: contrasenaController,
                obscureText: _isObscure,
                decoration: InputDecoration(
                  labelText: 'Contraseña',
                  suffixIcon: IconButton(
                    icon: Icon(
                      _isObscure ? Icons.visibility_off : Icons.visibility,
                      color: _isObscure ? Colors.grey : Colors.green,
                    ),
                    onPressed: () {
                      setState(() {
                        _isObscure = !_isObscure;
                      });
                    },
                  ),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                ),
                onChanged: (_) {
                  setState(() {
                    result = ''; // Limpiar el resultado al cambiar el texto
                  });
                },
              ),
              SizedBox(height: 16),
              ElevatedButton(
                onPressed:
                    enviarDatosAlServidor, // Llamar al método para enviar datos
                style: ElevatedButton.styleFrom(
                  primary: Color.fromARGB(255, 103, 165, 62),
                ),
                child: Text('Iniciar Sesión'),
              ),
              SizedBox(height: 32),
              Text('¿No tienes una cuenta?'),
              ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => RegistroScreen()),
                  );
                },
                style: ElevatedButton.styleFrom(
                  primary: Color.fromARGB(255, 103, 165, 62),
                ),
                child: Text('Registrarse'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
