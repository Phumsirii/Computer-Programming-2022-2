def get_sid_section(stu_rec):
  a=stu_rec.split(',')
  return [a[0],str(int(a[1]))]

def get_sid_sections(stu_recs):
    b=[]
    for c in stu_recs:
        b.append(get_sid_section(c))
    b.sort()
    return b

def get_section(sid_sections,sid):
    for d in sid_sections:
        if d[0]==sid:
            return d[1]
    return '0'

def get_stu_points(grader_points):
    a=[]
    for b in grader_points:
        a.append(b.split(','))
    name=[]
    score=[]
    for i in a:
        if i[0] in name:
            score[name.index(i[0])].append(int(i[2]))
        else:
            name.append(i[0])
            score.append([int(i[2])])
    z=[]
    for i in range(len(name)):
        z.append([name[i],max(score[i])])
    z.sort()
    return z

def get_stu_section_points(stu_points, sid_sections):
    a=[]
    for i in stu_points:
        a.append([get_section(sid_sections,i[0]),i[1],i[0]])
    return a
        
def get_section_point_count(stu_section_points, min_point):
    sec=[]
    n=[]
    for i in stu_section_points:
        if not i[0] in sec:
            sec.append(i[0])
            n.append(0)
    for i in stu_section_points:
        if i[1]>=min_point:
            n[sec.index(i[0])]+=1
    a=[]
    for i in range(len(n)):
        a.append([sec[i],n[i]])
    a.sort()
    return a
            

import copy
def test_f(case_name, f_name, expected_result, f_kwargs, allowed_unsorted_result=False):
    def show_warning(case_name, str1, str2, expected, actual):
        print("WARNING!! Something went wrong at", case_name)
        warning_txt = " ".join([str(e) for e in [str1, str2, expected, actual]])
        if len(warning_txt) < 100:
            print(warning_txt)
        else:
            print(str1)
            print(str2)
            print(expected)
            print("instead of")
            print(actual)

    f = eval(f_name)
    mut_val_b4_test = {}
    for key, val in f_kwargs.items():
        if type(val) is list:
            mut_val_b4_test[key] = copy.deepcopy(val)
    call_txt = f_name + "(" + str(list(f_kwargs.values()))[1:-1] + ")"
    result = f(**f_kwargs)
    if allowed_unsorted_result:
        if type(result) is list:
            result.sort()
            expected_result.sort()
    for key in mut_val_b4_test:
        if mut_val_b4_test[key] != f_kwargs[key]:
            show_warning(case_name,
                         "After calling " + call_txt + ",",
                         "argument " + key + " must have its value as before:",
                         mut_val_b4_test[key],
                         f_kwargs[key])
            return 1
    if type(expected_result) is not type(result):
        show_warning(case_name, call_txt, "should return variable type", type(expected_result), type(result))
        return 1
    if result != expected_result:
        show_warning(case_name, call_txt, "should return", expected_result, result)
        return 1
    return 0

def run_test(f_name, test_cases):
    print("------------------------------------------------------------")
    err_code = 0
    for idx, test_kwargs in enumerate(test_cases):
        case_name = "test " + f_name + " #" + str(idx+1)
        err_code |= test_f(case_name, f_name, **test_kwargs)
    if not err_code:
        print("Your function " + f_name + " is working well so far")

def test_get_sid_section():
    test_cases = []
    test_cases.append({"f_kwargs": {"stu_rec": "MrBond,007,BND"},
                       "expected_result": ["MrBond", "7"]})
    test_cases.append({"f_kwargs": {"stu_rec": "stu_CompProg,101,CPG"},
                       "expected_result": ["stu_CompProg", "101"]})
    test_cases.append({"f_kwargs": {"stu_rec": "A,1,A"},
                       "expected_result": ["A", "1"]})
    test_cases.append({"f_kwargs": {"stu_rec": "VeryVeryVeryVeryVeryLong,255,VeryVeryVeryVeryVeryLong"},
                       "expected_result": ["VeryVeryVeryVeryVeryLong", "255"]})
    test_cases.append({"f_kwargs": {"stu_rec": "6530000121,005,JTP"},
                       "expected_result": ["6530000121", "5"]})
    test_cases.append({"f_kwargs": {"stu_rec": "6430099921,011,SPJ"},
                       "expected_result": ["6430099921", "11"]})
    run_test("get_sid_section", test_cases)

