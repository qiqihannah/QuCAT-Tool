import os
import numpy as np
import subprocess
from programs import AI, AS, BV, CE, DM, SM
import rpy2.robjects as robjects
import random
from qiskit.visualization import plot_bloch_multivector

K = 100  # 100
Seed_N = 2


def dec2bin(n, bit):
    a = 1
    list = []
    while a > 0:
        a, b = divmod(n, 2)
        list.append(str(b))
        n = a
    s = ""
    for i in range(len(list) - 1, -1, -1):
        s += str(list[i])
    if bit == 10:
        s = s.zfill(10)  ####
    elif bit == 11:
        s = s.zfill(11)
    elif bit == 7:
        s = s.zfill(7)

    return s


def wrong_output(i, right_output):
    set_output = set(right_output)
    if i not in set_output:
        return True  # existing wrong output
    return False


# def Unique(input, i):
#   counts = collections.Counter(input)
#   if counts[input[i]] == 1:
#     return True
#   else:
#     return False


# generating test suites
# def gen_test_suites(n, o, mutant, program):
#     global Seed_N
#     folderGenerating = './inputs_' + str(K) + '/' + program + '/' + mutant + '_o' + str(o) + '/'
#     if not os.path.exists(folderGenerating):
#         os.makedirs(folderGenerating)
#     for i in range(K):
#         if n == 10:
#             print("pict p10.txt /o:" + str(o) + " /r:" + str(Seed_N) + "> D:\WXY\Quantum_CT\inputs_" + str(
#                 K) + "\\" + program + "\\" + mutant + "_o" + str(o) + "\input_" + program + "_" + mutant + '_' + str(
#                 i) + ".txt")
#             p = subprocess.Popen(
#                 "pict p10.txt /o:" + str(o) + " /r:" + str(Seed_N) + "> D:\WXY\Quantum_CT\inputs_" + str(
#                     K) + "\\" + program + "\\" + mutant + "_o" + str(
#                     o) + "\input_" + program + "_" + mutant + '_' + str(i) + ".txt", shell=True, stdout=subprocess.PIPE,
#                 cwd="D:\Download\PICT")
#             Seed_N += 1
#         if n == 11:
#             # p = subprocess.Popen("pict p10.txt /o:" + str(o) + " /r> E:\Code\Python_code\Quantum_CT\inputs\input_temp.txt", shell=True,
#             #                  stdout=subprocess.PIPE, cwd="D:\Download\PICT")
#             p = subprocess.Popen(
#                 "pict p11.txt /o:" + str(o) + " /r:" + str(Seed_N) + "> D:\WXY\Quantum_CT\inputs_" + str(
#                     K) + "\\" + program + "\\" + mutant + "_o" + str(
#                     o) + "\input_" + program + "_" + mutant + '_' + str(i) + ".txt", shell=True, stdout=subprocess.PIPE,
#                 cwd="D:\Download\PICT")
#             Seed_N += 1
#         if n == 7:
#             # p = subprocess.Popen("pict p10.txt /o:" + str(o) + " /r> E:\Code\Python_code\Quantum_CT\inputs\input_temp.txt", shell=True,
#             #                  stdout=subprocess.PIPE, cwd="D:\Download\PICT")
#             p = subprocess.Popen(
#                 "pict p7.txt /o:" + str(o) + " /r:" + str(Seed_N) + "> D:\WXY\Quantum_CT\inputs_" + str(
#                     K) + "\\" + program + "\\" + mutant + "_o" + str(
#                     o) + "\input_" + program + "_" + mutant + '_' + str(i) + ".txt", shell=True, stdout=subprocess.PIPE,
#                 cwd="D:\Download\PICT")
#             Seed_N += 1

