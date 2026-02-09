class BMI:

    def __init__(self):
        self.weight = 0.0
        self.height = 0.0

    def set_weight(self, w):
        self.weight = w
        return self.weight

    def set_height(self, h):
        self.height = h
        return self.height

    def cal_BMI(self):

        weight_value = self.weight
        height_value = self.height

        height_square = height_value * height_value

        bmi = weight_value / height_square

        return bmi

    def display_BMI(self):
        bmi = self.cal_BMI()

        bmi_rounded = round(bmi, 2)

        print("BMI is", bmi_rounded)

bmi_object = BMI()
bmi_object.set_weight(100)
bmi_object.set_height(5.9)
bmi_object.display_BMI()
