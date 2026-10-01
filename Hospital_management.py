from abc import ABC, abstractmethod


# ============================================================
# USER CLASS
# ============================================================

class User:
    def __init__(self, user_id, name, phone):
        self.user_id = user_id
        self.name = name
        self.phone = phone

    def display_info(self):
        print("ID:", self.user_id)
        print("Name:", self.name)
        print("Phone:", self.phone)


# ============================================================
# PATIENT CLASS - INHERITANCE
# ============================================================

class Patient(User):

    def __init__(self, patient_id, name, phone, age, gender):
        super().__init__(patient_id, name, phone)

        self.age = age
        self.gender = gender

        # Encapsulation
        self.__medical_history = []

    def add_medical_record(self, record):
        self.__medical_history.append(record)

    def get_medical_history(self):
        return self.__medical_history

    # Polymorphism
    def display_info(self):
        print("\n--- PATIENT INFORMATION ---")
        print("Patient ID:", self.user_id)
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Age:", self.age)
        print("Gender:", self.gender)


# ============================================================
# DOCTOR CLASS - INHERITANCE
# ============================================================

class Doctor(User):

    def __init__(self, doctor_id, name, phone, specialization):
        super().__init__(doctor_id, name, phone)

        self.specialization = specialization

    # Polymorphism
    def display_info(self):
        print("\n--- DOCTOR INFORMATION ---")
        print("Doctor ID:", self.user_id)
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Specialization:", self.specialization)


# ============================================================
# APPOINTMENT CLASS
# ============================================================

class Appointment:

    def __init__(
        self,
        appointment_id,
        patient,
        doctor,
        date,
        time
    ):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

        self.status = "Scheduled"

    def complete_appointment(self):
        self.status = "Completed"
        print("Appointment completed successfully.")

    def cancel_appointment(self):
        self.status = "Cancelled"
        print("Appointment cancelled successfully.")

    def display_info(self):
        print("\n--- APPOINTMENT ---")
        print("Appointment ID:", self.appointment_id)
        print("Patient:", self.patient.name)
        print("Doctor:", self.doctor.name)
        print("Date:", self.date)
        print("Time:", self.time)
        print("Status:", self.status)


# ============================================================
# MEDICAL RECORD CLASS
# ============================================================

class MedicalRecord:

    def __init__(
        self,
        record_id,
        patient,
        doctor,
        diagnosis,
        treatment
    ):
        self.record_id = record_id
        self.patient = patient
        self.doctor = doctor
        self.diagnosis = diagnosis
        self.treatment = treatment

    def display_info(self):
        print("\n--- MEDICAL RECORD ---")
        print("Record ID:", self.record_id)
        print("Patient:", self.patient.name)
        print("Doctor:", self.doctor.name)
        print("Diagnosis:", self.diagnosis)
        print("Treatment:", self.treatment)


# ============================================================
# MEDICINE CLASS
# ============================================================

class Medicine:

    def __init__(
        self,
        medicine_id,
        name,
        price,
        quantity
    ):
        self.medicine_id = medicine_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def reduce_stock(self, quantity):

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if quantity > self.quantity:
            raise ValueError(
                "Insufficient medicine stock."
            )

        self.quantity -= quantity

    def add_stock(self, quantity):

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

        self.quantity += quantity

    def display_info(self):
        print("\n--- MEDICINE ---")
        print("Medicine ID:", self.medicine_id)
        print("Medicine Name:", self.name)
        print("Price:", self.price)
        print("Available Quantity:", self.quantity)


# ============================================================
# PRESCRIPTION CLASS
# ============================================================

class Prescription:

    def __init__(
        self,
        prescription_id,
        patient,
        doctor
    ):
        self.prescription_id = prescription_id
        self.patient = patient
        self.doctor = doctor

        # Composition
        self.medicines = []

    def add_medicine(self, medicine, quantity):

        medicine.reduce_stock(quantity)

        self.medicines.append(
            (medicine, quantity)
        )

        print(
            medicine.name,
            "added to prescription."
        )

    def display_info(self):

        print("\n--- PRESCRIPTION ---")
        print(
            "Prescription ID:",
            self.prescription_id
        )

        print(
            "Patient:",
            self.patient.name
        )

        print(
            "Doctor:",
            self.doctor.name
        )

        print("\nMedicines:")

        if len(self.medicines) == 0:
            print("No medicines added.")

        else:

            for medicine, quantity in self.medicines:

                print(
                    medicine.name,
                    "- Quantity:",
                    quantity
                )


# ============================================================
# ROOM CLASS
# ============================================================