def gen_test_suites(n, o, mutant, program):
    global Seed_N
    folderGenerating = './inputs_' + str(K) + '/' + program + '/' + mutant + '_o' + str(o) + '/'
    if not os.path.exists(folderGenerating):
        os.makedirs(folderGenerating)
    for i in range(K):
        if n == 10:
            print("pict p10.txt /o:" + str(o) + " /r:" + str(Seed_N) + "> D:\WXY\Quantum_CT\inputs_" + str(
                K) + "\\" + program + "\\" + mutant + "_o" + str(o) + "\input_" + program + "_" + mutant + '_' + str(
                i) + ".txt")
            p = subprocess.Popen(
                "pict p10.txt /o:" + str(o) + " /r:" + str(Seed_N) + "> D:\WXY\Quantum_CT\inputs_" + str(
                    K) + "\\" + program + "\\" + mutant + "_o" + str(
                    o) + "\input_" + program + "_" + mutant + '_' + str(i) + ".txt", shell=True, stdout=subprocess.PIPE,
                cwd="D:\Download\PICT")
            Seed_N += 1
        if n == 11:
            # p = subprocess.Popen("pict p10.txt /o:" + str(o) + " /r> E:\Code\Python_code\Quantum_CT\inputs\input_temp.txt", shell=True,
            #                  stdout=subprocess.PIPE, cwd="D:\Download\PICT")
            p = subprocess.Popen(
                "pict p11.txt /o:" + str(o) + " /r:" + str(Seed_N) + "> D:\WXY\Quantum_CT\inputs_" + str(
                    K) + "\\" + program + "\\" + mutant + "_o" + str(
                    o) + "\input_" + program + "_" + mutant + '_' + str(i) + ".txt", shell=True, stdout=subprocess.PIPE,
                cwd="D:\Download\PICT")
            Seed_N += 1
        if n == 7:
            # p = subprocess.Popen("pict p10.txt /o:" + str(o) + " /r> E:\Code\Python_code\Quantum_CT\inputs\input_temp.txt", shell=True,
            #                  stdout=subprocess.PIPE, cwd="D:\Download\PICT")
            p = subprocess.Popen(
                "pict p7.txt /o:" + str(o) + " /r:" + str(Seed_N) + "> D:\WXY\Quantum_CT\inputs_" + str(
                    K) + "\\" + program + "\\" + mutant + "_o" + str(
                    o) + "\input_" + program + "_" + mutant + '_' + str(i) + ".txt", shell=True, stdout=subprocess.PIPE,
                cwd="D:\Download\PICT")
            Seed_N += 1


# def subprocess(n,o,program):
#   mutant = "M"
#   for i in range(1,6):
#     mutant = mutant + str(i)
#     gen_test_suites(n,o,mutant,program)


