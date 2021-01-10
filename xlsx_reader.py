import xlrd
import insert_data

BASE_FOLDER = ""
FILENAME = BASE_FOLDER + "soul_param.xlsx"

def read_soul_data_and_store_in_db(sheet):

    for rowx in range(sheet.nrows):
        print(rowx)

        values = sheet.row_values(rowx)

        Name, gender, age, income, race, education,physical_attractiveness = None,None,None,None,None,None,None
        #bio_chemistry, core_values, life_stage, mutual_selection, life_orientation, financial_security = None,None,None,None,None,None
        #ealthy_living, emotional_outlook, continuous_learning, behavior_pattern,interpersonal_skills,commitment_level, psychological_cost = None,None,None,None,None,None,None

        Name = values[0]
        gender = values[1]
        age = values[2]
        income = values[3]
        race = values[4]
        '''education = values[5]
        physical_attractiveness = values[6]
        bio_chemistry = values[7]
        core_values = values[8]
        life_stage = values[9]
        mutual_selection = values[10]
        life_orientation = values[11]
        financial_security = values[12]
        healthy_living = values[13]
        emotional_outlook = values[14]
        continuous_learning = values[15]
        behavior_pattern = values[16]
        interpersonal_skills = values[17]
        commitment_level = values[18]
        psychological_cost = values[19]'''
    
        #skipping first row
        if(Name=='name'):
            continue
        insert_data.add_data(Name, gender, age, income, race)



def read_xlsx():

    workbook = xlrd.open_workbook(FILENAME)
    read_soul_data_and_store_in_db(workbook.sheet_by_index(0))
    

def start():
    read_xlsx()

if __name__ == '__main__':
    start()        