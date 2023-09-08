# chest pain
TYPICAL_ANGINA, \
ATYPICAL_ANGINA, \
NON_ANGINAL, \
ASYMPTOMATIC \
    = [i for i in range(1, 4)]

# blood pressure
BP_LOW, \
BP_MEDIUM, \
BP_HIGH, \
BP_VERY_HIGH \
    = [i for i in range(5, 8)]

# cholestrol
CH_LOW, \
CH_MEDIUM, \
CH_HIGH, \
CH_VERY_HIGH \
    = [i for i in range(9, 12)]

# blood sugar
BS_VERY_HIGH  = 13

# ECG
ECG_NORMAL, \
ECG_ABNORMAL, \
ECG_HYPERTROPHY \
    = [i for i in range(14, 16)]
    
# heart rate
HR_LOW, \
HR_MEDIUM, \
HR_HIGH \
    = [i for i in range(17, 19)]
    
# exercise
PROHIBITED = 20
OK = 21

# depression (old peak)
OP_LOW, \
OP_RISK, \
OP_TERRIBLE \
    = [i for i in range(22, 24)]

# thallium
TH_NORMAL, \
TH_AVERAGE, \
TH_HIGH \
    = [i for i in range(25, 27)]

# sex
MALE = 28
FEMALE = 29

# age
AGE_YOUNG, \
AGE_MILD, \
AGE_OLD, \
AGE_VERY_OLD, \
    = [i for i in range(30, 31)]

# diagnosis
SICK1, \
SICK2, \
SICK3, \
SICK4, \
HEALTHY \
    = [i for i in range(32, 36)]