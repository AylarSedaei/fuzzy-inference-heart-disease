from constants import *
import fuzzy_sets

class Output:
    def __init__(self):
        self.membership = {
            SICK1: 0,
            SICK2: 0,
            SICK3: 0,
            SICK4:  0,
            HEALTHY: 0
        }
        self.membershipFunction = fuzzy_sets.output

    def update_membership(self, new_belonging, fuzzy_set):
        old_belonging = self.membership[fuzzy_set]
        self.membership[fuzzy_set] = max(old_belonging, new_belonging)

    def res_func(self, x):
        y = 0
        for fuzzy_set in self.membership:
            belonging = self.membershipFunction[fuzzy_set].compute_membership(x)
            cut = self.membership[fuzzy_set]
            y = max(y, min(belonging, cut))
        return y

    def defuzzify(self):
        """ Center of Mass """
        n = 10000
        delta = 200. / n
        points = [-100. + i * delta for i in range(n + 1)]

        s1, s2 = 0., 0.
        for x in points:
            s1 += self.res_func(x) * x * delta
            s2 += self.res_func(x) * delta

        try:
            z = s1 / s2
        except ZeroDivisionError:
            z = 0

        return z
