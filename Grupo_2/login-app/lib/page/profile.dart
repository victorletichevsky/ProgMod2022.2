import 'dart:io';
import 'package:flutter/material.dart';
import 'package:login_app/widgets/photopicker.dart';
import 'package:login_app/widgets/textbox.dart';

class Profile extends StatefulWidget {
  static const String id = "profile";
  static File? image;
  const Profile({Key? key}) : super(key: key);

  @override
  State<Profile> createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {
  void addImageToContainer() {
    if (Profile.image != null) {
      setState(() {
        Profile.image = Profile.image;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Profile Page"),
          backgroundColor: Colors.black12,
          elevation: 2.0,
        ),
        body: SingleChildScrollView(
          physics: const BouncingScrollPhysics(),
          child: Column(
            children: [
              SizedBox(height: MediaQuery.of(context).size.height * 0.05),
              PhotoPicker(context, addImageToContainer, "Adicione uma foto"),
              const Center(
                child: Text(
                  "Gustavo Soares",
                  style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontSize: 28),
                ),
              ),
              const Center(
                child: Text(
                  "20, Rio de Janeiro",
                  style: TextStyle(color: Colors.white, fontSize: 20),
                ),
              ),
              TextBox(context, "Conte um pouco sobre você"),
            ],
          ),
        ));
  }
}
