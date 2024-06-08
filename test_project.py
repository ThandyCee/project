import pytest
from project import add_patient, get_all_patients, add_doctor, get_all_doctors, book_appointment, view_appointments

def test_add_patient(monkeypatch):
    inputs = iter(["Mickey Mouse", "30", "1990-01-01"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    add_patient()
    patients = get_all_patients()
    assert any(p["name"] == "Mickey Mouse" for p in patients)

def test_add_doctor(monkeypatch):
    inputs = iter(["Dr. Mzila", "Cardiology"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    add_doctor()
    doctors = get_all_doctors()
    assert any(d["name"] == "Dr. Mzila" for d in doctors)

def test_book_appointment(monkeypatch):
    inputs = iter(["Mickey Mouse", "Dr. Mzila", "2023-06-15"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    book_appointment()
    view_appointments()

if __name__ == "__main__":
    pytest.main()
