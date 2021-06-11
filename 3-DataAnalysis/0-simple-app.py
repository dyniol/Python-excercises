import justpy as jp

def app():
    wp = jp.QuasarPage() # create variable with QuasarPage()
    h1 = jp.QDiv(
        a=wp,   # need to state to which variable we want to add this div
        text="Analysis of Course Reviews",
        classes="text-h3 text-center q-pa-md"   # classes are on https://quasar.dev/style/
    ) # creating divs like in html
    p1 = jp.QDiv(
        a=wp,
        text="These graphs represent course review analysis"
    )

    return wp

jp.justpy(app)