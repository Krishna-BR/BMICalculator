"""Main Module"""
import pandas as pd

class BMI:
    """ BMI Class Model
    """
    def __init__(self, df: pd.DataFrame):
        """ Constructor
            Args:
                data: List of Json Data
        """
        self.df = df
        self.bmi_calculator()

    @staticmethod
    def bmi_chart(bmi : float) -> pd.Series:
        """ Determines health risk and BMI category for a given BMI value

            Args:
                bmi: floating point value.
            Returns:
                Series with information about BMI Catgeory and Health Risk which gets broadcasted
                to a DataFrame
        """
        category, health_risk = None, None
        if bmi < 18.5:
            health_risk = "Malnutrition Risk"
            category = "Underweight"
        elif ( bmi >= 18.5 and bmi < 25):
            health_risk = "Low Risk"
            category = "Normal weight"
        elif ( bmi >= 25 and bmi < 30):
            health_risk = "Enhanced Risk"
            category = "Overweight"
        elif ( bmi >=30 and bmi < 35):
            health_risk = "Medium Risk"
            category = "Moderately obese"
        elif ( bmi >=35 and bmi < 40):
            health_risk = "High Risk"
            category = "Severely obese"
        else:
            health_risk = "Very High Risk"
            category = "Very severly obese"
        return pd.Series((category, health_risk))

    def bmi_calculator(self) -> pd.DataFrame:
        """ Calculates BMI in units of kg/(m**2). Also determines health risk and BMI category

            Args:
                self: Instance Variable.
            Returns:
                A DataFrame with 3 additional columns BMI(kg/m2), BMI Catgory and Health Risk
        """
        #initialisig
        self.df['BMI(kg/m2)'], self.df['BMI Category'], self.df['Health Risk']= None, None, None
        # calculating BMI
        self.df['BMI(kg/m2)'] = self.df.apply(lambda x : round(x['WeightKg']/(x['HeightCm']/100),2),
                                             axis=1)
        # determining category and health risk
        self.df[['BMI Category','Health Risk']] = self.df['BMI(kg/m2)'].apply(self.bmi_chart)

        return self.df

    def get_overweight_count(self) -> int:
        """ Gets the count of Overweight people

            Args:
                self: Instance Variable.
            Returns:
                Int : No of overweight people
        """
        return self.df[self.df['BMI Category'] == 'Overweight'].shape[0]

    def get_bmi_report(self):
        """ Gets the BMI report

            Args:
                self: Instance Variable.
            Returns:
                DataFrame
        """
        return self.df


# if __name__== '__main__':
#     data = [
#                 {"Gender":"Male","HeightCm":171,"WeightKg":96},
#                 {"Gender":"Male","HeightCm":161,"WeightKg":85},
#                 {"Gender":"Male","HeightCm":180,"WeightKg":77},
#                 {"Gender":"Female","HeightCm":166,"WeightKg":62},
#                 {"Gender":"Female","HeightCm":150,"WeightKg":70},
#                 {"Gender":"Female","HeightCm":167,"WeightKg":82},
#             ]

#     df_ = pd.DataFrame(data)
#     bmi_ = BMI(df_)
#     print(bmi_.get_overweight_count())
#     print(bmi_.get_bmi_report().columns)
#     print(list(BMI.bmi_chart(10.29)))