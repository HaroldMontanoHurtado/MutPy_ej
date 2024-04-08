from db.consultas import lis_emp, lis_clt, lis_report_vent

def isEmpl(name_empl):
    lista = lis_emp()
    for emp in lista:
        if emp[1] == name_empl:
            return True
    return False

def isCustomer(name_clt):
    lista = lis_clt()
    for clt in lista:
        if clt[1] == name_clt:
            return True
    return False

def cantVent(name_empl):
    lista = lis_report_vent()
    if isEmpl(name_empl):
        for report in lista:
            if report[0] == name_empl:
                return int(report[1])
        return 0