def calculate_fail_number_GA(input, mutant, program):
    # count_fail = 0  # the number that fails the test
    # count_wrong = []  # number of wrong output
    # pvalue = []
    pvalue = []
    count_times = 0
    right_output = []
    p = []  # probability
    wrong = 0
    flag_wrong = False
    fre = []
    flag_fail = False


    if program == 'AI':
        bit = 11
        bit_output = 10
        pt = AI.probabilityComputing(input)
    elif program == 'AS':
        bit = 10
        pt = AS.probabilityComputing(input)
    elif program == 'BV':
        bit = 10
        pt = BV.probabilityComputing(input)
    elif program == 'CE':
        bit = 11
        pt = CE.probabilityComputing(input)
    elif program == 'DM':
        bit = 11
        pt = DM.probabilityComputing(input)
    elif program == 'SM':
        bit = 7
        pt = SM.probabilityComputing(input)

    for i in range(len(pt)):
        if pt[i] > 1e-3:
            count_times += 1
            right_output.append(i)
            p.append(pt[i])

    if program == 'AI':
        if mutant == 'M1':
            cal = AI.AI_M1(input, count_times)
        elif mutant == 'M2':
            cal = AI.AI_M2(input, count_times)
        elif mutant == 'M3':
            cal = AI.AI_M3(input, count_times)
        elif mutant == 'M4':
            cal = AI.AI_M4(input, count_times)
        elif mutant == 'M5':
            cal = AI.AI_M5(input, count_times)
        elif mutant == 'M6':
            cal = AI.AI_M6(input, count_times)
        elif mutant == 'M7':
            cal = AI.AI_M7(input, count_times)
        elif mutant == 'M8':
            cal = AI.AI_M8(input, count_times)
        elif mutant == 'M9':
            cal = AI.AI_M9(input, count_times)
        elif mutant == 'M10':
            cal = AI.AI_M10(input, count_times)
        elif mutant == 'M11':
            cal = AI.AI_M11(input, count_times)
        elif mutant == 'M12':
            cal = AI.AI_M12(input, count_times)
        elif mutant == 'M13':
            cal = AI.AI_M13(input, count_times)
        elif mutant == 'M14':
            cal = AI.AI_M14(input, count_times)
        elif mutant == 'M15':
            cal = AI.AI_M15(input, count_times)

    elif program == 'AS':
        if mutant == 'M1':
            cal = AS.AS_M1(input, count_times)
        elif mutant == 'M2':
            cal = AS.AS_M2(input, count_times)
        elif mutant == 'M3':
            cal = AS.AS_M3(input, count_times)
        elif mutant == 'M4':
            cal = AS.AS_M4(input, count_times)
        elif mutant == 'M5':
            cal = AS.AS_M5(input, count_times)

    elif program == 'BV':
        if mutant == 'M1':
            cal = BV.BV_M1(input, count_times)
        elif mutant == 'M2':
            cal = BV.BV_M2(input, count_times)
        elif mutant == 'M3':
            cal = BV.BV_M3(input, count_times)
        elif mutant == 'M4':
            cal = BV.BV_M4(input, count_times)
        elif mutant == 'M5':
            cal = BV.BV_M5(input, count_times)

    elif program == 'CE':
        if mutant == 'M1':
            cal = CE.CE_M1(input, count_times)
        elif mutant == 'M2':
            cal = CE.CE_M2(input, count_times)
        elif mutant == 'M3':
            cal = CE.CE_M3(input, count_times)
        elif mutant == 'M4':
            cal = CE.CE_M4(input, count_times)
        elif mutant == 'M5':
            cal = CE.CE_M5(input, count_times)

    elif program == 'DM':
        if mutant == 'M1':
            cal = DM.DM_M1(input, count_times)
        elif mutant == 'M2':
            cal = DM.DM_M2(input, count_times)
        elif mutant == 'M3':
            cal = DM.DM_M3(input, count_times)
        elif mutant == 'M4':
            cal = DM.DM_M4(input, count_times)
        elif mutant == 'M5':
            cal = DM.DM_M5(input, count_times)

    elif program == 'SM':
        if mutant == 'M1':
            cal = SM.SM_M1(input, count_times)
        elif mutant == 'M2':
            cal = SM.SM_M2(input, count_times)
        elif mutant == 'M3':
            cal = SM.SM_M3(input, count_times)
        elif mutant == 'M4':
            cal = SM.SM_M4(input, count_times)
        elif mutant == 'M5':
            cal = SM.SM_M5(input, count_times)

    # print(cal)
    #
    # print('right output: '+str(right_output))

    # judge wrong outputs
    for j in range(len(pt)):
        j_s = dec2bin(j, bit)
        if j_s in cal:
            if wrong_output(j, right_output):
                #print("have wrong outputs")
                flag_wrong = True
                wrong += cal[j_s]
    #
    # chi test
    if flag_wrong == False:  # no wrong output
      if count_times == 1:  # only one output
        pvalue = 1
      else:
        for j in range(len(p)):
          j_s = dec2bin(right_output[j],bit)
          if j_s in cal:
            fre.append(cal[j_s])
          else:
            fre.append(0)
        p = np.array(p)
        fre = np.array(fre)
        p = robjects.FloatVector(p)
        fre = robjects.FloatVector(fre)
        # print('p:'+str(p))
        # print('fre:'+str(fre))
        robjects.r('''
                      chitest<-function(observed,theoretical){
                          test_result <- chisq.test(x = observed,p = theoretical)
                          pvalue = test_result$p.value
                          return (pvalue)
                      }
              ''')
        t = robjects.r['chitest'](fre, p)
        pvalue = t[0]
        # print('no wrong output')
    else:
      pvalue = 0
    #print(pvalue)
    if pvalue < 0.01:
      flag_fail = True
    right_output_dec2bin =[]
    for i in range(len(right_output)):
        right_output_dec2bin.append(dec2bin(right_output[i],bit_output))

    return flag_fail, cal, right_output_dec2bin

