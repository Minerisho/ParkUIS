import 'package:flutter/material.dart';
import 'package:inicio_sesion/Usuario/vehiculos.dart';
import 'package:inicio_sesion/Usuario/DatosUsuario.dart';

class PrincipalUser extends StatefulWidget {
  final String result;

  const PrincipalUser({Key? key, required this.result}) : super(key: key);
  @override
  _PrincipalUserState createState() => _PrincipalUserState();
}

class _PrincipalUserState extends State<PrincipalUser> {
  int _selectedIndex = 0;
  late List<Widget> _pages;

  @override
  void initState() {
    super.initState();
    _pages = [
      DatosUsuarioPage(result: widget.result),
      VehiculoPage(result: widget.result),
    ];
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Información de usuario'),
      ),
      body: IndexedStack(
        index: _selectedIndex,
        children: _pages,
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: 'Persona',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.directions_car),
            label: 'Vehículos',
          ),
          // BottomNavigationBarItem(
          //   icon: Icon(Icons.history),
          // ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.green[800],
        onTap: _onItemTapped,
      ),
    );
  }
}
