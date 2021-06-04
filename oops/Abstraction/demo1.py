
# Static variable

class Employee:

    comp_name="sathya"
    comp_con="123456789"

    @staticmethod
    def display_company_info():
        print("Company Name",Employee.comp_name)
        print("Company cno",Employee.comp_con)

Employee.display_company_info()