from flet import AutoCompleteSuggestion
from Controler import Controler


def auto_complete_suggestion_data() -> list[AutoCompleteSuggestion]:
    names = Controler.get_list_names()
    auto_complete_list = list()

    for name in names:
        auto_complete_list.append(
            AutoCompleteSuggestion(
                key=name,
                value=name,
            )
        )

    return auto_complete_list


def auto_complete_suggestion_id_routines() -> list[AutoCompleteSuggestion]:
    list_id = Controler.get_list_id_rutines()
    auto_complete_list = list()

    for idx in list_id:
        auto_complete_list.append(
            AutoCompleteSuggestion(
                key=str(idx),
                value=str(idx),
            )
        )

    return auto_complete_list
