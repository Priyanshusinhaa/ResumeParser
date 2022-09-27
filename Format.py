from pprint import pprint
class ResumeFormat:
    def __init__(self, **kwargs) -> None:
        self.obj = {
            'Name': None,
            'Email': None,
            'Address': None,
            'PhoneNumber': None,
            'DOB': None,
            'Country': None,
            'SocialMedia':{
                'Twitter': None,
                'LinkedIn': None,
                'Github': None,
                'Instagram': None,
                'Other': None
            },
            'Summary': None,
            'Experience': None,
            'Projects': None,
            'Education': None,
            'Skills': None,
            'Achievements': [],
            'Awards': [],
            'Reference': [],
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
            if key == 'phoneNumber':
                self.obj['PhoneNumber'] = val
            if key == 'dob':
                self.obj['DOB'] = val
            if key == 'country':
                self.obj['Country'] = val
            if key == 'socialMedia':
                self.obj['SocialMedia'] = val
            if key == 'summary':
                self.obj['Summary'] = val
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
            if key == 'awards':
                self.obj['Awards'] = val
            if key == 'reference':
                self.obj['Reference'] = val
            if key == 'publication':
                self.obj['Publication'] = val

    def __repr__(self) -> str:
        return str(self.obj)

            
            





# a = 'e'
# # a.upper()
# myobj = ResumeFormat(email = 'this@me.com', name = 'priyanshu')
# pprint(vars(myobj), sort_dicts=False)


