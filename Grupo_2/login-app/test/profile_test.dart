import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:login_app/main.dart';
import 'package:login_app/widgets/textbox.dart';
import 'package:login_app/widgets/photopicker.dart';

void main() {
  testWidgets('MyApp smoke test', (WidgetTester tester) async {
    await tester.pumpWidget(const Myapp());
    // Add tests here!
    void test() {}

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
                PhotoPicker(context, test, "Adicione uma foto"),
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
  });
}
