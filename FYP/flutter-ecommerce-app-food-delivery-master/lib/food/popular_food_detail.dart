import 'package:flutter/material.dart';
import 'package:food_delivery/utils/dimentions.dart';
import 'package:food_delivery/widgets/app_column.dart';
import 'package:food_delivery/widgets/app_icon.dart';
import 'package:food_odering_app/utils/dimentions.dart';
import 'package:food_odering_app/widgets/app_column.dart';
import 'package:food_odering_app/widgets/app_icon.dart';
import 'package:food_odering_app/widgets/big_text.dart';
import 'package:food_odering_app/widgets/exandable_text_widget.dart';

import '../widgets/big_text.dart';
import '../widgets/exandable_text_widget.dart';

class PopularFoodDetail extends StatelessWidget {
  const PopularFoodDetail({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [

          /// Background Image
          Positioned(
            left: 0,
            right: 0,
            child: Container(
              width: double.maxFinite,
              height: Dimension.popularFoodImgSize,
              decoration: const BoxDecoration(
                image: DecorationImage(
                  fit: BoxFit.cover,
                  image: AssetImage("assets/images/food0.png"),
                ),
              ),
            ),
          ),

          /// Top Icons
          Positioned(
            top: Dimension.height45,
            left: Dimension.width20,
            right: Dimension.width20,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: const [
                AppIcon(icon: Icons.arrow_back_ios),
                AppIcon(icon: Icons.shopping_cart_outlined),
              ],
            ),
          ),

          /// Food Introduction Container
          Positioned(
            left: 0,
            right: 0,
            bottom: 0,
            top: Dimension.popularFoodImgSize - 20,
            child: Container(
              padding: EdgeInsets.only(
                left: Dimension.width20,
                right: Dimension.width20,
                top: Dimension.height20,
              ),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.only(
                  topRight: Radius.circular(Dimension.radius20),
                  topLeft: Radius.circular(Dimension.radius20),
                ),
                color: Colors.white,
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const AppColumn(text: "Chinese Side"),
                  SizedBox(height: Dimension.height20),
                  const BigText(text: "Introduce"),
                  SizedBox(height: Dimension.height20),
                  const Expanded(
                    child: SingleChildScrollView(
                      child: ExpandableTextWidget(
                        text:
                        "Chicken marinated. Its taste is very juicy and feels fresh. You can enjoy your meal.",
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}