from pathlib import Path

def get_external_data_path() -> Path:
    
    return Path(__file__).parent / "external_data"

def read_external_data(file_name: str) -> str:
   
    external_data_path = get_external_data_path()
    file_path = external_data_path / file_name
    return file_path.read_text()

def reverse(string):
    return string[::-1]