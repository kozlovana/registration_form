from demoqa_tests.data import User
from demoqa_tests.model import app

user = User(
    first_name="Anastasia",
    last_name="Kozlova",
    email="kozlova@mail.com",
    gender="Female",
    mobile_number="8911911911",
    date_of_birth="27 February,1994",
    subjects=["Computer Science", "Maths"],
    hobbies=["Music"],
    photo="girl.png",
    current_address="Podgorica",
    state="NCR",
    city="Delhi",
)


def test_submit_form():
    app.given_opened_practice_form()

    app.form.set_first_name(user.first_name)\
        .set_last_name(user.last_name)\
        .set_email(user.email)\
        .set_gender(user.gender)\
        .set_mobile_number(user.mobile_number)\
        .set_date_of_birth(user.date_of_birth)\
        .set_subjects(user.subjects)\
        .subjects_should_have(user.subjects)\
        .set_hobbies(user.hobbies)\
        .set_photo(user.photo)\
        .set_current_address(user.current_address)\
        .set_state(user.state)\
        .set_city(user.city)\
        .submit()

    app.result.verify_sent_data(
        user.full_name(user.first_name, user.last_name),
        user.email,
        user.gender,
        user.mobile_number,
        user.date_of_birth,
        user.subjects,
        user.hobbies,
        user.photo,
        user.current_address,
        user.state_and_city(user.state, user.city),
    )