def calculate_fail_number(input, mutant, program):
    # count_fail = 0  # the number that fails the test
    # count_wrong = []  # number of wrong output
    # pvalue = []
    pvalue = []
    count_times = 0
    right_output = []
    p = []  # probability
    wrong = 0
    flag_wrong = False
    fre = []
    flag_fail = False


    if program == 'AI':
        bit = 11
        bit_output = 10
        pt = AI.probabilityComputing(input)
    elif program == 'AS':
        bit = 10
        pt = AS.probabilityComputing(input)
    elif program == 'BV':
        bit = 10
        pt = BV.probabilityComputing(input)
    elif program == 'CE':
        bit = 11
        pt = CE.probabilityComputing(input)
    elif program == 'DM':
        bit = 11
        pt = DM.probabilityComputing(input)
    elif program == 'SM':
        bit = 7
        pt = SM.probabilityComputing(input)

    for i in range(len(pt)):
        if pt[i] > 1e-3:
            count_times += 1
            right_output.append(i)
            p.append(pt[i])

    if program == 'AI':
        if mutant == 'M1':
            cal = AI.AI_M1(input, count_times)
        elif mutant == 'M2':
            cal = AI.AI_M2(input, count_times)
        elif mutant == 'M3':
            cal = AI.AI_M3(input, count_times)
        elif mutant == 'M4':
            cal = AI.AI_M4(input, count_times)
        elif mutant == 'M5':
            cal = AI.AI_M5(input, count_times)
        elif mutant == 'M6':
            cal = AI.AI_M6(input, count_times)
        elif mutant == 'M7':
            cal = AI.AI_M7(input, count_times)
        elif mutant == 'M8':
            cal = AI.AI_M8(input, count_times)
        elif mutant == 'M9':
            cal = AI.AI_M9(input, count_times)
        elif mutant == 'M10':
            cal = AI.AI_M10(input, count_times)
        elif mutant == 'M11':
            cal = AI.AI_M11(input, count_times)
        elif mutant == 'M12':
            cal = AI.AI_M12(input, count_times)
        elif mutant == 'M13':
            cal = AI.AI_M13(input, count_times)
        elif mutant == 'M14':
            cal = AI.AI_M14(input, count_times)
        elif mutant == 'M15':
            cal = AI.AI_M15(input, count_times)

    elif program == 'AS':
        if mutant == 'M1':
            cal = AS.AS_M1(input, count_times)
        elif mutant == 'M2':
            cal = AS.AS_M2(input, count_times)
        elif mutant == 'M3':
            cal = AS.AS_M3(input, count_times)
        elif mutant == 'M4':
            cal = AS.AS_M4(input, count_times)
        elif mutant == 'M5':
            cal = AS.AS_M5(input, count_times)

    elif program == 'BV':
        if mutant == 'M1':
            cal = BV.BV_M1(input, count_times)
        elif mutant == 'M2':
            cal = BV.BV_M2(input, count_times)
        elif mutant == 'M3':
            cal = BV.BV_M3(input, count_times)
        elif mutant == 'M4':
            cal = BV.BV_M4(input, count_times)
        elif mutant == 'M5':
            cal = BV.BV_M5(input, count_times)

    elif program == 'CE':
        if mutant == 'M1':
            cal = CE.CE_M1(input, count_times)
        elif mutant == 'M2':
            cal = CE.CE_M2(input, count_times)
        elif mutant == 'M3':
            cal = CE.CE_M3(input, count_times)
        elif mutant == 'M4':
            cal = CE.CE_M4(input, count_times)
        elif mutant == 'M5':
            cal = CE.CE_M5(input, count_times)

    elif program == 'DM':
        if mutant == 'M1':
            cal = DM.DM_M1(input, count_times)
        elif mutant == 'M2':
            cal = DM.DM_M2(input, count_times)
        elif mutant == 'M3':
            cal = DM.DM_M3(input, count_times)
        elif mutant == 'M4':
            cal = DM.DM_M4(input, count_times)
        elif mutant == 'M5':
            cal = DM.DM_M5(input, count_times)

    elif program == 'SM':
        if mutant == 'M1':
            cal = SM.SM_M1(input, count_times)
        elif mutant == 'M2':
            cal = SM.SM_M2(input, count_times)
        elif mutant == 'M3':
            cal = SM.SM_M3(input, count_times)
        elif mutant == 'M4':
            cal = SM.SM_M4(input, count_times)
        elif mutant == 'M5':
            cal = SM.SM_M5(input, count_times)

    # print(cal)
    #
    # print('right output: '+str(right_output))

    # judge wrong outputs
    for j in range(len(pt)):
        j_s = dec2bin(j, bit)
        if j_s in cal:
            if wrong_output(j, right_output):
                #print("have wrong outputs")
                flag_wrong = True
                wrong += cal[j_s]
    #
    # chi test
    if flag_wrong == False:  # no wrong output
      if count_times == 1:  # only one output
        pvalue = 1
      else:
        for j in range(len(p)):
          j_s = dec2bin(right_output[j],bit)
          if j_s in cal:
            fre.append(cal[j_s])
          else:
            fre.append(0)
        p = np.array(p)
        fre = np.array(fre)
        p = robjects.FloatVector(p)
        fre = robjects.FloatVector(fre)
        # print('p:'+str(p))
        # print('fre:'+str(fre))
        robjects.r('''
                      chitest<-function(observed,theoretical){
                          test_result <- chisq.test(x = observed,p = theoretical)
                          pvalue = test_result$p.value
                          return (pvalue)
                      }
              ''')
        t = robjects.r['chitest'](fre, p)
        pvalue = t[0]
        # print('no wrong output')
    else:
      pvalue = 0
    #print(pvalue)
    if pvalue < 0.01:
      flag_fail = True
    right_output_dec2bin =[]
    for i in range(len(right_output)):
        right_output_dec2bin.append(dec2bin(right_output[i],bit_output))

    return flag_fail, cal, right_output_dec2bin



