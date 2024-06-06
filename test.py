from main import get_ages


data = ['PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,1,1,0,0,male,24,0,0,0,0,0,0',
        '2,1,1,0,0,female,2,0,0,0,0,0,0',
        '3,0,2,0,0,male,0.4,0,0,0,0,0,0',
        '4,1,2,0,0,female,42,0,0,0,0,0,0',
        '5,1,3,0,0,male,54,0,0,0,0,0,0',
        '6,0,3,0,0,female,12,0,0,0,0,0,0',
        '7,0,2,0,0,male,43,0,0,0,0,0,0',
        '8,0,1,0,0,male,53,0,0,0,0,0,0',
        '9,1,3,0,0,male,12,0,0,0,0,0,0',
        '10,1,3,0,0,male,2,0,0,0,0,0,0',
        '11,0,2,0,0,female,1,0,0,0,0,0,0',
        '12,1,3,0,0,female,42,0,0,0,0,0,0',
        '13,1,3,0,0,female,42.2,0,0,0,0,0,0',
        '14,0,2,0,0,female,45,0,0,0,0,0,0',
        '15,1,1,0,0,male,75,0,0,0,0,0,0',
        '16,0,3,0,0,female,45,0,0,0.2,0,0',
        '17,1,3,0,0,male,43,0,0,0,0,0,0',
        '18,1,2,0,0,male,23,0,0,0,0,0,0',
        '19,0,1,0,0,female,52,0,0,0,0,0,0',
        '20,1,3,0,0,female,1,0,0,0,0,0,0'
        ]


def test_count_alive_male():
    assert len(get_ages(data, stat=True, sex='male')) == 7


def test_count_died_female():
    assert len(get_ages(data, stat=False, sex='female')) == 5


def test_max_died_female_age():
    assert max(get_ages(data, stat=False, sex='female')) == 52.0


def test_min_alive_male_age():
    assert min(get_ages(data, stat=True, sex='male')) == 2.0
