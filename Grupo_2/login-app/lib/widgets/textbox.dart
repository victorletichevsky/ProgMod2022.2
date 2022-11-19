import 'package:flutter/material.dart';

Widget TextBox(BuildContext context, description) {
  return Center(
    child: Container(
      margin: EdgeInsets.all(20),
      height: MediaQuery.of(context).size.height * 0.2,
      child: TextFormField(
        maxLines: 5,
        decoration: InputDecoration(
          fillColor: Colors.white,
          filled: true,
          border: OutlineInputBorder(),
          hintText: description,
        ),
      ),
    ),
  );
}