class Room:

    def __init__(
        self,
        room_number,
        room_type
    ):
        self.room_number = room_number
        self.room_type = room_type

        self.patient = None

    def assign_room(self, patient):

        if self.patient is not None:
            raise ValueError(
                "Room is already occupied."
            )

        self.patient = patient

        print(
            "Room",
            self.room_number,
            "assigned to",
            patient.name
        )

    def release_room(self):

        if self.patient is None:
            raise ValueError(
                "Room is already available."
            )

        print(
            "Room",
            self.room_number,
            "released."
        )

        self.patient = None

    def display_info(self):

        print("\n--- ROOM ---")
        print(
            "Room Number:",
            self.room_number
        )

        print(
            "Room Type:",
            self.room_type
        )

        if self.patient is None:
            print("Status: Available")

        else:
            print(
                "Status: Occupied by",
                self.patient.name
            )


# ============================================================
# BILL CLASS
# ============================================================

class Bill:

    def __init__(
        self,
        bill_id,
        patient,
        consultation_fee,
        medicine_charge,
        room_charge,
        lab_charge
    ):
        self.bill_id = bill_id
        self.patient = patient

        self.consultation_fee = consultation_fee
        self.medicine_charge = medicine_charge
        self.room_charge = room_charge
        self.lab_charge = lab_charge

    def calculate_total(self):

        return (
            self.consultation_fee
            + self.medicine_charge
            + self.room_charge
            + self.lab_charge
        )

    def display_info(self):

        print("\n--- HOSPITAL BILL ---")

        print(
            "Bill ID:",
            self.bill_id
        )

        print(
            "Patient:",
            self.patient.name
        )

        print(
            "Consultation Fee:",
            self.consultation_fee
        )

        print(
            "Medicine Charge:",
            self.medicine_charge
        )

        print(
            "Room Charge:",
            self.room_charge
        )

        print(
            "Lab Charge:",
            self.lab_charge
        )

        print("----------------------")

        print(
            "TOTAL:",
            self.calculate_total()
        )


# ============================================================
# PAYMENT - ABSTRACTION
# ============================================================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# ============================================================
# CASH PAYMENT - INHERITANCE
# ============================================================

class CashPayment(Payment):

    def pay(self, amount):

        print(
            "Cash payment successful:",
            amount
        )


# ============================================================
# CARD PAYMENT - INHERITANCE
# ============================================================

class CardPayment(Payment):

    def pay(self, amount):

        print(
            "Card payment successful:",
            amount
        )


# ============================================================
# HOSPITAL CLASS
# ============================================================

