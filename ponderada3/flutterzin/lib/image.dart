import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'dart:typed_data';

class ImageUploadScreen extends StatefulWidget {
  @override
  _ImageUploadScreenState createState() => _ImageUploadScreenState();
}

class _ImageUploadScreenState extends State<ImageUploadScreen> {
  File? _image;
  Uint8List? _receivedImageData;

  final picker = ImagePicker();

  Future getImage() async {
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);

    setState(() {
      if (pickedFile != null) {
        _image = File(pickedFile.path);
        print('Image selected: ${pickedFile.path}');
      } else {
        print('No image selected.');
      }
    });
  }

  Future uploadImage(File image) async {
    try {
      print('Uploading image: ${image.path}');
      final request = http.MultipartRequest(
        'POST',
        Uri.parse('http://10.128.0.78:5001/process'), 
      );
      request.files.add(await http.MultipartFile.fromPath('image', image.path));
      final response = await request.send();

      if (response.statusCode == 200) {
        final responseData = await response.stream.toBytes();
        setState(() {
          _receivedImageData = responseData;
        });
        print('Image uploaded successfully.');
      } else {
        print('Failed to upload image. Status code: ${response.statusCode}');
      }
    } catch (e) {
      print('Error uploading image: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Processamento de imagens'),
      ),
      body: SingleChildScrollView(
        child:Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              _image == null
                  ? const Text('No image selected.')
                  : Image.file(_image!),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: getImage,
                child: const Text('Select Image'),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: _image != null ? () => uploadImage(_image!) : null,
                child: const Text('Upload Image'),
              ),
              const SizedBox(height: 20),
              _receivedImageData == null
                  ? const Text('No image received.')
                  : Image.memory(_receivedImageData!),
            ],
          ),
        ),
      ),
    );
  }
}
