import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:image_picker/image_picker.dart';
import 'package:login_app/constants.dart';
import 'package:login_app/page/profile.dart';

Widget bottomSheet(BuildContext context) {
  Future pickImage(ImageSource source) async {
    try {
      final imageFile = await ImagePicker().pickImage(source: source);
      if (imageFile == null) return;

      final imageTemp = File(imageFile.path);
      Profile.image = imageTemp;
    } on PlatformException catch (e) {
      print('Failed to pick image: $e');
    }
  }

  return Container(
    height: MediaQuery.of(context).size.height * 0.13,
    width: MediaQuery.of(context).size.width,
    margin: EdgeInsets.symmetric(horizontal: 15, vertical: 20),
    child: Column(children: [
      Text(
        "Envie uma foto",
        style: TextStyle(fontSize: 20.0),
      ),
      SizedBox(
        height: MediaQuery.of(context).size.height * 0.02,
      ),
      Row(
        children: [
          ElevatedButton.icon(
              style: ElevatedButton.styleFrom(
                  elevation: 0.0, primary: kBackgroundColor2),
              onPressed: () {
                pickImage(ImageSource.camera);
              },
              icon: Icon(Icons.camera),
              label: const Text("Tire uma foto")),
          SizedBox(
            width: MediaQuery.of(context).size.width * 0.08,
          ),
          ElevatedButton.icon(
              style: ElevatedButton.styleFrom(
                  elevation: 0.0, primary: kBackgroundColor2),
              onPressed: () => pickImage(ImageSource.gallery),
              icon: const Icon(Icons.photo_album),
              label: const Text("Selecione uma foto"))
        ],
      ),
    ]),
  );
}
