from flet import Page, View


def change_view(page: Page, view: View):
    page.views.append(view)
    del page.views[0]
    page.update()

