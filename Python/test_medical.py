import medical

def test_get_sorted_diseases():
    xml_path = r"C:\Users\chava\OneDrive\Documents\python-Automotive-Batch9\Python\medicalissues.xml"

    result = expected = [
        "Asthama",
        "Fever",
        "Kindney stone",
        "Severe Cough"
    ]

    assert result == expected
