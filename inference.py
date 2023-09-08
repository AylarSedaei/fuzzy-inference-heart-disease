from defuzzification import Output
from fuzzification import *

class Rules:
    def __init__(self):
        self.output = Output()
        
    def infer(self, CP, BP, Ch, BS, ECG, HR, E, OP, Th, Sex, Age):
        "RULE 1: IF (age IS very_old) AND (chest_pain IS atypical_anginal) THEN health IS sick_4;"
        belonging = min(Age[AGE_VERY_OLD], CP[ATYPICAL_ANGINA])
        self.output.update_membership(belonging, SICK4)
        
        "RULE 2: IF (maximum_heart_rate IS high) AND (age IS old) THEN health IS sick_4;"
        belonging = min(HR[HR_HIGH], Age[AGE_OLD])
        self.output.update_membership(belonging, SICK4)
        
        "RULE 3: IF (sex IS male) AND (maximum_heart_rate IS medium) THEN health IS sick_3;"
        belonging = min(Sex[MALE], HR[HR_MEDIUM])
        self.output.update_membership(belonging, SICK3)
        
        "RULE 4: IF (sex IS female) AND (maximum_heart_rate IS medium) THEN health IS sick_2;"
        belonging = min(Sex[FEMALE], HR[HR_MEDIUM])
        self.output.update_membership(belonging, SICK2)
        
        "RULE 5: IF (chest_pain IS non_aginal_pain) AND (blood_pressure IS high) THEN health IS sick_3;"
        belonging = min(CP[NON_ANGINAL], BP[BP_HIGH])
        self.output.update_membership(belonging, SICK3)
        
        "RULE 6: IF (chest_pain IS typical_anginal) AND (maximum_heart_rate IS medium) THEN health IS sick_2;"
        belonging = min(CP[TYPICAL_ANGINA], HR[HR_MEDIUM])
        self.output.update_membership(belonging, SICK2)
        
        "RULE 7: IF (blood_sugar IS true) AND (age IS mild) THEN health IS sick_3;"
        belonging = min(BS[BS_VERY_HIGH], Age[AGE_MILD])
        self.output.update_membership(belonging, SICK3)
        
        "RULE 8: IF (blood_sugar IS false) AND (blood_pressure IS very_high) THEN health IS sick_2;"
        belonging = min(1-BS[BS_VERY_HIGH], BP[BP_VERY_HIGH])
        self.output.update_membership(belonging, SICK2)
        
        "RULE 9: IF (chest_pain IS asymptomatic) OR (age IS very_old) THEN health IS sick_1;"
        belonging = max(CP[ASYMPTOMATIC], Age[AGE_VERY_OLD])
        self.output.update_membership(belonging, SICK1)
        
        "RULE 10: IF (blood_pressure IS high) OR (maximum_heart_rate IS low) THEN health IS sick_1;"
        belonging = max(BP[BP_HIGH], HR[HR_LOW])
        self.output.update_membership(belonging, SICK1)
        
        "RULE 11: IF (chest_pain IS typical_anginal) THEN health IS healthy;"
        belonging = CP[TYPICAL_ANGINA]
        self.output.update_membership(belonging, HEALTHY)
        
        "RULE 12: IF (chest_pain IS atypical_anginal) THEN health IS sick_1;"
        belonging = CP[ATYPICAL_ANGINA]
        self.output.update_membership(belonging, SICK1)
        
        "RULE 13: IF (chest_pain IS non_aginal_pain) THEN health IS sick_2;"
        belonging = CP[NON_ANGINAL]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 14: IF (chest_pain IS asymptomatic) THEN health IS sick_3;"
        belonging = CP[ASYMPTOMATIC]
        self.output.update_membership(belonging, SICK3)
        
        "RULE 15: IF (chest_pain IS asymptomatic) THEN health IS sick_4;"
        belonging = CP[ASYMPTOMATIC]
        self.output.update_membership(belonging, SICK4)
        
        "RULE 16: IF (sex IS female) THEN health IS sick_1;"
        belonging = Sex[FEMALE]
        self.output.update_membership(belonging, SICK1)
        
        "RULE 17: IF (sex IS male) THEN health IS sick_2;"
        belonging = Sex[MALE]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 18: IF (blood_pressure IS low) THEN health IS healthy;"
        belonging = BP[BP_LOW]
        self.output.update_membership(belonging, HEALTHY)
        
        "RULE 19: IF (blood_pressure IS medium) THEN health IS sick_1;"
        belonging = BP[BP_MEDIUM]
        self.output.update_membership(belonging, SICK1)
        
        "RULE 20: IF (blood_pressure IS high) THEN health IS sick_2;"
        belonging = BP[BP_HIGH]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 21: IF (blood_pressure IS high) THEN health IS sick_3;"
        belonging = BP[BP_HIGH]
        self.output.update_membership(belonging, SICK3)
        
        "RULE 22: IF (blood_pressure IS very_high) THEN health IS sick_4;"
        belonging = BP[BP_VERY_HIGH]
        self.output.update_membership(belonging, SICK4)
        
        "RULE 23: IF (cholesterol IS low) THEN health IS	healthy;"
        belonging = Ch[CH_LOW]
        self.output.update_membership(belonging, HEALTHY)
        
        "RULE 24: IF (cholesterol IS medium) THEN health IS sick_1;"
        belonging = Ch[CH_MEDIUM]
        self.output.update_membership(belonging, SICK1)
        
        "RULE 25: IF (cholesterol IS high) THEN health IS sick_2;"
        belonging = Ch[CH_HIGH]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 26: IF (cholesterol IS high) THEN health IS sick_3;"
        belonging = Ch[CH_HIGH]
        self.output.update_membership(belonging, SICK3)
        
        "RULE 27: IF (cholesterol IS very_high) THEN health IS sick_4;"
        belonging = Ch[CH_VERY_HIGH]
        self.output.update_membership(belonging, SICK4)
        
        "RULE 28: IF (blood_sugar IS true) THEN health IS sick_2;"
        belonging = BS[BS_VERY_HIGH]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 29: IF (ECG IS normal) THEN health IS healthy;"
        belonging = ECG[ECG_NORMAL]
        self.output.update_membership(belonging, HEALTHY)
        
        "RULE 30: IF (ECG IS normal) THEN health IS sick_1;"
        belonging = ECG[ECG_NORMAL]
        self.output.update_membership(belonging, SICK1)
        
        "RULE 31: IF (ECG IS abnormal) THEN health IS sick_2;"
        belonging = ECG[ECG_ABNORMAL]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 32: IF (ECG IS hypertrophy) THEN health IS sick_3;"
        belonging = ECG[ECG_HYPERTROPHY]
        self.output.update_membership(belonging, SICK3)
        
        "RULE 33: IF (ECG IS hypertrophy) THEN health IS sick_4;"
        belonging = ECG[ECG_HYPERTROPHY]
        self.output.update_membership(belonging, SICK4)
        
        "RULE 34: IF (maximum_heart_rate IS low) THEN health IS healthy;"
        belonging = HR[HR_LOW]
        self.output.update_membership(belonging, HEALTHY)
        
        "RULE 35: IF (maximum_heart_rate IS medium) THEN health IS sick_1;"
        belonging = HR[HR_MEDIUM]
        self.output.update_membership(belonging, SICK1)
        
        "RULE 36: IF (maximum_heart_rate IS medium) THEN health IS sick_2;"
        belonging = HR[HR_MEDIUM]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 37: IF(maximum_heart_rate IS high) THEN health IS sick_3;"
        belonging = HR[HR_HIGH]
        self.output.update_membership(belonging, SICK3)
        
        "RULE 38: IF(maximum_heart_rate IS high) THEN health IS sick_4;"
        belonging = HR[HR_HIGH]
        self.output.update_membership(belonging, SICK4)
        
        "RULE 39: IF (exercise IS true) THEN health IS sick_2;"
        belonging = E[OK]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 40: IF (old_peak IS low) THEN health IS healthy;"
        belonging = OP[OP_LOW]
        self.output.update_membership(belonging, HEALTHY)
        
        "RULE 41: IF (old_peak IS low) THEN health IS sick_1;"
        belonging = OP[OP_LOW]
        self.output.update_membership(belonging, SICK1)
        
        "RULE 42: IF (old_peak IS terrible) THEN health IS sick_2;"
        belonging = OP[OP_TERRIBLE]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 43: IF (old_peak IS terrible) THEN health IS sick_3;"
        belonging = OP[OP_TERRIBLE]
        self.output.update_membership(belonging, SICK3)
        
        "RULE 44: IF (old_peak IS risk) THEN health IS sick_4;"
        belonging = OP[OP_RISK]
        self.output.update_membership(belonging, SICK4)
        
        "RULE 45: IF (thallium IS normal) THEN health IS healthy;"
        belonging = Th[TH_NORMAL]
        self.output.update_membership(belonging, HEALTHY)
        
        "RULE 46: IF (thallium IS normal) THEN health IS sick_1;"
        belonging = Th[TH_NORMAL]
        self.output.update_membership(belonging, SICK1)
        
        "RULE 47: IF (thallium IS medium) THEN health IS sick_2;"
        belonging = Th[TH_AVERAGE]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 48: IF (thallium IS high) THEN health IS sick_3;"
        belonging = Th[TH_HIGH]
        self.output.update_membership(belonging, SICK3)
        
        "RULE 49: IF (thallium IS high) THEN health IS sick_4;"
        belonging = Th[TH_HIGH]
        self.output.update_membership(belonging, SICK4)
        
        "RULE 50: IF (age IS young) THEN health IS healthy;"
        belonging = Age[AGE_YOUNG]
        self.output.update_membership(belonging, HEALTHY)
        
        "RULE 51: IF (age IS mild) THEN health IS sick_1;"
        belonging = Age[AGE_MILD]
        self.output.update_membership(belonging, SICK1)
        
        "RULE 52: IF (age IS old) THEN health IS sick_2;"
        belonging = Age[AGE_OLD]
        self.output.update_membership(belonging, SICK2)
        
        "RULE 53: IF (age IS old) THEN health IS sick_3;"
        belonging = Age[AGE_OLD]
        self.output.update_membership(belonging, SICK3)
        
        "RULE 54: IF (age IS very_old) THEN health IS sick_4;"
        belonging = Age[AGE_VERY_OLD]
        self.output.update_membership(belonging, SICK4)
        