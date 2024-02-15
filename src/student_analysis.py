import logging
import math


def calculate_student_situation(student_data):
    results = []
    total_classes = 60  # or another value, if variable
    for student in student_data:
        try:
            # Unpack the first 6 elements from the student data
            registration, name, absences, p1, p2, p3 = student[:6]
            # Convert string values to appropriate types
            absences = int(absences.strip()) if absences.strip() else 0
            p1 = float(p1.strip()) if p1.strip() else 0.0
            p2 = float(p2.strip()) if p2.strip() else 0.0
            p3 = float(p3.strip()) if p3.strip() else 0.0
        except ValueError as e:
            logging.error(f'Error processing line {student}: {e}')
            continue

        # Calculate the average with grades from 0 to 100
        average = (p1 + p2 + p3) / 3
        # Check if absences are more than 25% of total classes
        if absences > total_classes * 0.25:
            situation = "Reprovado por Falta"
            naf = 0  # Minimum grade for final approval not applicable
        elif average < 50:
            situation = "Reprovado por Nota"
            naf = 0  # Minimum grade for final approval not applicable
        elif average < 70:
            situation = "Exame Final"
            # Calculate the necessary grade for the final exam considering grades from 0 to 100
            naf = ((50 * 2) - average)  # Needed to achieve a final average of 50
            naf = math.ceil(naf) if naf > 0 else 0  # Use math.ceil to round up
        else:
            situation = "Aprovado"
            naf = 0  # Minimum grade for final approval not applicable

        # Append the student's situation and required grade for approval to the results list
        results.append([registration, name, situation, naf])
    logging.info('Student situations analyzed.')
    return results
