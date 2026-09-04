import streamlit as st

st.set_page_config(
    page_title="Python Data Structures Lab",
    page_icon="DS",
    layout="wide",
)

INITIAL_VARIABLES = {
    "shopping_list": ["apple", "milk", "bread", "apple"],
    "tasks": ["Wake up", "Brush teeth", "Eat breakfast", "Study", "Sleep"],
    "grades": {"Alice": 90, "Bob": 85, "Charlie": 88},
    "phonebook": {"Alice": "555-1111", "Bob": "555-2222", "Charlie": "555-3333"},
    "visitor_ids": {101, 202, 303},
    "chess_club": {"Alice", "Bob", "Charlie", "David"},
    "math_club": {"Charlie", "David", "Eve", "Frank"},
    "coordinates": (10, 20),
    "menu": ("Pizza", "Burger", "Pasta"),
}


def reset_variables():
    st.session_state.variables = {
        name: value.copy() if hasattr(value, "copy") else value
        for name, value in INITIAL_VARIABLES.items()
    }
    st.session_state.notice = "Variables reset to the lesson starting values."


if "variables" not in st.session_state:
    reset_variables()
if "notice" not in st.session_state:
    st.session_state.notice = "Choose an exercise to begin."


def display_value(value):
    return repr(value)


def show_variable_sidebar():
    with st.sidebar:
        st.header("Variables")
        st.caption("Live values from this practice session")
        for name, value in st.session_state.variables.items():
            st.markdown(f"**{name}**  ")
            st.caption(f"`{type(value).__name__}`  {display_value(value)}")
        st.divider()
        if st.button("Reset all variables", use_container_width=True):
            reset_variables()
            st.rerun()


def operation_result(message, variable_name):
    st.success(message)
    st.write("Current value:")
    st.code(f"{variable_name} = {display_value(st.session_state.variables[variable_name])}")


def list_exercise():
    st.subheader("Lists")
    st.write("Lists are ordered, mutable collections. Add or remove items and watch the variable change.")
    variable_name = st.selectbox("List variable", ["shopping_list", "tasks"])
    current_items = st.session_state.variables[variable_name]
    st.code(f"{variable_name} = {display_value(current_items)}")

    action = st.radio("List operation", ["Add an item", "Remove an item"], horizontal=True)
    item = st.text_input("Item", key=f"list_item_{variable_name}")
    if st.button("Apply list operation", type="primary"):
        if not item.strip():
            st.warning("Enter an item first.")
        elif action == "Add an item":
            current_items.append(item.strip())
            operation_result(f"Added {item.strip()!r} to {variable_name}.", variable_name)
        elif item.strip() not in current_items:
            st.warning(f"{item.strip()!r} is not in {variable_name}.")
        else:
            current_items.remove(item.strip())
            operation_result(f"Removed {item.strip()!r} from {variable_name}.", variable_name)


def dictionary_exercise():
    st.subheader("Dictionaries")
    st.write("Dictionaries store key-value pairs. Add a new key or modify the value of an existing key.")
    variable_name = st.selectbox("Dictionary variable", ["grades", "phonebook"])
    dictionary = st.session_state.variables[variable_name]
    st.code(f"{variable_name} = {display_value(dictionary)}")

    action = st.radio("Dictionary operation", ["Add key", "Modify value"], horizontal=True)
    key = st.text_input("Key")
    value_label = "Grade" if variable_name == "grades" else "Phone number"
    if variable_name == "grades":
        value = st.number_input(value_label, min_value=0, max_value=100, value=90)
    else:
        value = st.text_input(value_label)

    if st.button("Apply dictionary operation", type="primary"):
        clean_key = key.strip()
        if not clean_key:
            st.warning("Enter a key first.")
        elif action == "Add key" and clean_key in dictionary:
            st.warning(f"{clean_key!r} already exists. Choose Modify value.")
        elif action == "Modify value" and clean_key not in dictionary:
            st.warning(f"{clean_key!r} does not exist. Choose Add key.")
        else:
            dictionary[clean_key] = value
            operation_result(f"{action} applied to {variable_name}[{clean_key!r}].", variable_name)


def set_exercise():
    st.subheader("Sets")
    st.write("Sets contain unique values. Add or remove a value.")
    variable_name = st.selectbox("Set variable", ["visitor_ids", "chess_club", "math_club"])
    current_values = st.session_state.variables[variable_name]
    st.code(f"{variable_name} = {display_value(current_values)}")

    action = st.radio("Set operation", ["Add a value", "Remove a value"], horizontal=True)
    value = st.text_input("Value")
    if st.button("Apply set operation", type="primary"):
        if not value.strip():
            st.warning("Enter a value first.")
        else:
            converted_value = int(value) if variable_name == "visitor_ids" and value.isdigit() else value.strip()
            if action == "Add a value":
                if converted_value in current_values:
                    st.warning(f"Duplicate not added. {converted_value!r} is already in {variable_name}.")
                else:
                    current_values.add(converted_value)
                    operation_result(f"Added {converted_value!r} to {variable_name}.", variable_name)
            elif converted_value not in current_values:
                st.warning(f"{converted_value!r} is not in {variable_name}.")
            else:
                current_values.remove(converted_value)
                operation_result(f"Removed {converted_value!r} from {variable_name}.", variable_name)


def tuple_exercise():
    st.subheader("Tuples")
    st.write("Tuples are ordered, immutable collections. Their values cannot be changed after creation.")
    variable_name = st.selectbox("Tuple variable", ["coordinates", "menu"])
    current_value = st.session_state.variables[variable_name]
    st.code(f"{variable_name} = {display_value(current_value)}")
    st.button("Modify tuple", disabled=True, help="Tuples are immutable in Python.")
    st.info("Modification is unavailable because tuples cannot be changed. Create a new tuple if different values are needed.")


show_variable_sidebar()
st.title("Python Data Structures Lab")
st.write("Explore how each data structure behaves by interacting with its live variables.")

exercise = st.selectbox("Choose a data structure", ["Lists", "Dictionaries", "Sets", "Tuples"])
exercise_functions = {
    "Lists": list_exercise,
    "Dictionaries": dictionary_exercise,
    "Sets": set_exercise,
    "Tuples": tuple_exercise,
}
exercise_functions[exercise]()

st.divider()
st.caption(st.session_state.notice)