def test_get_sid_sections():
    test_cases = []
    test_cases.append({"f_kwargs": {"stu_recs": ["stu_CompProg,101,CPG", 
                                                 "MrBond,007,BND"]},
                       "expected_result": [["MrBond", "7"],
                                           ["stu_CompProg", "101"]]})
    test_cases.append({"f_kwargs": {"stu_recs": ["6530000121,005,JTP", 
                                                 "6430099921,011,SPJ"]},
                       "expected_result": [["6430099921", "11"],
                                           ["6530000121", "5"]]})
    test_cases.append({"f_kwargs": {"stu_recs": ["6530000121,005,JTP",
                                                 "6430099921,011,SPJ",
                                                 "MrBond,007,BND",
                                                 "stu_CompProg,101,CPG",
                                                 "VeryVeryVeryVeryVeryLong,255,VeryVeryVeryVeryVeryLong",
                                                 "A,1,A"]},
                       "expected_result": [['6430099921', '11'],
                                           ['6530000121', '5'],
                                           ['A', '1'],
                                           ['MrBond', '7'],
                                           ['VeryVeryVeryVeryVeryLong', '255'],
                                           ['stu_CompProg', '101']]})
    test_cases.append({"f_kwargs": {"stu_recs": []},
                       "expected_result": []})
    run_test("get_sid_sections", test_cases)

def test_get_section():
    test_cases = []
    test_cases.append({"f_kwargs": {"sid_sections": [["MrBond", "7"], ["stu_CompProg", "101"]], "sid": "MrBond"},
                       "expected_result": "7"})
    test_cases.append({"f_kwargs": {"sid_sections": [["MrBond", "7"], ["stu_CompProg", "101"]], "sid": "Luffy"},
                       "expected_result": "0"})
    test_cases.append({"f_kwargs": {"sid_sections": [["MrBond", "7"], ["stu_CompProg", "101"]], "sid": "mrBond"},
                       "expected_result": "0"})
    test_cases.append({"f_kwargs": {"sid_sections": [["MrBond", "7"], ["stu_CompProg", "101"]], "sid": "6530000121"},
                       "expected_result": "0"})
    test_cases.append({"f_kwargs": {"sid_sections": [['6530000121', '5'],
                                                     ["MrBond", "7"],
                                                     ["stu_CompProg", "101"]],
                                    "sid": "6530000121"},
                       "expected_result": "5"})
    run_test("get_section", test_cases)

def test_get_stu_points():
    test_cases = []
    test_cases.append({"f_kwargs": {"grader_points": ["MrBond,9:55:10,80", 
                                                      "stu_CompProg,9:40:18,60", 
                                                      "MrBond,9:59:19,100", 
                                                      "MrBond,10:02:43,0", 
                                                      "Luffy,10:09:59,0", 
                                                      "Lalisa,9:50:09,100", 
                                                      "Zoro,10:05:55,0"]},
                       "expected_result": [["Lalisa", 100], 
                                           ["Luffy", 0], 
                                           ["MrBond", 100],
                                           ["Zoro", 0], 
                                           ["stu_CompProg", 60]]})
    test_cases.append({"f_kwargs": {"grader_points": ["MrBond,9:55:10,80",
                                                      "6430099921,2 minutes ago,0",
                                                      "stu_CompProg,9:40:18,60", 
                                                      "MrBond,9:59:19,100", 
                                                      "6530000121,2 days ago,90", 
                                                      "MrBond,10:02:43,0", 
                                                      "Luffy,10:09:59,0", 
                                                      "6530000121,Yesterday,95", 
                                                      "Luffy,10:09:59,0", 
                                                      "Lalisa,9:50:09,100",
                                                      "6530000121,10:05:55,0", 
                                                      "VeryVeryVeryVeryVeryLong,2023-02-18 10:11:58,77", 
                                                      "Zoro,10:05:55,0"]},
                       "expected_result": [['6430099921', 0],
                                           ['6530000121', 95],
                                           ['Lalisa', 100],
                                           ['Luffy', 0],
                                           ['MrBond', 100],
                                           ['VeryVeryVeryVeryVeryLong', 77],
                                           ["Zoro", 0], 
                                           ["stu_CompProg", 60]]})
    run_test("get_stu_points", test_cases)

