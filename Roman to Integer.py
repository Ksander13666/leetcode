        s="ROMAN"
        rule_add = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        rule_div = {
            ('I', 'V'): 3,
            ('I', 'X'): 8,
            ('X', 'L'): 30,
            ('X', 'C'): 80,
            ('C', 'D'): 300,
            ('C', 'M'): 800,
        }

        n=0
        p=None
        for i in s:
            if p and rule_add[p] < rule_add[i]:
                n+=rule_div[(p,i)]
            else:
                n+=rule_add[i]
            p=i
        print n
