#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, url_for, request
import requests
import random
import os.path
import os
import random
import insert_data

# Local import
import soul_similarity as s2

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#
@app.route('/insert', methods=['GET','POST'])
def new_user():
    if request.method=='POST':
        name = request.values.get('name')
        gender = request.values.get('gender')
        age = request.values.get('age')
        income = request.values.get('income')

        race= request.values.get('race')
        '''education = request.values.get('education')
        physical_attractiveness= request.values.get('physical-attractiveness')
        bio_chemistry = request.values.get('bio-chemistry')
        core_values = request.values.get('corevalues')
        life_stage  = request.values.get('life-stage')
        mutual_selection  = request.values.get('mutual-selection')
        life_orientation  = request.values.get('life-orientation')
        financial_security  = request.values.get('financial-security')
        healthy_living = request.values.get('healthy-living')
        emotional_outlook  = request.values.get('emotional-learning')
        continuous_learning = request.values.get('continuous_learning')
        behavior_pattern  = request.values.get('Behavior_pattern')
        interpersonal_skills = request.values.get('Interpersonal_skills')
        commitment_level = request.values.get('Commitment_level')
        psychological_cost = request.values.get('Psychological_cost')'''
        print(name)
        print(gender)
        #print(psychological_cost)
        insert_data.add_data(name,gender,age,income,race)
    return render_template('newuser.html')
@app.route('/', methods=['GET'])
def index():

    sample_list = s2.get_all_souls()
    
    result = {
        'sample_souls' : sample_list
    }

    return render_template('index.html', result = result)

@app.route('/', methods=['POST'])
def result():

    soul_name = request.values.get('name')
 
    print(insert_data.select_data(soul_name))
    sample_list = s2.get_all_souls()
    try:
        rec_list = s2.find_similar_souls_auto(soul_name)
        print(rec_list)

        sample_list = s2.get_all_souls()
        result = {
            'rec_list' : rec_list,
            'sample_souls' : sample_list
        }

        return render_template('index.html', result = result)
    except:
        print("Not Found")
        current_soul = {
            'username' : 'not Found',
            'percentile' : 0
        }
        rec_list=[]
        rec_list.append(current_soul)

        result = {
            'rec_list' : rec_list,
            'sample_souls' : sample_list
        }
        return render_template('index.html', result = result)
    #print(rec_list)


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;1
    app.run('127.0.0.1', 4000, True)