def test_get_stu_section_points():
    test_cases = []
    test_cases.append({"f_kwargs": {"stu_points": [["Lalisa", 100], 
                                                   ["Luffy", 0], 
                                                   ["MrBond", 100], 
                                                   ["Zoro", 0], 
                                                   ["stu_CompProg", 60]], 
                                    "sid_sections": [["Lalisa", "101"], 
                                                     ["MrBond", "7"], 
                                                     ["Zoro", "7"], 
                                                     ["stu_CompProg", "101"]]},
                       "expected_result": [["101", 100, "Lalisa"],
                                           ["7", 100, "MrBond"],
                                           ["0", 0, "Luffy"],
                                           ["7", 0, "Zoro"],
                                           ["101", 60, "stu_CompProg"]],
                       "allowed_unsorted_result": True})
    test_cases.append({"f_kwargs": {"stu_points": [['6430099921', 0],
                                                   ['6530000121', 95],
                                                   ['Lalisa', 100],
                                                   ['Luffy', 0],
                                                   ['MrBond', 100],
                                                   ['VeryVeryVeryVeryVeryLong', 77],
                                                   ["Zoro", 0], 
                                                   ["stu_CompProg", 60]], 
                                    "sid_sections": [['6430099921', '11'],
                                                     ['6530000121', '5'],
                                                     ['A', '1'],
                                                     ["Lalisa", "101"],
                                                     ['MrBond', '7'],
                                                     ['VeryVeryVeryVeryVeryLong', '255'],
                                                     ["Zoro", "7"],
                                                     ["stu_CompProg", "101"]]},
                       "expected_result": [['11', 0, '6430099921'],
                                           ['255', 77, 'VeryVeryVeryVeryVeryLong'],
                                           ['5', 95, '6530000121'],
                                           ["101", 100, "Lalisa"],
                                           ["7", 100, "MrBond"],
                                           ["0", 0, "Luffy"],
                                           ["7", 0, "Zoro"],
                                           ["101", 60, "stu_CompProg"]],
                       "allowed_unsorted_result": True})
    run_test("get_stu_section_points", test_cases)

def test_get_section_point_count():
    test_cases = []
    test_cases.append({"f_kwargs": {"stu_section_points": [["101", 100, "Lalisa"],
                                                           ["0", 0, "Luffy"],
                                                           ["7", 100, "MrBond"],
                                                           ["7", 0, "Zoro"],
                                                           ["101", 60, "stu_CompProg"]], 
                                    "min_point": 60},
                       "expected_result": [["0", 0], ["101", 2], ["7", 1]]})
    test_cases.append({"f_kwargs": {"stu_section_points": [['11', 0, '6430099921'],
                                                           ['255', 77, 'VeryVeryVeryVeryVeryLong'],
                                                           ['5', 95, '6530000121'],
                                                           ["101", 100, "Lalisa"],
                                                           ["7", 100, "MrBond"],
                                                           ["0", 0, "Luffy"],
                                                           ["7", 0, "Zoro"],
                                                           ["101", 60, "stu_CompProg"]], 
                                    "min_point": 0},
                       "expected_result": [['0', 1],
                                           ['101', 2],
                                           ['11', 1],
                                           ['255', 1],
                                           ['5', 1],
                                           ['7', 2]]})
    test_cases.append({"f_kwargs": {"stu_section_points": [['11', 0, '6430099921'],
                                                           ['255', 77, 'VeryVeryVeryVeryVeryLong'],
                                                           ['5', 95, '6530000121'],
                                                           ["101", 100, "Lalisa"],
                                                           ["7", 100, "MrBond"],
                                                           ["0", 0, "Luffy"],
                                                           ["7", 0, "Zoro"],
                                                           ["101", 60, "stu_CompProg"]], 
                                    "min_point": 100},
                       "expected_result": [['0', 0],
                                           ['101', 1],
                                           ['11', 0],
                                           ['255', 0],
                                           ['5', 0],
                                           ['7', 1]]})
    run_test("get_section_point_count", test_cases)

test_get_sid_section()
test_get_sid_sections()
test_get_section()
test_get_stu_points()
test_get_stu_section_points()
test_get_section_point_count()