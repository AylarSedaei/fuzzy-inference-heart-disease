from defuzzification import Output
from fuzzification import *
from inference import Rules

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance


    def calculate_result(self, input):
        CP = chest_pain(input['CP']).fuzzify()
        BP = blood_pressure(input['BP']).fuzzify()
        Ch = cholestrol(input['Ch']).fuzzify()
        BS = blood_sugar(input['BS']).fuzzify()
        ECG = ECG(input['ECG']).fuzzify()
        HR = heart_rate(input['HR']).fuzzify()
        E = exercise(input['E']).fuzzify()
        OP = old_peak(input['OP']).fuzzify()
        Th = thallium_scan(input['Th']).fuzzify()
        Sex = gender(input['Sex']).fuzzify()
        Age = age(input['age']).fuzzify()
    
        output = Rules().infer(CP, BP, Ch, BS, ECG, HR, E, OP, Th, Sex, Age)
        defuzzed_output = output.defuzzify()
        return defuzzed_output
    
    @staticmethod
    def get_final_result(input_dict: dict, self) -> str:
        defuzzed_output = self.calculate_result(input_dict)
        outputString = ''
        if defuzzed_output < 1.78:
            outputString += 'healthy'
        if 1 <= defuzzed_output <= 2.51:
            if outputString != '':
                outputString += '& '
            outputString += 'Sick1 '
        if 1.78 <= defuzzed_output <= 3.25:
            if outputString != '':
                outputString += '& '
            outputString += 'Sick2 '
        if 1.5 <= defuzzed_output <= 4.5:
            if outputString != '':
                outputString += '& '
            outputString += 'Sick3 '
        if defuzzed_output > 3.25:
            if outputString != '':
                outputString += '& '
            outputString += 'Sick4 '
        outputString += ': ' + str(defuzzed_output)
        return outputString