class Hospital:

    def __init__(self, name):

        self.name = name

        self.patients = []
        self.doctors = []
        self.appointments = []
        self.medical_records = []
        self.medicines = []
        self.prescriptions = []
        self.rooms = []
        self.bills = []

    # --------------------------------------------------------
    # PATIENT
    # --------------------------------------------------------

    def add_patient(self):

        try:

            patient_id = int(
                input("Enter Patient ID: ")
            )

            name = input(
                "Enter Patient Name: "
            )

            phone = input(
                "Enter Phone Number: "
            )

            age = int(
                input("Enter Age: ")
            )

            gender = input(
                "Enter Gender: "
            )

            patient = Patient(
                patient_id,
                name,
                phone,
                age,
                gender
            )

            self.patients.append(patient)

            print(
                "Patient",
                name,
                "registered successfully."
            )

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # DOCTOR
    # --------------------------------------------------------

    def add_doctor(self):

        try:

            doctor_id = int(
                input("Enter Doctor ID: ")
            )

            name = input(
                "Enter Doctor Name: "
            )

            phone = input(
                "Enter Phone Number: "
            )

            specialization = input(
                "Enter Specialization: "
            )

            doctor = Doctor(
                doctor_id,
                name,
                phone,
                specialization
            )

            self.doctors.append(doctor)

            print(
                "Doctor",
                name,
                "added successfully."
            )

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # VIEW PATIENTS
    # --------------------------------------------------------

    def view_patients(self):

        print("\n========== PATIENTS ==========")

        if len(self.patients) == 0:

            print("No patients registered.")

            return

        for patient in self.patients:

            patient.display_info()

    # --------------------------------------------------------
    # VIEW DOCTORS
    # --------------------------------------------------------

    def view_doctors(self):

        print("\n========== DOCTORS ==========")

        if len(self.doctors) == 0:

            print("No doctors available.")

            return

        for doctor in self.doctors:

            doctor.display_info()

    # --------------------------------------------------------
    # FIND PATIENT
    # --------------------------------------------------------

    def find_patient(self, patient_id):

        for patient in self.patients:

            if patient.user_id == patient_id:

                return patient

        return None

    # --------------------------------------------------------
    # FIND DOCTOR
    # --------------------------------------------------------

    def find_doctor(self, doctor_id):

        for doctor in self.doctors:

            if doctor.user_id == doctor_id:

                return doctor

        return None

    # --------------------------------------------------------
    # FIND MEDICINE
    # --------------------------------------------------------

    def find_medicine(self, medicine_id):

        for medicine in self.medicines:

            if medicine.medicine_id == medicine_id:

                return medicine

        return None

    # --------------------------------------------------------
    # FIND APPOINTMENT
    # --------------------------------------------------------

    def find_appointment(
        self,
        appointment_id
    ):

        for appointment in self.appointments:

            if (
                appointment.appointment_id
                == appointment_id
            ):

                return appointment

        return None

    # --------------------------------------------------------
    # BOOK APPOINTMENT
    # --------------------------------------------------------

    def book_appointment(self):

        try:

            appointment_id = int(
                input(
                    "Enter Appointment ID: "
                )
            )

            patient_id = int(
                input(
                    "Enter Patient ID: "
                )
            )

            doctor_id = int(
                input(
                    "Enter Doctor ID: "
                )
            )

            patient = self.find_patient(
                patient_id
            )

            doctor = self.find_doctor(
                doctor_id
            )

            if patient is None:

                print(
                    "Patient not found."
                )

                return

            if doctor is None:

                print(
                    "Doctor not found."
                )

                return

            date = input(
                "Enter Appointment Date: "
            )

            time = input(
                "Enter Appointment Time: "
            )

            appointment = Appointment(
                appointment_id,
                patient,
                doctor,
                date,
                time
            )

            self.appointments.append(
                appointment
            )

            print(
                "Appointment booked successfully."
            )

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # VIEW APPOINTMENTS
    # --------------------------------------------------------

    def view_appointments(self):

        print(
            "\n========== APPOINTMENTS =========="
        )

        if len(self.appointments) == 0:

            print(
                "No appointments available."
            )

            return

        for appointment in self.appointments:

            appointment.display_info()

    # --------------------------------------------------------
    # COMPLETE APPOINTMENT
    # --------------------------------------------------------

    def complete_appointment(self):

        try:

            appointment_id = int(
                input(
                    "Enter Appointment ID: "
                )
            )

            appointment = self.find_appointment(
                appointment_id
            )

            if appointment is None:

                print(
                    "Appointment not found."
                )

                return

            appointment.complete_appointment()

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # CANCEL APPOINTMENT
    # --------------------------------------------------------

    def cancel_appointment(self):

        try:

            appointment_id = int(
                input(
                    "Enter Appointment ID: "
                )
            )

            appointment = self.find_appointment(
                appointment_id
            )

            if appointment is None:

                print(
                    "Appointment not found."
                )

                return

            appointment.cancel_appointment()

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # ADD MEDICAL RECORD
    # --------------------------------------------------------

    def add_medical_record(self):

        try:

            record_id = int(
                input(
                    "Enter Medical Record ID: "
                )
            )

            patient_id = int(
                input(
                    "Enter Patient ID: "
                )
            )

            doctor_id = int(
                input(
                    "Enter Doctor ID: "
                )
            )

            patient = self.find_patient(
                patient_id
            )

            doctor = self.find_doctor(
                doctor_id
            )

            if patient is None:

                print(
                    "Patient not found."
                )

                return

            if doctor is None:

                print(
                    "Doctor not found."
                )

                return

            diagnosis = input(
                "Enter Diagnosis: "
            )

            treatment = input(
                "Enter Treatment: "
            )

            record = MedicalRecord(
                record_id,
                patient,
                doctor,
                diagnosis,
                treatment
            )

            self.medical_records.append(
                record
            )

            patient.add_medical_record(
                record
            )

            print(
                "Medical record added successfully."
            )

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # VIEW MEDICAL RECORDS
    # --------------------------------------------------------

    def view_medical_records(self):

        print(
            "\n========== MEDICAL RECORDS =========="
        )

        if len(self.medical_records) == 0:

            print(
                "No medical records available."
            )

            return

        for record in self.medical_records:

            record.display_info()

    # --------------------------------------------------------
    # ADD MEDICINE
    # --------------------------------------------------------

    def add_medicine(self):

        try:

            medicine_id = int(
                input(
                    "Enter Medicine ID: "
                )
            )

            name = input(
                "Enter Medicine Name: "
            )

            price = float(
                input(
                    "Enter Medicine Price: "
                )
            )

            quantity = int(
                input(
                    "Enter Available Quantity: "
                )
            )

            medicine = Medicine(
                medicine_id,
                name,
                price,
                quantity
            )

            self.medicines.append(
                medicine
            )

            print(
                "Medicine added successfully."
            )

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # VIEW MEDICINES
    # --------------------------------------------------------

    def view_medicines(self):

        print(
            "\n========== MEDICINES =========="
        )

        if len(self.medicines) == 0:

            print(
                "No medicines available."
            )

            return

        for medicine in self.medicines:

            medicine.display_info()

    # --------------------------------------------------------
    # CREATE PRESCRIPTION
    # --------------------------------------------------------

    def create_prescription(self):

        try:

            prescription_id = int(
                input(
                    "Enter Prescription ID: "
                )
            )

            patient_id = int(
                input(
                    "Enter Patient ID: "
                )
            )

            doctor_id = int(
                input(
                    "Enter Doctor ID: "
                )
            )

            patient = self.find_patient(
                patient_id
            )

            doctor = self.find_doctor(
                doctor_id
            )

            if patient is None:

                print(
                    "Patient not found."
                )

                return

            if doctor is None:

                print(
                    "Doctor not found."
                )

                return

            prescription = Prescription(
                prescription_id,
                patient,
                doctor
            )

            while True:

                print(
                    "\nAvailable Medicines:"
                )

                self.view_medicines()

                medicine_id = input(
                    "\nEnter Medicine ID "
                    "(or type done): "
                )

                if medicine_id.lower() == "done":

                    break

                try:

                    medicine_id = int(
                        medicine_id
                    )

                    quantity = int(
                        input(
                            "Enter Quantity: "
                        )
                    )

                    medicine = self.find_medicine(
                        medicine_id
                    )

                    if medicine is None:

                        print(
                            "Medicine not found."
                        )

                        continue

                    prescription.add_medicine(
                        medicine,
                        quantity
                    )

                except ValueError as e:

                    print(
                        "Error:",
                        e
                    )

            self.prescriptions.append(
                prescription
            )

            print(
                "Prescription created successfully."
            )

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # VIEW PRESCRIPTIONS
    # --------------------------------------------------------

    def view_prescriptions(self):

        print(
            "\n========== PRESCRIPTIONS =========="
        )

        if len(self.prescriptions) == 0:

            print(
                "No prescriptions available."
            )

            return

        for prescription in self.prescriptions:

            prescription.display_info()

    # --------------------------------------------------------
    # ADD ROOM
    # --------------------------------------------------------

    def add_room(self):

        try:

            room_number = int(
                input(
                    "Enter Room Number: "
                )
            )

            room_type = input(
                "Enter Room Type: "
            )

            room = Room(
                room_number,
                room_type
            )

            self.rooms.append(
                room
            )

            print(
                "Room",
                room_number,
                "added successfully."
            )

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # VIEW ROOMS
    # --------------------------------------------------------

    def view_rooms(self):

        print(
            "\n========== ROOMS =========="
        )

        if len(self.rooms) == 0:

            print(
                "No rooms available."
            )

            return

        for room in self.rooms:

            room.display_info()

    # --------------------------------------------------------
    # FIND ROOM
    # --------------------------------------------------------

    def find_room(self, room_number):

        for room in self.rooms:

            if room.room_number == room_number:

                return room

        return None

    # --------------------------------------------------------
    # ASSIGN ROOM
    # --------------------------------------------------------

    def assign_room(self):

        try:

            room_number = int(
                input(
                    "Enter Room Number: "
                )
            )

            patient_id = int(
                input(
                    "Enter Patient ID: "
                )
            )

            room = self.find_room(
                room_number
            )

            patient = self.find_patient(
                patient_id
            )

            if room is None:

                print(
                    "Room not found."
                )

                return

            if patient is None:

                print(
                    "Patient not found."
                )

                return

            room.assign_room(
                patient
            )

        except ValueError as e:

            print(
                "Error:",
                e
            )

    # --------------------------------------------------------
    # RELEASE ROOM
    # --------------------------------------------------------

    def release_room(self):

        try:

            room_number = int(
                input(
                    "Enter Room Number: "
                )
            )

            room = self.find_room(
                room_number
            )

            if room is None:

                print(
                    "Room not found."
                )

                return

            room.release_room()

        except ValueError as e:

            print(
                "Error:",
                e
            )

    # --------------------------------------------------------
    # CREATE BILL
    # --------------------------------------------------------

    def create_bill(self):

        try:

            bill_id = int(
                input(
                    "Enter Bill ID: "
                )
            )

            patient_id = int(
                input(
                    "Enter Patient ID: "
                )
            )

            patient = self.find_patient(
                patient_id
            )

            if patient is None:

                print(
                    "Patient not found."
                )

                return

            consultation_fee = float(
                input(
                    "Enter Consultation Fee: "
                )
            )

            medicine_charge = float(
                input(
                    "Enter Medicine Charge: "
                )
            )

            room_charge = float(
                input(
                    "Enter Room Charge: "
                )
            )

            lab_charge = float(
                input(
                    "Enter Lab Charge: "
                )
            )

            bill = Bill(
                bill_id,
                patient,
                consultation_fee,
                medicine_charge,
                room_charge,
                lab_charge
            )

            self.bills.append(
                bill
            )

            print(
                "Bill created successfully."
            )

            bill.display_info()

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # VIEW BILLS
    # --------------------------------------------------------

    def view_bills(self):

        print(
            "\n========== BILLS =========="
        )

        if len(self.bills) == 0:

            print(
                "No bills available."
            )

            return

        for bill in self.bills:

            bill.display_info()

    # --------------------------------------------------------
    # PAYMENT
    # --------------------------------------------------------

    def make_payment(self):

        try:

            bill_id = int(
                input(
                    "Enter Bill ID: "
                )
            )

            bill = None

            for b in self.bills:

                if b.bill_id == bill_id:

                    bill = b

                    break

            if bill is None:

                print(
                    "Bill not found."
                )

                return

            amount = bill.calculate_total()

            print(
                "\nPayment Amount:",
                amount
            )

            print(
                "\n1. Cash Payment"
            )

            print(
                "2. Card Payment"
            )

            choice = input(
                "Choose Payment Method: "
            )

            if choice == "1":

                payment = CashPayment()

                payment.pay(amount)

            elif choice == "2":

                payment = CardPayment()

                payment.pay(amount)

            else:

                print(
                    "Invalid payment option."
                )

        except ValueError:

            print(
                "Invalid input."
            )

    # --------------------------------------------------------
    # MENU
    # --------------------------------------------------------

    def menu(self):

        while True:

            print("\n")
            print("================================")
            print("       CITY CARE HOSPITAL")
            print("================================")

            print("\n1. Add Patient")
            print("2. Add Doctor")
            print("3. View Patients")
            print("4. View Doctors")

            print("\n5. Book Appointment")
            print("6. View Appointments")
            print("7. Complete Appointment")
            print("8. Cancel Appointment")

            print("\n9. Add Medical Record")
            print("10. View Medical Records")

            print("\n11. Add Medicine")
            print("12. View Medicines")

            print("\n13. Create Prescription")
            print("14. View Prescriptions")

            print("\n15. Add Room")
            print("16. View Rooms")
            print("17. Assign Room")
            print("18. Release Room")

            print("\n19. Create Bill")
            print("20. View Bills")
            print("21. Make Payment")

            print("\n22. Exit")

            print(
                "\n================================"
            )

            choice = input(
                "Enter your choice: "
            )

            # Patient
            if choice == "1":

                self.add_patient()

            # Doctor
            elif choice == "2":

                self.add_doctor()

            elif choice == "3":

                self.view_patients()

            elif choice == "4":

                self.view_doctors()

            # Appointment
            elif choice == "5":

                self.book_appointment()

            elif choice == "6":

                self.view_appointments()

            elif choice == "7":

                self.complete_appointment()

            elif choice == "8":

                self.cancel_appointment()

            # Medical
            elif choice == "9":

                self.add_medical_record()

            elif choice == "10":

                self.view_medical_records()

            # Medicine
            elif choice == "11":

                self.add_medicine()

            elif choice == "12":

                self.view_medicines()

            # Prescription
            elif choice == "13":

                self.create_prescription()

            elif choice == "14":

                self.view_prescriptions()

            # Room
            elif choice == "15":

                self.add_room()

            elif choice == "16":

                self.view_rooms()

            elif choice == "17":

                self.assign_room()

            elif choice == "18":

                self.release_room()

            # Bill
            elif choice == "19":

                self.create_bill()

            elif choice == "20":

                self.view_bills()

            # Payment
            elif choice == "21":

                self.make_payment()

            # Exit
            elif choice == "22":

                print(
                    "\nThank you for using"
                )

                print(
                    "CITY CARE HOSPITAL."
                )

                print(
                    "Program ended."
                )

                break

            else:

                print(
                    "Invalid choice."
                )


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    hospital = Hospital(
        "CITY CARE HOSPITAL"
    )

    hospital.menu()