import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

Widget Myapp() {
  return const SizedBox(
    height: 10,
  );
}

void main() {
  testWidgets('MyApp smoke test', (WidgetTester tester) async {
    await tester.pumpWidget(Myapp());
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
              ],
            ),
          ));
    }
  });
}
