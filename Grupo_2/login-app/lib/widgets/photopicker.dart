// REQUISITOS PARA IMPLEMENTAÇÃO
// BIBLIOTECA getwidget: ^2.0.4 ou maior
// NECESSÁRIO COLOCAR NO ARQUIVO ONDE FOR IMPLEMENTADO A FUNÇÃO addImageToContainer()

// void addImageToContainer() {
//     if (Profile.image != null) {
//       setState(() {
//         Profile.image = Profile.image;
//       });
//     }
//   }

// NECESSÁRIO CRIAR VARIAVEL PARA ARMAZENAR FOTO
// static File? image;

import 'package:flutter/material.dart';
import 'package:getwidget/getwidget.dart';
import 'package:login_app/page/profile.dart';
import 'package:login_app/widgets/bottomsheet.dart';

Widget PhotoPicker(BuildContext context, changeButton, photoLabel) {
  return Padding(
    padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
    child: Center(
      child: Stack(
        children: List.generate(
          1,
          (stackIndex) {
            if (Profile.image == null) {
              return Container(
                width: MediaQuery.of(context).size.width * 0.3,
                height: MediaQuery.of(context).size.height * 0.15,
                child: OutlinedButton.icon(
                    style: OutlinedButton.styleFrom(
                        side: BorderSide(width: 2.0), elevation: 1.0),
                    onPressed: () async {
                      await showModalBottomSheet(
                          context: context,
                          builder: ((context) => (bottomSheet(context))));
                      changeButton();
                    },
                    icon: Icon(
                      Icons.photo,
                      color: Colors.white,
                    ),
                    label: Text(photoLabel,
                        style: TextStyle(color: Colors.white))),
              );
            } else {
              return CircleAvatar(
                radius: MediaQuery.of(context).size.width * 0.19,
                backgroundColor: Colors.black,
                child: GFAvatar(
                  backgroundImage: FileImage(Profile.image!),
                  shape: GFAvatarShape.circle,
                  radius: MediaQuery.of(context).size.width * 0.18,
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.end,
                        children: [
                          IconButton(
                            onPressed: () async {
                              await showModalBottomSheet(
                                  context: context,
                                  builder: ((context) =>
                                      (bottomSheet(context))));
                              changeButton();
                            },
                            icon: Icon(Icons.add_a_photo),
                            iconSize: 30,
                            color: Colors.white,
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              );
            }
          },
        ),
      ),
    ),
  );
}
