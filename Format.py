from pprint import pprint
class ResumeFormat:
    def __init__(self, **kwargs) -> None:
        self.obj = {
            'Name': None,
            'Email': None,
            'Address': None,
            'Phone': None,
            'DOB': None,
            'Country': None,
            'Experience': None,
            'Projects': None,
            'Education': None,
            'Skills': None,
            'Achievements': [],
            'Publication': []
        }
        for key, val in kwargs.items():
            key = key.lower()
            if key == 'name':
                self.obj['Name'] = val
            if key == 'email':
                self.obj['Email'] = val
            if key == 'address':
                self.obj['Address'] = val
            if key == 'phone':
                self.obj['Phone'] = val
            if key == 'dob':
                self.obj['DOB'] = val
            if key == 'country':
                self.obj['Country'] = val
            if key == 'experience':
                self.obj['Experience'] = val
            if key == 'projects':
                self.obj['Projects'] = val
            if key == 'education':
                self.obj['Education'] = val
            if key == 'skills':
                self.obj['Skills'] = val
            if key == 'achievements':
                self.obj['Achievements'] = val
            if key == 'publication':
                self.obj['Publication'] = val

    def __repr__(self) -> str:
        return str(self.obj)