# doing testing
def comb_testing(mutant, program, o):
    dir_root = './inputs_' + str(K) + '/' + program + '/' + mutant + '_o' + str(o) + '/'
    # input_file = open('./inputs/'+'input_'+program+"_"+mutant+".txt")
    count_list = []  # the list of test cases in different test suites
    fail_list = []  # the list of test cases that fail in different test suites
    fail_suite_count = 0
    for i in range(K):
        input_file = open(dir_root + 'input_' + program + '_' + mutant + '_' + str(i) + '.txt')
        count = 0  # the number of test cases in one test suite
        count_fail = 0  # the number of test cases that fail in one test suite
        input_file.readline()
        input_str = input_file.readline().replace('\n', '').replace('\t', '')
        while input_str != "":
            count += 1
            input = int(input_str, 2)
            flag_fail, f = calculate_fail_number_GA(input, mutant, 'Comb', program, o)
            input_str = input_file.readline().replace('\n', '').replace('\t', '')
            if flag_fail == True:
                count_fail += 1
        # f = open('./results/'+program+'/' + program + '_' + mutant + '_' + 'Comb' + '.txt', 'a')
        f.write('fail / total :' + str(count_fail) + ' / ' + str(count))
        f.write('\n')
        if count_fail > 0:
            fail_suite_count += 1
        fail_list.append(count_fail)
        count_list.append(count)
    f.write('\n')
    for i in range(K):
        f.write(str(fail_list[i]) + ' / ' + str(count_list[i]))
        f.write('\t')
    f.write('\n')
    f.write('number of fail suites / total number of suites : ' + str(fail_suite_count) + '/' + str(len(count_list)))
    f.write('\n')
    f.write('number of fail cases / total number of cases : ' + str(sum(fail_list)) + ' / ' + str(sum(count_list)))
    f.write('\n')
    return count_list


# Random
def random_testing(mutant, program, count_list, n, o):
    count_list_r = count_list[:]
    fail_list = []
    fail_suite_count = 0
    for i in range(len(count_list)):
        count_fail = 0
        while count_list[i] != 0:
            input_str = ''
            for j in range(n):
                bit = random.randint(0, 1)
                input_str += str(bit)
            input = int(input_str, 2)
            flag_fail, f = calculate_fail_number_GA(input, mutant, 'Random', program, o)
            count_list[i] = count_list[i] - 1
            if flag_fail == True:
                count_fail += 1
        # f = open('./results/' + program + '/' + program + '_' + mutant + '_' + 'Random' + '.txt', 'a')
        f.write('fail / total :' + str(count_fail) + ' / ' + str(count_list_r[i]))
        f.write('\n')
        if count_fail > 0:
            fail_suite_count += 1
        fail_list.append(count_fail)
    f.write('\n')
    for i in range(K):
        f.write(str(fail_list[i]) + ' / ' + str(count_list_r[i]))
        f.write('\t')
    f.write('\n')
    f.write('number of fail suites / total number of suites : ' + str(fail_suite_count) + '/' + str(len(count_list_r)))
    f.write('\n')
    f.write('number of fail cases / total number of cases : ' + str(sum(fail_list)) + ' / ' + str(sum(count_list_r)))
    f.write('\n')


