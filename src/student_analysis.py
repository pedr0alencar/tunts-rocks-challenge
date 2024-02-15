import logging
import math  # Importa o módulo math

def calculate_student_situation(student_data):
    results = []
    total_classes = 60  # ou outro valor, se variável
    for student in student_data:
        try:
            matricula, name, absences, p1, p2, p3 = student[:6]
            absences = int(absences.strip()) if absences.strip() else 0
            p1 = float(p1.strip()) if p1.strip() else 0.0
            p2 = float(p2.strip()) if p2.strip() else 0.0
            p3 = float(p3.strip()) if p3.strip() else 0.0
        except ValueError as e:
            logging.error(f'Error processing line {student}: {e}')
            continue

        # Calcula a média com notas de 0 a 100
        average = (p1 + p2 + p3) / 3
        if absences > total_classes * 0.25:
            situation = "Reprovado por Falta"
            naf = 0
        elif average < 50:
            situation = "Reprovado por Nota"
            naf = 0
        elif average < 70:
            situation = "Exame Final"
            # Calcula a nota necessária na final considerando notas de 0 a 100
            naf = ((50 * 2) - average)  # Necessário para atingir média final de 50
            naf = math.ceil(naf) if naf > 0 else 0  # Usa math.ceil para arredondar para cima
        else:
            situation = "Aprovado"
            naf = 0

        results.append([matricula, name, situation, naf])
    logging.info('Situações dos alunos analisadas.')
    return results
