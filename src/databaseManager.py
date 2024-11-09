import psycopg2
# In total exist 1 database and 5 table. Among them:
# 1 - Users {UID, firstName, lastName, email, pollsNumber, registeredAt, password}
# 2 - Polls {}
# 3 - Questions {}
# 4 - Completion {}
# 5 - Answers {}
connection = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="pass",
    dbname="postgres"
)

cursor = connection.cursor()


def add_user(email, first_name, last_name, password) -> bool:
    return True


def delete_user(email, password) -> bool:
    return True

# creates a poll, generates unique code, returns it (necessary to access polls)
def add_poll(poll_name, creator_email) -> str:
    return ""

def add_question_to_poll(poll_unique_id, question_type, *args) -> bool:
    is_required: bool = bool(args[0])
    text: str = args[1]
    match question_type:
        case "text":
            pass
        case "poll":
            is_multiple_choice: bool = args[2]
            choose_types = [arg for arg in args[3:]]
        case "scale":
            start_value = args[2]
            end_value = args[3]
        case _:
            return False


def add_answer_to_poll(poll_UID) -> True:
    pass


def edit_poll(poll_UID):
    pass

def add_question(poll_UID):
    pass