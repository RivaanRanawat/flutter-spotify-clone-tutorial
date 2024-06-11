import 'dart:io';

class ServerConstant {
  static String serverURL =
      Platform.isAndroid ? 'http://10.0.2.2:8000' : 'http://127.0.0.1:8000';
}