if __name__ == '__main__':
    # #SM
    # count_fail = 0
    # program = 'SM'
    # mutant = 'M5'
    # f = open('./count_'+program+'_'+mutant+'_2.txt','w')
    # for i in range(128):
    #     flag = []
    #     flag.append(calculate_fail_number_GA(i,mutant,program))
    #     flag.append(calculate_fail_number_GA(i,mutant,program))
    #     flag.append(calculate_fail_number_GA(i,mutant,program))
    #     if flag[0] == True and flag[1] == True and flag[2] == True:
    #         count_fail += 1
    #         f.write(str(i))
    #         f.write('\n')
    #         f.write(str(dec2bin(i,7)))
    #         f.write('\n')
    #         f.write('\n')
    # f.write(str(count_fail))
    # print(count_fail)

    #AI
    # count_fail = 0
    # program = 'AI'
    # mutant = 'M15'
    # f = open('./AI/count_'+program+'_'+mutant+'_1.txt','w')
    # for i in range(1024):
    #     flag0, cal0, right_output0 = calculate_fail_number_GA(i, mutant, program)
    #     flag1, cal1, right_output1 = calculate_fail_number_GA(i, mutant, program)
    #     flag2, cal2, right_output2 = calculate_fail_number_GA(i, mutant, program)
    #     if flag0 == True and flag1 == True and flag2 == True:
    #         count_fail += 1
    #         f.write(str(i))
    #         f.write('\n')
    #         f.write('input: ')
    #         f.write(str(dec2bin(i,10)))
    #         f.write('\n')
    #         f.write('right output: ')
    #         f.write('\n')
    #         f.write(str(right_output0))
    #         f.write('\n')
    #         f.write('output: ')
    #         f.write('\n')
    #         f.write(str(cal0))
    #         f.write('\n')
    #         f.write(str(cal1))
    #         f.write('\n')
    #         f.write(str(cal2))
    #         f.write('\n')
    #         f.write('\n')
    # f.write(str(count_fail))
    # print(count_fail)

    #print(calculate_fail_number_GA(0,'M1','AS'))






    # gen_test_suites(10, 2, 'M1', 'AI')
    # gen_test_suites(10, 2, 'M2', 'AI')
    # gen_test_suites(10, 2, 'M3', 'AI')
    # gen_test_suites(10, 3, 'M3', 'AI')
    # gen_test_suites(10, 2, 'M4', 'AI')
    # gen_test_suites(10, 3, 'M4', 'AI')
    # gen_test_suites(10, 4, 'M4', 'AI')
    # gen_test_suites(10, 2, 'M5', 'AI')
    # gen_test_suites(10, 3, 'M5', 'AI')
    # gen_test_suites(10, 4, 'M5', 'AI')
    # gen_test_suites(10, 5, 'M5', 'AI')
    # gen_test_suites(10, 2, 'M6', 'AI')
    # gen_test_suites(10, 3, 'M6', 'AI')
    # gen_test_suites(10, 4, 'M6', 'AI')
    # gen_test_suites(10, 5, 'M6', 'AI')
    # gen_test_suites(10, 6, 'M6', 'AI')
    # gen_test_suites(10, 2, 'M7', 'AI')
    # gen_test_suites(10, 3, 'M7', 'AI')
    # gen_test_suites(10, 4, 'M7', 'AI')
    # gen_test_suites(10, 5, 'M7', 'AI')
    # gen_test_suites(10, 6, 'M7', 'AI')
    # gen_test_suites(10, 7, 'M7', 'AI')
    #
    count_list = comb_testing('M1', 'AI', 2)
    random_testing('M1', 'AI', count_list, 10, 2)
    # count_list = comb_testing('M2', 'AI', 2)
    # random_testing('M2', 'AI', count_list, 10, 2)
    # count_list = comb_testing('M3', 'AI', 2)
    # random_testing('M3', 'AI', count_list, 10, 2)
    # count_list = comb_testing('M3', 'AI', 3)
    # random_testing('M3', 'AI', count_list, 10, 3)
    # count_list = comb_testing('M4', 'AI', 2)
    # random_testing('M4', 'AI', count_list, 10, 2)
    # count_list = comb_testing('M4', 'AI', 3)
    # random_testing('M4', 'AI', count_list, 10, 3)
    # count_list = comb_testing('M4', 'AI', 4)
    # random_testing('M4', 'AI', count_list, 10, 4)
    # count_list = comb_testing('M5', 'AI', 2)
    # random_testing('M5', 'AI', count_list, 10, 2)
    # count_list = comb_testing('M5', 'AI', 3)
    # random_testing('M5', 'AI', count_list, 10, 3)
    # count_list = comb_testing('M5', 'AI', 4)
    # random_testing('M5', 'AI', count_list, 10, 4)
    # count_list = comb_testing('M5', 'AI', 5)
    # random_testing('M5', 'AI', count_list, 10, 5)
    # count_list = comb_testing('M6', 'AI', 2)
    # random_testing('M6', 'AI', count_list, 10, 2)
    # count_list = comb_testing('M6', 'AI', 3)
    # random_testing('M6', 'AI', count_list, 10, 3)
    # count_list = comb_testing('M6', 'AI', 4)
    # random_testing('M6', 'AI', count_list, 10, 4)
    # count_list = comb_testing('M6', 'AI', 5)
    # random_testing('M6', 'AI', count_list, 10, 5)
    # count_list = comb_testing('M6', 'AI', 6)
    # random_testing('M6', 'AI', count_list, 10, 6)
    # count_list = comb_testing('M7', 'AI', 2)
    # random_testing('M7', 'AI', count_list, 10, 2)
    # count_list = comb_testing('M7', 'AI', 3)
    # random_testing('M7', 'AI', count_list, 10, 3)
    # count_list = comb_testing('M7', 'AI', 4)
    # random_testing('M7', 'AI', count_list, 10, 4)
    # count_list = comb_testing('M7', 'AI', 5)
    # random_testing('M7', 'AI', count_list, 10, 5)
    # count_list = comb_testing('M7', 'AI', 6)
    # random_testing('M7', 'AI', count_list, 10, 6)
    # count_list = comb_testing('M7', 'AI', 7)
    # random_testing('M7', 'AI', count_list, 10, 7)

    # gen_test_suites(10, 2, 'M1', 'AS')
    # gen_test_suites(10, 2, 'M2', 'AS')
    # gen_test_suites(10, 2, 'M3', 'AS')
    # gen_test_suites(10, 3, 'M4', 'AS')
    # gen_test_suites(10, 2, 'M5', 'AS')
    #
    # gen_test_suites(10, 2, 'M1', 'BV')
    # gen_test_suites(10, 2, 'M2', 'BV')
    # gen_test_suites(10, 2, 'M3', 'BV')
    # gen_test_suites(10, 2, 'M4', 'BV')
    # gen_test_suites(10, 3, 'M5', 'BV')
    #
    # gen_test_suites(10, 2, 'M1', 'CE')
    # gen_test_suites(10, 2, 'M2', 'CE')
    # gen_test_suites(10, 3, 'M3', 'CE')
    # gen_test_suites(10, 2, 'M4', 'CE')
    # gen_test_suites(10, 2, 'M5', 'CE')
    #
    # gen_test_suites(11, 2, 'M1', 'DM')
    # gen_test_suites(11, 2, 'M2', 'DM')
    # gen_test_suites(11, 2, 'M3', 'DM')
    # gen_test_suites(11, 2, 'M4', 'DM')
    # gen_test_suites(11, 3, 'M5', 'DM')
    #
    # gen_test_suites(7, 2, 'M1', 'SM')
    # gen_test_suites(7, 2, 'M2', 'SM')
    # gen_test_suites(7, 2, 'M3', 'SM')
    # gen_test_suites(7, 3, 'M4', 'SM')
    # gen_test_suites(7, 2, 'M5', 'SM')

    # count_list = comb_testing('M1','AI')
    # random_testing('M1','AI',count_list,10)
    # count_list = comb_testing('M2','AI')
    # random_testing('M2','AI',count_list,10)
    # count_list = comb_testing('M3','AI')
    # random_testing('M3','AI',count_list,10)
    # count_list = comb_testing('M4','AI')
    # random_testing('M4','AI',count_list,10)
    # count_list = comb_testing('M5','AI')
    # random_testing('M5','AI',count_list,10)

    # count_list = comb_testing('M1','AS')
    # random_testing('M1','AS',count_list,10)
    # count_list = comb_testing('M2','AS')
    # random_testing('M2','AS',count_list,10)
    # count_list = comb_testing('M3','AS')
    # random_testing('M3','AS',count_list,10)
    # count_list = comb_testing('M4','AS')
    # random_testing('M4','AS',count_list,10)
    # count_list = comb_testing('M5','AS')
    # random_testing('M5','AS',count_list,10)

    # count_list = comb_testing('M1','BV')
    # random_testing('M1','BV',count_list,10)
    # count_list = comb_testing('M2','BV')
    # random_testing('M2','BV',count_list,10)
    # count_list = comb_testing('M3','BV')
    # random_testing('M3','BV',count_list,10)
    # count_list = comb_testing('M4','BV')
    # random_testing('M4','BV',count_list,10)
    # count_list = comb_testing('M5','BV')
    # random_testing('M5','BV',count_list,10)
    # #
    # count_list = comb_testing('M1','CE')
    # random_testing('M1','CE',count_list,10)
    # count_list = comb_testing('M2','CE')
    # random_testing('M2','CE',count_list,10)
    # count_list = comb_testing('M3','CE')
    # random_testing('M3','CE',count_list,10)
    # count_list = comb_testing('M4','CE')
    # random_testing('M4','CE',count_list,10)
    # count_list = comb_testing('M5','CE')
    # random_testing('M5','CE',count_list,10)
    #
    # count_list = comb_testing('M1','DM')
    # random_testing('M1','DM',count_list,11)
    # count_list = comb_testing('M2','DM')
    # random_testing('M2','DM',count_list,11)
    # count_list = comb_testing('M3','DM')
    # random_testing('M3','DM',count_list,11)
    # count_list = comb_testing('M4','DM')
    # random_testing('M4','DM',count_list,11)
    # count_list = comb_testing('M5','DM')
    # random_testing('M5','DM',count_list,11)
    #
    # count_list = comb_testing('M1','SM')
    # random_testing('M1','SM',count_list,7)
    # count_list = comb_testing('M2','SM')
    # random_testing('M2','SM',count_list,7)
    # count_list = comb_testing('M3','SM')
    # random_testing('M3','SM',count_list,7)
    # count_list = comb_testing('M4','SM')
    # random_testing('M4','SM',count_list,7)
    # count_list = comb_testing('M5','SM')
    # random_testing('M5','SM',count_list,7)

    # gen_test_suites(10, 4, 'M7', 'AI')
    # count_list = comb_testing('M7','AI')
    # random_testing('M7','AI',count_list,10)

    # gen_test_suites(10, 2, 'M8', 'AI')
    # count_list = comb_testing('M8','AI')
    # random_testing('M8','AI',count_list,10)

# qc = QuantumCircuit(3)
# # Apply H-gate to each qubit:
# for qubit in range(3):
#     qc.h(qubit)
# # See the circuit:
# qc.draw()
#
# # Let's see the result
# svsim = Aer.get_backend('statevector_simulator')
# qobj = assemble(qc)
# final_state = svsim.run(qobj).result().get_statevector()
#
# # In Jupyter Notebooks we can display this nicely using Latex.
# # If not using Jupyter Notebooks you may need to remove the
# # array_to_latex function and use print(final_state) instead.
# #from qiskit_textbook.tools import array_to_latex
# print(final_state)

# qc = QuantumCircuit(2)
# qc.x(0)
# qc.draw()
#
# # Simulate the unitary
# usim = Aer.get_backend('unitary_simulator')
# qobj = assemble(qc)
# unitary = usim.run(qobj).result().get_unitary()
#
# print(unitary)

# qc = QuantumCircuit(2)
# # Apply H-gate to the first:
# qc.h(0)
# qc.draw()
#
# # Let's see the result:
# svsim = Aer.get_backend('statevector_simulator')
# qobj = assemble(qc)
# final_state = svsim.run(qobj).result().get_statevector()
# # Print the statevector neatly:
# print(final_state)


