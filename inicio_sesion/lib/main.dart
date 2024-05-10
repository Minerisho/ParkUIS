// ignore_for_file: prefer_const_constructors, use_build_context_synchronously, prefer_for_elements_to_map_fromiterable, avoid_print, deprecated_member_use, use_key_in_widget_constructors, library_private_types_in_public_api, unnecessary_string_interpolations, prefer_const_literals_to_create_immutables, prefer_const_constructors_in_immutables

import 'package:inicio_sesion/Home.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Catay',
      home: HomeScreen(),
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primaryColor: Color.fromARGB(255, 103, 165, 62),
        visualDensity: VisualDensity.adaptivePlatformDensity,
        appBarTheme: AppBarTheme(
          color: Color.fromARGB(255, 103, 165, 62),
        ),
        buttonTheme: ButtonThemeData(
          buttonColor: Color.fromARGB(255, 103, 165, 62),
          textTheme: ButtonTextTheme.primary,
        ),
        inputDecorationTheme: InputDecorationTheme(
          focusedBorder: OutlineInputBorder(
            borderSide: BorderSide(
              color: Color.fromARGB(255, 103, 165, 62),
              width: 2.0,
            ),
          ),
          enabledBorder: OutlineInputBorder(
            borderSide: BorderSide(
              color: Color.fromARGB(255, 103, 165, 62),
              width: 1.0,
            ),
          ),
          labelStyle: TextStyle(
            color: Color.fromARGB(255, 103, 165, 62),
          ),
        ),
        textSelectionTheme: TextSelectionThemeData(
          cursorColor: Color.fromARGB(255, 103, 165, 62),
        ),
      ),
    );
  }
}
