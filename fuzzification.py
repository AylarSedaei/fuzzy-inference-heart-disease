from unittest import case
from constants import *
import fuzzy_sets

class chest_pain:
    def __init__(self, x):
        self.membership = {
            TYPICAL_ANGINA: 0,
            ATYPICAL_ANGINA: 0,
            NON_ANGINAL: 0,
            ASYMPTOMATIC: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets.chest_pain_fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = 1. if (self.membershipFunction[fuzzy_set] == self.x) else 0.
        return self.membership

        
class blood_pressure:
    def __init__(self, x):
        self.membership = {
            BP_LOW: 0,
            BP_MEDIUM: 0,
            BP_HIGH: 0,
            BP_VERY_HIGH: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets.blood_pressure_fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = self.membershipFunction[fuzzy_set].compute_membership(self.x)
        return self.membership


class cholestrol:
    def __init__(self, x):
        self.membership = {
            CH_LOW: 0,
            CH_MEDIUM: 0,
            CH_HIGH: 0,
            CH_VERY_HIGH: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets.cholestrol_fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = self.membershipFunction[fuzzy_set].compute_membership(self.x)
        return self.membership
    
        
class blood_sugar:
    def __init__(self, x):
        self.membership = {
            BS_VERY_HIGH: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets.blood_sugar_fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = self.membershipFunction[fuzzy_set].compute_membership(self.x)
        return self.membership

class ECG:
    def __init__(self, x):
        self.membership = {
            ECG_NORMAL: 0,
            ECG_ABNORMAL: 0, 
            ECG_HYPERTROPHY: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets.ECG_fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = self.membershipFunction[fuzzy_set].compute_membership(self.x)
        return self.membership


class heart_rate:
    def __init__(self, x):
        self.membership = {
            HR_LOW: 0,
            HR_MEDIUM: 0,
            HR_HIGH: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets.heart_rate_fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = self.membershipFunction[fuzzy_set].compute_membership(self.x)
        return self.membership


class exercise:
    def __init__(self, x):
        self.membership = {
            PROHIBITED: 0,
            OK: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets.exercise_fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = 1. if (self.membershipFunction[fuzzy_set] == self.x) else 0.
        return self.membership


class old_peak:
    def __init__(self, x):
        self.membership = {
            OP_LOW: 0,
            OP_RISK: 0,
            OP_TERRIBLE: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets._fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = self.membershipFunction[fuzzy_set].compute_membership(self.x)
        return self.membership


class thallium_scan:
    def __init__(self, x):
        self.membership = {
            TH_NORMAL: 0,
            TH_AVERAGE: 0,
            TH_HIGH: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets.thallium_fuzzify

    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = 1. if (self.membershipFunction[fuzzy_set] == self.x) else 0.
        return self.membership


class gender:
    def __init__(self, x):
        self.membership = {
            MALE: 0,
            FEMALE: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets.sex_fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = 1. if (self.membershipFunction[fuzzy_set] == self.x) else 0.
        return self.membership


class age:
    def __init__(self, x):
        self.membership = {
            AGE_YOUNG: 0,
            AGE_MILD: 0,
            AGE_OLD: 0,
            AGE_VERY_OLD: 0
        }
        self.x = x
        self.membershipFunction = fuzzy_sets._fuzzify
    
    def fuzzify(self):
        for fuzzy_set in self.membership:
            self.membership[fuzzy_set] = self.membershipFunction[fuzzy_set].compute_membership(self.x)
        return self.membership
