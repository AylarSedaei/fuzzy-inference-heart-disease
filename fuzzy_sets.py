from numpy import negative
from constants import *

class Triangle:
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Line:
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2

        def calculate_y(self, x):
            if self.p1.x == self.p2.x:
                return 1.

            m = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
            b = self.p1.y - (m * self.p1.x)

            return m * x + b

    def __init__(self, x1, x2, x3):
        self.p1 = self.Point(x1 * 1., 0.)
        self.p2 = self.Point(x2 * 1., 1.)
        self.p3 = self.Point(x3 * 1., 0.)

        self.l1 = self.Line(self.p1, self.p2)
        self.l2 = self.Line(self.p2, self.p3)
        
        
    def compute_membership(self, x):
        if not self.p1.x <= x <= self.p3.x:
            return 0.
        if self.p1.x <= x <= self.p2.x:
            return self.l1.calculate_y(x)
        if self.p2.x <= x <= self.p3.x:
            return self.l2.calculate_y(x)

class Slide:
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Line:
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2

        def calculate_y(self, x):
            if self.p1.x == self.p2.x:
                return 1.
            m = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
            b = self.p1.y - (m * self.p1.x)
            return m * x + b

    def __init__(self, x1, x2, slope):
        self.slope = slope  # slope == true: /     slope == false: \
        if slope:
            self.p1 = self.Point(x1*1., 0.)
            self.p2 = self.Point(x2*1., 1.)
        else:
            self.p1 = self.Point(x1*1., 1.)
            self.p2 = self.Point(x2*1., 0.)
        self.l = self.Line(self.p1, self.p2)
        
    def compute_membership(self, x):
        if self.slope:
            if x < self.p1.x:
                return 0.
            elif self.p1.x <= x <= self.p2.x:
                return self.l.calculate_y(x)
            elif self.p2.x < x:
                return 1.
        else:
            if x < self.p1.x:
                return 1.
            elif self.p1.x <= x <= self.p2.x:
                return self.l.calculate_y(x)
            elif self.p2.x < x:
                return 0.



chest_pain_fuzzify = {
    TYPICAL_ANGINA: 1,
    ATYPICAL_ANGINA: 2,
    NON_ANGINAL: 3,
    ASYMPTOMATIC: 4
}

blood_pressure_fuzzify = {
    BP_LOW: Slide(111, 134, False),
    BP_MEDIUM: Triangle(127, 139, 153),
    BP_HIGH: Triangle(153, 157, 172),
    BP_VERY_HIGH: Slide(154, 171, True)
}

cholestrol_fuzzify = {
    CH_LOW: Slide(151, 197, False),
    CH_MEDIUM: Triangle(188, 215, 250),
    CH_HIGH: Triangle(217, 263, 307),
    CH_VERY_HIGH: Slide(281, 347, True)
}

blood_sugar_fuzzify = {
    BS_VERY_HIGH: Slide(119.9999, 120, True)
}

ECG_fuzzify = {
    ECG_NORMAL: Slide(0, .4, False),
    ECG_ABNORMAL: Triangle(0.2, 1, 1.8),
    ECG_HYPERTROPHY: Slide(1.4, 1.9, True)
}

heart_rate_fuzzify = {
    HR_LOW: Slide(100, 141, False),
    HR_MEDIUM: Triangle(111, 152, 194),
    HR_HIGH: Slide(152, 210, True)
}

exercise_fuzzify = {
    PROHIBITED: 0,
    OK: 1
}

old_peak_fuzzify = {
    OP_LOW: Slide(1, 2, False),
    OP_RISK: Triangle(1.5, 2.8, 4.2),
    OP_TERRIBLE: Slide(2.5, 4, True)
}


thallium_fuzzify = {
    TH_NORMAL: 3,
    TH_AVERAGE: 6,
    TH_HIGH: 7
}

sex_fuzzify = {
    MALE: 0,
    FEMALE: 1
}

age_fuzzify = {
    AGE_YOUNG: Slide(29, 38, False),
    AGE_MILD: Triangle(33, 38, 45),
    AGE_OLD: Triangle(40, 48, 58),
    AGE_VERY_OLD: Slide(52, 60, True)
}

output = {
    SICK1: Slide(0.25, 1, False),
    SICK2: Triangle(0, 1, 2),
    SICK3: Triangle(1, 2, 3),
    SICK4: Triangle(2, 3, 4),
    HEALTHY: Slide(3, 3.75, True)
}
