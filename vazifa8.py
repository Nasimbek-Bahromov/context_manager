# 1.savol
# class StudentRoyxati:
#     def __init__(self, birinchi_royxat=None):
#         self.birinchi_royxat = birinchi_royxat if birinchi_royxat else []
#         self._ishchi_royxat = list(self.birinchi_royxat)

#     def qoshish(self, talaba):
#         self._ishchi_royxat.append(talaba)

#     def __enter__(self):
#         self._zaxira_royxat = list(self.birinchi_royxat) 
#         return self

#     def __exit__(self, xato_turi, xato_maqomi, iz_qoldiruvchi):
#         if xato_turi:
#             self._ishchi_royxat = self._zaxira_royxat  
#             return False 
#         else:
#             self.birinchi_royxat = self._ishchi_royxat 
#             return True

#     def royxatni_olish(self):
#         return self.birinchi_royxat

# try:
#     mening_talabalarim = StudentRoyxati(['Ali', 'Vali', 'Salim'])
#     with mening_talabalarim as student:
#         student.qoshish('Hasan')
#         student.qoshish('Husan')

#     print("Natija:", mening_talabalarim.royxatni_olish())
# except Exception as e:
#     print(f"Xatolik: {e}, Natija: {mening_talabalarim.royxatni_olish()}")

# 2.savol

# class StudentsKontekstiMenejeri:
#     def __init__(self, students):
#         self.students = students
#         self._eski_holat = None

#     def __enter__(self):
#         self._eski_holat = list(self.students)
#         return self.students

#     def __exit__(self, xatolik_turi, xatolik_xabar, iz):
#         if xatolik_turi is not None:
#             self.students.clear()
#             self.students.extend(self._eski_holat)
#             return True 
        
# students = ['Ali', 'Vali', 'Salim']
# with StudentsKontekstiMenejeri(students) as st:
#     st.append('Hasan')
#     st.append('Husan')

# print("Natija:", students) 



