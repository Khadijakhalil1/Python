// icon_and_text_widget.dart

import 'package:flutter/material.dart';
import 'package:food_odering_app/widgets/small%20text.dart';
import '../utils/dimentions.dart';
import 'dimension.dart';
import 'small_text.dart';

class IconAndTextWidget extends StatelessWidget {
  final IconData icon;
  final String text;
  final Color iconColor;

  const IconAndTextWidget({
    Key? key,
    required this.icon,
    required this.text,
    required this.iconColor,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Icon(
          icon,
          color: iconColor,
          size: Dimension.iconSize24,
        ),
        const SizedBox(width: 5),
        SmallText(text: text),
      ],
    );
  }
}